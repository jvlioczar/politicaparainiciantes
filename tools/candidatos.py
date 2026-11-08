"""Todas as pessoas que disputaram a Presidência nas eleições diretas da Nova República (1989 a 2026), com partido e
percentual no 1º turno, a partir das páginas da Wikipédia de cada eleição. CAND_FIG traz as figuras que ainda não
estavam no site, nos mesmos campos de figuras.py. HIST monta o histórico de cada candidatura."""
EXD, DIR, CDI, CEN, CES, ESQ, EXE = 'Extrema-direita', 'Direita', 'Centro-direita', 'Centro', 'Centro-esquerda', 'Esquerda', 'Extrema-esquerda'
POL, JOR, INT, INF, ART, JUR, REL = 'Político', 'Jornalista', 'Intelectual', 'Influenciador', 'Artista', 'Jurista', 'Líder religioso'
LULA, FHC = 'Luiz Inácio Lula da Silva', 'Fernando Henrique Cardoso'

# ano: [(nome no site, partido, % no 1º turno)]
ELEICOES = {
 '1989': [('Fernando Collor', 'PRN', '30,48'), (LULA, 'PT', '17,19'), ('Leonel Brizola', 'PDT', '16,51'), ('Mário Covas', 'PSDB', '11,52'), ('Paulo Maluf', 'PDS', '8,85'), ('Guilherme Afif Domingos', 'PL', '4,84'), ('Ulysses Guimarães', 'PMDB', '4,74'), ('Roberto Freire', 'PCB', '1,14'), ('Aureliano Chaves', 'PFL', '0,89'), ('Ronaldo Caiado', 'PSD', '0,72'), ('Affonso Camargo Neto', 'PTB', '0,56'), ('Enéas Carneiro', 'Prona', '0,53'), ('Marronzinho', 'PSP', '0,35'), ('Paulo Gontijo', 'PP', '0,29'), ('Zamir Teixeira', 'PCN', '0,28'), ('Lívia Maria Pio', 'PN', '0,27'), ('Eudes Mattar', 'PLP', '0,24'), ('Fernando Gabeira', 'PV', '0,19'), ('Celso Brant', 'PMN', '0,16'), ('Antônio Pedreira', 'PPB', '0,13'), ('Manoel Horta', 'PDC do B', '0,12')],
 '1994': [(FHC, 'PSDB', '54,75'), (LULA, 'PT', '26,60'), ('Enéas Carneiro', 'Prona', '7,30'), ('Orestes Quércia', 'PMDB', '4,37'), ('Leonel Brizola', 'PDT', '3,33'), ('Esperidião Amin', 'PPR', '2,73'), ('Carlos Antônio Gomes', 'PRN', '0,55'), ('Hernani Fortuna', 'PSC', '0,38')],
 '1998': [(FHC, 'PSDB', '53,06'), (LULA, 'PT', '31,71'), ('Ciro Gomes', 'PPS', '10,97'), ('Enéas Carneiro', 'Prona', '2,14'), ('Ivan Frota', 'PMN', '0,37'), ('Alfredo Sirkis', 'PV', '0,31'), ('Zé Maria', 'PSTU', '0,30'), ('João de Deus Barbosa de Jesus', 'PTdoB', '0,29'), ('José Maria Eymael', 'PSDC', '0,25'), ('Thereza Ruiz', 'PTN', '0,25'), ('Sérgio Bueno', 'PSC', '0,18'), ('Vasco Azevedo Neto', 'PSN', '0,16')],
 '2002': [(LULA, 'PT', '46,44'), ('José Serra', 'PSDB', '23,20'), ('Anthony Garotinho', 'PSB', '17,87'), ('Ciro Gomes', 'PPS', '11,97'), ('Zé Maria', 'PSTU', '0,47'), ('Rui Costa Pimenta', 'PCO', '0,05')],
 '2006': [(LULA, 'PT', '48,61'), ('Geraldo Alckmin', 'PSDB', '41,64'), ('Heloísa Helena', 'PSOL', '6,85'), ('Cristovam Buarque', 'PDT', '2,64'), ('Ana Maria Rangel', 'PRP', '0,13'), ('José Maria Eymael', 'PSDC', '0,07'), ('Luciano Bivar', 'PSL', '0,06'), ('Rui Costa Pimenta', 'PCO', '0,00')],
 '2010': [('Dilma Rousseff', 'PT', '46,91'), ('José Serra', 'PSDB', '32,61'), ('Marina Silva', 'PV', '19,33'), ('Plínio de Arruda Sampaio', 'PSOL', '0,87'), ('José Maria Eymael', 'PSDC', '0,09'), ('Zé Maria', 'PSTU', '0,08'), ('Levy Fidelix', 'PRTB', '0,06'), ('Ivan Pinheiro', 'PCB', '0,04'), ('Rui Costa Pimenta', 'PCO', '0,01')],
 '2014': [('Dilma Rousseff', 'PT', '41,59'), ('Aécio Neves', 'PSDB', '33,55'), ('Marina Silva', 'PSB', '21,32'), ('Luciana Genro', 'PSOL', '1,55'), ('Pastor Everaldo', 'PSC', '0,75'), ('Eduardo Jorge', 'PV', '0,61'), ('Levy Fidelix', 'PRTB', '0,43'), ('Zé Maria', 'PSTU', '0,09'), ('José Maria Eymael', 'PSDC', '0,06'), ('Mauro Iasi', 'PCB', '0,05'), ('Rui Costa Pimenta', 'PCO', '0,01')],
 '2018': [('Jair Bolsonaro', 'PSL', '46,03'), ('Fernando Haddad', 'PT', '29,28'), ('Ciro Gomes', 'PDT', '12,47'), ('Geraldo Alckmin', 'PSDB', '4,76'), ('João Amoêdo', 'Novo', '2,50'), ('Cabo Daciolo', 'Patriota', '1,26'), ('Henrique Meirelles', 'MDB', '1,20'), ('Marina Silva', 'Rede', '1,00'), ('Alvaro Dias', 'Podemos', '0,80'), ('Guilherme Boulos', 'PSOL', '0,58'), ('Vera Lúcia', 'PSTU', '0,05'), ('José Maria Eymael', 'DC', '0,04'), ('João Goulart Filho', 'PPL', '0,03')],
 '2022': [(LULA, 'PT', '48,43'), ('Jair Bolsonaro', 'PL', '43,20'), ('Simone Tebet', 'MDB', '4,16'), ('Ciro Gomes', 'PDT', '3,04'), ('Soraya Thronicke', 'União Brasil', '0,51'), ("Felipe d'Avila", 'Novo', '0,47'), ('Padre Kelmon', 'PTB', '0,07'), ('Léo Péricles', 'UP', '0,05'), ('Sofia Manzano', 'PCB', '0,04'), ('Vera Lúcia', 'PSTU', '0,02'), ('José Maria Eymael', 'DC', '0,01')],
 '2026': [(LULA, 'PT', '45,16'), ('Flávio Bolsonaro', 'PL', '47,03'), ('Augusto Cury', 'Avante', '2,89'), ('Renan Santos', 'Missão', '2,24'), ('Ronaldo Caiado', 'PSD', '2,18'), ('Romeu Zema', 'Novo', '0,27'), ('Samara Martins', 'UP', '0,10'), ('Hertz Dias', 'PSTU', '0,04'), ('Clariana Barão', 'DC', '0,03'), ('Edmilson Costa', 'PCB', '0,02'), ('Wilson Grassi', 'Democrata', '0,01'), ('Rui Costa Pimenta', 'PCO', '0,01')],
}
# ano: (eleito, % no 2º turno ou None, derrotado no 2º turno, % dele)
DESFECHO = {
 '1989': ('Fernando Collor', '53,03', LULA, '46,97'), '1994': (FHC, None, None, None), '1998': (FHC, None, None, None),
 '2002': (LULA, '61,27', 'José Serra', '38,73'), '2006': (LULA, '60,83', 'Geraldo Alckmin', '39,17'),
 '2010': ('Dilma Rousseff', '56,05', 'José Serra', '43,95'), '2014': ('Dilma Rousseff', '51,64', 'Aécio Neves', '48,36'),
 '2018': ('Jair Bolsonaro', '55,13', 'Fernando Haddad', '44,87'), '2022': (LULA, '50,90', 'Jair Bolsonaro', '49,10'),
 '2026': (LULA, '51,79', 'Flávio Bolsonaro', '48,21'),
}
MULHERES = {'Lívia Maria Pio', 'Thereza Ruiz', 'Heloísa Helena', 'Ana Maria Rangel', 'Dilma Rousseff', 'Marina Silva', 'Luciana Genro', 'Vera Lúcia', 'Simone Tebet', 'Soraya Thronicke', 'Sofia Manzano', 'Samara Martins', 'Clariana Barão'}

def _texto(ano, nome, partido, pct):
    a = 'a' if nome in MULHERES else 'o'
    el, p2, der, pd = DESFECHO[ano]
    pr = 'pela' if partido in ('Rede', 'UP', 'DC') else 'pelo'
    base = f'Candidat{a} {pr} {partido}, com {pct}% no 1º turno'
    if nome == el: return base + (f'. Eleit{a} no 2º turno, com {p2}%.' if p2 else f'. Eleit{a} no 1º turno.')
    if nome == der: return base + f'. Derrotad{a} no 2º turno, com {pd}%.'
    return base + '.'

HIST = {}
for _ano, _lista in ELEICOES.items():
    for _n, _p, _pct in _lista:
        HIST.setdefault(_n, []).append((_ano, _texto(_ano, _n, _p, _pct)))

_A = 'Categoria aproximada, por falta de posições públicas conhecidas.'
CAND_FIG = [
('Guilherme Afif Domingos','',CDI,POL,'psd','Empresário, vice-governador de São Paulo (2011-2014), ministro da Micro e Pequena Empresa no governo Dilma e assessor de Paulo Guedes.','Liberal na economia e ligado ao empresariado; passou pelo PL, pelo DEM e pelo PSD. Categoria aproximada.',[]),
('Aureliano Chaves','',CDI,POL,'','Governador de Minas Gerais (1975-1978) e vice-presidente de João Figueiredo (1979-1985). Morreu em 2003.','Vice da ditadura que apoiou a transição para a Nova República e foi candidato do PFL em 1989. Categoria aproximada.',[]),
('Affonso Camargo Neto','',CDI,POL,'','Engenheiro, senador pelo Paraná e ministro dos Transportes de Sarney e de Collor (1929-2011).','Político de partidos de centro-direita; candidato do PTB em 1989. Categoria aproximada.',[]),
('Marronzinho','',CEN,POL,'','José Alcides Marronzinho de Oliveira, sindicalista e figura folclórica da política paulista nos anos 1980.','Sem identidade ideológica clara; ficou conhecido por declarações controversas e por responder a dezenas de processos por calúnia e difamação. Categoria aproximada.',[]),
('Paulo Gontijo',None,CEN,POL,'','Candidato do pequeno Partido do Povo (PP) à Presidência em 1989.',_A,[]),
('Zamir Teixeira','Zamir José Teixeira',CEN,POL,'','Empresário e vereador em Campo Mourão, no Paraná, candidato pelo PCN em 1989.',_A,[]),
('Lívia Maria Pio',None,CEN,POL,'','Advogada, primeira mulher a disputar a Presidência do Brasil, pelo PN em 1989.',_A,[]),
('Eudes Mattar',None,CEN,POL,'','Candidato do Partido Liberal Progressista (PLP) à Presidência em 1989.',_A,[]),
('Celso Brant','',CEN,POL,'','Jurista, professor e escritor mineiro (1920-2004), candidato pelo PMN em 1989.','Nacionalista na economia. Categoria aproximada.',[]),
('Antônio Pedreira','',CEN,POL,'','Jornalista baiano (1943-2013), candidato pelo PPB em 1989.',_A,[]),
('Manoel Horta',None,CEN,POL,'','Candidato do PDC do B à Presidência em 1989.',_A,[]),
('Orestes Quércia','',CEN,POL,'mdb','Governador de São Paulo (1987-1991) e chefe do PMDB paulista por décadas (1938-2010).','Político de centro e de base municipalista, típico do PMDB. Categoria aproximada.',[]),
('Esperidião Amin','',CDI,POL,'pp','Governador de Santa Catarina por dois mandatos, senador e deputado federal pelo PP.','Conservador, de um partido herdeiro da Arena. Categoria aproximada.',[]),
('Carlos Antônio Gomes','',CEN,POL,'','Advogado gaúcho (1942-2017), candidato pelo PRN em 1994.',_A,[]),
('Hernani Fortuna','',DIR,POL,'uniao','Almirante da reserva e ex-comandante da Escola Superior de Guerra, candidato pelo PSC em 1994.','Militar conservador. Categoria aproximada.',[]),
('Ivan Frota','',DIR,POL,'','Brigadeiro reformado da Aeronáutica (1930-2022), candidato pelo PMN em 1998.','Militar nacionalista. Categoria aproximada.',[]),
('João de Deus Barbosa de Jesus','',CEN,POL,'','Comerciante, jornalista e escritor baiano (1932-2002), candidato pelo PTdoB em 1998.',_A,[]),
('Thereza Ruiz','',CEN,POL,'','Administradora de empresas, segunda mulher a disputar a Presidência, pelo PTN em 1998.',_A,[]),
('Sérgio Bueno',None,CEN,POL,'','Candidato do PSC à Presidência em 1998.',_A,[]),
('Vasco Azevedo Neto','',CEN,POL,'','Engenheiro e ex-deputado federal pela Bahia (1916-2010), candidato pelo PSN em 1998.',_A,[]),
('Ana Maria Rangel',None,CEN,POL,'','Candidata do PRP à Presidência em 2006.',_A,[]),
('Luciano Bivar','',CDI,POL,'uniao','Empresário, presidente do PSL, partido pelo qual Bolsonaro se elegeu em 2018, e depois do União Brasil.','Rompeu com Bolsonaro em 2019, numa disputa pelo comando do PSL. Categoria aproximada.',[]),
('Plínio de Arruda Sampaio','',ESQ,POL,'psol','Promotor, deputado constituinte e militante católico de esquerda (1930-2014).','Defensor da reforma agrária; foi do PT e depois do PSOL.',[]),
('Ivan Pinheiro',None,EXE,POL,'pcb','Ex-secretário-geral do PCB, candidato à Presidência em 2010.','Marxista-leninista.',[]),
('Pastor Everaldo','',DIR,REL,'','Pastor da Assembleia de Deus e ex-presidente do PSC, candidato à Presidência em 2014.','Conservador religioso; o PSC lançou Wilson Witzel ao governo do Rio em 2018.',[]),
('João Goulart Filho','',CES,POL,'','Filho do ex-presidente João Goulart, candidato pelo PPL em 2018.','Trabalhista e nacionalista, no legado do pai. Categoria aproximada.',[]),
('Sofia Manzano',None,EXE,INT,'pcb','Economista e professora, candidata do PCB à Presidência em 2022.','Marxista-leninista.',[]),
('Hertz Dias',None,EXE,POL,'pstu','Professor, candidato do PSTU à Presidência em 2026.','Trotskista.',[]),
('Clariana Barão',None,CDI,POL,'dc','Advogada, candidata da Democracia Cristã à Presidência em 2026, depois das desistências de Aldo Rebelo e de Joaquim Barbosa.','Democracia cristã. Categoria aproximada.',[]),
('Edmilson Costa',None,EXE,INT,'pcb','Economista, candidato do PCB à Presidência em 2026.','Marxista-leninista.',[]),
('Wilson Grassi',None,CEN,POL,'democrata','Veterinário, candidato do Democrata, antigo Partido da Mulher Brasileira, à Presidência em 2026.',_A,[]),
]

# detalhes que valem manter junto ao resultado
ANOTA = {
 ('Marina Silva', '2014'): 'Substituiu Eduardo Campos, morto num acidente aéreo durante a campanha.',
 ('Enéas Carneiro', '1989'): 'Ficou famoso pelo bordão “Meu nome é Enéas”.',
 ('Leonel Brizola', '1989'): 'Ficou a menos de um ponto de ir ao 2º turno.',
 ('Fernando Haddad', '2018'): 'Entrou depois que o TSE barrou a candidatura de Lula.',
 ('Padre Kelmon', '2022'): 'Substituiu Roberto Jefferson, barrado pela Justiça Eleitoral.',
}
