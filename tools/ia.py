"""Leitura por mecanismos de busca e assistentes de IA. Roda depois que todas as páginas foram escritas e:
1. enriquece o JSON-LD de cada página conforme o tipo (lição, artigo, perfil de pessoa, partido, glossário, coleção);
2. escreve llms.txt (mapa comentado do site, no formato de llmstxt.org) e llms-full.txt (texto das lições e artigos).
Lê só o HTML gerado, então o mesmo arquivo serve aos três sites (Política, Ética e Ciência Para Iniciantes)."""
import html, json, os, re

NIVEIS = ('Iniciante', 'Intermediário', 'Avançado')
LD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)

def _txt(h):
    h = re.sub(r'<(script|style|svg|noscript|button)\b.*?</\1>', ' ', h, flags=re.S | re.I)
    return ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', h)).split())

def _ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace('</', '<\\/') + '</script>'

def _fontes(h, site):
    m = re.search(r'<h2>Fontes e leituras</h2>\s*<ul>(.*?)</ul>', h, re.S)
    if not m: return []
    out = []
    for u, t in re.findall(r'<a href="([^"]+)"[^>]*>(.*?)</a>', m.group(1), re.S):
        t = _txt(t)
        if u.startswith('http') and not t.startswith('Buscar n'): out.append((t, u))
    return out

def _resumo(h):
    m = re.search(r'<aside class="lado">.*?<dl>(.*?)</dl>', h, re.S)
    return {_txt(k): (v, _txt(v)) for k, v in re.findall(r'<dt>(.*?)</dt><dd>(.*?)</dd>', m.group(1), re.S)} if m else {}

def _paginas(root):
    for d, _, fs in os.walk(root):
        rel = os.path.relpath(d, root).replace('\\', '/')
        if rel != '.' and rel.startswith(('.', 'tools', 'assets', 'node_modules')): continue
        for f in fs:
            if f.endswith('.html') and f != '404.html' and not f.startswith('_'):
                yield (f if rel == '.' else f'{rel}/{f}')

def enriquece(root, site):
    """Reescreve o JSON-LD das páginas com dados que o build não passava à função de metadados. Devolve as páginas lidas."""
    lidas = {}
    for p in _paginas(root):
        c = os.path.join(root, p)
        h = open(c, encoding='utf-8').read()
        if 'http-equiv="refresh"' in h: continue
        m = LD.search(h)
        if not m: continue
        try: dado = json.loads(m.group(1))
        except ValueError: continue
        grafo = dado.get('@graph', [dado])
        pag = next((g for g in grafo if g.get('@type') not in ('WebSite', 'BreadcrumbList')), None)
        trilha = [i['name'] for g in grafo if g.get('@type') == 'BreadcrumbList' for i in g['itemListElement']]
        pai = trilha[1] if len(trilha) > 2 else ''
        fontes = _fontes(h, site)
        res = _resumo(h)
        art = re.search(r'<article class="leitura">(.*?)</article>', h, re.S) or re.search(r'<div class="[^"]*leitura[^"]*">(.*?)</main>', h, re.S)
        info = dict(t=(pag or {}).get('name') or _txt(re.search(r'<title>(.*?)</title>', h, re.S).group(1)).split(' | ')[0],
                    d=(pag or {}).get('description', ''), pai=pai, tipo=(pag or {}).get('@type', 'WebSite'),
                    corpo=art.group(1) if art else '')
        lidas[p] = info
        if pag is None: continue
        citacao = [{'@type': 'CreativeWork', 'name': t, 'url': u} for t, u in fontes if 'wikipedia.org' not in u or 'Wikip' in t][:20]
        wiki = [u for t, u in fontes if 'wikipedia.org/wiki/' in u and t.startswith('Wikipédia: ') and 'presidencial' not in t]
        tipo = pag.get('@type')
        if tipo == 'WebPage' and p.startswith(('debates/', 'dilemas/')) and art:
            # debates e dilemas são textos editoriais: viram artigos
            pag.update({'@type': 'Article', 'headline': pag.get('name', '')[:110], 'datePublished': pag.get('dateModified', ''), 'publisher': grafo[0].get('publisher'), 'mainEntityOfPage': pag.get('url')})
            tipo = 'Article'; lidas[p]['tipo'] = 'Article'
        if tipo == 'Article' and pai in NIVEIS:
            # lição: recurso educativo, com nível, tempo, temas, objetivos e fontes
            pag['@type'] = ['Article', 'LearningResource']
            rtipo = 'Teste' if os.path.basename(p).startswith('teste-') else 'Revisão' if os.path.basename(p).startswith('revisao-') else 'Lição'
            pag.update(educationalLevel=pai, learningResourceType=rtipo, isAccessibleForFree=True,
                       audience={'@type': 'EducationalAudience', 'educationalRole': 'student'})
            tempo = re.search(r'(\d+)\s*min', res.get('Tempo', ('', ''))[1] or '')
            if not tempo: tempo = re.search(r'(\d+) min de leitura', h)
            if tempo: pag['timeRequired'] = f'PT{tempo.group(1)}M'
            if 'Temas' in res: pag['keywords'] = res['Temas'][1]
            obj = re.search(r'(?:vai conseguir|Nesta lição, você vai)</p>\s*<ul>(.*?)</ul>', h, re.S)
            if obj: pag['teaches'] = [_txt(x) for x in re.findall(r'<li>(.*?)</li>', obj.group(1), re.S)]
            if citacao: pag['citation'] = citacao
        elif tipo == 'Article':
            pag['isAccessibleForFree'] = True
            if citacao: pag['citation'] = citacao
        elif tipo == 'WebPage' and isinstance(pag.get('about'), dict) and pag['about'].get('@type') == 'Person':
            # perfil: a página é sobre uma pessoa (políticos, filósofos, pensadores)
            pessoa = {'@type': 'Person', 'name': pag['about']['name'], 'description': pag.get('description', '')}
            if wiki: pessoa['sameAs'] = wiki
            if 'Partido' in res:
                lk = re.search(r'href="([^"]+)"', res['Partido'][0])
                pessoa['affiliation'] = {'@type': 'PoliticalParty', 'name': res['Partido'][1], **({'url': site + '/' + re.sub(r'^(\.\./)+', '', lk.group(1))} if lk else {})}
            pag['@type'] = 'ProfilePage'; pag.pop('about'); pag['mainEntity'] = pessoa
        elif tipo == 'WebPage' and isinstance(pag.get('about'), dict) and pag['about'].get('@type') == 'Organization' and p.startswith('partidos/'):
            partido = {'@type': 'PoliticalParty', 'name': pag['about']['name'], 'description': pag.get('description', '')}
            if 'Fundação' in res and re.fullmatch(r'\d{4}', res['Fundação'][1]): partido['foundingDate'] = res['Fundação'][1]
            if wiki: partido['sameAs'] = wiki
            pag['about'] = partido
        if '<dl class="glossario">' in h:
            termos = [{'@type': 'DefinedTerm', 'name': _txt(t), 'description': _txt(re.search(r'<p>(.*?)</p>', d, re.S).group(1)) if re.search(r'<p>(.*?)</p>', d, re.S) else _txt(d)}
                      for t, d in re.findall(r'<dt>(.*?)</dt>\s*<dd>(.*?)</dd>', h, re.S)]
            if termos:
                pag['mainEntity'] = {'@type': 'DefinedTermSet', 'name': pag.get('name', ''), 'hasDefinedTerm': termos}
        elif pag.get('@type') == 'CollectionPage':
            cartoes = [(u, re.search(r'<h3>(.*?)</h3>', c, re.S).group(1)) for u, c in re.findall(r'<a class="cartao[^"]*"[^>]*?href="([^"]+)"[^>]*>(.*?)</a>', h, re.S) if '<h3>' in c]
            vistos, itens = set(), []
            for u, t in cartoes:
                if u.startswith('http') or u in vistos: continue
                vistos.add(u); itens.append({'@type': 'ListItem', 'position': len(itens) + 1, 'name': _txt(t), 'url': site + '/' + re.sub(r'^(\.\./)+', '', u)})
            if itens: pag['mainEntity'] = {'@type': 'ItemList', 'numberOfItems': len(itens), 'itemListElement': itens[:200]}
        novo = h[:m.start()] + _ld(dado) + h[m.end():]
        if novo != h:
            open(c, 'w', encoding='utf-8', newline='\n').write(novo)
    return lidas

def _md(corpo):
    """Converte o corpo de uma lição em texto simples com marcações de Markdown."""
    c = re.sub(r'<(script|style|svg|button|form)\b.*?</\1>', ' ', corpo, flags=re.S | re.I)
    c = re.sub(r'<div class="(?:quiz|posicao|pratica|marcar|relac|pager)[^"]*".*?</div>\s*</div>', ' ', c, flags=re.S)
    c = re.sub(r'<h2[^>]*>(.*?)</h2>', lambda m: '\n\n## ' + _txt(m.group(1)) + '\n', c, flags=re.S)
    c = re.sub(r'<h3[^>]*>(.*?)</h3>', lambda m: '\n\n### ' + _txt(m.group(1)) + '\n', c, flags=re.S)
    c = re.sub(r'<tr[^>]*>(.*?)</tr>', lambda m: '\n| ' + ' | '.join(_txt(x) for x in re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', m.group(1), re.S)) + ' |', c, flags=re.S)
    c = re.sub(r'<li[^>]*>(.*?)</li>', lambda m: '\n- ' + _txt(m.group(1)), c, flags=re.S)
    c = re.sub(r'</p>|<br\s*/?>|</ul>|</ol>|</div>|</section>|</summary>|</table>', '\n\n', c)
    c = html.unescape(re.sub(r'<[^>]+>', '', c))
    c = re.sub(r'[ \t]+', ' ', c)
    return re.sub(r'\n\s*\n\s*\n+', '\n\n', c).strip()

NOTA = ('Guia educativo gratuito, em português do Brasil, publicado pela BiblioVerse. Cada página traz as fontes ao final; '
        'classificações e veredictos são estimativas editoriais explicadas na própria página e abertas a correção.')

def llms(root, site, nome, atualizado, lidas, resumo=None, nota=NOTA, max_lista=150):
    """Escreve llms.txt e llms-full.txt a partir das páginas lidas por enriquece()."""
    antigo = open(os.path.join(root, 'llms.txt'), encoding='utf-8').read() if os.path.exists(os.path.join(root, 'llms.txt')) else ''
    secoes = re.search(r'## Principais seções\n\n(.*?)(?:\n\n|$)', antigo, re.S)
    if resumo is None:
        r = re.search(r'^> (.+)$', antigo, re.M)
        resumo = r.group(1) if r else nome
    grupos = {}
    for p, x in sorted(lidas.items()):
        if x['pai'] and x['t']: grupos.setdefault(x['pai'], []).append((p, x))
    linhas = [f'# {nome}', '', f'> {resumo}', '', nota, '', f'Atualizado em {atualizado[8:10]}/{atualizado[5:7]}/{atualizado[:4]}. Texto completo das lições e artigos em [llms-full.txt]({site}/llms-full.txt).', '']
    if secoes: linhas += ['## Principais seções', '', secoes.group(1).strip(), '']
    ordem = [n for n in NIVEIS if n in grupos] + sorted(g for g in grupos if g not in NIVEIS)
    opcional = []
    for g in ordem:
        its = grupos[g]
        if len(its) > max_lista:
            opcional.append(f'- {g}: {len(its)} páginas, listadas no [sitemap]({site}/sitemap.xml)')
            continue
        titulo = f'Lições do nível {g}' if g in NIVEIS else g
        linhas += [f'## {titulo}', ''] + [f'- [{x["t"]}]({site}/{p}): {x["d"]}' for p, x in its] + ['']
    linhas += ['## Optional', ''] + opcional + [f'- [Mapa do site]({site}/sitemap.xml)', f'- [Texto completo]({site}/llms-full.txt)', '']
    open(os.path.join(root, 'llms.txt'), 'w', encoding='utf-8', newline='\n').write('\n'.join(linhas))
    # texto completo: lições primeiro, por nível, depois os artigos
    partes = [f'# {nome}', '', f'> {resumo}', '', nota, '']
    def tem(x): return 'Article' in (x['tipo'] if isinstance(x['tipo'], list) else [x['tipo']]) and x['corpo']
    for g in ordem:
        for p, x in grupos[g]:
            if not tem(x): continue
            partes += ['', '---', '', f'# {x["t"]}', '', f'Fonte: {site}/{p}' + (f' · {g}' if g else ''), '', x['d'], '', _md(x['corpo'])]
    open(os.path.join(root, 'llms-full.txt'), 'w', encoding='utf-8', newline='\n').write('\n'.join(partes) + '\n')
