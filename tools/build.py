"""Gera todas as páginas do site. Uso: python tools/build.py"""
import json, os, re, sys, unicodedata
from html import escape as e
from urllib.parse import quote
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from licoes_iniciante import INICIANTE
from licoes_intermediario import INTERMEDIARIO
from licoes_avancado import AVANCADO
from brasil import CARGOS, ORGAOS, HISTORIA, RANKING, CASOS, PESSOAS, SITES, LIVROS
from partidos import P, W, ORDEM_ESP
from extras import NOVA, DESPOLITIZADO, NEM_TUDO, META, TEMAS
from figuras import F, CATEGORIAS, TIPOS
from vertentes import V, FAMILIAS_V
from debates import DEBATES, ANTIGOS
from vieses import V as VIES, CATS
from vieses_explica import E as VIES_E
from vieses_wiki import W as VIES_W
VIES_TDL = {x[0] for x in VIES}
for _x in VIES_W:
    VIES.append(_x[:4] + _x[6:8]); VIES_E[_x[0]] = (_x[4], _x[5])
assert len({x[0] for x in VIES}) == len(VIES)
from tribalismo import TRIBALISMO, META_TRIBALISMO
from medo_eco import MEDO, META_MEDO, ECO, META_ECO
from informacao import PERIGOS_INFO, HISTORIA_LICOES, META_INFORMACAO
from mudar_ideia import MUDAR, META_MUDAR
from ultraconservadorismo import ULTRA, META_ULTRA
from estrangeiro import ESTRANGEIRO, META_ESTRANGEIRO
from testar_visao import TESTAR, META_TESTAR
from progresso import PROGRESSO, META_PROGRESSO
from avancado_novas import AV_NOVAS, META_AV, SUL, META_SUL
from mapa_ed import ED
from reforco import REFORCO
from grandes_debates import DEBATES_P, TEMAS_D, ROT_PESO, SITES_U, GRUPOS_S, NAC, INT
from mundo import M as MUNDO, GRUPOS_M, REGIOES
from mundo_extremistas import X as EXTREMISTAS, EXT as GRUPO_EXT
from conceitos import CONCEITOS, META_CONCEITOS
from sofismo import SOFISMO, META_SOFISMO, SOFISMAS, TRUQUES
from basico import BASICO
from dossies import D, ROTULO, FAMILIAS, PROBLEMAS, FRASES, TROCAS, CHECK
from revisao import NOVAS_INICIANTE, NOVAS_INTERMEDIARIO, NOVAS_AVANCADO, META_REVISAO, BASICO_REVISAO, REFORCO_REVISAO, GRUPOS, ORDEM_GRUPOS
import arte

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://politicaparainiciantes.biblioverse.org'
NOME = 'Política Para Iniciantes'
EXT = 'target="_blank" rel="noopener"'
i_pos = next(i for i, l in enumerate(INTERMEDIARIO) if l['slug'] == 'estado-e-mercado')
META['sofismo'] = META_SOFISMO
META.update(META_CONCEITOS)
META['mudar-de-ideia'] = META_MUDAR
META['perigo-do-ultraconservadorismo'] = META_ULTRA
META['perigo-de-culpar-o-estrangeiro'] = META_ESTRANGEIRO
META['testar-visao-moral'] = META_TESTAR
META['progresso-moral-e-politico'] = META_PROGRESSO
META.update(META_INFORMACAO)
INTERMEDIARIO[0:0] = CONCEITOS
i_pos += len(CONCEITOS)
META['politica-do-medo'] = META_MEDO
META['camaras-de-eco'] = META_ECO
for _l in reversed(PERIGOS_INFO):
    INTERMEDIARIO.insert(i_pos, _l)
INTERMEDIARIO.insert(i_pos, ECO)
INTERMEDIARIO.insert(i_pos, MEDO)
META['perigo-do-tribalismo'] = META_TRIBALISMO
INTERMEDIARIO.insert(i_pos, TRIBALISMO)
INTERMEDIARIO.insert(i_pos, SOFISMO)
INTERMEDIARIO.insert(i_pos, NOVA)
INICIANTE.insert(1, DESPOLITIZADO)
INTERMEDIARIO.extend(HISTORIA_LICOES)
INTERMEDIARIO.append(SUL)
META[SUL['slug']] = META_SUL
AVANCADO.extend(AV_NOVAS)
META.update(META_AV)
INTERMEDIARIO.append(NEM_TUDO)
AVANCADO.insert(next(i for i, l in enumerate(AVANCADO) if l['slug'] == 'senciocentrismo'), PROGRESSO)
INTERMEDIARIO.insert(next(i for i, l in enumerate(INTERMEDIARIO) if l['slug'] == 'vieses-cognitivos') + 1, MUDAR)
INTERMEDIARIO.insert(next(i for i, l in enumerate(INTERMEDIARIO) if l['slug'] == 'mudar-de-ideia') + 1, TESTAR)
INTERMEDIARIO.insert(next(i for i, l in enumerate(INTERMEDIARIO) if l['slug'] == 'perigo-do-reacionarismo') + 1, ULTRA)
INTERMEDIARIO.insert(next(i for i, l in enumerate(INTERMEDIARIO) if l['slug'] == 'politica-do-medo') + 1, ESTRANGEIRO)
# lições da revisão de novembro de 2026
META.update(META_REVISAO); BASICO.update(BASICO_REVISAO); REFORCO.update(REFORCO_REVISAO)
def _apos(ls, slug, nova): ls.insert(next(i for i, l in enumerate(ls) if l['slug'] == slug) + 1, nova)
_NI = {l['slug']: l for l in NOVAS_INICIANTE}; _NM = {l['slug']: l for l in NOVAS_INTERMEDIARIO}
_apos(INICIANTE, 'democracia', _NI['como-uma-lei-e-feita']); _apos(INICIANTE, 'como-uma-lei-e-feita', _NI['o-que-e-um-partido'])
_apos(INTERMEDIARIO, 'imposto-e-roubo', _NM['economia-para-entender-politica']); _apos(INTERMEDIARIO, 'perigo-do-messianismo', _NM['perigo-do-populismo'])
_apos(AVANCADO, 'politicas-baseadas-em-evidencias', NOVAS_AVANCADO[0]); _apos(INTERMEDIARIO, 'numero-de-projetos', _NM['corrupcao']); _apos(INTERMEDIARIO, 'perigo-da-midia-alternativa', _NM['como-ler-a-midia-tradicional']); _apos(INTERMEDIARIO, 'cambridge-analytica', _NM['pesquisas-eleitorais'])
# grupos e ordem de cada nível: a lista é ordenada pelos grupos (ordenação estável mantém a sequência dentro do grupo)
for _n, _ls in (('iniciante', INICIANTE), ('intermediario', INTERMEDIARIO), ('avancado', AVANCADO)):
    for _l in _ls: _l['grupo'] = GRUPOS.get(_l['slug'], _l.get('grupo', ''))
    _o = ORDEM_GRUPOS[_n]; assert all(_l['grupo'] in _o for _l in _ls), [_l['slug'] for _l in _ls if _l['grupo'] not in _o]
    _ls.sort(key=lambda l: _o.index(l['grupo']))
NIVEIS = [('iniciante', 'Iniciante', INICIANTE, 'Política para iniciantes', 'Os conceitos, sem enrolação: o que é política, o que está por trás dela e como votar melhor.', 'v'),
          ('intermediario', 'Intermediário', INTERMEDIARIO, 'Política intermediária', 'Como nossa mente nos engana, os grandes perigos e as perguntas difíceis.', ''),
          ('avancado', 'Avançado', AVANCADO, 'Política avançada', 'Quem chega ao poder, como reformar a democracia e quem deve contar.', 'a')]
for slug, rot, ls, _, _, _ in NIVEIS:
    for i, l in enumerate(ls):
        l.update(nivel=slug, nivel_rot=rot, i=i, temas=META[l['slug']][0], quiz=META[l['slug']][1])
TODAS = INICIANTE + INTERMEDIARIO + AVANCADO
for l in INICIANTE:
    x = BASICO[l['slug']]
    blocos = f'<div class="ajuda"><section class="analogia"><h3>Uma analogia</h3><p>{e(x["analogia"])}</p></section><section class="crianca"><h3>Explicando para uma criança</h3><p>{e(x["crianca"])}</p></section></div>'
    fim = l['corpo'].index('</p>') + 4
    l['corpo'] = l['corpo'][:fim] + blocos + l['corpo'][fim:] + x['fundo']
    l['fontes'] = l['fontes'] + x['fontes']
for l in INTERMEDIARIO + AVANCADO:
    if 'class="ajuda"' in l['corpo']: continue
    x = REFORCO[l['slug']]
    blocos = f'<div class="ajuda"><section class="analogia"><h3>Uma analogia</h3><p>{e(x["analogia"])}</p></section><section class="crianca"><h3>Explicando para uma criança</h3><p>{e(x["crianca"])}</p></section></div>'
    fim = l['corpo'].index('</p>') + 4
    l['corpo'] = l['corpo'][:fim] + blocos + l['corpo'][fim:] + x.get('fundo', '')
PARTIDO = {p['id']: p for p in P}
for p in P: p.update(D[p['id']])
PRESID = json.load(open(os.path.join(ROOT, 'data', 'presidenciais.json'), encoding='utf-8'))
PRESID['missao'] = [dict(ano='2026', cand='Renan Santos', pct='2,24', pos='4')]
try: VOTOS = json.load(open(os.path.join(ROOT, 'data', 'votos.json'), encoding='utf-8'))
except OSError: VOTOS = []
# como cada partido aparece na API da Câmara
COD = {'uniao': ['UNIÃO', 'UNIAO'], 'republicanos': ['REPUBLICANOS', 'PRB'], 'pode': ['PODE', 'PTN'], 'solidariedade': ['SOLIDARIEDADE', 'SD', 'SDD'], 'cidadania': ['CIDADANIA', 'PPS'], 'avante': ['AVANTE', 'PTdoB'], 'pl': ['PL', 'PR'], 'mdb': ['MDB', 'PMDB'], 'missao': ['MISSÃO'], 'novo': ['NOVO'], 'rede': ['REDE'], 'prd': ['PRD'], 'mobiliza': ['MOBILIZA', 'PMN'], 'agir': ['AGIR', 'PTC'], 'democrata': ['PMB']}
def resume(d): return dict(s=d.get('Sim', 0), n=d.get('Não', 0), o=sum(v for k, v in d.items() if k not in ('Sim', 'Não')))
VIDS = {}
for p in P:
    for c in COD.get(p['id'], [p['s']]): VIDS[c] = p['id']
V_JSON = [dict(rot=v['rot'], ano=v['ano'], desc=v['desc'], data=v.get('data', ''), tot=resume(v['tot']), p={k: resume(x) for k, x in v['partidos'].items() if k != 'S.PART.'}) for v in VOTOS]
def voto_de(pid, v):
    for c in COD.get(pid, [PARTIDO[pid]['s']]):
        if c in v['p']: return c, v['p'][c]
    return None, None
FERR = [('quem-faz-o-que', 'Quem faz o quê?', 'Um problema, sete cargos. Você sabe quem cobrar?', 'cargo'), ('valor-ou-fato', 'Valor ou fato?', 'Treine separar o que se discute com argumento moral do que se checa com dados.', 'valor'), ('como-votaram', 'Como os partidos votaram', 'Dados oficiais da Câmara, partido por partido, em votações decisivas.', 'votos'), ('comparador', 'Comparador de partidos', 'Coloque até três partidos lado a lado.', 'compara'), ('arvore-dos-partidos', 'Árvore dos partidos', 'De onde veio cada sigla, de Arena a Missão.', 'arvore'), ('teste-de-troca', 'Teste de troca', 'Você julgaria o mesmo ato de quem você rejeita?', 'troca'), ('ficha-do-candidato', 'Ficha do candidato', 'Um checklist que fica salvo no seu navegador.', 'ficha'), ('simulador-de-cadeiras', 'Simulador de cadeiras', 'Veja como votos viram vagas em uma eleição proporcional.', 'cadeira'), ('voto-preferencial', 'Simulador de voto preferencial', 'Os mesmos eleitores, duas regras, resultados diferentes.', 'urna'), ('que-truque-e-esse', 'Que truque é esse?', 'Identifique os sofismas mais comuns em frases políticas.', 'troca')]
BR = [('cargos.html', 'O que cada cargo faz', 'De vereador a presidente: quem decide o quê.'), ('poderes.html', 'Os Poderes e órgãos', 'Executivo, Legislativo, Judiciário, MP, TCU e mais.'), ('historia.html', 'História da política brasileira', 'Da Colônia à eleição de 2026.'), ('partidos.html', f'Dossiê dos {len(P)} partidos', 'Linha do tempo, casos, votos e eleições de cada um.'), ('politicos.html', 'Políticos e figuras', 'Cards e dossiês, do espectro inteiro.'), ('ranking-da-mentira.html', 'Ranking da mentira', 'O que dizem as agências de checagem.'), ('acompanhar.html', 'Onde acompanhar', 'Sites e pessoas para se informar com ponderação.')]
ESP_POS = {'Extrema-esquerda': 6, 'Esquerda': 20, 'Centro-esquerda': 36, 'Centro': 50, 'Independente (declarado)': 54, 'Independente (declarado); centro-direita': 62, 'Centro a centro-direita': 58, 'Centro-direita': 68, 'Direita': 86}
FAIXA = {'Extrema-esquerda': 'Esquerda', 'Esquerda': 'Esquerda', 'Centro-esquerda': 'Centro-esquerda', 'Centro': 'Centro', 'Independente (declarado)': 'Centro', 'Independente (declarado); centro-direita': 'Centro-direita', 'Centro a centro-direita': 'Centro-direita', 'Centro-direita': 'Centro-direita', 'Direita': 'Direita'}

ATUALIZADO = '2026-11-03'
PAGINAS = []
SECOES = {'debates': ('debates.html', 'Principais debates', 'Os dois lados, a complexidade e o que os dados indicam.'), 'mundo': ('mundo.html', 'Figuras internacionais', 'Trajetória, posições e controvérsias, com fontes.'), 'politicos': ('politicos.html', 'Políticos e figuras', 'Trajetória, posições e controvérsias, com fontes.'), 'vertentes': ('vertentes.html', 'Vertentes políticas', 'Ideias, história, forças e contradições explicadas.'), 'vieses': ('vieses.html', 'Vieses cognitivos', 'Entenda com exemplo e veja os efeitos no julgamento moral e político.'), 'partidos': ('partidos.html', 'Partidos', 'Dossiê com fontes.'), 'ferramentas': ('ferramentas.html', 'Ferramentas', 'Ferramenta interativa e gratuita, sem cadastro.')}
PAIS_NIVEL = {'iniciante.html': 'Iniciante', 'intermediario.html': 'Intermediário', 'avancado.html': 'Avançado'}
HUBS = {'catalogo.html', 'iniciante.html', 'intermediario.html', 'avancado.html', 'brasil.html', 'partidos.html', 'politicos.html', 'mundo.html', 'debates.html', 'sites.html', 'vertentes.html', 'vieses.html', 'ferramentas.html', 'biblioteca.html', 'acompanhar.html'}

def desc_seo(path, desc):
    d = re.sub(r'\s+', ' ', re.sub('<[^>]+>', '', desc)).strip()
    if d and d[-1] not in '.!?…': d += '.'
    if len(d) < 70:
        sec = SECOES.get(path.split('/')[0]) if '/' in path else None
        d += ' ' + (sec[2] if sec else 'Explicação simples e com fontes, sem escolher time.')
    if len(d) > 160: d = d[:157].rsplit(' ', 1)[0].rstrip(' ,;:') + '…'
    return d

def dados(path, title, desc, url, atual, home):
    org = {'@type': 'Organization', 'name': 'BiblioVerse', 'url': 'https://biblioverse.org'}
    site = {'@type': 'WebSite', '@id': SITE + '/#site', 'name': NOME, 'url': SITE + '/', 'inLanguage': 'pt-BR', 'publisher': org}
    if home:
        grafo = [site]
    else:
        pasta = path.split('/')[0] if '/' in path else ''
        pai = (SECOES[pasta][0], SECOES[pasta][1]) if pasta in SECOES else ((atual, PAIS_NIVEL[atual]) if atual in PAIS_NIVEL else None)
        trilha = [('Início', SITE + '/')] + ([(pai[1], f'{SITE}/{pai[0]}')] if pai else []) + [(title, url)]
        migalhas = {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(trilha)]}
        base = {'name': title, 'headline': title[:110], 'description': desc, 'url': url, 'inLanguage': 'pt-BR', 'isPartOf': {'@id': SITE + '/#site'}, 'dateModified': ATUALIZADO, 'image': SITE + '/assets/share.png'}
        if atual in PAIS_NIVEL or pasta in ('vertentes', 'vieses'):
            pagina = {'@type': 'Article', 'datePublished': ATUALIZADO, 'author': {'@type': 'Organization', 'name': NOME, 'url': SITE + '/sobre.html'}, 'publisher': org, 'mainEntityOfPage': url, **base}
        elif pasta in ('politicos', 'mundo'):
            pagina = {'@type': 'WebPage', 'about': {'@type': 'Person', 'name': title}, **base}
        elif pasta == 'partidos':
            pagina = {'@type': 'WebPage', 'about': {'@type': 'Organization', 'name': title.split(':')[0]}, **base}
        elif pasta == 'ferramentas':
            pagina = {'@type': 'WebApplication', 'applicationCategory': 'EducationalApplication', 'operatingSystem': 'Web', 'isAccessibleForFree': True, 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'BRL'}, **base}
        elif path in HUBS:
            pagina = {'@type': 'CollectionPage', **base}
        else:
            pagina = {'@type': 'WebPage', **base}
        for k in ('headline',):
            if pagina['@type'] != 'Article': pagina.pop(k, None)
        grafo = [site, pagina, migalhas]
    return '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': grafo}, ensure_ascii=False).replace('</', '<\\/') + '</script>'

def titulos_ok(corpo):
    """Título da analogia não é seção, e páginas de cards não saltam de h1 para h3."""
    corpo = re.sub(r'(<section class="(?:analogia|crianca)">)<h3>(.*?)</h3>', r'\1<p class="ti">\2</p>', corpo)
    m = re.search(r'</h1>.*?<h([2-6])[\s>]', corpo, re.S)
    fim = corpo.find('</section>', corpo.find('</h1>'))
    if m and m.group(1) == '3' and fim > 0:
        fim += len('</section>')
        return corpo[:fim] + '<h2 class="so-leitor">Nesta página</h2>' + corpo[fim:]
    return corpo

def mapa_ed(pre=''):
    assert set(ED) == {v['s'] for v in V}
    dots = ''.join(f'''<a class="ponto f{COR_FAM[v["f"]]}{" esq" if ED[v["s"]][0] > 35 else ""}" href="{pre}vertentes/{v["s"]}.html" style="left:{(ED[v["s"]][0] + 100) * .44 + 6:.1f}%;top:{(100 - ED[v["s"]][1]) * .44 + 6:.1f}%" title="{e(v["n"])}"><span>{e(v["n"])}</span></a>''' for v in V)
    leg = ''.join(f'<span><i class="fam f{COR_FAM[f]}"></i>{e(f)}</span>' for f in FAMILIAS_V)
    return f'''<div class="mapa2 mapa-ed" role="group" aria-label="Mapa de esquerda e direita"><span class="eixo t">Ruptura</span><span class="eixo b">Reforma gradual</span><span class="eixo l">Esquerda</span><span class="eixo r">Direita</span>{dots}</div><div class="leg">{leg}</div>
<p class="legenda">Na horizontal, a posição entre esquerda e direita. Na vertical, o quanto a corrente aceita mudar por dentro das regras ou quer romper com elas. São posições aproximadas e uma escolha editorial, discutível: este mapa descreve correntes, não mede você. Algumas, como o populismo, aparecem nos dois lados. Clique em uma para abrir.</p>'''

def page(path, title, desc, corpo, atual='', home=False):
    PAGINAS.append(path)
    erro = path == '404.html'
    desc = desc_seo(path, desc)
    corpo = titulos_ok(corpo)
    pre = '../' * path.count('/')
    url = SITE + '/' + ('' if path == 'index.html' else path)
    full = title if home else f'{title} | {NOME}'
    if len(full) > 60: full = title
    artigo = atual in PAIS_NIVEL or path.split('/')[0] in ('vertentes', 'vieses')
    pre_tag = '<base href="/"/>\n' if erro else ''
    indexa = '<meta name="robots" content="noindex"/>\n' if erro else f'<link rel="canonical" href="{url}"/>\n' + dados(path, title, desc, url, atual, home) + '\n'
    l = lambda u, t: f'<a href="{pre}{u}">{e(t)}</a>'
    niveis = ''.join(l(f'{s}.html', r) for s, r, *_ in NIVEIS)
    ferr = ''.join(l(f'ferramentas/{a}.html', b) for a, b, _, _ in FERR[:7]) + l('ferramentas.html', 'Todas as ferramentas →')
    br = ''.join(l(u, t) for u, t, _ in BR)
    item = lambda u, t: f'<a href="{pre}{u}"{" aria-current=page" if u == atual else ""}>{e(t)}</a>'
    html = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8"/>
{pre_tag}<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{e(full)}</title>
<meta name="description" content="{e(desc)}"/>
{indexa}<meta property="og:type" content="{'article' if artigo else 'website'}"/>
<meta property="og:site_name" content="{NOME}"/>
<meta property="og:title" content="{e(full)}"/>
<meta property="og:description" content="{e(desc)}"/>
<meta property="og:url" content="{url}"/>
<meta property="og:locale" content="pt_BR"/>
<meta property="og:image" content="{SITE}/assets/share.png"/>
<meta property="og:image:width" content="1200"/>
<meta property="og:image:height" content="630"/>
<meta property="og:image:alt" content="{NOME}"/>
{f'<meta property="article:modified_time" content="{ATUALIZADO}"/>' if artigo else ''}
<meta name="twitter:card" content="summary_large_image"/>
<meta name="theme-color" content="#14206b"/>
<link rel="icon" href="{pre}assets/icon.svg" type="image/svg+xml"/>
<link rel="apple-touch-icon" href="{pre}assets/icon-180.png"/>
<link rel="manifest" href="{pre}manifest.webmanifest"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Fraunces:ital,opsz,wght,SOFT@0,9..144,400,100;0,9..144,600,100;0,9..144,700,100;1,9..144,500,100&display=swap"/>
<link rel="stylesheet" href="{pre}assets/style.css"/>
<script src="https://biblioverse.org/superbar.js" async></script>
</head>
<body data-base="{pre}">
<nav id="bvbar" class="bvbar" data-current="politicaparainiciantes" data-offset="none" aria-label="BiblioVerse" style="position:relative;height:44px;background:linear-gradient(90deg,#4f7cff,#7a5cff)"><a href="https://biblioverse.org" style="color:#fff;line-height:44px;padding:0 14px;font-weight:700;text-decoration:none">BiblioVerse</a></nav>
<a class="skip" href="#main">Pular para o conteúdo</a>
<header class="topo"><div class="wrap topo-in">
<a class="marca" href="{pre}index.html">{arte.LOGO}<span>Política<br/>Para Iniciantes</span></a>
<nav class="menu" aria-label="Principal"><div class="drop"><button type="button" aria-expanded="false">Explorar ▾</button><div class="mega" hidden><div><p class="ti">Níveis</p>{niveis}{l('vertentes.html', 'Vertentes políticas')}{l('vieses.html', 'Vieses cognitivos')}{l('debates.html', 'Principais debates')}{l('catalogo.html', 'Tudo, com filtros →')}</div><div><p class="ti">Brasil</p>{br}</div><div><p class="ti">Ferramentas</p>{ferr}</div></div></div>{item('partidos.html', 'Partidos')}{item('politicos.html', 'Políticos')}{item('mundo.html', 'Mundo')}{item('debates.html', 'Debates')}{item('vertentes.html', 'Vertentes')}{item('vieses.html', 'Vieses')}{item('ferramentas.html', 'Ferramentas')}{item('biblioteca.html', 'Biblioteca')}</nav>
<button class="bbusca" type="button" aria-label="Buscar no site">🔍<span> Buscar</span> <kbd>Ctrl K</kbd></button>
<button class="hamb" type="button" aria-label="Abrir menu" aria-expanded="false">☰</button>
</div></header>
<div id="busca" hidden><div class="bcx" role="dialog" aria-label="Buscar no site"><input id="q" type="search" placeholder="Busque um tema ou partido" autocomplete="off"/><div class="res" id="res"></div></div></div>
<main id="main">{corpo}</main>
<footer class="rodape"><div class="wrap rodape-in">
<div><strong>{NOME}</strong><p>Explicações objetivas e simples sobre política, sem camisa de partido. Com fontes e aberto a correções.</p><p>Parte da <a href="https://biblioverse.org">BiblioVerse</a>.</p></div>
<div><p class="ti">Aprender</p><ul><li>{l('comece-aqui.html', 'Comece aqui')}</li><li>{l('iniciante.html', 'Iniciante')}</li><li>{l('intermediario.html', 'Intermediário')}</li><li>{l('avancado.html', 'Avançado')}</li><li>{l('vertentes.html', 'Vertentes políticas')}</li><li>{l('vieses.html', 'Vieses cognitivos')}</li><li>{l('catalogo.html', 'Catálogo')}</li></ul></div>
<div><p class="ti">Brasil</p><ul><li>{l('cargos.html', 'Cargos')}</li><li>{l('poderes.html', 'Poderes')}</li><li>{l('historia.html', 'História')}</li><li>{l('partidos.html', 'Partidos')}</li><li>{l('politicos.html', 'Políticos e figuras')}</li><li>{l('mundo.html', 'Figuras internacionais')}</li><li>{l('ranking-da-mentira.html', 'Ranking da mentira')}</li></ul></div>
<div><p class="ti">Mais</p><ul><li>{l('ferramentas.html', 'Ferramentas')}</li><li>{l('biblioteca.html', 'Biblioteca')}</li><li>{l('sites.html', 'Sites sobre política')}</li><li>{l('debates.html', 'Principais debates')}</li><li>{l('sobre.html', 'Sobre')}</li><li>{l('privacidade.html', 'Política de privacidade')}</li></ul></div>
</div></footer>
<script src="{pre}assets/app.js" defer></script>
</body></html>
'''
    html = html.replace('href="index.html"', 'href="./"').replace('href="../index.html"', 'href="../"')
    full_path = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    open(full_path, 'w', encoding='utf-8', newline='\n').write(html)

def cabeca(kicker, titulo, lede='', pre='', meta=''):
    return f'<section class="cabeca"><div class="wrap"><p class="trilha">{kicker}</p><h1>{e(titulo)}</h1>' + (f'<p class="lede">{lede}</p>' if lede else '') + meta + '</div></section>'
def fontes(ls):
    return '<aside class="fontes"><h2>Fontes e leituras</h2><ul>' + ''.join(f'<li><a href="{e(u)}" {EXT}>{e(t)}</a></li>' for t, u in ls) + '</ul></aside>'
def tabelas(h): return h.replace('<table>', '<div class="tabela"><table>').replace('</table>', '</table></div>')
def tempo_leitura(h): return max(2, round(len(re.sub('<[^>]+>', ' ', h).split()) / 190))
def cartao_licao(l, pre=''):
    tg = ''.join(f'<span class="tag">{e(TEMAS[t])}</span>' for t in l['temas'])
    return f'<a class="cartao" data-licao="{l["slug"]}" data-temas="{" ".join(l["temas"])}" data-nivel="{l["nivel"]}" href="{pre}{l["slug"]}.html"><span class="linha-cartao"><span class="tipo {l["nivel"]}">{e(l["nivel_rot"])}</span></span><h3>{e(l["titulo"])}</h3><p>{e(l["resumo"])}</p><span class="tags" style="margin-top:auto;padding-top:6px">{tg}</span></a>'
def cartao_ferr(a, b, c, n, pre=''): return f'<a class="cartao" data-temas="ferramenta" data-nivel="ferr" href="{pre}ferramentas/{a}.html">{arte.icone(n)}<h3>{e(b)}</h3><p>{e(c)}</p></a>'
def relacionados(l):
    alvos = [x for x in TODAS if x['slug'] != l['slug'] and set(x['temas']) & set(l['temas'])]
    alvos.sort(key=lambda x: (x['nivel'] != l['nivel'], -len(set(x['temas']) & set(l['temas']))))
    return f'<section class="relac"><div class="wrap"><h2>Continue</h2><div class="grade">{"".join(cartao_licao(x) for x in alvos[:3])}</div></div></section>'
def bloco_quiz(q):
    return f'<div class="quiz" data-quiz="{e(json.dumps(q, ensure_ascii=False))}"><p class="k">Teste rápido</p><div class="alvo"></div></div>'

# ---------- início ----------
def inicio():
    niv = ''.join(f'<div><h2><span class="grad {g}">{e(r)}</span></h2><p>{e(d)}</p><a class="btn {g}" href="{s}.html">Começar</a><small>{len(ls)} lições</small></div>' for s, r, ls, _, d, g in NIVEIS)
    temas = ''.join(f'<a href="catalogo.html?tema={k}">{e(v)}</a>' for k, v in TEMAS.items())
    secoes = ''.join(f'<a class="cartao" href="{u}">{arte.icone(i)}<h3>{e(t)}</h3><p>{e(d)}</p></a>' for u, i, t, d in [
        ('catalogo.html', 'ficha', 'Aprenda', f'{len(TODAS)} lições em três níveis, com busca por tema.'),
        ('brasil.html', 'cargo', 'Política brasileira', 'Cargos, Poderes e a história do país.'),
        ('partidos.html', 'cadeira', 'Partidos', f'Dossiê dos {len(P)} partidos e como votaram.'),
        ('politicos.html', 'troca', 'Políticos e figuras', f'{len(F)} perfis, com posições e controvérsias.'),
        ('mundo.html', 'compara', 'Figuras internacionais', f'{len(MUNDO) + len(EXTREMISTAS)} governantes, estadistas, ativistas, jornalistas e extremistas.'),
        ('vertentes.html', 'arvore', 'Vertentes', f'{len(V)} correntes, com forças e contradições.'),
        ('vieses.html', 'valor', 'Vieses cognitivos', f'{len(VIES)} atalhos e erros do pensamento.'),
        ('debates.html', 'valor', 'Principais debates', f'{len(DEBATES_P)} temas: os dois lados e onde os dados pesam.'),
        ('sites.html', 'ficha', 'Sites sobre política', f'{len(SITES_U)} sites para checar, investigar e acompanhar.'),
        ('ferramentas.html', 'compara', 'Ferramentas', f'{len(FERR)} jogos, comparadores e simuladores.'),
        ('ranking-da-mentira.html', 'votos', 'Ranking da mentira', 'Quem mais teve frases checadas como falsas.'),
        ('biblioteca.html', 'livro', 'Biblioteca', 'Livros e leituras para cada nível.'),
    ])
    br = ''.join(f'<a class="cartao" href="{u}"><h3>{e(t)}</h3><p>{e(d)}</p></a>' for u, t, d in BR)
    votos = len(VOTOS)
    corpo = f'''<section class="capa"><div class="wrap capa-in"><div><h1>Entenda a <span class="grifo">política</span>, do <span class="grifo v">básico</span> ao <span class="grifo a">avançado</span>, e pense por você.</h1><p class="lede">Explicações objetivas e simples, com fontes, em três níveis. Do que significa “pólis” até como cada partido brasileiro votou.</p><div class="cta"><a class="btn" href="comece-aqui.html">Comece aqui</a><a class="btn alt" href="vieses.html">Catálogo de vieses</a></div></div>{arte.hero()}</div></section>
<section class="noite"><div class="wrap niveis">{niv}</div></section>
<section class="secao areia"><div class="wrap"><div class="sec-cab"><h2>Explore o site</h2><p>Escolha por onde quer ir.</p></div><div class="grade">{secoes}</div></div></section>
<section class="secao"><div class="wrap numeros"><div><b class="grad">{len(TODAS)}</b><span>lições em três níveis</span></div><div><b class="grad v">{len(P)}</b><span>partidos com dossiê</span></div><div><b class="grad a">{len(DEBATES_P)}</b><span>grandes debates explicados</span></div><div><b class="grad">{len(FERR)}</b><span>ferramentas interativas</span></div></div></section>
<section class="secao areia"><div class="wrap"><div class="sec-cab"><h2>Política brasileira</h2><p>Como o sistema funciona, de onde veio e quem o disputa.</p></div><div class="grade">{br}</div></div></section>
<section class="secao"><div class="wrap capa-in" style="padding-block:0"><div><h2>Liberal, marxista, anarquista?</h2><p style="font-size:1.1rem">{len(V)} vertentes políticas explicadas: o que defendem, de onde vieram e o que dizem seus críticos, em um mapa de dois eixos.</p><a class="btn" href="vertentes.html">Explorar as vertentes</a></div><div class="temas">{"".join(f'<a href="vertentes/{s}.html">{n}</a>' for s, n in [('liberalismo-classico','Liberalismo clássico'),('anarcocapitalismo','Anarcocapitalismo'),('social-democracia','Social-democracia'),('marxismo','Marxismo'),('anarquismo','Anarquismo'),('conservadorismo','Conservadorismo')])}</div></div></section>
<section class="secao"><div class="wrap"><div class="sec-cab"><h2>O que você quer entender?</h2></div><div class="temas">{temas}</div></div></section>
<section class="noite"><div class="wrap secao capa-in" style="padding-block:48px"><div><h2>Onde você está?</h2><p style="color:#fff">Dois testes para conhecer suas ideias antes de julgar as dos outros.</p></div><div class="cta"><a class="btn v" href="https://ethicstest.biblioverse.org/" {EXT}>Teste de Visão Moral</a><a class="btn" href="https://www.idrlabs.com/pt/coordenadas-politicas/teste.php" {EXT}>Teste de Coordenadas Políticas</a></div></div></section>'''
    page('index.html', 'Política Para Iniciantes: do básico ao avançado', 'Guia de política em três níveis, com ferramentas interativas e dossiês dos partidos brasileiros.', corpo, home=True)

def comece():
    _p1 = ['o-que-e-politica', 'valores-e-decisoes', 'esquerda-e-direita', 'democracia', 'como-uma-lei-e-feita', 'o-que-e-um-partido', 'como-votar-bem', 'checagem-de-fatos']
    p1 = sorted((l for l in INICIANTE if l['slug'] in _p1), key=lambda l: _p1.index(l['slug']))
    corpo = cabeca('Comece aqui', 'Novo em política? Comece por aqui', 'Um caminho curto para ter o básico em cerca de uma hora. Depois, siga pelo tema que mais te interessar.')
    corpo += f'''<div class="wrap secao"><h2>1. Entenda o básico</h2><p>Oito lições curtas, nesta ordem: o que é política, valores e fatos, os lados, como o sistema funciona e como votar.</p><div class="grade">{"".join(cartao_licao(l) for l in p1)}</div>
<h2 style="margin-top:2.4rem">2. Saiba quem faz o quê</h2><div class="grade">{cartao_ferr(*FERR[0])}<a class="cartao" href="cargos.html"><h3>O que cada cargo faz</h3><p>Funções, mandatos e limites.</p></a><a class="cartao" href="poderes.html"><h3>Os Poderes</h3><p>Quem faz leis, quem executa, quem julga.</p></a></div>
<h2 style="margin-top:2.4rem">3. Descubra o que você pensa</h2><div class="grade"><a class="cartao" href="https://ethicstest.biblioverse.org/" {EXT}><h3 class="ext">Teste de Visão Moral</h3><p>Como você pensa o certo e o errado.</p></a><a class="cartao" href="https://www.idrlabs.com/pt/coordenadas-politicas/teste.php" {EXT}><h3 class="ext">Teste de Coordenadas Políticas</h3><p>Sua posição em dois eixos.</p></a>{cartao_ferr(*FERR[5])}</div>
<h2 style="margin-top:2.4rem">4. Olhe os partidos</h2><div class="grade">{cartao_ferr(*FERR[2])}{cartao_ferr(*FERR[3])}<a class="cartao" href="partidos.html"><h3>Todos os dossiês</h3><p>{len(P)} partidos.</p></a></div>
<h2 style="margin-top:2.4rem">5. Entre nos debates</h2><div class="grade"><a class="cartao" href="debates.html"><h3>Os principais debates</h3><p>Os dois lados e o que os dados indicam.</p></a><a class="cartao" href="mundo.html"><h3>Figuras internacionais</h3><p>Quem governa, quem inspirou e quem causou o mal.</p></a><a class="cartao" href="sites.html"><h3>Sites sobre política</h3><p>Para checar e acompanhar por conta própria.</p></a></div></div>'''
    page('comece-aqui.html', 'Comece aqui', 'Um caminho curto para entender o básico de política.', corpo, atual='comece-aqui.html')

def catalogo():
    bt = lambda k, v, t: f'<button type="button" data-k="{k}" data-v="{v}" aria-pressed="false">{e(t)}</button>'
    filt = '<div class="filtros" role="group" aria-label="Nível">' + bt('nivel', '', 'Todos os níveis') + ''.join(bt('nivel', s, r) for s, r, *_ in NIVEIS) + bt('nivel', 'ferr', 'Ferramentas') + '</div><div class="filtros" role="group" aria-label="Tema">' + bt('tema', '', 'Todos os temas') + ''.join(bt('tema', k, v) for k, v in TEMAS.items()) + '</div>'
    itens = ''.join(cartao_licao(l) for l in TODAS) + ''.join(cartao_ferr(*f) for f in FERR)
    corpo = cabeca('Biblioteca / Catálogo', 'Tudo em um só lugar', 'Filtre por nível ou por tema.') + f'<div class="wrap secao"><input class="fq" id="fq" type="search" placeholder="Filtrar por palavra" aria-label="Filtrar"/>{filt}<p class="contagem" id="contagem" role="status"></p><div class="grade" id="catalogo">{itens}</div></div>'
    page('catalogo.html', 'Catálogo', 'Todas as lições e ferramentas, com filtros por nível e tema.', corpo, atual='catalogo.html')

# ---------- níveis e lições ----------
def nivel(slug, rot, ls, titulo, desc, g):
    grupos = {}
    for l in ls: grupos.setdefault(l.get('grupo', ''), []).append(l)
    cont = ''
    for gr, its in grupos.items():
        if gr: cont += f'<h2 class="grupo">{e(gr)}</h2>'
        cont += f'<div class="grade">{"".join(cartao_licao(l) for l in its)}</div>'
    if slug == 'iniciante': cont += f'<h2 class="grupo">Saiba quem faz o quê</h2><div class="grade"><a class="cartao" href="cargos.html"><h3>O que cada cargo faz</h3><p>Vereador, prefeito, deputado, senador, presidente.</p></a><a class="cartao" href="poderes.html"><h3>Os três Poderes</h3><p>Quem faz as leis, quem executa, quem julga.</p></a>{cartao_ferr(*FERR[0])}</div>'
    if slug == 'intermediario': cont += f'<h2 class="grupo">No Brasil</h2><div class="grade"><a class="cartao" href="historia.html"><h3>História da política brasileira</h3><p>Da Colônia a 2026.</p></a><a class="cartao" href="partidos.html"><h3>Dossiê dos partidos</h3><p>Os {len(P)} partidos registrados no TSE.</p></a>{cartao_ferr(*FERR[2])}</div>'
    if slug == 'avancado': cont += f'<h2 class="grupo">Experimente</h2><div class="grade">{cartao_ferr(*FERR[8])}{cartao_ferr(*FERR[7])}</div>'
    prog = f'<div class="barra-prog" id="pg-{slug}" data-prog="{",".join(l["slug"] for l in ls)}" style="max-width:420px;background:#ffffff33"><i></i></div><small data-prog-t="pg-{slug}" style="color:#fff"></small>'
    page(f'{slug}.html', titulo, desc, cabeca(f'Nível {rot}', titulo, e(desc), meta=f'<div style="margin-top:1.1rem">{prog}</div>') + f'<div class="wrap secao" style="padding-top:18px">{cont}</div>', atual=f'{slug}.html')

LICAO_DEBATES = {
 'imposto-e-roubo': ['impostos', 'grandes-fortunas'], 'estado-e-mercado': ['tamanho-do-estado', 'privatizacao', 'estatizacao'], 'politicas-publicas': ['programas-sociais', 'subsidios'], 'bem-comum': ['programas-sociais', 'saude'],
 'perigo-de-culpar-o-estrangeiro': ['imigracao'], 'globalizacao': ['imigracao'], 'religiao-e-estado': ['religiao-estado'], 'liberdade-de-expressao': ['liberdade-expressao-debate', 'regulamentacao-redes'], 'respeitar-crencas': ['liberdade-expressao-debate', 'pseudociencias'],
 'checagem-de-fatos': ['fake-news', 'regulamentacao-redes'], 'perigo-da-midia-alternativa': ['fake-news'], 'perigo-dos-grupos-de-mensagem': ['fake-news'], 'perigo-dos-bots': ['regulamentacao-redes', 'inteligencia-artificial'], 'cambridge-analytica': ['bigtechs'], 'camaras-de-eco': ['regulamentacao-redes'],
 'senciocentrismo': ['direitos-animais', 'animais-de-rua'], 'progresso-moral-e-politico': ['direitos-animais', 'identidade-lgbt'], 'politicas-baseadas-em-evidencias': ['evidencias-debate', 'pseudociencias'], 'perigo-do-ultraconservadorismo': ['identidade-lgbt', 'aborto'], 'perigo-do-reacionarismo': ['identidade-lgbt'],
 'regras-e-desobediencia': ['reforma-agraria'], 'presidencialismo-de-coalizao': ['poder-do-stf', 'supersalarios'], 'perigo-de-questionar-a-democracia': ['poder-do-stf', 'voto-obrigatorio'], 'melhorar-a-democracia': ['voto-obrigatorio', 'poder-do-stf'], 'teorias-da-justica': ['grandes-fortunas', 'programas-sociais'],
 'testar-visao-moral': ['aborto', 'direitos-animais'], 'poder-paralelo': ['narcoterrorismo', 'seguranca-publica'],
 'como-uma-lei-e-feita': ['poder-do-stf'], 'o-que-e-um-partido': ['voto-obrigatorio', 'representatividade'], 'economia-para-entender-politica': ['impostos', 'previdencia', 'desemprego'], 'perigo-do-populismo': ['representatividade', 'poder-do-stf'], 'corrupcao': ['supersalarios', 'subsidios'], 'como-ler-a-midia-tradicional': ['fake-news', 'regulamentacao-redes'], 'pesquisas-eleitorais': ['voto-obrigatorio', 'fake-news'], 'perigo-do-maniqueismo': ['seguranca-publica', 'armas'], 'politica-do-medo': ['seguranca-publica', 'imigracao'], 'etica-normativa': ['eutanasia', 'aborto'], 'esquerda-e-direita': ['tamanho-do-estado'], 'contrato-social': ['impostos'], 'perigo-das-revolucoes': ['reforma-agraria'],
}
APELIDOS_MUNDO = {'Franklin Roosevelt': 'Franklin D. Roosevelt', 'Mustafa Kemal Atatürk': 'Mustafa Kemal Atatürk', 'Martin Luther King Jr.': 'Martin Luther King Jr.'}
def debates_da_licao(l):
    its = [d for d in DEBATES_P if d['s'] in LICAO_DEBATES.get(l['slug'], [])]
    if not its: return ''
    return '<div class="nota"><strong>No debate público:</strong> ' + ', '.join(f'<a href="debates/{d["s"]}.html">{e(d["n"])}</a>' for d in its) + '.</div>'
def nomes_para_mundo(html):
    for f in MUN:
        html = html.replace(f'<strong>{f["nome"]}</strong>', f'<a href="mundo/{f["slug"]}.html"><strong>{f["nome"]}</strong></a>')
    return html.replace('<strong>Franklin Roosevelt</strong>', '<a href="mundo/franklin-d-roosevelt.html"><strong>Franklin Roosevelt</strong></a>')

def indice(l, ls):
    i = l['i']; n = len(ls)
    def seta(alvo, rel, sim, rot):
        if alvo: return f'<a class="indice-seta" rel="{rel}" href="{alvo["slug"]}.html" aria-label="{rot}: {e(alvo["titulo"])}" title="{rot}: {e(alvo["titulo"])}">{sim}</a>'
        return f'<span class="indice-seta off" aria-hidden="true">{sim}</span>'
    pontos = ''
    for j, x in enumerate(ls):
        rot = f'Lição {j + 1}: {e(x["titulo"])}'
        atual = ' aria-current="page"' if j == i else ''
        pontos += f'<li><a href="{x["slug"]}.html" data-ponto="{x["slug"]}" title="{rot}" aria-label="{rot}"{atual}></a></li>'
    return f'<nav class="indice {l["nivel"]}" aria-label="Lições do nível {e(l["nivel_rot"])}"><div class="wrap"><p class="indice-pos"><a href="{l["nivel"]}.html">{e(l["nivel_rot"])}</a> · Lição {i + 1} de {n}</p><div class="indice-nav">{seta(ls[i - 1] if i else None, "prev", "←", "Lição anterior")}<ol>{pontos}</ol>{seta(ls[i + 1] if i + 1 < n else None, "next", "→", "Próxima lição")}</div></div></nav>'

def licao(l, ls):
    i = l['i']; ant = ls[i - 1] if i else None; prox = ls[i + 1] if i + 1 < len(ls) else None
    pager = '<nav class="pager" aria-label="Lições">'
    if ant: pager += f'<a href="{ant["slug"]}.html"><small>← Anterior</small>{e(ant["titulo"])}</a>'
    if prox: pager += f'<a class="prox" href="{prox["slug"]}.html"><small>Próxima →</small>{e(prox["titulo"])}</a>'
    pager += '</nav>'
    ordem = [n[0] for n in NIVEIS]
    if not prox and l['nivel'] != ordem[-1]:
        seg = NIVEIS[ordem.index(l['nivel']) + 1]
        pager += f'<div class="fim-nivel"><p class="ti">Você chegou ao fim do nível {e(l["nivel_rot"])}</p><p>Continue com {len(seg[2])} lições do nível {e(seg[1])}.</p><a class="btn {seg[5]}" href="{seg[0]}.html">Ir para o curso {e(seg[1])} →</a></div>'
    min_ = tempo_leitura(l['corpo'])
    tg = ''.join(f'<a class="tag" href="catalogo.html?tema={t}">{e(TEMAS[t])}</a>' for t in l['temas'])
    meta = f'<div class="meta"><span class="tipo {l["nivel"]}">{e(l["nivel_rot"])}</span>{tg}<span>{min_} min de leitura</span></div>'
    topo = cabeca(f'<a href="{l["nivel"]}.html">{e(l["nivel_rot"])}</a>' + (f' / {e(l["grupo"])}' if l.get('grupo') else ''), l['titulo'], e(l['resumo']), meta=meta)
    lado = f'''<aside class="lado"><div class="caixa"><h2>Em resumo</h2><dl><dt>Nível</dt><dd>{e(l["nivel_rot"])}</dd><dt>Tempo</dt><dd>{min_} minutos</dd><dt>Temas</dt><dd>{e(", ".join(TEMAS[t] for t in l["temas"]))}</dd></dl></div><div class="caixa toc-caixa"><h2>Nesta lição</h2><ul class="toc"></ul></div><button class="marcar" type="button" data-id="{l["slug"]}">Marcar como lida</button></aside>'''
    corpo = indice(l, ls) + topo + f'<div class="wrap layout"><article class="leitura">{(nomes_para_mundo(tabelas(l["corpo"])) if l["slug"] in ("maiores-estadistas", "maiores-ativistas") else tabelas(l["corpo"])).replace("<!--MAPA-ED-->", f'<h3 id="mapa">Um mapa em coordenadas</h3>{mapa_ed()}')}{debates_da_licao(l)}{bloco_quiz(l["quiz"])}{fontes(l["fontes"])}{pager}</article>{lado}</div>' + relacionados(l)
    page(f'{l["slug"]}.html', l['titulo'], l['resumo'], corpo, atual=f'{l["nivel"]}.html')

# ---------- Brasil ----------
def brasil_hub():
    extra = [('presidencialismo-de-coalizao.html', 'Presidencialismo de coalizão', 'Por que o presidente negocia tanto, e o que é o Centrão.'), ('politicas-publicas.html', 'Orçamento e políticas públicas', 'De onde vem e para onde vai o dinheiro.'), ('como-votar-bem.html', 'Como votar da melhor forma', 'Um roteiro para a próxima eleição.'), ('numero-de-projetos.html', 'O perigo de contar projetos', 'O que olhar em um mandato.'), ('como-uma-lei-e-feita.html', 'Como uma lei é feita', 'Da proposta ao veto, e quem pode barrar.'), ('corrupcao.html', 'Corrupção', 'Por que existe e o que funciona contra ela.')]
    cards = ''.join(f'<a class="cartao" href="{u}"><h3>{e(t)}</h3><p>{e(d)}</p></a>' for u, t, d in BR + extra)
    page('brasil.html', 'Política brasileira', 'Cargos, poderes, história, partidos e checagem: como a política funciona no Brasil.', cabeca('Brasil', 'Política brasileira', 'Como o sistema funciona, de onde veio e quem o disputa.') + f'<div class="wrap secao"><div class="grade">{cards}</div></div>', atual='brasil.html')

def cargos():
    cards = ''
    for c in CARGOS:
        cards += f'<div class="cargo"><span class="tipo">{e(c["esfera"])} · {e(c["poder"])}</span><h3 style="margin-top:.6rem">{e(c["n"])}</h3><dl><dt>Mandato</dt><dd>{e(c["mandato"])}</dd><dt>Idade mínima</dt><dd>{e(c["idade"])}</dd><dt>Quantos</dt><dd>{e(c["vagas"])}</dd><dt>Como chega lá</dt><dd>{e(c["eleicao"])}</dd></dl><p><strong>Faz:</strong> {e(c["faz"])}</p><p class="nao"><strong>Não faz:</strong> {e(c["nao"])}</p></div>'
    corpo = cabeca('Brasil', 'O que cada cargo faz', 'Saber quem faz o quê é o melhor remédio contra promessa impossível.')
    corpo += f'''<div class="wrap secao"><div class="tabela"><table><thead><tr><th>Esfera</th><th>Executivo (governa)</th><th>Legislativo (faz leis e fiscaliza)</th></tr></thead><tbody><tr><td>União</td><td>Presidente</td><td>Deputados federais e senadores</td></tr><tr><td>Estado e DF</td><td>Governador</td><td>Deputados estaduais ou distritais</td></tr><tr><td>Município</td><td>Prefeito</td><td>Vereadores</td></tr></tbody></table></div>
<div class="cta"><a class="btn" href="ferramentas/quem-faz-o-que.html">Jogar “Quem faz o quê?”</a></div>
<div class="grade" style="grid-template-columns:repeat(auto-fill,minmax(min(310px,100%),1fr))">{cards}</div>
<div class="nota"><strong>Quem cuida do quê, em geral:</strong> a creche e o posto de saúde costumam ser do município; o ensino médio e a polícia, do estado; as universidades federais, a Previdência e a Polícia Federal, da União. O SUS e a educação são compartilhados. Por isso vale cobrar a esfera certa.</div>
{fontes([('Constituição Federal', 'https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm'), ('Toda Política: guia do candidato', 'https://www.todapolitica.com/'), ('Politize!', 'https://www.politize.com.br/'), ('TSE', 'https://www.tse.jus.br/')])}</div>'''
    page('cargos.html', 'O que cada cargo faz', 'Função, mandato e limites de vereador, prefeito, deputado, governador, senador, presidente e outros cargos no Brasil.', corpo, atual='brasil.html')

def poderes():
    rows = ''.join(f'<tr><td><strong>{e(n)}</strong></td><td>{e(g)}</td><td>{e(q)}</td><td>{e(f)}</td></tr>' for n, g, q, f in ORGAOS)
    corpo = cabeca('Brasil', 'Os Poderes e suas funções', 'Quem faz a lei, quem a executa e quem julga não podem ser a mesma pessoa. Poder sem limite vira abuso.')
    corpo += f'''<div class="wrap estreito leitura secao"><div class="pilares"><div><h3>Executivo</h3><p><strong>Governa.</strong> Coloca as leis em prática e administra o orçamento. Presidente, governadores, prefeitos, ministros.</p></div><div><h3>Legislativo</h3><p><strong>Faz leis e fiscaliza.</strong> Aprova o orçamento e abre CPIs. Congresso, assembleias e câmaras municipais.</p></div><div><h3>Judiciário</h3><p><strong>Interpreta e julga.</strong> Aplica a lei e guarda a Constituição. STF, tribunais e juízes.</p></div></div>
<h2>Freios e contrapesos</h2><div class="tabela"><table><thead><tr><th>Quem</th><th>Pode</th><th>Sobre quem</th></tr></thead><tbody><tr><td>Presidente</td><td>Vetar leis e indicar ministros do STF</td><td>Legislativo e Judiciário</td></tr><tr><td>Congresso</td><td>Derrubar vetos, abrir CPIs, julgar impeachment e aprovar indicados</td><td>Executivo e Judiciário</td></tr><tr><td>STF</td><td>Anular leis e atos inconstitucionais; julgar autoridades</td><td>Executivo e Legislativo</td></tr></tbody></table></div>
<h2>Como uma lei nasce</h2><ol><li>Alguém propõe: parlamentar, presidente, STF em certos casos, ou cidadãos (iniciativa popular).</li><li>Comissões analisam.</li><li>O plenário vota, e a outra casa revisa.</li><li>O presidente sanciona ou veta.</li><li>O Congresso pode derrubar o veto.</li></ol><p>Emendas à Constituição exigem 3/5 dos votos, em dois turnos, nas duas casas. Medidas provisórias valem de imediato, mas perdem efeito sem aprovação do Congresso.</p>
<h2>Como tirar um presidente</h2><p>O impeachment exige crime de responsabilidade. A Câmara autoriza por 2/3, e o Senado julga, com 2/3 para condenar. Foi usado contra Collor (1992, que renunciou durante o julgamento) e Dilma (2016).</p></div>
<div class="wrap secao" style="padding-top:0"><h2 style="margin-bottom:12px">Os outros órgãos</h2><div class="tabela"><table><thead><tr><th>Órgão</th><th>Onde fica</th><th>Quem compõe</th><th>O que faz</th></tr></thead><tbody>{rows}</tbody></table></div>
{fontes([('Constituição Federal', 'https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm'), ('Toda Política', 'https://www.todapolitica.com/'), ('Agência Senado', 'https://www12.senado.leg.br/noticias')])}</div>'''
    page('poderes.html', 'Os Poderes e suas funções', 'Executivo, Legislativo, Judiciário e órgãos como MP, TCU e TSE: o que faz cada um e como se limitam.', corpo, atual='brasil.html')

def historia():
    li = ''.join(f'<li><b>{e(a)}</b><div><h3>{e(t)}</h3><p>{e(d)}</p></div></li>' for a, t, d in HISTORIA)
    corpo = cabeca('Brasil', 'História da política brasileira', 'Golpes, constituições, ditaduras e aberturas. Muita coisa de hoje vem daqui.')
    corpo += f'''<div class="wrap estreito secao"><ol class="tempo">{li}</ol>
<div class="nota"><strong>O que se repete:</strong> o Brasil já teve sete constituições e várias rupturas. O período desde 1985 é o mais longo de democracia com voto amplo da nossa história.</div>
{fontes([('História do Brasil (Wikipédia)', 'https://pt.wikipedia.org/wiki/Hist%C3%B3ria_do_Brasil'), ('Comissão Nacional da Verdade', 'https://cnv.memoriasreveladas.gov.br/'), ('Nexo Jornal', 'https://www.nexojornal.com.br/'), ('Agência Brasil', 'https://agenciabrasil.ebc.com.br/')])}</div>'''
    page('historia.html', 'História da política brasileira', 'Da Colônia à eleição de 2026: uma linha do tempo da política no Brasil.', corpo, atual='brasil.html')

# ---------- partidos ----------
def linha_voto(pid):
    h = ''
    for v in V_JSON:
        c, x = voto_de(pid, v)
        if not x: continue
        t = x['s'] + x['n'] + x['o'] or 1
        h += f'<div class="vbar" style="grid-template-columns:minmax(120px,190px) 1fr 66px"><span title="{e(v["desc"])}"><strong>{e(v["rot"])}</strong> <small>{v["ano"]}</small></span><span class="vtrilho"><i class="vs" style="width:{x["s"] / t * 100:.1f}%"></i><i class="vn" style="width:{x["n"] / t * 100:.1f}%"></i><i class="vo" style="width:{x["o"] / t * 100:.1f}%"></i></span><span>{x["s"]} × {x["n"]}</span></div>'
    return h
LEG = '<div class="leg"><span><i class="vs"></i>A favor</span><span><i class="vn"></i>Contra</span><span><i class="vo"></i>Abstenção ou obstrução</span></div>'
def partidos():
    ord_ = sorted(P, key=lambda p: (ORDEM_ESP.index(p['esp']), p['s']))
    cards = ''.join(f'<a class="cartao partido" href="partidos/{p["id"]}.html" data-e="{e(FAIXA[p["esp"]])}"><span class="n">{p["num"]}</span><span class="sig">{e(p["s"])}</span><p>{e(p["n"])}</p><div class="esp" aria-hidden="true"><i style="left:{ESP_POS[p["esp"]]}%"></i></div><p><small>{e(p["esp"])}</small></p></a>' for p in ord_)
    bots = '<button type="button" data-e="" aria-pressed="true">Todos</button>' + ''.join(f'<button type="button" data-e="{f}" aria-pressed="false">{f}</button>' for f in ['Esquerda', 'Centro-esquerda', 'Centro', 'Centro-direita', 'Direita'])
    alt = {}
    pts = ''
    for p in ord_:
        x = ESP_POS[p['esp']]; n = alt.get(x, 0); alt[x] = n + 1
        pts += f'<a href="partidos/{p["id"]}.html" style="left:{x}%;bottom:{38 + n * 22}px">{e(p["s"])}</a>'
    corpo = cabeca('Brasil', 'Dossiê dos partidos brasileiros', f'Os {len(P)} partidos registrados no TSE: origem, líderes, casos, votos reais e mudanças de posição.')
    corpo += f'''<div class="wrap secao"><div class="sec-cab"><h2>O mapa</h2><p>Clique em uma sigla.</p></div><div class="mapa" style="height:{38 + max(alt.values()) * 22 + 24}px">{pts}<div class="trilho"></div><span style="left:6%">Esquerda</span><span style="left:50%">Centro</span><span style="left:94%">Direita</span></div>
<div class="nota"><strong>Como ler:</strong> a posição é aproximada e muda conforme quem classifica. Usamos o Valor Econômico (2025), via Wikipédia, e a Wikipédia para Missão e Democrata. Federações: Brasil da Esperança (PT, PCdoB, PV), PSDB Cidadania, PSOL REDE, Renovação Solidária (PRD, Solidariedade) e União Progressista (União, PP).</div>
<div class="cta"><a class="btn" href="ferramentas/comparador.html">Comparar partidos</a><a class="btn alt" href="ferramentas/como-votaram.html">Como votaram</a><a class="btn alt" href="ferramentas/arvore-dos-partidos.html">Árvore dos partidos</a></div>
<input class="fq" id="fq" type="search" placeholder="Filtrar por nome, sigla ou número" aria-label="Filtrar partidos"/><div class="filtros" role="group" aria-label="Espectro">{bots}</div><div class="grade" id="partidos">{cards}</div></div>'''
    page('partidos.html', 'Dossiê dos partidos brasileiros', f'Origem, presidentes, casos, votos e alinhamento dos {len(P)} partidos registrados no TSE.', corpo, atual='partidos.html')
    for i, p in enumerate(P):
        wiki = W + quote(p['wiki'], safe='()_')
        pres = ''.join(f'<li>{e(x)}</li>' for x in p['pres_lista'])
        aviso = '<p class="legenda">Lista parcial: não confirmamos todos os nomes e períodos deste partido.</p>' if p['parcial'] else ''
        casos = ''.join(f'<div class="caso"><span class="st {st}">{ROTULO[st]}</span><h3>{e(t)}</h3><p>{e(x)} <a href="{e(u)}" {EXT}>{e(fr)} ↗</a></p></div>' for st, t, x, fr, u in p['casos'])
        tl = ''.join(f'<li><b>{a}</b><span>{e(t)}</span></li>' for a, t in sorted(p['linha'], key=lambda x: x[0]))
        pr = PRESID.get(p['id'], [])
        prs = ''
        if pr:
            prs = '<h2>Eleições presidenciais</h2><p class="legenda">Candidato próprio ou apoiado, com o percentual do resultado que a Wikipédia registra para aquela chapa (no 2º turno, quando houve).</p><div class="tabela"><table><thead><tr><th>Ano</th><th>Candidato</th><th>Votos</th></tr></thead><tbody>' + ''.join(f'<tr><td>{x["ano"]}</td><td>{e(x["cand"])}</td><td>{x["pct"]}%</td></tr>' for x in pr) + '</tbody></table></div>'
        vt = linha_voto(p['id'])
        vts = f'<h2>Como votou na Câmara</h2><p>Dados oficiais: a favor × contra na bancada do partido na época.</p>{LEG}{vt}<p class="legenda">Fonte: <a href="https://dadosabertos.camara.leg.br/" {EXT}>Dados Abertos da Câmara</a>. <a href="../ferramentas/como-votaram.html">Ver todos os partidos</a>.</p>' if vt else '<h2>Como votou na Câmara</h2><p>O partido não aparece com bancada própria nas votações que reunimos. Veja <a href="../ferramentas/como-votaram.html">a comparação</a>.</p>'
        f = [('Wikipédia: ' + p['n'], wiki), ('Partidos registrados no TSE', 'https://www.tse.jus.br/partidos/partidos-registrados-no-tse/registrados-no-tse'), ('Bancadas na Câmara', 'https://www.camara.leg.br/deputados/quem-sao'), ('Buscar na Lupa', 'https://www.agencialupa.org/?s=' + quote(p['n'])), ('Buscar no Aos Fatos', 'https://www.aosfatos.org/noticias/?q=' + quote(p['n']))] + p.get('fx', [])
        ant, prox = P[i - 1], P[(i + 1) % len(P)]
        mesmos = [x for x in P if x['id'] != p['id'] and ((p['fed'] and x['fed'] == p['fed']) or FAIXA[x['esp']] == FAIXA[p['esp']])][:3]
        rel = ''.join(f'<a class="cartao partido" href="{x["id"]}.html"><span class="n">{x["num"]}</span><span class="sig">{e(x["s"])}</span><p>{e(x["resumo"])}</p></a>' for x in mesmos)
        compara = f'../ferramentas/comparador.html?a={p["id"]}&b={"pl" if p["id"] != "pl" else "pt"}'
        lado = f'''<aside class="lado"><div class="caixa"><h2>Em resumo</h2><dl><dt>Número</dt><dd>{p["num"]}</dd><dt>Fundação</dt><dd>{e(p["ano"])}</dd><dt>Registro no TSE</dt><dd>{e(p["reg"])}</dd><dt>Presidente</dt><dd>{e(p["pres"])}</dd>{"<dt>Federação</dt><dd>" + e(p["fed"]) + "</dd>" if p["fed"] else ""}<dt>Espectro</dt><dd>{e(p["esp"])}<div class="esp" aria-hidden="true"><i style="left:{ESP_POS[p["esp"]]}%"></i></div></dd></dl></div><div class="caixa toc-caixa"><h2>Neste dossiê</h2><ul class="toc"></ul></div><a class="btn alt" style="text-align:center" href="{compara}">Comparar</a></aside>'''
        meta = f'<div class="meta"><span class="tipo">Dossiê</span><a class="tag" href="../partidos.html">{e(p["esp"])}</a><span>Atualizado em novembro de 2026</span></div>'
        espn = '<div class="nota"><strong>Sobre o espectro:</strong> ' + p['esp_nota'] + '</div>' if p.get('esp_nota') else ''
        corpo = cabeca('<a href="../partidos.html">Partidos</a>', f'{p["s"]}: {p["n"]}' if p['s'].lower() != p['n'].lower() else p['n'], e(p['resumo']), meta=meta)
        corpo += f'''<div class="wrap layout"><article class="leitura"><h2>Fundação e contexto</h2><p>{e(p["contexto"])}</p><p><strong>Fundadores e nomes da origem:</strong> {e(p["fund"])}</p>
<h2>Linha do tempo</h2><ol class="tempo-p">{tl}</ol>
<h2>Presidentes</h2><ul class="pres">{pres}</ul>{aviso}
<h2>Políticos de destaque</h2><p>{liga_nomes(e(p["dest"]))}</p>
<h2>Polêmicas e escândalos</h2><div class="nota alerta" style="font-size:.92rem;margin-top:0">Acusação não é condenação. Veja a etiqueta de cada caso, que resume a situação que conseguimos apurar, e o link da fonte. Decisões podem mudar.</div>{casos}
<h2>Valores</h2><p>{e(p["val"])}</p>{espn}
<h2>Projetos relevantes</h2><p>{e(p["proj"])}</p>
{vts}
<h2>Votações e momentos históricos</h2><p>{e(p["vot"])}</p>
{prs}
<h2>Como o alinhamento mudou</h2><p>{e(p["ali"])}</p>
{fontes(f)}
<nav class="pager" aria-label="Partidos"><a href="{ant["id"]}.html"><small>← Anterior</small>{e(ant["s"])}</a><a class="prox" href="{prox["id"]}.html"><small>Próximo →</small>{e(prox["s"])}</a></nav></article>{lado}</div>
<section class="relac"><div class="wrap"><h2>Partidos próximos</h2><div class="grade">{rel}</div></div></section>'''
        page(f'partidos/{p["id"]}.html', f'{p["s"]}: dossiê do partido', f'{p["n"]}: fundação, presidentes, escândalos, votos e mudanças de alinhamento.', corpo, atual='partidos.html')

# ---------- figuras ----------
AVISO = 'É preciso ter cuidado: alta tendenciosidade.'
ATENTO = 'Fique atento nas contradições.'
COR_CAT = {c: i for i, c in enumerate(CATEGORIAS)}
def tag_cat(c): return f'<span class="tipo cat c{COR_CAT[c]}">{e(c)}</span>'
def alerta(cat): return AVISO if cat.startswith('Extrema') else ATENTO if cat in ('Direita', 'Esquerda') else ''
def slug_de(n):
    s = unicodedata.normalize('NFD', n); s = ''.join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')
FIG = [dict(nome=x[0], wiki=x[1], cat=x[2], tipo=x[3], pid=x[4], quem=x[5], porque=x[6], pol=x[7], slug=slug_de(x[0])) for x in F]
PONDER = {n: (d, u) for n, d, u in PESSOAS}
for f in FIG:
    if f['nome'] in PONDER: f['quem'], f['perfil'] = PONDER[f['nome']]
assert all(any(f['nome'] == n for f in FIG) for n in PONDER)
for n in list(DEBATES) + list(ANTIGOS):
    assert any(f['nome'] == n for f in FIG), n
for f in FIG:
    f['cand'] = DEBATES.get(f['nome'], []) + ANTIGOS.get(f['nome'], [])
    f['deb'] = f['nome'] in DEBATES
FIG.sort(key=lambda f: (CATEGORIAS.index(f['cat']), slug_de(f['nome'])))
assert len({f['slug'] for f in FIG}) == len(FIG)
def extrema(f): return f['cat'].startswith('Extrema')
def liga_nomes(txt):
    for f in sorted(FIG, key=lambda f: -len(f['nome'])):
        n = e(f['nome'])
        txt = re.sub(r'(?<![>\w])' + re.escape(n) + r'(?![\w<])', f'<a href="../politicos/{f["slug"]}.html">{n}</a>', txt)
    return txt
def cartao_fig(f, pre=''):
    aviso = f'<span class="aviso-ext">⚠ {alerta(f["cat"])}</span>' if alerta(f['cat']) else ''
    return f'<a class="cartao fig" href="{pre}{f["slug"]}.html" data-cat="{e(f["cat"])}" data-tipo="{e(f["tipo"])}" data-deb="{1 if f["deb"] else ""}"><h3>{e(f["nome"])}</h3><span class="linha-cartao">{tag_cat(f["cat"])}<span class="tipo ferr">{e(f["tipo"])}</span>{'<span class="tipo intermediario">Debate presidencial</span>' if f['deb'] else ''}</span><p>{e(f["quem"])}</p>{aviso}</a>'
def figuras():
    bc = '<div class="filtros" role="group" aria-label="Espectro"><button type="button" data-k="cat" data-v="" aria-pressed="true">Todas</button>' + ''.join(f'<button type="button" data-k="cat" data-v="{c}" aria-pressed="false">{c}</button>' for c in CATEGORIAS) + '</div>'
    bt = '<div class="filtros" role="group" aria-label="Tipo"><button type="button" data-k="tipo" data-v="" aria-pressed="true">Todos os tipos</button>' + ''.join(f'<button type="button" data-k="tipo" data-v="{c}" aria-pressed="false">{c}</button>' for c in TIPOS) + '</div><div class="filtros" role="group" aria-label="Debates"><button type="button" data-k="deb" data-v="" aria-pressed="true">Com ou sem debate</button><button type="button" data-k="deb" data-v="1" aria-pressed="false">Foram a debates presidenciais na TV (2018, 2022 e 2026)</button></div>'
    gr = ''
    for c in CATEGORIAS:
        its = [f for f in FIG if f['cat'] == c]
        av = f'<p class="aviso-ext grande">⚠ {AVISO} Confira as afirmações destas figuras em mais de uma fonte.</p>' if c.startswith('Extrema') else f'<p class="aviso-ext grande">⚠ {ATENTO}</p>' if alerta(c) else ''
        gr += f'<section class="grupo-fig" data-grupo="{c}"><h2 class="grupo">{tag_cat(c)} <small>({len(its)})</small></h2>{av}<div class="grade">' + ''.join(cartao_fig(f, 'politicos/') for f in its) + '</div></section>'
    corpo = cabeca('Brasil', 'Políticos e figuras políticas', f'{len(FIG)} dossiês de políticos, jornalistas, intelectuais, artistas e influenciadores, de todo o espectro.')
    corpo += f'''<div class="wrap secao"><div class="nota alerta" style="margin-top:0"><strong>Como ler as categorias:</strong> a posição é uma estimativa deste site, baseada em como cada pessoa age, o que defende e como é descrita pela imprensa e pela Wikipédia. Rótulos são contestáveis, muita gente os rejeita e as posições mudam com o tempo. Em cada dossiê, explicamos o motivo. Estar em uma categoria não é um elogio nem uma acusação. Discorda? Mande a fonte.</div>
<input class="fq" id="fq" type="search" placeholder="Buscar por nome" aria-label="Buscar figura"/>{bc}{bt}<p class="contagem" id="contagem" role="status"></p><div id="figuras">{gr}</div><p class="legenda">Procura alguém de fora do Brasil? Veja as <a href="mundo.html">figuras internacionais</a>.</p></div>'''
    page('politicos.html', 'Políticos e figuras políticas', 'Cards e dossiês de políticos e influenciadores brasileiros, da extrema-esquerda à extrema-direita.', corpo, atual='politicos.html')
    for f in FIG:
        wiki = '' if f['wiki'] is None else W + quote(f['wiki'] or f['nome'], safe='()_').replace('%20', '_')
        par = PARTIDO.get(f['pid'])
        pol = ''.join(f'<div class="caso"><span class="st {st}">{ROTULO[st]}</span><p style="margin-top:.35rem">{e(x)}</p></div>' for st, x in f['pol']) or '<p>Não registramos aqui nenhum caso de grande repercussão. Isso não significa que não exista: consulte as fontes abaixo.</p>'
        aviso = f'<div class="nota alerta aviso-pag"><strong>⚠ {AVISO}</strong> Esta categoria reúne discursos muito militantes. Confira o que é dito em mais de uma fonte.</div>' if extrema(f) else f'<div class="nota alerta aviso-pag"><strong>⚠ {ATENTO}</strong> Compare o que é dito com o que é feito, e com o que a mesma pessoa já defendeu.</div>' if alerta(f['cat']) else ''
        fontes_f = ([('Wikipédia: ' + f['nome'], wiki)] if wiki else []) + [(f'Wikipédia: eleição presidencial de {x[0]}', f'https://pt.wikipedia.org/wiki/Elei%C3%A7%C3%A3o_presidencial_no_Brasil_em_{x[0]}') for x in DEBATES.get(f['nome'], [])] + [('Buscar na Lupa', 'https://www.agencialupa.org/?s=' + quote(f['nome'])), ('Buscar no Aos Fatos', 'https://www.aosfatos.org/noticias/?q=' + quote(f['nome'])), ('Buscar no Nexo Jornal', 'https://www.nexojornal.com.br/search?q=' + quote(f['nome']))]
        lado = f'<aside class="lado"><div class="caixa"><h2>Em resumo</h2><dl><dt>Categoria</dt><dd>{e(f["cat"])}</dd><dt>Tipo</dt><dd>{e(f["tipo"])}</dd>' + (f'<dt>Partido</dt><dd><a href="../partidos/{par["id"]}.html">{e(par["s"])}</a></dd>' if par else '') + '</dl></div></aside>'
        mesmos = [x for x in FIG if x['cat'] == f['cat'] and x['slug'] != f['slug']]
        i = FIG.index(f) % max(1, len(mesmos))
        rel = ''.join(cartao_fig(x) for x in (mesmos[i:] + mesmos[:i])[:3])
        corpo = cabeca('<a href="../politicos.html">Políticos e figuras</a>', f['nome'], e(f['quem']), meta=f'<div class="meta">{tag_cat(f["cat"])}<span class="tipo ferr">{e(f["tipo"])}</span><span>Atualizado em novembro de 2026</span></div>')
        corpo += f'''<div class="wrap layout"><article class="leitura">{aviso}{f'<div class="nota" style="margin-top:0"><a href="{e(f["perfil"])}" {EXT}>Ver perfil ↗</a></div>' if f.get('perfil') else ''}<h2>Por que nesta categoria</h2><p>{e(f["porque"])}</p><p class="legenda">Classificação aproximada e contestável. <a href="../politicos.html">Entenda o critério</a>.</p>{f'<h2>Partido</h2><p>Ligação com o <a href="../partidos/{par["id"]}.html">{e(par["n"])}</a>, pela filiação atual ou pela trajetória. Veja o dossiê.</p>' if par else ''}
{f'<h2>Candidaturas à Presidência</h2><ul class="tempo-p">' + ''.join(f'<li><b>{a}</b><span>{e(x)}</span></li>' for a, x in sorted(f["cand"])) + '</ul>' if f['cand'] else ''}<h2>Polêmicas e processos</h2>{pol}<p class="legenda">Acusação não é condenação. Decisões podem mudar.</p>{fontes(fontes_f)}</article>{lado}</div><section class="relac"><div class="wrap"><h2>Na mesma categoria</h2><div class="grade">{rel}</div></div></section>'''
        page(f'politicos/{f["slug"]}.html', f['nome'], f'{f["nome"]}: {f["quem"]}', corpo, atual='politicos.html')

# ---------- mundo ----------
MUN = [dict(nome=x[0], wiki=x[1], cat=x[2], grupo=x[3], pais=x[4], reg=x[5], quem=x[6], porque=x[7], pol=x[8], slug=slug_de(x[0])) for x in MUNDO]
MUN += [dict(nome=x[0], wiki=x[1], cat=x[2], grupo=GRUPO_EXT, pais=x[3], reg=x[4], quem=x[5], como=x[6], mal=x[7], critica=x[8], licao=x[9], vitimas=x[10], pol=[], porque='', slug=slug_de(x[0])) for x in EXTREMISTAS]
assert len({f['slug'] for f in MUN}) == len(MUN)
def cartao_m(f, pre=''):
    aviso = f'<span class="aviso-ext">⚠ {alerta(f["cat"])}</span>' if alerta(f['cat']) else ''
    return f'<a class="cartao fig" href="{pre}{f["slug"]}.html" data-cat="{e(f["cat"])}" data-tipo="{e(f["grupo"])}" data-reg="{e(f["reg"])}"><h3>{e(f["nome"])}</h3><span class="linha-cartao">{tag_cat(f["cat"])}<span class="tipo ferr">{e(f["pais"])}</span></span><p>{e(f["quem"])}</p>{aviso}</a>'
MEMORIA = '<p class="aviso-ext grande">Estes políticos causaram o mal: guerras, massacres, tortura e genocídios. Estão aqui para não serem esquecidos, e para que aprendamos a reconhecer como chegaram ao poder. Explicar não é defender.</p>'
def pagina_extremista(f):
    return f'''<div class="nota alerta aviso-pag"><strong>Este político causou o mal.</strong> Esta página não presta homenagem. Ela existe para lembrar as vítimas e para ajudar a reconhecer e impedir que isso se repita. Explicar não é defender.</div>
<h2>Como chegou ao poder</h2><p>{f["como"]}</p>
<h2>O mal que causou</h2><p>{f["mal"]}</p>
<h2>Uma crítica</h2><p>{f["critica"]}</p>
<h2>Como não repetir</h2><p>{f["licao"]}</p>
<ol class="roteiro"><li>Desconfie de quem promete salvar o país e pede poder sem limites.</li><li>Não aceite que um grupo de pessoas seja tratado como praga ou inimigo interno.</li><li>Defenda imprensa livre, tribunais independentes e o direito de oposição, mesmo para quem você não gosta.</li><li>Recuse a ideia de que os fins justificam os meios, de qualquer lado.</li><li>Guarde a memória e não aceite negação dos crimes.</li></ol>
<p>Leia também: <a href="../perigo-do-fanatismo.html">fanatismo</a>, <a href="../perigo-do-messianismo.html">messianismo</a>, <a href="../atores-malevolentes.html">atores malevolentes</a> e <a href="../perigo-de-questionar-a-democracia.html">como democracias morrem</a>.</p>
<div class="nota memorial"><strong>Às vítimas</strong><p>Nossa memória e nossas condolências {f["vitimas"]}. Cada número nesta página foi uma pessoa com nome, família e futuro.</p></div>'''

def mundo():
    fil = lambda k, rot, todos, vs: f'<div class="filtros" role="group" aria-label="{rot}"><button type="button" data-k="{k}" data-v="" aria-pressed="true">{todos}</button>' + ''.join(f'<button type="button" data-k="{k}" data-v="{c}" aria-pressed="false">{c}</button>' for c in vs) + '</div>'
    gr = ''
    for g in GRUPOS_M + [GRUPO_EXT]:
        its = sorted((f for f in MUN if f['grupo'] == g), key=lambda f: slug_de(f['nome']))
        gr += f'<section class="grupo-fig" data-grupo="{g}"><h2 class="grupo">{g} <small>({len(its)})</small></h2>{MEMORIA if g == GRUPO_EXT else ''}<div class="grade">' + ''.join(cartao_m(f, 'mundo/') for f in its) + '</div></section>'
    corpo = cabeca('Mundo', 'Figuras políticas internacionais', f'{len(MUN)} dossiês de governantes, estadistas, ativistas, jornalistas, e dos extremistas que a história não pode esquecer.')
    corpo += f'''<div class="wrap secao"><div class="nota alerta" style="margin-top:0"><strong>Como ler:</strong> esquerda e direita mudam de país para país e de época para época, e por isso a categoria é só uma aproximação. Em figuras históricas, ela serve apenas como orientação. Quem governa pode mudar: conferimos em novembro de 2026.</div>
<input class="fq" id="fq" type="search" placeholder="Buscar por nome ou país" aria-label="Buscar figura"/>{fil("tipo", "Grupo", "Todos os grupos", GRUPOS_M + [GRUPO_EXT])}{fil("reg", "Região", "Todas as regiões", REGIOES)}{fil("cat", "Espectro", "Todo o espectro", CATEGORIAS)}<p class="contagem" id="contagem" role="status"></p><div id="figuras">{gr}</div><p class="legenda">Veja também os <a href="politicos.html">políticos e figuras do Brasil</a> e as lições sobre <a href="maiores-estadistas.html">estadistas</a> e <a href="maiores-ativistas.html">ativistas</a>.</p>{fontes([("Wikipédia: chefes de Estado e de governo atuais", "https://en.wikipedia.org/wiki/List_of_current_heads_of_state_and_government")])}</div>'''
    page('mundo.html', 'Figuras políticas internacionais', 'Presidentes e primeiros-ministros, estadistas, ativistas e jornalistas políticos do mundo, com contexto e controvérsias.', corpo, atual='mundo.html')
    for f in MUN:
        wiki = f['wiki'] if f['wiki'].startswith('http') else W + quote(f['wiki'] or f['nome'], safe='()_.').replace('%20', '_')
        pol = ''.join(f'<div class="caso"><span class="st {st}">{ROTULO[st]}</span><p style="margin-top:.35rem">{e(x)}</p></div>' for st, x in f['pol']) or '<p>Não registramos aqui uma controvérsia específica. Isso não significa que não exista: consulte as fontes abaixo.</p>'
        aviso = f'<div class="nota alerta aviso-pag"><strong>⚠ {AVISO}</strong> Confira o que é dito em mais de uma fonte.</div>' if extrema(f) else f'<div class="nota alerta aviso-pag"><strong>⚠ {ATENTO}</strong> Compare o que é dito com o que é feito.</div>' if alerta(f['cat']) else ''
        fontes_f = [('Wikipédia: ' + f['nome'], wiki), ('Buscar na BBC', 'https://www.bbc.co.uk/search?q=' + quote(f['nome'])), ('Buscar na Britannica', 'https://www.britannica.com/search?query=' + quote(f['nome']))]
        lado = f'<aside class="lado"><div class="caixa"><h2>Em resumo</h2><dl><dt>Grupo</dt><dd>{e(f["grupo"])}</dd><dt>País</dt><dd>{e(f["pais"])}</dd><dt>Categoria</dt><dd>{e(f["cat"])}</dd></dl></div></aside>'
        mesmos = [x for x in MUN if x['grupo'] == f['grupo'] and x['slug'] != f['slug']]
        i = MUN.index(f) % max(1, len(mesmos))
        rel = ''.join(cartao_m(x) for x in (mesmos[i:] + mesmos[:i])[:3])
        corpo = cabeca('<a href="../mundo.html">Mundo</a>', f['nome'], e(f['quem']), meta=f'<div class="meta">{tag_cat(f["cat"])}<span class="tipo ferr">{e(f["pais"])}</span><span>Atualizado em novembro de 2026</span></div>')
        miolo = pagina_extremista(f) + '<p class="legenda">Números de mortos são estimativas de historiadores e variam entre as fontes. A categoria no topo é só uma aproximação.</p>' if f['grupo'] == GRUPO_EXT else f'''{aviso}<h2>Por que nesta categoria</h2><p>{e(f["porque"])}</p><p class="legenda">Classificação aproximada e contestável. <a href="../mundo.html">Entenda o critério</a>.</p><h2>Polêmicas e processos</h2>{pol}<p class="legenda">Acusação não é condenação. Decisões podem mudar.</p>'''
        corpo += f'''<div class="wrap layout"><article class="leitura">{miolo}{fontes(fontes_f)}</article>{lado}</div><section class="relac"><div class="wrap"><h2>No mesmo grupo</h2><div class="grade">{rel}</div></div></section>'''
        page(f'mundo/{f["slug"]}.html', f['nome'], f'{f["nome"]}: {f["quem"]}', corpo, atual='mundo.html')

# ---------- debates ----------
def cartao_d(d, pre=''):
    return f'<a class="cartao deb" href="{pre}{d["s"]}.html"><span class="linha-cartao"><span class="peso {d["p"][0]}">{e(ROT_PESO[d["p"][0]])}</span></span><h3>{e(d["n"])}</h3><p>{e(d["r"])}</p></a>'
def debates_pub():
    assert len({d['s'] for d in DEBATES_P}) == len(DEBATES_P)
    gr = ''.join(f'<h2 class="grupo">{e(t)}</h2><div class="grade">' + ''.join(cartao_d(d, 'debates/') for d in DEBATES_P if d['t'] == t) + '</div>' for t in TEMAS_D)
    leg = ''.join(f'<li><span class="peso {k}">{e(v)}</span></li>' for k, v in ROT_PESO.items())
    corpo = cabeca('Debates', 'Os principais debates políticos', f'{len(DEBATES_P)} temas que dividem o público: os dois lados, por que é complexo, e onde a lógica e os dados pesam mais.')
    corpo += f'''<div class="wrap secao"><div class="nota" style="margin-top:0"><strong>Como ler:</strong> não existe imparcialidade em dizer sempre que “os dois lados têm razão”. Em cada tema, mostramos a posição de cada lado e por que o debate é complexo. Quando a <a href="testar-visao-moral.html">imparcialidade</a>, a lógica e os dados pesam para um lado, dizemos isso, e explicamos por quê. Essa avaliação é do site e pode ser contestada.</div><ul class="leg-peso">{leg}</ul>{gr}<p class="legenda">Para ir além, veja os <a href="catalogo.html">cursos</a>, a <a href="biblioteca.html">biblioteca</a> e <a href="testar-visao-moral.html">como testar sua visão moral</a>.</p></div>'''
    page('debates.html', 'Os principais debates políticos', 'Armas, aborto, drogas, impostos, imigração e mais: os dois lados de cada debate, por que é complexo e onde as evidências pesam.', corpo, atual='debates.html')
    for d in DEBATES_P:
        lado = lambda x: f'<div><h3>{e(x[0])}</h3><ul>' + ''.join(f'<li>{e(i)}</li>' for i in x[1]) + '</ul></div>'
        sub = ('<h2>Subtópicos</h2><dl class="subs">' + ''.join(f'<dt>{e(a)}</dt><dd>{e(b)}</dd>' for a, b in d['sub']) + '</dl>') if d['sub'] else ''
        lig = list(d['f']) + [(x['titulo'], f'../{x["slug"]}.html') for x in TODAS if d['s'] in LICAO_DEBATES.get(x['slug'], [])]
        vistos = set(); lig = [(n, u) for n, u in lig if not (u in vistos or vistos.add(u))]
        ler = ('<p class="links-d"><strong>Leia também:</strong> ' + ', '.join(f'<a href="{u}">{e(n)}</a>' for n, u in lig) + '.</p>') if lig else ''
        mesmos = [x for x in DEBATES_P if x['t'] == d['t'] and x['s'] != d['s']]
        i = DEBATES_P.index(d) % max(1, len(mesmos))
        rel = ''.join(cartao_d(x) for x in (mesmos[i:] + mesmos[:i])[:3])
        fontes_d = list(d.get('fx', [])) + [('Wikipédia: ' + d['n'], 'https://pt.wikipedia.org/w/index.php?search=' + quote(d['n'])), ('Buscar no Nexo Jornal', 'https://www.nexojornal.com.br/search?q=' + quote(d['n'])), ('Buscar no Politize!', 'https://www.politize.com.br/?s=' + quote(d['n']))]
        corpo = cabeca('<a href="../debates.html">Debates</a> / ' + e(d['t']), d['n'], e(d['r']))
        corpo += f'''<div class="wrap estreito leitura secao"><p class="abre">{e(d["v"])}</p><h2>A posição de cada lado</h2><div class="dois-lados">{lado(d["a"])}{lado(d["b"])}</div><p class="legenda">Posições gerais. Muita gente concorda em parte com cada lado.</p>{d.get("extra", "")}<h2>Por que é complexo</h2><ul>{"".join(f"<li>{e(x)}</li>" for x in d["c"])}</ul><h2>O que a lógica e os dados indicam</h2><div class="nota veredito {d["p"][0]}"><strong>{e(ROT_PESO[d["p"][0]])}</strong><p>{e(d["p"][1])}</p></div><p class="legenda">Avaliação do site, sujeita a críticas. <a href="../mudar-de-ideia.html">Evidências novas podem mudar esta avaliação.</a></p>{sub}<h2>Perguntas para pensar</h2><ol class="roteiro"><li>Qual parte é fato, e qual é valor?</li><li>Quem paga o preço de cada opção?</li><li>Eu aceitaria essa regra sem saber em que lugar estaria?</li><li>O que me faria mudar de ideia?</li></ol>{ler}{fontes(fontes_d)}</div><section class="relac"><div class="wrap"><h2>No mesmo tema</h2><div class="grade">{rel}</div></div></section>'''
        page(f'debates/{d["s"]}.html', d['n'], f'{d["n"]}: {d["r"]} Os dois lados e o que os dados indicam.', corpo, atual='debates.html')

def sites_uteis():
    gr = ''
    for g in GRUPOS_S:
        its = [s for s in SITES_U if s[3] == g]
        cards = ''
        for b in (NAC, INT):
            sel = [s for s in its if s[4] == b]
            if sel:
                cards += f'<div class="ambito" data-amb="{b}"><h3 class="tit-amb">{b}</h3><div class="grade">' + ''.join(f'<a class="cartao" href="{e(u)}" {EXT}><h3 class="ext">{e(n)}</h3><p>{e(dd)}</p></a>' for n, u, dd, _, _ in sel) + '</div></div>'
        gr += f'<section class="grupo-s"><h2 class="grupo">{e(g)} <small>({len(its)})</small></h2>{cards}</section>'
    fil = f'<div class="filtros" id="famb" role="group" aria-label="Âmbito"><button type="button" data-a="" aria-pressed="true">Todos</button><button type="button" data-a="{NAC}" aria-pressed="false">{NAC}</button><button type="button" data-a="{INT}" aria-pressed="false">{INT}</button></div>'
    corpo = cabeca('Fontes', 'Biblioteca de sites sobre política', 'Sites para checar fatos, avaliar a mídia, investigar e acompanhar políticos e organizações.')
    corpo += f'''<div class="wrap secao"><div class="nota alerta" style="margin-top:0">Nenhum site é neutro nem infalível. Alguns têm linha editorial declarada, e outros publicam material bruto. Compare fontes e confira o método.</div>{fil}<div id="sites">{gr}</div><p class="legenda">Veja também a <a href="biblioteca.html">biblioteca de livros</a>, e a lição sobre <a href="checagem-de-fatos.html">checagem de fatos</a>.</p></div>'''
    page('sites.html', 'Biblioteca de sites sobre política', 'Checagem de fatos, viés midiático, jornalismo investigativo, transparência e observatórios, nacionais e internacionais.', corpo, atual='sites.html')

# ---------- vertentes ----------
COR_FAM = {f: i for i, f in enumerate(FAMILIAS_V)}
def fig_slug(n): return next((f['slug'] for f in FIG if f['nome'] == n), None)
def cartao_v(v, pre=''):
    al = f'<span class="aviso-ext">⚠ {e(v["a"])}</span>' if v.get('a') else ''
    return f'<a class="cartao vert" href="{pre}{v["s"]}.html" data-f="{e(v["f"])}"><span class="tipo fam f{COR_FAM[v["f"]]}">{e(v["f"])}</span><h3>{e(v["n"])}</h3><p>{e(v["r"])}</p>{al}</a>'
def vertentes():
    dots = ''.join(f'<a class="ponto f{COR_FAM[v["f"]]}{" esq" if v["x"] > 35 else ""}" href="vertentes/{v["s"]}.html" style="left:{(v["x"] + 100) * .44 + 6:.1f}%;top:{(100 - v["y"]) * .44 + 6:.1f}%" title="{e(v["n"])}"><span>{e(v["n"])}</span></a>' for v in V)
    leg = ''.join(f'<span><i class="fam f{COR_FAM[f]}"></i>{e(f)}</span>' for f in FAMILIAS_V)
    bots = '<button type="button" data-f="" aria-pressed="true">Todas</button>' + ''.join(f'<button type="button" data-f="{e(f)}" aria-pressed="false">{e(f)}</button>' for f in FAMILIAS_V)
    gr = ''
    for f in FAMILIAS_V:
        gr += f'<section class="grupo-v" data-grupo="{e(f)}"><h2 class="grupo">{e(f)}</h2><div class="grade">' + ''.join(cartao_v(v, 'vertentes/') for v in V if v['f'] == f) + '</div></section>'
    dados = json.dumps([dict(s=v['s'], n=v['n'], e=v['e'], m=v['m'], d=v['d'], q=v['q'], p=v['p'], c=v['c'], forte=v['forte'], contra=v['contra'], ap=v['apelo']) for v in V], ensure_ascii=False).replace('</', '<\\/')
    corpo = cabeca('Ideias', 'Vertentes políticas', f'{len(V)} correntes de pensamento, do anarcocapitalismo ao anarcocomunismo: o que defendem, de onde vieram, pontos fortes, contradições e como aparecem no Brasil.')
    corpo += f"""<div class="wrap secao"><div class="sec-cab"><h2>O mapa das ideias</h2><p>Dois eixos ajudam mais do que uma linha só. Clique em uma vertente para abrir.</p></div>
<div class="mapa2" role="group" aria-label="Mapa das vertentes"><span class="eixo t">Mais autoridade</span><span class="eixo b">Mais liberdade individual</span><span class="eixo l">Economia coletiva</span><span class="eixo r">Livre mercado</span>{dots}</div><div class="leg">{leg}</div>
</div>
<div class="wrap secao" style="padding-top:0"><div class="sec-cab"><h2>O mapa de esquerda e direita</h2><p>As mesmas correntes, agora entre esquerda e direita, e entre reforma e ruptura.</p></div>
{mapa_ed()}
<p class="legenda">Posições aproximadas, escolhidas por este site para orientar, não para medir. Cada corrente tem muitas variações, e os próprios defensores podem discordar. Faça o <a href="https://www.idrlabs.com/pt/coordenadas-politicas/teste.php" {EXT}>Teste de Coordenadas Políticas</a> para ver onde você cairia.</p>
<h2 style="margin:2.2rem 0 .8rem">Compare</h2><div class="grade" style="grid-template-columns:repeat(auto-fit,minmax(170px,1fr));margin-bottom:14px"><label class="campo">Vertente 1<select id="va"></select></label><label class="campo">Vertente 2<select id="vb"></select></label><label class="campo">Vertente 3<select id="vc"></select></label></div><div class="tabela"><table class="compara" id="vcomp"></table></div><script type="application/json" id="dados-vert">{dados}</script>
<h2 style="margin:2.2rem 0 .8rem">Todas as vertentes</h2><input class="fq" id="vq" type="search" placeholder="Filtrar por nome ou ideia" aria-label="Filtrar vertentes"/><div class="filtros" id="vfam" role="group" aria-label="Família">{bots}</div><div id="vertentes">{gr}</div></div>"""
    page('vertentes.html', 'Vertentes políticas', 'Liberalismo, anarcocapitalismo, social-democracia, marxismo, anarquismo e outras correntes: ideias, história, críticas e o caso brasileiro.', corpo, atual='vertentes.html')
    for i, v in enumerate(V):
        pts = ''.join(f'<a href="../partidos/{p}.html" class="tipo">{e(PARTIDO[p]["s"])}</a>' for p in v['pa'])
        fgs = ''.join(f'<a href="../politicos/{fig_slug(n)}.html" class="tipo ferr">{e(n)}</a>' for n in v['fi'] if fig_slug(n))
        for n in v['fi']:
            assert fig_slug(n), n
        liga = ''
        if pts: liga += f'<h3>Partidos com influência dessa ideia</h3><p class="tags">{pts}</p>'
        if fgs: liga += f'<h3>Figuras ligadas ou associadas</h3><p class="tags">{fgs}</p>'
        if liga: liga += '<p class="legenda">Associação aproximada. Influência não quer dizer que o partido ou a pessoa adote tudo o que a corrente defende.</p>'
        aviso = f'<div class="nota alerta" style="margin-top:0"><strong>⚠ {e(v["a"])}</strong></div>' if v.get('a') else ''
        wiki = W + quote(v['w'], safe='()_-')
        mesmas = [x for x in V if x['f'] == v['f'] and x['s'] != v['s']][:3]
        ant, prox = V[i - 1], V[(i + 1) % len(V)]
        lado = f'<aside class="lado"><div class="caixa"><h2>Em resumo</h2><dl><dt>Família</dt><dd>{e(v["f"])}</dd><dt>Estado</dt><dd>{e(v["e"])}</dd><dt>Economia</dt><dd>{e(v["m"])}</dd></dl></div><div class="caixa toc-caixa"><h2>Nesta página</h2><ul class="toc"></ul></div></aside>'
        corpo = cabeca('<a href="../vertentes.html">Vertentes políticas</a>', v['n'], e(v['r']), meta=f'<div class="meta"><span class="tipo fam f{COR_FAM[v["f"]]}">{e(v["f"])}</span></div>')
        corpo += f"""<div class="wrap layout"><article class="leitura">{aviso}<h2>A ideia central</h2><p>{e(v["i"])}</p>
<h2>Como vê cada questão</h2><div class="tabela"><table><tbody><tr><th>Estado</th><td>{e(v["e"])}</td></tr><tr><th>Economia</th><td>{e(v["m"])}</td></tr><tr><th>Liberdades</th><td>{e(v["d"])}</td></tr><tr><th>Igualdade</th><td>{e(v["q"])}</td></tr></tbody></table></div>
<h2>Pensadores e referências</h2><p>{e(v["p"])}</p><h2>Na história</h2><p>{e(v["h"])}</p><h2>No Brasil</h2><p>{e(v["b"])}</p>{liga}<h2>{"Por que atraiu pessoas" if v["apelo"] else "Pontos fortes: o que pode estar certo"}</h2><ul class="lista-forte">{"".join(f"<li>{e(x)}</li>" for x in v["forte"])}</ul>{'<p class="legenda">Explicar por que uma ideia atraiu pessoas não é dizer que ela está certa.</p>' if v["apelo"] else ''}<h2>Contradições</h2><ul class="lista-contra">{"".join(f"<li>{e(x)}</li>" for x in v["contra"])}</ul><h2>O que dizem os críticos</h2><p>{e(v["c"])}</p>
{fontes([(v.get("wl") or "Wikipédia: " + v["n"], wiki)] + v.get("fx", []))}<nav class="pager" aria-label="Vertentes"><a href="{ant["s"]}.html"><small>← Anterior</small>{e(ant["n"])}</a><a class="prox" href="{prox["s"]}.html"><small>Próxima →</small>{e(prox["n"])}</a></nav></article>{lado}</div><section class="relac"><div class="wrap"><h2>Vertentes próximas</h2><div class="grade">{"".join(cartao_v(x) for x in mesmas)}</div></div></section>"""
        page(f'vertentes/{v["s"]}.html', v['n'], v['r'], corpo, atual='vertentes.html')

# ---------- vieses ----------
TDL = 'https://thedecisionlab.com/biases/'
def slug_v(x): return x[0].removeprefix('the-')
CAT_V = list(CATS)
def cartao_vies(x, pre=''):
    return f'<a class="cartao vies" href="{pre}{slug_v(x)}.html" data-c="{e(x[2])}"><span class="tipo cvies v{CAT_V.index(x[2])}">{e(x[2])}</span><h3>{e(x[1])}</h3><p>{e(x[3])}</p></a>'
def vieses():
    bots = '<button type="button" data-c="" aria-pressed="true">Todos</button>' + ''.join(f'<button type="button" data-c="{e(c)}" aria-pressed="false">{e(c)}</button>' for c in CAT_V)
    gr = ''
    for c in CAT_V:
        gr += f'<section class="grupo-vies" data-g="{e(c)}"><h2 class="grupo">{e(c)}</h2><p class="legenda" style="font-size:.98rem">{e(CATS[c])}</p><div class="grade">' + ''.join(cartao_vies(x, 'vieses/') for x in sorted(VIES, key=lambda y: slug_de(y[1])) if x[2] == c) + '</div></section>'
    corpo = cabeca('Mente', 'Vieses cognitivos', f'{len(VIES)} atalhos e erros do pensamento: o que são, e como afetam seu julgamento moral e político.')
    corpo += f"""<div class="wrap secao"><div class="nota" style="margin-top:0"><strong>Todo mundo tem vieses,</strong> inclusive quem acha que não tem. Saber reconhecê-los no adversário é fácil: o difícil é reconhecê-los em si mesmo. Comece pela <a href="vieses-cognitivos.html">lição introdutória</a> e faça o <a href="ferramentas/teste-de-troca.html">teste de troca</a>.</div>
<input class="fq" id="vbq" type="search" placeholder="Filtrar por nome ou ideia" aria-label="Filtrar vieses"/><div class="filtros" id="vbf" role="group" aria-label="Categoria">{bots}</div><p class="contagem" id="vbc" role="status"></p><div id="vieses">{gr}</div>
<p class="legenda" style="margin-top:2rem">Lista baseada no <a href="https://thedecisionlab.com/biases-index" {EXT}>índice do The Decision Lab</a> e na <a href="https://en.wikipedia.org/wiki/List_of_cognitive_biases" {EXT}>lista de vieses cognitivos da Wikipédia</a>. As explicações e os efeitos morais e políticos foram escritos para este site. Alguns efeitos são aplicações nossas, e não resultados de estudos sobre política.</p></div>"""
    page('vieses.html', 'Vieses cognitivos', 'Mais de 250 vieses explicados, com seus efeitos no pensamento moral e político.', corpo, atual='vieses.html')
    for i, x in enumerate(VIES):
        c = x[2]; mesmos = [y for y in VIES if y[2] == c and y[0] != x[0]]
        j = i % max(1, len(mesmos)); rel = (mesmos[j:] + mesmos[:j])[:3]
        ant, prox = VIES[i - 1], VIES[(i + 1) % len(VIES)]
        corpo = cabeca('<a href="../vieses.html">Vieses cognitivos</a>', x[1], e(x[3]), meta=f'<div class="meta"><span class="tipo cvies v{CAT_V.index(c)}">{e(c)}</span></div>')
        corpo += f"""<div class="wrap estreito leitura secao"><h2 style="margin-top:0">O que é</h2><p class="abre">{e(VIES_E[x[0]][0])}</p><div class="ex-vies"><strong>No dia a dia:</strong> {e(VIES_E[x[0]][1])}</div><h2>Como isso afeta a moral e a política</h2><div class="efeitos"><section class="efeito-m"><h2>No pensamento moral</h2><p>{e(x[4])}</p></section><section class="efeito-p"><h2>No pensamento político</h2><p>{e(x[5])}</p></section></div><div class="nota"><strong>Como reduzir:</strong> {e(CATS[c])}</div>{fontes([("The Decision Lab: " + x[0].replace("-", " "), TDL + x[0])] if x[0] in VIES_TDL else [("Wikipédia: List of cognitive biases", "https://en.wikipedia.org/wiki/List_of_cognitive_biases")])}<nav class="pager" aria-label="Vieses"><a href="{slug_v(ant)}.html"><small>← Anterior</small>{e(ant[1])}</a><a class="prox" href="{slug_v(prox)}.html"><small>Próximo →</small>{e(prox[1])}</a></nav></div><section class="relac"><div class="wrap"><h2>Na mesma categoria</h2><div class="grade">{"".join(cartao_vies(y) for y in rel)}</div></div></section>"""
        page(f'vieses/{slug_v(x)}.html', x[1], f'{x[1]}: {x[3]}', corpo, atual='vieses.html')

# ---------- ferramentas ----------
def ferramentas():
    cards = ''.join(cartao_ferr(*f) for f in FERR)
    page('ferramentas.html', 'Ferramentas', 'Jogos, comparadores e simuladores para aprender política fazendo.', cabeca('Ferramentas', 'Aprenda fazendo', 'Sem cadastro. O que fica salvo, fica só no seu navegador.') + f'<div class="wrap secao"><div class="grade">{cards}</div></div>', atual='ferramentas.html')
    def fp(a, tit, lede, corpo):
        d = next(x[2] for x in FERR if x[0] == a)
        page(f'ferramentas/{a}.html', tit, d, cabeca('<a href="../ferramentas.html">Ferramentas</a>', tit, lede) + f'<div class="wrap ferr secao" style="padding-top:28px">{corpo}</div>', atual='ferramentas.html')
    JOGO = '<div id="jogo" class="quiz" style="margin-top:0"><div class="placar"><span></span><span></span></div><div class="barra-prog"><i></i></div><div class="alvo" style="margin-top:14px"></div><button class="btn prox-q" type="button" style="margin-top:12px" hidden>Próxima</button></div>'
    dj = lambda t, it: f'<script type="application/json" id="dados-jogo">{json.dumps(dict(tipo=t, itens=it), ensure_ascii=False).replace("</", "<\\/")}</script>'
    fp('quem-faz-o-que', 'Quem faz o quê?', 'Um problema, sete cargos. Saber quem cobrar é metade do caminho.', JOGO + dj('cargos', [[a, b, c] for a, b, c in PROBLEMAS]) + '<p class="legenda">Muitas áreas são compartilhadas. Aqui vale o responsável principal.</p><p><a href="../cargos.html">Veja o que cada cargo faz</a>.</p>')
    fp('valor-ou-fato', 'Valor ou fato?', 'Antes de discutir, descubra o que está em jogo: uma questão moral ou uma questão de evidências.', JOGO + dj('frases', [[a, b, c] for a, b, c in FRASES]) + '<p><a href="../valores-e-decisoes.html">Entenda a diferença</a>.</p>')
    fp('que-truque-e-esse', 'Que truque é esse?', 'Dez frases, seis truques. Quanto mais você reconhece, menos cai neles.', JOGO + f'<script type="application/json" id="dados-jogo">{json.dumps(dict(tipo="truques", ops=TRUQUES, itens=[list(x) for x in SOFISMAS]), ensure_ascii=False)}</script>' + '<p class="legenda">Frases fictícias, escritas para o exercício. Elas não são citações de ninguém.</p><p><a href="../sofismo.html">Leia a lição sobre sofismo</a>.</p>')
    ids = {}
    for p in P:
        for c in COD.get(p['id'], [p['s']]): ids[c] = p['id']
    dv = json.dumps(dict(votos=V_JSON, ids=ids, partidos=[dict(id=p['id'], s=p['s'], num=p['num'], esp=p['esp'], ano=p['ano'], pres=p['pres'], fed=p['fed'], val=p['val'], ali=p['ali'], vot=COD.get(p['id'], [p['s']])) for p in P]), ensure_ascii=False).replace('</', '<\\/')
    dvs = f'<script type="application/json" id="dados-votos">{dv}</script>'
    sem = '' if V_JSON else '<div class="nota alerta">Os dados de votação ainda não foram carregados.</div>'
    # tabela geral
    colunas = V_JSON
    cor = lambda f: f'hsl({int(f * 140)} 55% 40%)'
    linhas = ''
    for p in sorted(P, key=lambda p: ESP_POS[p['esp']]):
        celulas = ''
        tem = False
        for v in colunas:
            c, x = voto_de(p['id'], v)
            tt = (x['s'] + x['n']) if x else 0
            if tt:
                tem = True; fr = x['s'] / tt
                celulas += f'<td><span class="celula" style="background:{cor(fr)}" title="{x["s"]} a favor, {x["n"]} contra">{round(fr * 100)}%</span></td>'
            else: celulas += '<td><span class="celula x">–</span></td>'
        if tem: linhas += f'<tr><td><a href="../partidos/{p["id"]}.html">{e(p["s"])}</a></td>{celulas}</tr>'
    mat = '<h2 style="margin-top:2.2rem">Visão geral</h2><p>Percentual de votos a favor entre os “sim” e “não” de cada partido. Da esquerda para a direita no espectro, de cima para baixo.</p><div class="tabela"><table class="matriz"><thead><tr><th>Partido</th>' + ''.join(f'<th>{e(v["rot"])} {v["ano"]}</th>' for v in colunas) + f'</tr></thead><tbody>{linhas}</tbody></table></div>' if V_JSON else ''
    fp('como-votaram', 'Como os partidos votaram', 'Discurso é uma coisa, voto é outra. Veja o que cada bancada fez em votações decisivas.', sem + f'<label class="campo">Escolha a votação<select id="vot"></select></label><p id="vot-desc"></p>{LEG}<div id="lista-votos"></div>{mat}<p class="legenda">Fonte: <a href="https://dadosabertos.camara.leg.br/" {EXT}>API Dados Abertos da Câmara dos Deputados</a>. Conta o partido do deputado na data da votação, por isso aparecem siglas extintas. Votação nominal de plenário; “a favor” é o voto “sim” no texto votado, então leia a descrição.</p>{dvs}')
    fp('comparador', 'Comparador de partidos', 'Coloque até três partidos lado a lado.', f'<div class="grade" style="grid-template-columns:repeat(auto-fit,minmax(170px,1fr));margin-bottom:16px"><label class="campo">Partido 1<select id="pa"></select></label><label class="campo">Partido 2<select id="pb"></select></label><label class="campo">Partido 3<select id="pc"></select></label></div>{LEG}<div class="tabela"><table class="compara" id="comp"></table></div>{dvs}')
    def fio(f):
        o = []
        for x in f:
            m = re.match(r'^([a-z]+):(.+)$', x)
            o.append(f'<a href="../partidos/{m.group(1)}.html">{e(m.group(2))}</a>' if m else f'<b>{e(x)}</b>')
        return '<div class="fio">' + '<i>→</i>'.join(o) + '</div>'
    fams = ''.join(f'<div class="familia"><h3>{e(n)}</h3>{"".join(fio(f) for f in fs)}</div>' for n, fs in FAMILIAS)
    fp('arvore-dos-partidos', 'Árvore dos partidos', 'Muitas siglas novas são velhas conhecidas. Em azul, os partidos atuais: clique para abrir o dossiê.', fams + '<p class="legenda">Versão simplificada: mostra as principais fusões, rachas e trocas de nome. Saídas de grupos e dissidências parciais estão nos dossiês.</p>')
    tr = f'<div id="troca" class="quiz" style="margin-top:0"><p class="k">Mesma situação, dois políticos</p><p class="cena"></p><div class="ops"></div><p class="fb" role="status"></p><button class="btn prox-q" type="button" style="margin-top:10px" hidden>Outra situação</button></div><script type="application/json" id="dados-troca">{json.dumps(TROCAS, ensure_ascii=False)}</script><div class="nota">Pense em nomes reais, um de cada vez. Nada é enviado nem salvo. O objetivo é perceber o <a href="../vieses-cognitivos.html">raciocínio motivado</a> em si mesmo.</div>'
    fp('teste-de-troca', 'Teste de troca', 'Você julgaria o mesmo ato do mesmo jeito se viesse de quem você rejeita?', tr)
    chk = ''
    for g, its in CHECK.items():
        chk += f'<h3 style="margin-top:1rem">{e(g)}</h3>' + ''.join(f'<label class="chk"><input type="checkbox"/><span>{e(x)}</span></label>' for x in its)
    fp('ficha-do-candidato', 'Ficha do candidato', 'Antes de votar, passe cada candidato por este checklist. Ele fica salvo só no seu navegador.', f'<div class="quiz" id="ficha" style="margin-top:0"><label class="campo">Nome do candidato ou candidata<input type="text" id="ficha-nome" placeholder="Ex.: fulana"/></label><div id="ficha-prog" class="barra-prog"><i></i></div><small id="ficha-t"></small>{chk}<div class="cta"><button class="btn alt" type="button" onclick="print()">Imprimir</button><button class="btn alt" type="button" id="ficha-limpa">Limpar</button></div></div><p>Roteiro completo em <a href="../como-votar-bem.html">como votar da melhor forma</a>.</p>')
    ps = [('Partido A', 42000), ('Partido B', 31000), ('Partido C', 17000), ('Partido D', 8000), ('Partido E', 2000)]
    ins = ''.join(f'<label class="campo">{n}<input type="number" min="0" step="500" value="{v}" data-p="{n}"/></label>' for n, v in ps)
    fp('simulador-de-cadeiras', 'Simulador de cadeiras', 'Em deputados e vereadores, seu voto ajuda primeiro o partido. Mude os votos e veja as vagas.', f'<div class="quiz" id="sim" style="margin-top:0"><label class="campo" style="max-width:220px">Vagas em disputa<input type="number" id="cad" min="1" max="70" value="20"/></label><div class="grade" style="grid-template-columns:repeat(auto-fit,minmax(140px,1fr))">{ins}</div><div id="sim-res" role="status"></div></div><div class="nota">Versão simplificada: divide as vagas pelo quociente eleitoral e distribui as sobras pelas maiores médias. A regra real tem ainda exigências de votação mínima para partidos e candidatos (80% e 20% do quociente, além de regras para as sobras).</div>')
    G = [dict(ordem=['Ana', 'Bruno', 'Clara'], n=40, t='Ana → Bruno → Clara'), dict(ordem=['Bruno', 'Clara', 'Ana'], n=35, t='Bruno → Clara → Ana'), dict(ordem=['Clara', 'Bruno', 'Ana'], n=25, t='Clara → Bruno → Ana')]
    gi = ''.join(f'<label class="campo">{e(g["t"])}<input type="number" min="0" value="{g["n"]}"/></label>' for g in G)
    fp('voto-preferencial', 'Simulador de voto preferencial', 'Três candidatos e três grupos de eleitores, cada grupo com sua ordem de preferência. Mude os números.', f'<div class="quiz" id="pref" style="margin-top:0"><div class="grade" style="grid-template-columns:repeat(auto-fit,minmax(170px,1fr))">{gi}</div><div id="pref-res" role="status" style="margin-top:12px"></div></div><script type="application/json" id="dados-pref">{json.dumps(G, ensure_ascii=False)}</script><p>Entenda mais em <a href="../melhorar-a-democracia.html">ideias para melhorar a democracia</a>.</p>')

# ---------- ranking ----------
def ranking():
    mx = RANKING[0][1]
    bars = ''.join(f'<div class="barra"><span>{i + 1}º</span><span>{e(n)}</span><i style="width:{v / mx * 100:.1f}%">{str(v).replace(".", ",")}%</i></div>' for i, (n, v, _, _) in enumerate(RANKING))
    casos = ''
    for c in CASOS:
        its = ''.join(f'<li>{e(t)} <a href="{e(u)}" {EXT}>{e(s)} ↗</a></li>' for t, s, u in c['itens'])
        casos += f'<div class="pessoa"><h3>{e(c["n"])} <small>{e(c["p"])}</small></h3><ul>{its}</ul></div>'
    LUPA = 'https://uploads.agencialupa.org/2026/07/RELATORIO-ANATOMIA-DA-DESINFORMACAO-ELEITORAL_LUPA-FINAL.pdf'
    corpo = cabeca('Brasil', 'Ranking da mentira', 'Quem mais teve declarações classificadas como falsas pelas agências de checagem, e o que esse número pode e não pode dizer.')
    corpo += f'''<div class="wrap estreito leitura secao"><h2>O ranking da Lupa</h2><p>Em 2026, o Observatório Lupa analisou uma década de checagens. Este é o maior percentual de frases falsas entre os 23 políticos com mais de 30 frases checadas (os dez primeiros que o relatório publica):</p>
<div class="barras" role="img" aria-label="Percentual de frases falsas por político">{bars}</div>
<p class="legenda">Fonte: <a href="{LUPA}" {EXT}>Lupa, Anatomia da desinformação eleitoral (2026), p. 19-20</a>. Bolsonaro: 102 de 236 frases; Lula: 22 de 83.</p>
<div class="nota alerta"><strong>Como não ler:</strong> a própria Lupa alerta que quem fala mais e é mais checado pode parecer mais mentiroso. O número mede frases selecionadas para checagem em campanhas, não todas as falas nem a intenção de mentir. “Falso” também não é o mesmo que crime.</div>
<h2>O caso mais documentado</h2><p>O Aos Fatos manteve um contador de Jair Bolsonaro enquanto presidente: <a href="https://www.aosfatos.org/noticias/mentiras-bolsonaro/" {EXT}>6.685 declarações falsas ou distorcidas em 1.459 dias</a>, cerca de 4,6 por dia. Não há contador igual para outros presidentes, então o número não permite comparação direta.</p>
<h2>Outros nomes conhecidos</h2><p>Estes não aparecem entre os dez primeiros da Lupa e não têm um número comparável. Listamos casos documentados, sem ordem de gravidade.</p>{casos}
<h2>Mentira, distorção e cinismo</h2><p>Nem toda frase falsa é igual: há erro, exagero, distorção e mentira deliberada. E há o cinismo, quando o político sabe que foi desmentido e repete mesmo assim, porque a frase rende voto. Esse jogo também depende do público: quem sabe que é falso e compartilha porque ajuda o seu lado participa dele. O risco oposto é o eleitor cínico, para quem “todo político mente, então tanto faz”. Esta página mostra que há diferenças. Veja a <a href="sofismo.html">lição sobre sofismo e cinismo</a>.</p>
<h2>Também vale saber</h2><p>Em 2023, a <a href="https://apublica.org/2023/08/acoes-judiciais-apontam-que-metade-dos-politicos-que-espalham-fake-news-e-do-pl/" {EXT}>Agência Pública</a> encontrou, em ações judiciais, que quase metade dos políticos identificados por espalhar fake news era do PL. A base são processos, não checagens. Veja como <a href="checagem-de-fatos.html">se defender da desinformação</a>.</p>
<p class="legenda">Encontrou um erro ou um caso importante que falta, de qualquer lado? Mande a fonte para corrigirmos.</p></div>'''
    page('ranking-da-mentira.html', 'Ranking da mentira', 'Quem mais teve falas classificadas como falsas, segundo a Lupa e o Aos Fatos: Bolsonaro, Lula, Nikolas Ferreira, Flávio Bolsonaro, Janones e outros.', corpo, atual='brasil.html')

# ---------- acompanhar, biblioteca, sobre ----------
def acompanhar():
    # a antiga página foi mesclada à biblioteca de sites: fica só o redirecionamento
    open(os.path.join(ROOT, 'acompanhar.html'), 'w', encoding='utf-8', newline='\n').write('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Biblioteca de sites sobre política</title><meta name="robots" content="noindex"><link rel="canonical" href="sites.html"><meta http-equiv="refresh" content="0; url=sites.html"></head><body><p>Esta página mudou para a <a href="sites.html">biblioteca de sites sobre política</a>.</p></body></html>')

def biblioteca():
    n_cls = {'Iniciante': 'iniciante', 'Intermediário': 'intermediario', 'Avançado': 'avancado'}
    cart = lambda t, a, d, n, u: f'<a class="cartao" href="{e(u)}" {EXT}><span class="tipo {n_cls[n]}">{e(n)}</span><h3 class="ext" style="margin-top:.3rem">{e(t)}</h3><p><em>{e(a)}</em></p><p>{e(d)}</p></a>'
    NIV_L = [('Iniciante', 'Para começar: leitura acessível, sem exigir formação prévia.'), ('Intermediário', 'Ideias mais densas, mas ainda boas para o público geral.'), ('Avançado', 'Clássicos e obras acadêmicas: pedem mais tempo e, às vezes, um guia de leitura.')]
    li = ''.join(f'<h2 class="grupo">{n} <small>({sum(1 for x in LIVROS if x[3] == n)})</small></h2><p>{d}</p><div class="grade">' + ''.join(cart(*x) for x in LIVROS if x[3] == n) + '</div>' for n, d in NIV_L)
    corpo = cabeca('Fontes', 'Biblioteca', f'{len(LIVROS)} livros para entender política, separados por nível de dificuldade.') + f'<div class="wrap secao">{li}<p class="legenda">Procura sites em vez de livros? Veja a <a href="sites.html">biblioteca de sites sobre política</a>.</p></div>'
    page('biblioteca.html', 'Biblioteca', 'Livros e leituras recomendadas sobre política, por nível.', corpo, atual='biblioteca.html')

def privacidade():
    corpo = cabeca('Sobre', 'Política de privacidade', 'Em resumo: não há cadastro, não usamos cookies próprios nem ferramentas de análise de visitas.') + '''<div class="wrap estreito leitura secao"><p class="abre">Esta página explica quais dados podem ser tratados quando você usa o Política Para Iniciantes, em linha com a Lei Geral de Proteção de Dados (LGPD, Lei 13.709/2018).</p>
<p><em>Última atualização: 2 de novembro de 2026.</em></p>
<h2>O que não fazemos</h2><ul><li>Não pedimos cadastro, login ou pagamento.</li><li>Não há formulário que envie seus dados para nós.</li><li>Não usamos cookies próprios, publicidade ou ferramentas de análise de visitas.</li><li>Não vendemos nem compartilhamos dados pessoais.</li></ul>
<h2>O que fica no seu navegador</h2><p>Alguns recursos usam o armazenamento local (<em>localStorage</em>) do seu aparelho. Essas informações não são enviadas para nós:</p>
<div class="tabela"><table><thead><tr><th>Recurso</th><th>O que guarda</th></tr></thead><tbody><tr><td>Marcar como lida</td><td>A lista de lições que você marcou</td></tr><tr><td>Ficha do candidato</td><td>Os itens marcados e o nome que você digitou para identificar a ficha</td></tr></tbody></table></div>
<p>Para apagar, limpe os dados deste site nas configurações do navegador. Em aparelhos compartilhados, outras pessoas podem ver essas marcações.</p>
<h2>Serviços de terceiros</h2><p>Como em qualquer site, seu navegador envia dados técnicos, como endereço IP e tipo de navegador, aos serviços que entregam as páginas e arquivos:</p>
<div class="tabela"><table><thead><tr><th>Serviço</th><th>Para quê</th></tr></thead><tbody><tr><td>Hospedagem do site</td><td>Entregar as páginas. O provedor pode manter registros técnicos de acesso</td></tr><tr><td><a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google Fonts</a></td><td>Carregar as fontes do site</td></tr><tr><td><a href="https://biblioverse.org">BiblioVerse</a></td><td>Carregar a barra superior com as bibliotecas da BiblioVerse</td></tr></tbody></table></div>
<h2>Links externos</h2><p>Indicamos fontes, livros e testes em outros sites, como os testes de Visão Moral e de Coordenadas Políticas. Ao acessá-los, valem as regras de privacidade de cada um, e vale ler antes de responder.</p>
<h2>Crianças e adolescentes</h2><p>O site é educativo e não pede dados pessoais a pessoas de nenhuma idade.</p>
<h2>Seus direitos</h2><p>A LGPD garante direitos como acesso, correção e eliminação de dados pessoais. Como não mantemos cadastro nem guardamos o que você faz aqui, em geral não temos dados que permitam identificar você. O que está no seu aparelho fica sob seu controle.</p>
<h2>Mudanças</h2><p>Se o funcionamento do site mudar, por exemplo com novas ferramentas ou serviços, esta página será atualizada, com nova data.</p></div>'''
    page('privacidade.html', 'Política de privacidade', 'Quais dados podem ser tratados ao usar o Política Para Iniciantes, e o que fica só no seu navegador.', corpo)

def sobre():
    corpo = cabeca('Sobre', 'Sobre este projeto') + '''<div class="wrap estreito leitura secao"><p class="abre">Um guia para quem quer entender política sem precisar escolher um time antes.</p>
<h2>Posição editorial</h2><p>O site não apoia partido nem candidato, mas reconhece que a neutralidade total não existe, há sempre valores que nos guiam. Este projeto parte de valores e posições também: a ética vem antes da política, valores e fatos devem ser separados, é preciso tentar buscar o melhor cenário entre todos os disponíveis, e todos com a capacidade de sofrer devem ser considerados e ter seus interesses incluídos no debate político. Quando um tema está em aberto, apresentamos os lados.</p>
<h2>Como apuramos</h2><p>Usamos Wikipédia, TSE, Senado, Câmara, agências de checagem e imprensa de referência, evitando portais muito à direita ou muito à esquerda. As votações vêm diretamente da API oficial da Câmara. Dados de partidos têm como base novembro de 2026 e mudam com frequência.</p><p>Os dossiês são resumos, não processos completos. Acusação não é condenação, e decisões são revistas. Ao ver um erro, mande a correção com a fonte.</p>
<h2>Seus dados</h2><p>Não há cadastro. Lições lidas e fichas ficam só no seu navegador. Veja a <a href="privacidade.html">política de privacidade</a>.</p>
<h2>Parte da BiblioVerse</h2><p>Este site faz parte da <a href="https://biblioverse.org">BiblioVerse</a>.</p></div>'''
    page('sobre.html', 'Sobre', 'Posição editorial e método de apuração do Política Para Iniciantes.', corpo)

def arquivos():
    urls = ['index.html', 'comece-aqui.html', 'catalogo.html', 'iniciante.html', 'intermediario.html', 'avancado.html', 'brasil.html', 'cargos.html', 'poderes.html', 'historia.html', 'partidos.html', 'ranking-da-mentira.html', 'ferramentas.html', 'biblioteca.html', 'sobre.html'] + [l['slug'] + '.html' for l in TODAS] + [f'partidos/{p["id"]}.html' for p in P] + [f'ferramentas/{f[0]}.html' for f in FERR] + ['politicos.html', 'vertentes.html', 'vieses.html'] + [f'vieses/{slug_v(x)}.html' for x in VIES] + [f'vertentes/{v["s"]}.html' for v in V] + [f'politicos/{f["slug"]}.html' for f in FIG]
    w = lambda n, t: open(os.path.join(ROOT, n), 'w', encoding='utf-8', newline='\n').write(t)
    w('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{SITE}/{"" if u == "index.html" else u}</loc><lastmod>{ATUALIZADO}</lastmod></url>\n' for u in sorted(set(PAGINAS + urls) - {'404.html'})) + '</urlset>\n')
    w('llms.txt', f'# {NOME}\n\n> Guia gratuito de política em português, em três níveis, com fontes, dossiês de partidos, vertentes, vieses cognitivos e ferramentas.\n\n## Principais seções\n\n- [Comece aqui]({SITE}/comece-aqui.html)\n- [Catálogo de lições]({SITE}/catalogo.html)\n- [Política brasileira]({SITE}/brasil.html)\n- [Partidos]({SITE}/partidos.html)\n- [Políticos e figuras]({SITE}/politicos.html)\n- [Figuras internacionais]({SITE}/mundo.html)\n- [Principais debates]({SITE}/debates.html)\n- [Vertentes políticas]({SITE}/vertentes.html)\n- [Vieses cognitivos]({SITE}/vieses.html)\n- [Ferramentas]({SITE}/ferramentas.html)\n- [Biblioteca]({SITE}/biblioteca.html)\n- [Sites sobre política]({SITE}/sites.html)\n- [Sobre e método]({SITE}/sobre.html)\n')
    w('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
    w('CNAME', 'politicaparainiciantes.biblioverse.org\n')
    w('.nojekyll', '')
    w('.gitignore', '__pycache__/\n')
    w('manifest.webmanifest', json.dumps(dict(name=NOME, short_name='Política', start_url='/', display='standalone', background_color='#fbf9f5', theme_color='#14206b', icons=[dict(src='assets/icon.svg', sizes='any', type='image/svg+xml'), dict(src='assets/icon-192.png', sizes='192x192', type='image/png'), dict(src='assets/icon-512.png', sizes='512x512', type='image/png')]), ensure_ascii=False))
    w('assets/icon.svg', arte.LOGO.replace(' aria-hidden="true"', ' xmlns="http://www.w3.org/2000/svg"'))
    busca = [dict(t=f['nome'], d=f'{f["pais"]} · {f["quem"]}', u=f'mundo/{f["slug"]}.html') for f in MUN] + [dict(t=d['n'], d='Debate · ' + d['r'], u=f'debates/{d["s"]}.html') for d in DEBATES_P] + [dict(t='Figuras políticas internacionais', d='Governantes, estadistas, ativistas, jornalistas e extremistas', u='mundo.html'), dict(t='Os principais debates políticos', d='Os dois lados e o que os dados indicam', u='debates.html'), dict(t='Biblioteca de sites sobre política', d='Checagem, viés, investigação, transparência e observatórios', u='sites.html')] + [dict(t=l['titulo'], d=l['nivel_rot'] + ' · ' + l['resumo'], u=l['slug'] + '.html') for l in TODAS] + [dict(t=f'{p["s"]}: {p["n"]}', d=f'Partido nº {p["num"]} · {p["esp"]}', u=f'partidos/{p["id"]}.html') for p in P] + [dict(t=f[1], d='Ferramenta · ' + f[2], u=f'ferramentas/{f[0]}.html') for f in FERR] + [dict(t=x[1], d='Viés · ' + x[3], u=f'vieses/{slug_v(x)}.html') for x in VIES] + [dict(t=v['n'], d='Vertente · ' + v['r'], u=f'vertentes/{v["s"]}.html') for v in V] + [dict(t=t, d=d, u=u) for u, t, d in BR] + [dict(t=f['nome'], d=f'{f["cat"]} · {f["quem"]}', u=f'politicos/{f["slug"]}.html') for f in FIG]
    w('assets/busca.json', json.dumps(busca, ensure_ascii=False))
    page('404.html', 'Página não encontrada', 'Esta página não existe.', cabeca('Erro 404', 'Página não encontrada', 'Volte para o <a href="/" style="color:#fff">início</a> ou use a busca.'))

os.makedirs(os.path.join(ROOT, 'assets'), exist_ok=True)
inicio(); comece(); catalogo()
for s, r, ls, t, d, g in NIVEIS:
    nivel(s, r, ls, t, d, g)
    for l in ls: licao(l, ls)
figuras(); mundo(); debates_pub(); sites_uteis(); vertentes(); vieses(); brasil_hub(); cargos(); poderes(); historia(); partidos(); ferramentas(); ranking(); acompanhar(); biblioteca(); sobre(); privacidade(); arquivos()
print(f'{len(TODAS)} lições, {len(P)} partidos, {len(VOTOS)} votações, {len(FERR)} ferramentas.')
