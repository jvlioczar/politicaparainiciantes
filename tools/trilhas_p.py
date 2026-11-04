"""Trilhas de estudo e os três casos-fio do curso de política."""
TRILHAS = [
 dict(s='duas-horas', n='Política em duas horas', d='O essencial: o que é política, valores e fatos, esquerda e direita, democracia, como uma lei é feita, como votar e como checar.', tempo='2 horas',
      licoes=['o-que-e-politica', 'valores-e-decisoes', 'esquerda-e-direita', 'democracia', 'como-uma-lei-e-feita', 'como-votar-bem', 'checagem-de-fatos', 'sem-binarismo']),
 dict(s='votar', n='Para votar melhor', d='Partidos, candidatos, pesquisas, promessas e as armadilhas do outsider e do mito.', tempo='2 horas',
      licoes=['o-que-e-um-partido', 'como-votar-bem', 'numero-de-projetos', 'pesquisas-eleitorais', 'comparar-projetos', 'perigo-do-outsider', 'perigo-do-messianismo', 'corrupcao']),
 dict(s='desinformacao', n='Contra a desinformação', d='Checagem, grupos de mensagem, bots, câmaras de eco, mídia alternativa e tradicional.', tempo='2 horas',
      licoes=['checagem-de-fatos', 'perigo-dos-grupos-de-mensagem', 'perigo-dos-bots', 'camaras-de-eco', 'perigo-da-midia-alternativa', 'como-ler-a-midia-tradicional', 'cambridge-analytica', 'pesquisas-eleitorais']),
 dict(s='perigos', n='Os perigos ideológicos', d='Maniqueísmo, fanatismo, tribalismo, medo, revoluções, reacionarismo, populismo, bode expiatório e golpismo.', tempo='3 horas',
      licoes=['perigo-do-maniqueismo', 'perigo-do-fanatismo', 'perigo-do-tribalismo', 'politica-do-medo', 'perigo-das-revolucoes', 'perigo-do-reacionarismo', 'perigo-do-populismo', 'perigo-de-culpar-o-estrangeiro', 'perigo-de-questionar-a-democracia']),
 dict(s='economia', n='Estado e economia', d='Os termos da economia, impostos, Estado e mercado, orçamento, bem comum, globalização e justiça.', tempo='3 horas',
      licoes=['economia-para-entender-politica', 'imposto-e-roubo', 'estado-e-mercado', 'politicas-publicas', 'bem-comum', 'globalizacao', 'divisao-internacional-do-trabalho', 'teorias-da-justica']),
 dict(s='mente', n='A mente política', d='Vieses, intuições morais, mudar de ideia, inteligência a serviço da crença, preconceito e sofismas.', tempo='2 horas',
      licoes=['vieses-cognitivos', 'mente-moralista', 'mudar-de-ideia', 'inteligencia-nao-protege', 'estereotipo-preconceito-discriminacao', 'sofismo', 'testar-visao-moral']),
 dict(s='etica', n='Ética na política', d='Valores, teorias, testes de imparcialidade, relativismo, progresso, quem conta e os animais na política.', tempo='3 horas',
      licoes=['valores-e-decisoes', 'etica-normativa', 'testar-visao-moral', 'relativismo-e-circulo-moral', 'progresso-moral-e-politico', 'sencientismo', 'politica-baseada-na-senciencia', 'direito-animal']),
]

CASOS_FIO = [
 ('onibus', 'A tarifa do ônibus', 'A prefeitura precisa decidir: subir a tarifa, subsidiar com imposto, ou mudar o contrato com a empresa. Cada escolha tem quem ganha e quem paga.'),
 ('frigorifico', 'O frigorífico da cidade', 'O maior empregador do município polui o rio, cria animais em confinamento e pede isenção fiscal para não fechar.'),
 ('boato', 'O boato na véspera', 'Um áudio falso contra um candidato viraliza nos grupos de mensagem na véspera da eleição. O candidato perde por pouco.'),
]
RESPOSTAS_FIO = {
'iniciante': [
 ('Valores e fatos', 'Valor: quem deve pagar o transporte, o usuário ou todos? Fato: quanto custa cada opção e o que acontece com a demanda.', 'Valor: o emprego vale mais que o rio e os animais? Fato: quantos empregos, quanta poluição, quanto custa a isenção.', 'Valor: vale tudo para vencer? Fato: o áudio é falso, e dá para provar.'),
 ('Esquerda e direita', 'A esquerda tende ao subsídio e à tarifa social; a direita, à concorrência e à tarifa que cubra o custo. Os dois têm casos a favor.', 'A direita tende a proteger o empregador; a esquerda, a regular. Nenhum dos dois costuma contar os animais.', 'Os dois lados já usaram e já sofreram boatos; o rótulo não protege.'),
 ('Democracia e instituições', 'Quem decide: prefeito, Câmara ou agência? A decisão passou por consulta?', 'A fiscalização ambiental existe e funciona? Quem aprova a isenção, e com que transparência?', 'A Justiça Eleitoral pode agir; a checagem e a imprensa livre são a defesa.'),
 ('Incentivos e interesses', 'A empresa quer o subsídio sem meta; o prefeito quer a tarifa baixa até a eleição.', 'Benefício concentrado (a empresa) contra custo espalhado (o rio, a saúde, os animais).', 'Quem produziu o áudio ganha; quem encaminhou não paga nada.'),
 ('Quem conta', 'Conta quem usa o ônibus, quem paga imposto e quem não tem carro.', 'Contam os trabalhadores, os vizinhos do rio e, se sentem, os animais confinados.', 'Conta o eleitor enganado e o candidato prejudicado; e conta a confiança de todos.'),
],
'intermediario': [
 ('Valores e fatos', 'Falha de mercado (monopólio de linha) e falha de governo (contrato mal desenhado): a pergunta certa é por setor, não Estado ou mercado.', 'Externalidade: o preço da carne não inclui o rio nem o sofrimento; a isenção transfere o custo a todos.', 'Mentira viraliza por emoção; a checagem chega tarde. O que a evidência diz sobre o efeito de boatos em eleições é menor do que parece, e ainda assim grave.'),
 ('Esquerda e direita', 'Teste do véu: que tarifa você aceitaria sem saber se teria carro? As vertentes divergem sobre subsidiar ou abrir concorrência, não sobre o teste.', 'O libertarismo de coração sangrante e a social-democracia discordam do meio, não da prioridade a quem está pior; ambos tendem a ignorar os animais.', 'Populistas de qualquer lado usam o boato; liberais e democratas de qualquer lado dependem de que ele seja punido.'),
 ('Democracia e instituições', 'Orçamento: subsídio compete com saúde e educação na LOA; emendas podem distorcer a decisão.', 'Captura: a empresa escreve a lei que a regula? Lobby transparente é legítimo; captura, não.', 'Como democracias morrem: pela erosão da confiança na informação. A regulação das redes é o debate aberto.'),
 ('Incentivos e interesses', 'Benefício concentrado (empresa) e custo espalhado (passageiros e contribuintes): quem se organiza vence sem que ninguém perceba.', 'A corrupção como conta de incentivos: discricionariedade na isenção, pouca auditoria, ganho alto.', 'Disparo em massa e bots criam a ilusão de consenso; quem financia raramente aparece.'),
 ('Quem conta', 'Pensar no bem comum: os piores (quem depende do ônibus) primeiro, e o longo prazo (a cidade sem carro).', 'Direito ambiental e direito animal: a lei protege o rio e proíbe a crueldade, mas pouco alcança a criação industrial.', 'Direitos humanos e liberdade de expressão: a mentira deliberada não é opinião; o limite é estreito e definido.'),
],
'avancado': [
 ('Valores e fatos', 'Políticas baseadas em evidência: testar tarifa zero num bairro, medir, corrigir. Valor decide o fim; evidência, o meio.', 'Teorias da justiça: Rawls aceita a isenção se beneficiar os piores; Nozick a rejeita como privilégio; o utilitarista soma, incluindo os animais se for coerente.', 'Inteligência a serviço da crença: quem já desconfiava do candidato acredita no áudio e o defende com mais habilidade.'),
 ('Esquerda e direita', 'Pragmatismo: julgar pelo que produz; a ética da responsabilidade de Weber cobra as consequências previsíveis da tarifa.', 'A crítica ao identitarismo e ao economicismo converge: nenhum dos dois conta quem não vota; o sencientismo é a lente que faltava.', 'Teoria da ferradura nos métodos: extremos dos dois lados aceitam o boato como arma; o centro não está imune.'),
 ('Democracia e instituições', 'Presidencialismo de coalizão em escala municipal: o subsídio vira moeda de troca na Câmara.', 'Melhorar a democracia: assembleias cidadãs sorteadas decidiriam melhor do que a Câmara capturada?', 'Atores malevolentes prosperam onde o boato não tem custo; instituições devem supor o pior candidato, não o melhor.'),
 ('Incentivos e interesses', 'Riscos de longo prazo: uma cidade desenhada para o carro é uma decisão quase irreversível.', 'Progresso moral e político: a lei ambiental avançou; a prática, não. O que faz a prática acompanhar?', 'Fanatismo ideológico: a certeza absoluta sobre o adversário é o que torna o boato crível e a punição desejada.'),
 ('Quem conta', 'Política baseada na senciência: a tarifa afeta quem respira a poluição, inclusive quem não vota.', 'Sencientismo: os animais do frigorífico são a maioria dos afetados e não aparecem em nenhuma planilha; a avaliação de impacto os incluiria.', 'Relativismo e círculo moral: a verdade não é relativa ao lado; a defesa do eleitor enganado vale para o adversário também.'),
],
}
