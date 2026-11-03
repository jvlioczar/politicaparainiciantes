"""Baixa da API da Câmara como cada partido votou em votações históricas e grava data/votos.json.
Uso: python tools/coleta_votos.py. Só precisa rodar de novo para acrescentar votações."""
import collections, concurrent.futures as cf, json, os, re, urllib.parse, urllib.request
API = 'https://dadosabertos.camara.leg.br/api/v2/'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# (rótulo, ano, explicação, id da votação ou (id da proposição, placar para localizar a votação))
ALVOS = [
 ('Teto de Gastos', '2016', 'Limitou o crescimento das despesas federais por 20 anos.', '2088351-235'),
 ('Reforma trabalhista', '2017', 'Mudou a CLT e deu mais peso a acordos entre empresas e trabalhadores.', (2122076, 'Sim: 296')),
 ('Reforma da Previdência', '2019', 'Mudou idades e regras de aposentadoria.', '2192459-636'),
 ('Marco do Saneamento', '2019', 'Abriu o saneamento a mais concorrência privada.', (2207613, 'Sim 276')),
 ('Autonomia do Banco Central', '2021', 'Deu mandato próprio à diretoria do BC.', (2265124, 'Sim: 339')),
 ('Privatização da Eletrobras', '2021', 'Autorizou a desestatização da empresa.', '2270789-73'),
 ('Voto impresso', '2021', 'Propunha cédula impressa auditável. Teve maioria simples, mas não os 308 votos exigidos, e foi rejeitada.', '2220292-229'),
 ('Marco temporal', '2023', 'Limitava a demarcação de terras indígenas às ocupadas em 1988.', '345311-270'),
 ('Arcabouço fiscal', '2023', 'Substituiu o Teto de Gastos por novas regras fiscais.', '2357053-47'),
 ('Reforma tributária', '2023', 'Unificou impostos sobre o consumo. Votação em 1º turno.', '2196833-326'),
 ('Fim da saída temporária', '2024', 'Restringiu as “saidinhas” de presos. Emendas do Senado.', '493361-84'),
 ('PEC da Blindagem', '2025', 'Dificultava processos contra parlamentares. Votação em 1º turno.', '2270800-135'),
 ('PL da Dosimetria', '2025', 'Reduz penas de condenados pelos atos de 8 de janeiro de 2023.', '2358548-89'),
]
def get(p):
    for t in range(4):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(API + p, headers={'Accept': 'application/json', 'User-Agent': 'politicaparainiciantes/1.0'}), timeout=90))['dados']
        except Exception as e: err = e
    print('falhou', p, err); return []
def um(a):
    rot, ano, desc, alvo = a
    if isinstance(alvo, tuple):
        vs = [v for v in get(f'proposicoes/{alvo[0]}/votacoes') if alvo[1] in (v.get('descricao') or '')]
        if not vs: print('não achei', rot); return None
        vid = vs[0]['id']
    else: vid = alvo
    v = get(f'votacoes/{vid}')
    votos = get(f'votacoes/{vid}/votos')
    if len(votos) < 100: print('sem votos nominais', rot, len(votos)); return None
    por, tot = collections.defaultdict(collections.Counter), collections.Counter()
    for x in votos:
        por[x['deputado_']['siglaPartido']][x['tipoVoto']] += 1; tot[x['tipoVoto']] += 1
    d = v if isinstance(v, dict) else {}
    print(rot, vid, dict(tot))
    return dict(rot=rot, ano=ano, desc=desc, id=vid, data=d.get('data', ''), texto=(d.get('descricao') or '')[:300], tot=dict(tot), partidos={k: dict(c) for k, c in por.items()})
out = [r for r in cf.ThreadPoolExecutor(5).map(um, ALVOS) if r]
os.makedirs(os.path.join(ROOT, 'data'), exist_ok=True)
json.dump(out, open(os.path.join(ROOT, 'data', 'votos.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(out), 'votações gravadas')
