"""Cargos, poderes, história, ranking e páginas de referência. Datas verificadas em novembro de 2026."""

CARGOS = [
 dict(n='Vereador(a)', esfera='Município', poder='Legislativo', mandato='4 anos', idade='18', vagas='De 9 a 55, conforme a população', eleicao='Proporcional', faz='Propõe e vota leis municipais, aprova o orçamento da cidade e fiscaliza a prefeitura. Pode abrir CPI municipal e cassar o prefeito.', nao='Não asfalta rua nem constrói escola: pode pedir, mas quem executa é a prefeitura.'),
 dict(n='Prefeito(a)', esfera='Município', poder='Executivo', mandato='4 anos, com uma reeleição', idade='21', vagas='1 por município (mais de 5.500 no país)', eleicao='Majoritária; 2º turno se houver mais de 200 mil eleitores', faz='Governa a cidade: escolas de educação básica, postos de saúde, transporte urbano, coleta de lixo, ruas e plano diretor.', nao='Não muda lei federal e não controla a Polícia Militar.'),
 dict(n='Deputado(a) estadual ou distrital', esfera='Estado', poder='Legislativo', mandato='4 anos', idade='21', vagas='De 24 a 94, conforme o estado', eleicao='Proporcional', faz='Faz leis estaduais, aprova o orçamento do estado e fiscaliza o governador.', nao='Não legisla sobre direito penal ou trabalhista, que são federais.'),
 dict(n='Governador(a)', esfera='Estado', poder='Executivo', mandato='4 anos, com uma reeleição', idade='30', vagas='27 (26 estados e o DF)', eleicao='Majoritária com 2º turno', faz='Comanda as polícias Civil e Militar, as escolas de ensino médio, hospitais estaduais e estradas estaduais.', nao='Não muda o Código Penal nem controla a Polícia Federal.'),
 dict(n='Deputado(a) federal', esfera='União', poder='Legislativo', mandato='4 anos', idade='21', vagas='513 na Câmara, de 8 a 70 por estado', eleicao='Proporcional', faz='Representa a população. Propõe e vota leis nacionais e emendas à Constituição, vota o orçamento e autoriza abrir processo de impeachment.', nao='Não executa obras. Indica verbas por emendas, mas a execução é do Executivo.'),
 dict(n='Senador(a)', esfera='União', poder='Legislativo', mandato='8 anos', idade='35', vagas='81, sendo 3 por estado', eleicao='Majoritária; renovação de 1/3 e 2/3 alternadamente', faz='Representa os estados. Vota e revisa leis, aprova ministros do STF e embaixadores, e julga o presidente em impeachment.', nao='Não tem mais peso por estado populoso: São Paulo e Roraima têm 3 cada.'),
 dict(n='Presidente da República', esfera='União', poder='Executivo', mandato='4 anos, com uma reeleição', idade='35', vagas='1', eleicao='Majoritária com 2º turno', faz='Chefe de Estado e de governo. Nomeia ministros, propõe e veta leis, edita medidas provisórias, comanda as Forças Armadas e a política externa, e indica ministros do STF.', nao='Não faz lei sozinho nem fecha o Congresso ou o STF.'),
 dict(n='Vice (presidente, governador ou prefeito)', esfera='Todas', poder='Executivo', mandato='O mesmo do titular', idade='A do titular', vagas='1 por chapa', eleicao='Junto com o titular', faz='Substitui o titular em ausências e assume em caso de vaga.', nao='Não tem poder próprio, além do que o titular delegar.'),
 dict(n='Ministro(a) de Estado', esfera='União', poder='Executivo', mandato='Sem prazo; livre nomeação', idade='21', vagas='Definidas por lei do governo', eleicao='Nomeado pelo presidente', faz='Comanda uma área do governo, como saúde, educação ou fazenda.', nao='Não é eleito, e pode ser demitido a qualquer hora.'),
 dict(n='Secretário(a) estadual ou municipal', esfera='Estado/Município', poder='Executivo', mandato='Sem prazo; livre nomeação', idade='Varia', vagas='Conforme o governo', eleicao='Nomeado', faz='Equivalente local do ministro: saúde, educação, segurança, transporte.', nao='Não é eleito.'),
]

ORGAOS = [
 ('Supremo Tribunal Federal (STF)', 'Judiciário', '11 ministros, indicados pelo presidente e aprovados pelo Senado; aposentadoria aos 75 anos.', 'Guarda a Constituição. Julga se leis são constitucionais e processa autoridades como presidente e parlamentares.'),
 ('Superior Tribunal de Justiça (STJ)', 'Judiciário', '33 ministros.', 'Dá a última palavra sobre leis federais que não envolvem a Constituição.'),
 ('Tribunal Superior Eleitoral (TSE)', 'Judiciário', '7 ministros, vindos do STF, do STJ e da advocacia.', 'Organiza as eleições, registra partidos e julga crimes e disputas eleitorais.'),
 ('Tribunais de Justiça e federais', 'Judiciário', 'Juízes concursados e desembargadores.', 'Julgam os casos do dia a dia na primeira e na segunda instância.'),
 ('Ministério Público (MP)', 'Função essencial', 'Promotores e procuradores concursados. O procurador-geral da República é indicado pelo presidente.', 'Acusa em ações penais e defende a lei e os interesses coletivos. Não é governo nem advogado do governo.'),
 ('Defensoria Pública', 'Função essencial', 'Defensores concursados.', 'Dá assistência jurídica gratuita a quem não pode pagar.'),
 ('Advocacia-Geral da União (AGU)', 'Função essencial', 'Advogado-geral nomeado pelo presidente.', 'É a advogada do governo federal.'),
 ('Tribunal de Contas da União (TCU)', 'Auxilia o Legislativo', '9 ministros, indicados pelo Congresso e pelo presidente.', 'Fiscaliza o uso do dinheiro federal. Estados e alguns municípios têm tribunais próprios.'),
 ('Polícia Federal', 'Executivo', 'Subordinada ao Ministério da Justiça.', 'Investiga crimes federais, como corrupção com dinheiro da União e tráfico internacional.'),
 ('Polícias Civil e Militar', 'Executivo estadual', 'Subordinadas ao governador.', 'A Civil investiga, a Militar patrulha.'),
 ('Forças Armadas', 'Executivo', 'Sob comando do presidente.', 'Defendem o país. A Constituição não lhes dá papel de “poder moderador”, como confirmou o STF.'),
 ('Banco Central', 'Autarquia autônoma', 'Diretoria com mandato próprio desde 2021.', 'Define juros e cuida da estabilidade da moeda.'),
 ('Agências reguladoras', 'Autarquias', 'Diretores com mandato, como Anvisa, Anatel e ANP.', 'Regulam e fiscalizam setores específicos.'),
]

HISTORIA = [
 ('1500–1822', 'Colônia', 'Portugal explora a terra e os povos indígenas, com economia baseada em escravidão africana. O poder local fica com grandes proprietários. A Inconfidência Mineira (1789) é reprimida.'),
 ('1822–1889', 'Império', 'D. Pedro I declara a Independência em 1822 e outorga a Constituição de 1824, com o Poder Moderador. O voto é censitário. O Brasil é o último país das Américas a abolir a escravidão (1888).'),
 ('1889–1930', 'República Velha', 'Um golpe militar proclama a República. A Constituição de 1891 separa Igreja e Estado. Na “política do café com leite”, oligarquias de São Paulo e Minas se revezam; o voto é aberto, e o coronelismo manda no interior.'),
 ('1930–1945', 'Era Vargas', 'A Revolução de 1930 leva Getúlio Vargas ao poder. Em 1932 vêm o voto secreto e o voto feminino; em 1943, a CLT. Em 1937, o Estado Novo vira ditadura, com censura e perseguição.'),
 ('1946–1964', 'República de 1946', 'Eleições competitivas com PSD, UDN e PTB. Vargas volta eleito e se mata em 1954. JK constrói Brasília. Jânio renuncia em 1961. João Goulart defende reformas de base em meio à polarização da Guerra Fria.'),
 ('1964–1985', 'Ditadura militar', 'Golpe depõe Goulart. Bipartidarismo com Arena e MDB. O AI-5 (1968) fecha o Congresso e amplia censura e tortura. A Comissão Nacional da Verdade reconheceu 434 mortos e desaparecidos. Há crescimento no “milagre” e, depois, dívida e inflação. Lei da Anistia em 1979.'),
 ('1985–1990', 'Redemocratização', 'As Diretas Já perdem no Congresso em 1984, mas Tancredo Neves vence no Colégio Eleitoral. Ele morre antes da posse, e José Sarney assume. A Constituição de 1988, a “Cidadã”, cria o SUS e amplia direitos.'),
 ('1990–1994', 'Collor e Itamar', 'Collor, o primeiro presidente eleito diretamente após a ditadura, confisca a poupança e sofre impeachment em 1992. Itamar Franco assume, e o Plano Real (1994) derruba a hiperinflação.'),
 ('1995–2002', 'FHC', 'Estabilidade, privatizações e Lei de Responsabilidade Fiscal. A emenda da reeleição é aprovada em 1997 sob suspeita de compra de votos. Surgem programas como o Bolsa Escola.'),
 ('2003–2010', 'Lula 1 e 2', 'Crescimento com alta das commodities, Bolsa Família e queda da pobreza. Em 2005, o escândalo do mensalão; em 2012, o STF condena os envolvidos.'),
 ('2011–2016', 'Dilma', 'Primeira presidenta. Junho de 2013 leva milhões às ruas. A Lava Jato começa em 2014, com recessão severa em 2015-2016. Impeachment em 2016, por crime de responsabilidade fiscal.'),
 ('2016–2018', 'Temer', 'Teto de Gastos e reforma trabalhista. A delação da JBS abala o governo, e a Câmara barra duas denúncias contra o presidente. Lula é preso em 2018, e o TSE o impede de disputar.'),
 ('2019–2022', 'Bolsonaro', 'Reforma da Previdência e pandemia, com mais de 700 mil mortos no Brasil. Conflitos com o STF e ataques às urnas. Em 2021 o STF anula as condenações de Lula.'),
 ('2023–2026', 'Lula 3', 'Os atos golpistas de 8 de janeiro de 2023. Arcabouço fiscal e reforma tributária. Em 2025, o STF condena Bolsonaro a 27 anos por tentativa de golpe. Em outubro de 2026, Lula vence Flávio Bolsonaro no 2º turno por 51,78% a 48,22% dos votos válidos.'),
]

# Observatório Lupa, Anatomia da desinformação eleitoral (2026), p. 19-20
RANKING = [('Jair Bolsonaro', 43.2, 'PL', '102 falsas em 236 frases'), ('Wilson Witzel', 38.9, '', ''), ('Marcelo Crivella', 36.2, '', ''), ('Pablo Marçal', 31.2, '', ''), ('Sebastião Melo', 30.6, '', ''), ('Manuela D’Ávila', 29.7, '', ''), ('Luiz Inácio Lula da Silva', 26.5, 'PT', '22 falsas em 83 frases'), ('Alvaro Dias', 26.1, '', ''), ('Ciro Gomes', 24.8, '', ''), ('Eduardo Paes', 24.4, '', '')]

CASOS = [
 dict(n='Nikolas Ferreira', p='PL-MG', itens=[
   ('O TSE manteve em 2023 multa de R$ 30 mil por vídeo que dizia que Lula desviou R$ 242,2 bilhões da saúde. O tribunal considerou o conteúdo desinformação.', 'Poder360', 'https://www.poder360.com.br/justica/tse-nega-recurso-de-nikolas-ferreira-em-processo-contra-lula/'),
   ('Em janeiro de 2025, o vídeo sobre o Pix viralizou em meio a boatos sobre taxação. O Aos Fatos concluiu que ele usou o tema sem espalhar diretamente desinformação, mas alimentou o clima de boato, e que depois se espalharam montagens falsas sobre o vídeo.', 'Aos Fatos', 'https://www.aosfatos.org/noticias/video-nikolas-ferreira-pix/')]),
 dict(n='Flávio Bolsonaro', p='PL-RJ', itens=[
   ('Em entrevista de agosto de 2026, disse que não foi encontrada arma no 8 de Janeiro; o Aos Fatos mostrou registros de armas roubadas do GSI por manifestantes.', 'Aos Fatos', 'https://aosfatos.org/noticias/checamos-flavio-bolsonaro-globo/'),
   ('Canal “Tropa do Flávio”, ligado à campanha: 17 publicações falsas ou distorcidas em uma semana de outubro de 2026.', 'Aos Fatos', 'https://www.aosfatos.org/noticias/tropa-do-flavio-mensagens-enganosas/'),
   ('Ele também foi alvo: é falso que tenha dito “marginais andarão comigo”; a legenda foi adulterada. Também é falsa a capa de revista sobre o fim do salário mínimo.', 'Aos Fatos', 'https://www.aosfatos.org/noticias/flavio-debate-globo-marginais/')]),
 dict(n='André Janones', p='deputado federal, MG', itens=[
   ('Em 2022, apoiando Lula, adotou táticas que ele mesmo descreveu como “deixar uma fala no ar”. O TSE mandou remover posts que ligavam falsamente Bolsonaro à suspensão do piso da enfermagem.', 'Metrópoles', 'https://www.metropoles.com/brasil/justica/tse-determina-remocao-de-postagens-de-andre-janones-contra-bolsonaro'),
   ('O TSE também mandou remover posts que associavam Bolsonaro ao ataque de Roberto Jefferson a policiais, com multa diária em caso de repetição. Janones nega ter divulgado fake news.', 'Gazeta SP', 'https://www.gazetasp.com.br/brasil/tse-remove-posts-de-janones-que-ligam-bolsonaro-a-roberto-jefferson/')]),
 dict(n='Carla Zambelli', p='ex-deputada, PL-SP', itens=[('O TSE determinou a remoção de vídeo com informação falsa nas eleições de 2022. Ela também aparece, com Osmar Terra e Eduardo Bolsonaro, entre os que mais desinformaram sobre covid no Twitter, em levantamento do Aos Fatos.', 'Congresso em Foco', 'https://congressoemfoco.com.br/area/justica/tse-manda-redes-sociais-deletarem-video-de-carla-zambelli-com-fake-news')]),
]

PESSOAS = [
 ('João Paulo Charleaux', 'Jornalista e escritor de política internacional e política externa', 'https://x.com/jpcharleaux'),
 ('Gabriela Prioli', 'Advogada, comunicadora e comentarista política', 'https://instagram.com/gabrielaprioli'),
 ('Fernando Schüler', 'Professor do Insper, filósofo e cientista político', 'https://x.com/fernandoschuler'),
 ('Lauany Schultz', 'Comunicadora, criadora do projeto Política Essencial', 'https://instagram.com/lauanyschultz'),
 ('Lilia Schwarcz', 'Historiadora e antropóloga, da USP e da ABL', 'https://instagram.com/liliaschwarcz'),
 ('Vitor Douglas de Andrade', 'Filósofo, professor e divulgador científico', 'https://instagram.com/vitorandradefilo'),
 ('Míriam Leitão', 'Jornalista de economia e política econômica', 'https://x.com/miriamleitao'),
 ('Pedro Doria', 'Jornalista, escritor e fundador do Meio', 'https://x.com/pedrodoria'),
 ('Bruno Frederico Müller', 'Comunicador sobre política e atualidades', 'https://facebook.com/bfredmuller'),
 ('Pedro Burgos', 'Jornalista e pesquisador de mídia e dados', 'https://x.com/Burgos'),
 ('Sérgio Abranches', 'Cientista político e sociólogo', 'https://instagram.com/sabranches'),
 ('Maurício Ricardo', 'Chargista, músico e historiador', 'https://youtube.com/@FalaMR'),
 ('Thomas V. Conti', 'Economista, cientista de dados e professor do Insper', 'https://x.com/ThomasVConti'),
 ('Átila Iamarino', 'Biólogo e divulgador científico que também analisa política', 'https://youtube.com/@AtilaIamarino'),
 ('Filipe Figueiredo', 'Historiador, do Xadrez Verbal, colunista de política internacional', 'https://instagram.com/filipefigueiredoxv'),
 ('Joel Pinheiro da Fonseca', 'Economista, filósofo e colunista de perspectiva liberal', 'https://x.com/JoelPinheiro85'),
]

SITES = {
 'Aprender política': [('Politize!', 'https://www.politize.com.br/', 'Educação política apartidária'), ('Toda Política', 'https://www.todapolitica.com/', 'Guias do eleitor e do candidato'), ('Nexo Jornal', 'https://www.nexojornal.com.br/', 'Explicações e contexto'), ('Meio', 'https://www.canalmeio.com.br/', 'Resumo diário de notícias')],
 'Notícias e reportagem': [('Agência Brasil', 'https://agenciabrasil.ebc.com.br/', 'Agência pública'), ('BBC News Brasil', 'https://www.bbc.com/portuguese', 'Internacional em português'), ('Folha de S.Paulo', 'https://www.folha.uol.com.br/', 'Jornal'), ('O Estado de S. Paulo', 'https://www.estadao.com.br/', 'Jornal'), ('G1', 'https://g1.globo.com/', 'Portal de notícias'), ('CNN Brasil', 'https://www.cnnbrasil.com.br/', 'Portal e TV'), ('Reuters', 'https://www.reuters.com/', 'Agência internacional'), ('AP', 'https://apnews.com/', 'Agência internacional')],
 'Investigação e bastidores': [('Agência Pública', 'https://apublica.org/', 'Jornalismo investigativo'), ('Repórter Brasil', 'https://reporterbrasil.org.br/', 'Direitos e trabalho'), ('The Intercept Brasil', 'https://www.intercept.com.br/', 'Investigação, com viés declarado à esquerda'), ('JOTA', 'https://www.jota.info/', 'Judiciário e regulação')],
 'Checar fatos': [('Agência Lupa', 'https://www.agencialupa.org/', 'Checagem'), ('Aos Fatos', 'https://www.aosfatos.org/', 'Checagem'), ('Projeto Comprova', 'https://projetocomprova.com.br/', 'Coalizão de veículos'), ('Fato ou Fake', 'https://g1.globo.com/fato-ou-fake/', 'Checagem do g1')],
 'Medir viés': [('Ad Fontes Media', 'https://adfontesmedia.com/', 'Mapa de viés e confiabilidade (foco nos EUA)'), ('AllSides', 'https://www.allsides.com/unbiased-balanced-news', 'Mesma notícia por vários lados'), ('Ground News', 'https://ground.news/', 'Compara a cobertura')],
 'Fontes oficiais': [('TSE', 'https://www.tse.jus.br/', 'Eleições e partidos'), ('Senado Federal', 'https://www12.senado.leg.br/', 'Projetos e votos'), ('Câmara dos Deputados', 'https://www.camara.leg.br/', 'Projetos e votos'), ('Portal da Transparência', 'https://portaldatransparencia.gov.br/', 'Gastos federais')],
}

LIVROS = [
 ('Política para Iniciantes', 'Louie Stowell (Usborne)', 'Introdução ilustrada para quem está começando.', 'Iniciante', 'https://www.amazon.com.br/s?k=Pol%C3%ADtica+para+Iniciantes+Stowell'),
 ('O Livro da Política', 'Vários autores (Globo Livros)', 'As grandes ideias e pensadores em formato visual.', 'Iniciante', 'https://www.amazon.com.br/s?k=O+livro+da+pol%C3%ADtica'),
 ('Direita e Esquerda', 'Norberto Bobbio', 'As razões de uma distinção política; igualdade como critério.', 'Intermediário', 'https://www.google.com/search?tbm=bks&q=Bobbio+Direita+e+Esquerda'),
 ('A Mente Moralista', 'Jonathan Haidt', 'Por que boas pessoas são divididas por política e religião.', 'Intermediário', 'https://www.google.com/search?tbm=bks&q=Haidt+A+Mente+Moralista'),
 ('A rebeldia tornou-se de direita?', 'Pablo Stefanoni', 'Como a nova direita tomou para si a imagem de rebelde.', 'Intermediário', 'https://www.google.com/search?tbm=bks&q=A+rebeldia+tornou-se+de+direita'),
 ('A Morte da Verdade: Notas sobre a Mentira na Era Trump', 'Michiko Kakutani (Intrínseca)', 'Como o desprezo pelos fatos e pela razão abre caminho para o autoritarismo.', 'Intermediário', 'https://www.amazon.com.br/s?k=A+Morte+da+Verdade+Kakutani'),
 ('Como Vencer um Debate sem Precisar Ter Razão', 'Arthur Schopenhauer', 'A Dialética Erística: 38 estratagemas para vencer discussões, úteis para reconhecer truques.', 'Intermediário', 'https://www.google.com/search?tbm=bks&q=Schopenhauer+Como+vencer+um+debate+sem+precisar+ter+raz%C3%A3o'),
 ('Como as Democracias Morrem', 'Levitsky e Ziblatt', 'Como líderes eleitos corroem o sistema por dentro.', 'Intermediário', 'https://www.google.com/search?tbm=bks&q=Como+as+democracias+morrem'),
 ('The Nature of Human Values', 'Milton Rokeach', 'Clássico sobre valores e sua relação com a política.', 'Avançado', 'https://www.google.com/search?tbm=bks&q=Rokeach+The+Nature+of+Human+Values'),
 ('Left and Right', 'Jean Laponce', 'A topografia das percepções políticas.', 'Avançado', 'https://www.google.com/search?tbm=bks&q=Laponce+Left+and+Right+Topography+of+Political+Perceptions'),
 ('Introdução à Filosofia Política', 'Jonathan Wolff', 'Panorama claro das grandes questões: por que ter Estado, liberdade, democracia e justiça.', 'Intermediário', 'https://www.google.com/search?tbm=bks&q=Jonathan+Wolff+Introdu%C3%A7%C3%A3o+%C3%A0+Filosofia+Pol%C3%ADtica'),
 ('O Príncipe', 'Nicolau Maquiavel', 'Clássico do século XVI sobre como conquistar e manter o poder.', 'Intermediário', 'https://www.google.com/search?tbm=bks&q=Maquiavel+O+Pr%C3%ADncipe'),
 ('1984', 'George Orwell', 'Romance sobre um regime totalitário de vigilância, propaganda e manipulação da verdade.', 'Iniciante', 'https://www.google.com/search?tbm=bks&q=George+Orwell+1984'),
 ('A República', 'Platão', 'Diálogo sobre a justiça e a cidade ideal, governada por filósofos.', 'Avançado', 'https://www.google.com/search?tbm=bks&q=Plat%C3%A3o+A+Rep%C3%BAblica'),
 ('Dicionário de Política', 'Norberto Bobbio, Nicola Matteucci e Gianfranco Pasquino', 'Obra de referência com os principais conceitos políticos, para consultar por verbete.', 'Avançado', 'https://www.google.com/search?tbm=bks&q=Bobbio+Matteucci+Pasquino+Dicion%C3%A1rio+de+Pol%C3%ADtica'),
 ('Ética Prática', 'Peter Singer', 'Aplica a ética a questões reais, como pobreza, tratamento dos animais, aborto e meio ambiente, com o princípio da igual consideração de interesses.', 'Intermediário', 'https://www.google.com/search?tbm=bks&q=Peter+Singer+%C3%89tica+Pr%C3%A1tica'),
 ('Reasoned Politics', 'Magnus Vinding', 'Valores e evidências, com foco em reduzir o sofrimento. PDF gratuito.', 'Avançado', 'https://magnusvinding.com/wp-content/uploads/2022/03/reasoned-politics.pdf'),
 ('Zoopolis: A Political Theory of Animal Rights', 'Sue Donaldson e Will Kymlicka', 'Propõe cidadania para animais domesticados, residência para os que vivem perto de nós e soberania para os selvagens.', 'Avançado', 'https://willkymlicka.ca/publications/books/animals'),
 ('Animals and the Constitution', 'John Adenitire e Raffael Fasel', 'Um constitucionalismo baseado na senciência, que inclui os interesses dos animais governados.', 'Avançado', 'https://academic.oup.com/book/59826'),
 ('Sentientist Politics: A Theory of Global Inter-Species Justice', 'Alasdair Cochrane', 'Uma teoria política que inclui todos os seres sencientes.', 'Avançado', 'https://global.oup.com/academic/product/sentientist-politics-9780198789802'),
 ('Uma Teoria da Justiça', 'John Rawls', 'O véu da ignorância e o que é uma sociedade justa.', 'Avançado', 'https://www.google.com/search?tbm=bks&q=Rawls+Uma+teoria+da+justi%C3%A7a'),
 ('Contra a Democracia (Against Democracy)', 'Jason Brennan', 'O argumento mais conhecido pela epistocracia.', 'Avançado', 'https://www.google.com/search?tbm=bks&q=Brennan+Against+Democracy'),
]
from urllib.parse import quote as _q
_NOVOS = [
('A Revolução dos Bichos', 'George Orwell', 'Fábula curta sobre como uma revolução pode virar tirania.', 'Iniciante'),
('Sobre a Tirania', 'Timothy Snyder', 'Lições curtas e práticas do século XX para defender a democracia.', 'Iniciante'),
('Justiça: o que é fazer a coisa certa', 'Michael Sandel', 'Parte de casos concretos e torna a filosofia política acessível.', 'Iniciante'),
('Sobre a Liberdade', 'John Stuart Mill', 'A defesa clássica da liberdade individual e de expressão.', 'Intermediário'),
('Manifesto Comunista', 'Karl Marx e Friedrich Engels', 'Texto curto, essencial para entender o marxismo e seus críticos.', 'Intermediário'),
('O Caminho da Servidão', 'Friedrich Hayek', 'A crítica liberal ao planejamento central da economia.', 'Intermediário'),
('Reflexões sobre a Revolução na França', 'Edmund Burke', 'A base do pensamento conservador moderno.', 'Intermediário'),
('Eichmann em Jerusalém', 'Hannah Arendt', 'O julgamento de um burocrata nazista e a “banalidade do mal”.', 'Intermediário'),
('Por que as Nações Fracassam', 'Daron Acemoglu e James Robinson', 'Como as instituições ajudam a explicar riqueza e pobreza.', 'Intermediário'),
('Raízes do Brasil', 'Sérgio Buarque de Holanda', 'O “homem cordial” e a mistura entre o público e o privado.', 'Intermediário'),
('Cidadania no Brasil', 'José Murilo de Carvalho', 'Como os direitos civis, políticos e sociais chegaram ao país.', 'Intermediário'),
('Política', 'Aristóteles', 'Os regimes de governo e a ideia do ser humano como animal político.', 'Avançado'),
('Leviatã', 'Thomas Hobbes', 'O medo, o soberano e a origem do contrato social.', 'Avançado'),
('Segundo Tratado sobre o Governo', 'John Locke', 'Direitos naturais, propriedade e o direito de resistir.', 'Avançado'),
('Do Contrato Social', 'Jean-Jacques Rousseau', 'Soberania popular e vontade geral.', 'Avançado'),
('O Federalista', 'Alexander Hamilton, James Madison e John Jay', 'Como limitar o poder com instituições.', 'Avançado'),
('A Democracia na América', 'Alexis de Tocqueville', 'As virtudes e os riscos da democracia, incluindo a tirania da maioria.', 'Avançado'),
('Anarquia, Estado e Utopia', 'Robert Nozick', 'O libertarismo em sua melhor versão, em resposta a Rawls.', 'Avançado'),
('O Segundo Sexo', 'Simone de Beauvoir', 'Obra fundadora do feminismo moderno.', 'Avançado'),
('Origens do Totalitarismo', 'Hannah Arendt', 'Como o nazismo e o stalinismo foram possíveis.', 'Avançado'),
('Os Condenados da Terra', 'Frantz Fanon', 'O colonialismo visto por quem o sofreu. É polêmico pela defesa da violência.', 'Avançado'),
('Desenvolvimento como Liberdade', 'Amartya Sen', 'Desenvolvimento medido pelo que as pessoas podem ser e fazer.', 'Avançado'),
('O Capital no Século XXI', 'Thomas Piketty', 'A longa história da desigualdade. Vale ler junto com seus críticos.', 'Avançado'),
('Democracy for Realists', 'Christopher Achen e Larry Bartels', 'Um retrato incômodo de como os eleitores decidem de fato.', 'Avançado'),
('Os Donos do Poder', 'Raymundo Faoro', 'O patrimonialismo na formação política do Brasil.', 'Avançado'),
('Casa-Grande & Senzala', 'Gilberto Freyre', 'Clássico sobre a formação do Brasil, muito lido e muito criticado.', 'Avançado'),
('Presidencialismo de Coalizão', 'Sérgio Abranches', 'Como o sistema político brasileiro funciona.', 'Avançado'),
]
assert not {x[0] for x in _NOVOS} & {x[0] for x in LIVROS}
LIVROS.append(('Uma Introdução aos Princípios da Moral e da Legislação (1789)', 'Jeremy Bentham', 'Obra fundadora do utilitarismo: leis devem ser julgadas pelo prazer e pela dor que causam. Traz a famosa pergunta sobre os animais: podem sofrer?', 'Avançado', 'https://pt.wikipedia.org/wiki/Jeremy_Bentham'))
LIVROS.append(('Ideologias', 'Gabriela Prioli (Companhia das Letras)', 'Explica quem são e o que pensam os liberais, os conservadores e os socialistas, com um convite ao diálogo.', 'Iniciante', 'https://www.companhiadasletras.com.br/livro/9786559211531/ideologias'))
LIVROS += [x + ('https://www.google.com/search?tbm=bks&q=' + _q(x[0] + ' ' + x[1]),) for x in _NOVOS]



from lote_debates_livros import LIVROS_NOVOS as _L2
assert not {x[0] for x in _L2} & {x[0] for x in LIVROS}, {x[0] for x in _L2} & {x[0] for x in LIVROS}
LIVROS += [x + ('https://www.google.com/search?tbm=bks&q=' + _q(x[0] + ' ' + x[1]),) for x in _L2]
