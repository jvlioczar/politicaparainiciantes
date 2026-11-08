"""Candidatos à Presidência que foram a debates na TV nos últimos dez anos, a partir das páginas da Wikipédia de cada eleição.
Em 2018, os debates de Band, RedeTV!, Gazeta, Aparecida, SBT, Record e Globo. Em 2022, Band, SBT e Globo. Em 2026, Band, Veja/Rede Brasil e Globo."""
D18 = 'Band, RedeTV!, Estadão/Gazeta, Aparecida, SBT, Record e Globo'
DEBATES = {
 'Jair Bolsonaro': [('2018', 'Candidato pelo PSL, eleito. Foi aos debates da Band e da RedeTV!, antes do atentado.'), ('2022', 'Candidato à reeleição pelo PL. Debates da Band, do SBT e da Globo, e o da Band no 2º turno.')],
 'Geraldo Alckmin': [('2018', f'Candidato pelo PSDB. Debates: {D18}.')],
 'Marina Silva': [('2018', f'Candidata pela Rede. Debates: {D18}.')],
 'Ciro Gomes': [('2018', f'Candidato pelo PDT. Debates: {D18}.'), ('2022', 'Candidato pelo PDT. Debates da Band, do SBT e da Globo.')],
 'Alvaro Dias': [('2018', f'Candidato pelo Podemos. Debates: {D18}.')],
 'Henrique Meirelles': [('2018', f'Candidato pelo MDB. Debates: {D18}.')],
 'Guilherme Boulos': [('2018', f'Candidato pelo PSOL. Debates: {D18}.')],
 'Cabo Daciolo': [('2018', 'Candidato pelo Patriota. Debates da Band, da RedeTV!, do SBT e da Record.')],
 'Fernando Haddad': [('2018', 'Candidato pelo PT após o TSE barrar Lula. Debates da Aparecida, do SBT, da Record e da Globo no 1º turno. Não houve debate no 2º turno.')],
 'Luiz Inácio Lula da Silva': [('2022', 'Candidato pelo PT, eleito. Debates da Band e da Globo no 1º turno, e o da Band no 2º. Faltou ao do SBT.'), ('2026', 'Candidato à reeleição pelo PT. Faltou ao debate da Band no 1º turno e foi ao da Globo no 2º turno.')],
 'Simone Tebet': [('2022', 'Candidata pelo MDB. Debates da Band, do SBT e da Globo.')],
 'Soraya Thronicke': [('2022', 'Candidata pelo União Brasil. Debates da Band, do SBT e da Globo.')],
 "Felipe d'Avila": [('2022', 'Candidato pelo Novo. Debates da Band, do SBT e da Globo.')],
 'Padre Kelmon': [('2022', 'Candidato pelo PTB, em substituição a Roberto Jefferson. Debates do SBT e da Globo.')],
 'Renan Santos': [('2026', 'Candidato pelo Missão. Debate da Band.')],
 'Ronaldo Caiado': [('2026', 'Candidato pelo PSD. Debates da Band e de Veja/Rede Brasil.')],
 'Augusto Cury': [('2026', 'Candidato pelo Avante. Debate da Band.')],
 'Romeu Zema': [('2026', 'Candidato pelo Novo. Debate de Veja/Rede Brasil.')],
 'Flávio Bolsonaro': [('2026', 'Candidato pelo PL. Faltou ao debate da Band no 1º turno e foi ao da Globo no 2º turno.')],
}
# Candidatos anteriores que também devem aparecer com o histórico
ANTIGOS = {
 'Ciro Gomes': [('1998', 'Candidato pelo PPS, com 10,97%.'), ('2002', 'Candidato pelo PPS, com 11,97%.')],
 'Marina Silva': [('2010', 'Candidata pelo PV, com 19,33%.'), ('2014', 'Candidata pelo PSB, após a morte de Eduardo Campos.')],
 'Geraldo Alckmin': [('2006', 'Candidato pelo PSDB, derrotado por Lula no 2º turno.')],
 'Luiz Inácio Lula da Silva': [('1989', 'Candidato pelo PT, derrotado por Collor no 2º turno.'), ('1994', 'Candidato pelo PT, 2º lugar.'), ('1998', 'Candidato pelo PT, 2º lugar.'), ('2002', 'Candidato pelo PT, eleito.'), ('2006', 'Candidato pelo PT, reeleito.')],
 'Enéas Carneiro': [('1989', 'Candidato pelo Prona, com seu famoso “Meu nome é Enéas”.'), ('1994', 'Candidato pelo Prona, ficou em 3º lugar.'), ('1998', 'Candidato pelo Prona.')],
 'Leonel Brizola': [('1989', 'Candidato pelo PDT, ficou em 3º, a 0,5% dos votos de ir ao 2º turno.'), ('1994', 'Candidato pelo PDT, com 3,18%.'), ('1998', 'Vice na chapa de Lula.')],
}
