"""Índice de busca completo: depois que todas as páginas foram escritas, acrescenta a busca.json os subtítulos (h2 e
h3) e as palavras do conteúdo de cada página, e inclui as páginas que ainda não estavam no índice. O script do site
ordena os resultados por título, subtítulo, descrição e conteúdo. O mesmo arquivo é usado nos três sites."""
import html, json, os, re, unicodedata
from collections import Counter

# palavras muito comuns que não ajudam a achar uma página
PARADAS = set('''a ao aos as ate com como da das de dela dele deles do dos e ela elas ele eles em entre era essa esse esta
este eu foi foram ha isso isto ja la mais mas me mesmo muito na nao nas nem no nos o os ou para pela pelas pelo pelos por
porque qual quando que quem se sem ser seu seus sua suas sao tambem tem um uma umas uns voce sobre ainda depois antes cada
outra outro outros outras pode podem todo toda todos todas onde assim tao estao esta isso''' .split())

def norm(s):
    return unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode().lower()

def _texto(h):
    h = re.sub(r'<(script|style|svg|noscript)\b.*?</\1>', ' ', h, flags=re.S | re.I)
    return html.unescape(re.sub(r'<[^>]+>', ' ', h))

def _ler(caminho):
    h = open(caminho, encoding='utf-8').read()
    if 'http-equiv="refresh"' in h: return None
    t = re.search(r'<title>(.*?)</title>', h, re.S)
    d = re.search(r'<meta name="description" content="([^"]*)"', h)
    m = re.search(r'<main\b[^>]*>(.*)</main>', h, re.S)
    corpo = m.group(1) if m else h
    # o que vem depois de "Fontes e leituras" e as caixas de navegação não ajudam a busca
    corpo = re.split(r'<h2[^>]*>\s*(?:Fontes e leituras|Fontes)\s*</h2>', corpo)[0]
    subs = [' '.join(_texto(x).split()) for x in re.findall(r'<h[23][^>]*>(.*?)</h[23]>', corpo, re.S)]
    return dict(t=html.unescape(t.group(1)).split(' | ')[0].strip() if t else '', d=html.unescape(d.group(1)) if d else '',
                subs=[s for s in subs if s], txt=_texto(corpo), links=len(re.findall(r'<a\s', corpo)))

def enriquece(root, paginas):
    arq = os.path.join(root, 'assets', 'busca.json')
    busca = json.load(open(arq, encoding='utf-8'))
    por_url = {}
    for b in busca: por_url.setdefault(b['u'], []).append(b)
    lidas = {}
    for p in dict.fromkeys(paginas):
        if p == '404.html' or not p.endswith('.html'): continue
        c = os.path.join(root, p)
        if os.path.exists(c):
            x = _ler(c)
            if x: lidas[p] = x
    # subtítulos que se repetem em muitas páginas ("Em resumo", "Continue") não distinguem nada
    freq = Counter(s for x in lidas.values() for s in set(x['subs']))
    comuns = {s for s, n in freq.items() if n >= max(8, len(lidas) // 40)}
    for p, x in lidas.items():
        grupo = por_url.get(p)
        if not grupo:
            if p == 'index.html': continue
            b = dict(t=x['t'], d=x['d'][:140], u=p); busca.append(b); por_url[p] = [b]
        else:  # várias entradas na mesma página (verbetes de um glossário): só a principal recebe o conteúdo
            b = next((y for y in grupo if norm(y['t']) == norm(x['t'])), None)
            if b is None:
                if len(grupo) > 1: continue
                b = grupo[0]
        subs = [s for s in dict.fromkeys(x['subs']) if s not in comuns and s != b['t']]
        if subs: b['s'] = ' · '.join(subs)[:400]
        ja = set(re.findall(r'[a-z0-9]+', norm(b['t'] + ' ' + b.get('d', '') + ' ' + b.get('s', ''))))
        pal = [w for w in dict.fromkeys(re.findall(r'[a-z0-9]+', norm(x['txt']))) if len(w) > 2 and w not in PARADAS and w not in ja and not w.isdigit()]
        # páginas que são listas de links (catálogo, índices, revisões) citariam qualquer termo: ficam sem o conteúdo
        if pal and x['links'] < 80: b['c'] = ' '.join(pal)
    json.dump(busca, open(arq, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, separators=(',', ':'))
    return len(busca)
