"""Lições acrescentadas na revisão de novembro de 2026: como uma lei é feita, partidos, economia básica,
pesquisas eleitorais, populismo, corrupção e leitura crítica da grande mídia. Também define os grupos e a
ordem das lições de cada nível (GRUPOS e ORDEM_GRUPOS), usados por build.py."""
INI = 'Como o sistema funciona'
CE = 'Conceitos essenciais'
PI = 'Perigos ideológicos'
DR = 'Desinformação e redes'
EI = 'Estado, poder e instituições'

NOVAS_INICIANTE = [
dict(slug='como-uma-lei-e-feita', grupo=INI, titulo='Como uma lei é feita', resumo='Da ideia à sanção: quem pode propor, por onde o projeto passa, quem pode barrar e o que acontece quando a lei contraria a Constituição.', corpo='''
<p class="abre">Uma lei não nasce pronta. Ela começa como uma proposta, passa por comissões e votações nas duas casas do Congresso, pode ser vetada pelo presidente e ainda pode ser derrubada pelo Supremo se contrariar a Constituição. Conhecer esse caminho ajuda a entender por que “aprovar” demora, e quem é responsável em cada etapa.</p>
<h2>Nem toda regra é uma lei</h2>
<table><thead><tr><th>Norma</th><th>O que é</th><th>Quem aprova</th></tr></thead><tbody>
<tr><td><strong>Constituição</strong></td><td>A regra de todas as regras. Nenhuma lei pode contrariá-la</td><td>Assembleia Constituinte (1988). Mudanças só por emenda</td></tr>
<tr><td><strong>Emenda constitucional (PEC)</strong></td><td>Altera o texto da Constituição</td><td>3/5 dos deputados e 3/5 dos senadores, em dois turnos em cada casa. Não passa por sanção do presidente</td></tr>
<tr><td><strong>Lei complementar</strong></td><td>Regula temas que a Constituição reservou a ela, como as finanças públicas</td><td>Maioria absoluta: mais da metade de todos os membros de cada casa</td></tr>
<tr><td><strong>Lei ordinária</strong></td><td>A lei comum, da maioria dos assuntos</td><td>Maioria simples dos presentes, com quórum mínimo</td></tr>
<tr><td><strong>Medida provisória (MP)</strong></td><td>Editada pelo presidente em caso de urgência. Vale na hora, mas perde efeito se o Congresso não a aprovar em até 120 dias</td><td>Presidente edita; Congresso confirma ou rejeita</td></tr>
<tr><td><strong>Decreto</strong></td><td>Detalha como uma lei será aplicada. Não pode criar obrigação nova</td><td>Presidente, governador ou prefeito</td></tr>
</tbody></table>
<p class="legenda">Estados e municípios têm suas próprias constituições (ou leis orgânicas) e leis, que não podem contrariar as federais nos temas reservados à União.</p>
<h2>O caminho de um projeto de lei</h2>
<ol class="passos">
<li><strong>Alguém propõe.</strong> Um deputado, um senador, o presidente, o STF e o Ministério Público em certos temas, ou os próprios cidadãos, por iniciativa popular. Alguns assuntos só o presidente pode propor, como a criação de cargos no Executivo e o orçamento.</li>
<li><strong>Comissões analisam.</strong> A Comissão de Constituição e Justiça verifica se o projeto é constitucional. Comissões temáticas, como as de Saúde ou Educação, discutem o conteúdo. Um <strong>relator</strong> escreve um parecer e, muitas vezes, reescreve o texto. É aqui que boa parte da negociação acontece, e também onde os projetos ficam parados.</li>
<li><strong>O plenário vota</strong>, se o projeto chegar lá. Muitos projetos são aprovados só nas comissões, em caráter conclusivo. O presidente da Câmara ou do Senado decide o que entra na pauta, e isso é um poder enorme.</li>
<li><strong>A outra casa revisa.</strong> O que começa na Câmara vai ao Senado, e vice-versa. Se a segunda casa altera o texto, ele volta para a primeira decidir sobre as mudanças.</li>
<li><strong>O presidente sanciona ou veta</strong>, no todo ou em parte, em 15 dias úteis. O veto precisa ser justificado.</li>
<li><strong>O Congresso pode derrubar o veto</strong>, com a maioria absoluta de deputados e de senadores, em sessão conjunta.</li>
<li><strong>Publicação.</strong> A lei entra em vigor na data que ela mesma define. Se não disser nada, 45 dias depois de publicada.</li>
</ol>
<h2>Quem pode barrar uma lei</h2>
<ul>
<li><strong>O presidente da Casa</strong>, ao não colocar o projeto em votação. Há milhares de projetos esperando.</li>
<li><strong>O relator e as comissões</strong>, com um parecer contrário ou com a demora.</li>
<li><strong>O presidente da República</strong>, com o veto.</li>
<li><strong>O Supremo Tribunal Federal</strong>, se a lei contrariar a Constituição. Isso pode ser pedido por partidos com representação no Congresso, pela Procuradoria-Geral da República, pela OAB e por outros legitimados, em ações como a ADI. O Supremo não faz leis, mas pode anular as que forem inconstitucionais, e a disputa sobre os limites desse poder é constante. Veja o <a href="debates/poder-do-stf.html">debate sobre o poder do STF</a>.</li>
</ul>
<h2>A iniciativa popular</h2>
<p>Os cidadãos podem apresentar um projeto de lei à Câmara com assinaturas de 1% do eleitorado nacional, distribuídas por pelo menos cinco estados. É difícil, mas já aconteceu: a Lei da Ficha Limpa, de 2010, que impede a candidatura de condenados por órgãos colegiados, nasceu assim, com mais de 1,6 milhão de assinaturas. Depois de apresentado, o projeto segue o mesmo caminho dos outros.</p>
<h2>Por que demora, e por que às vezes é rápido demais</h2>
<p>O caminho longo é proposital: dá tempo para ouvir quem é afetado e corrigir erros. O problema aparece nos dois extremos. Projetos importantes ficam anos parados porque não interessam a quem controla a pauta. E, em outros casos, um texto de centenas de páginas é votado de madrugada, com urgência, sem que os próprios parlamentares tenham lido. Também é comum o chamado <strong>jabuti</strong>: um trecho sem relação com o tema, inserido em um projeto que já vai ser aprovado.</p>
<div class="nota"><strong>Para acompanhar:</strong> todo projeto tem um número e uma página nos sites da <a href="https://www.camara.leg.br/" target="_blank" rel="noopener">Câmara</a> e do <a href="https://www12.senado.leg.br/" target="_blank" rel="noopener">Senado</a>, com o texto, o relator, os pareceres e o resultado de cada votação. Quem diz “aprovei uma lei” quase sempre aprovou junto com centenas de outros parlamentares: veja <a href="numero-de-projetos.html">o perigo de contar projetos</a> e <a href="cargos.html">o que cada cargo faz</a>.</div>
''', fontes=[('Constituição Federal, arts. 59 a 69', 'https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm'), ('Processo legislativo (Wikipédia)', 'https://pt.wikipedia.org/wiki/Processo_legislativo'), ('Lei da Ficha Limpa (Wikipédia)', 'https://pt.wikipedia.org/wiki/Lei_da_Ficha_Limpa'), ('Agência Senado: glossário legislativo', 'https://www12.senado.leg.br/noticias/glossario-legislativo'), ('Portal da Câmara', 'https://www.camara.leg.br/')]),

dict(slug='o-que-e-um-partido', grupo=INI, titulo='Para que servem os partidos', resumo='Ninguém se elege sem partido no Brasil. O que eles fazem, de onde vem o dinheiro deles, por que são tantos e como avaliar um.', corpo='''
<p class="abre">No Brasil, não existe candidatura sem partido. Ele é o grupo que reúne pessoas com ideias parecidas, escolhe candidatos, organiza a disputa e, depois da eleição, forma blocos no Congresso. Na teoria, é o elo entre o eleitor e o poder. Na prática, muitos funcionam como empresas de eleição, e por isso vale saber como avaliá-los.</p>
<h2>O que um partido faz</h2>
<ul>
<li><strong>Seleciona candidatos.</strong> Para disputar, a pessoa precisa estar filiada há pelo menos seis meses e ser escolhida na convenção do partido.</li>
<li><strong>Organiza as ideias.</strong> Todo partido tem um estatuto e um programa registrados no TSE. Vale ler: alguns dizem muito, outros quase nada.</li>
<li><strong>Forma bancadas.</strong> No Congresso, os partidos (ou blocos de partidos) indicam líderes, dividem as comissões e orientam votações. Veja <a href="como-uma-lei-e-feita.html">como uma lei é feita</a>.</li>
<li><strong>Sustenta ou faz oposição ao governo.</strong> Como nenhum partido tem maioria sozinho, o presidente negocia com vários. É o <a href="presidencialismo-de-coalizao.html">presidencialismo de coalizão</a>.</li>
<li><strong>Elege pessoas que você não escolheu.</strong> Na eleição de deputado e vereador, o voto conta primeiro para o partido ou federação. Seu voto pode ajudar a eleger outro candidato da mesma lista. Veja <a href="como-votar-bem.html">como a conta funciona</a>.</li>
</ul>
<h2>De onde vem o dinheiro</h2>
<table><thead><tr><th>Fonte</th><th>Como funciona</th></tr></thead><tbody>
<tr><td><strong>Fundo partidário</strong></td><td>Dinheiro público, pago todo ano, para manter os partidos. Dividido sobretudo conforme os votos para a Câmara</td></tr>
<tr><td><strong>Fundo eleitoral</strong></td><td>Dinheiro público só para campanhas, criado em 2017 depois que o STF proibiu doações de empresas. Em 2024, foi de cerca de R$ 4,9 bilhões. A cúpula de cada partido decide quem recebe quanto</td></tr>
<tr><td><strong>Doações de pessoas físicas</strong></td><td>Permitidas, com limite de 10% da renda do doador no ano anterior. Doação de empresa é proibida desde 2015</td></tr>
<tr><td><strong>Tempo de rádio e TV</strong></td><td>Gratuito para os partidos, pago pelo Estado com renúncia fiscal, e dividido conforme o tamanho das bancadas</td></tr>
</tbody></table>
<p>Tudo isso é público e pode ser consultado no <a href="https://divulgacandcontas.tse.jus.br/" target="_blank" rel="noopener">DivulgaCandContas</a>. Como o dinheiro vem em grande parte do Estado e é distribuído pelas direções partidárias, quem controla o partido tem muito poder sobre quem se elege.</p>
<h2>Por que o Brasil tem tantos partidos</h2>
<p>Há cerca de 30 partidos registrados, e cerca de 20 com cadeiras na Câmara. Alguns motivos:</p>
<ul>
<li><strong>Voto proporcional com lista aberta:</strong> partidos pequenos conseguem eleger alguém, e o eleitor vota em pessoas, não em programas.</li>
<li><strong>Coligações, até 2018:</strong> siglas pequenas se juntavam a grandes para eleger deputados e, em troca, ganhavam fundo e tempo de TV. Isso acabou nas eleições proporcionais a partir de 2020.</li>
<li><strong>Dinheiro público:</strong> ter um partido dá acesso a fundo e tempo de TV, e isso vira moeda de troca.</li>
</ul>
<p>Desde 2017, uma <strong>cláusula de desempenho</strong> exige um mínimo de votos para o partido ter acesso ao fundo e ao tempo de TV, e o mínimo sobe a cada eleição até 2030. Por isso houve fusões, como a que criou o União Brasil, e <strong>federações</strong>, em que dois ou mais partidos agem como um só por pelo menos quatro anos. O número de siglas com representação vem caindo. Veja a <a href="ferramentas/arvore-dos-partidos.html">árvore dos partidos</a>.</p>
<h2>Fidelidade e troca de partido</h2>
<p>Deputados e vereadores que trocam de partido fora da janela permitida, sem justa causa, podem perder o mandato, porque a cadeira é considerada do partido. A “janela partidária” abre por 30 dias, seis meses antes da eleição, e é quando se veem as grandes migrações, muitas vezes em busca de fundo e espaço na chapa.</p>
<h2>Como avaliar um partido</h2>
<ol class="roteiro">
<li><strong>Como vota?</strong> O voto da bancada em temas decisivos diz mais do que o nome. Veja <a href="ferramentas/como-votaram.html">como os partidos votaram</a>.</li>
<li><strong>Quem está nele?</strong> Os candidatos, os financiadores e os condenados.</li>
<li><strong>Com quem se alia?</strong> Um partido que apoia qualquer governo em troca de cargos tem pouca ideologia e muita conveniência.</li>
<li><strong>O programa bate com a prática?</strong> Compare o que está registrado no TSE com o histórico. Use o <a href="ferramentas/comparador.html">comparador</a>.</li>
<li><strong>Como trata quem discorda dentro dele?</strong> Partidos sem disputa interna costumam ser propriedade de um dono.</li>
</ol>
<div class="nota"><strong>Rótulo não basta.</strong> Nomes como “social”, “democrático”, “trabalhista” ou “liberal” dizem pouco sobre o que a sigla faz hoje. Partidos mudam de posição, trocam de nome e se fundem. Consulte o <a href="partidos.html">dossiê de cada partido</a>, com linha do tempo, casos e votos.</div>
''', fontes=[('TSE: partidos registrados', 'https://www.tse.jus.br/partidos/partidos-registrados-no-tse'), ('Partido político (Wikipédia)', 'https://pt.wikipedia.org/wiki/Partido_pol%C3%ADtico'), ('Fundo Especial de Financiamento de Campanha (Wikipédia)', 'https://pt.wikipedia.org/wiki/Fundo_Especial_de_Financiamento_de_Campanha'), ('Cláusula de barreira (Wikipédia)', 'https://pt.wikipedia.org/wiki/Cl%C3%A1usula_de_barreira'), ('TSE: DivulgaCandContas', 'https://divulgacandcontas.tse.jus.br/')]),
]

NOVAS_INTERMEDIARIO = [
dict(slug='economia-para-entender-politica', grupo=CE, titulo='Economia básica para entender política', resumo='PIB, inflação, juros, dívida e déficit aparecem em quase todo debate. O que cada um significa, como afeta sua vida e por que os políticos brigam por eles.', corpo='''
<p class="abre">Boa parte das brigas políticas é, no fundo, uma briga econômica: quanto o governo gasta, de quem cobra, o que faz com os juros e com a dívida. Sem entender meia dúzia de termos, a discussão vira só slogan. Esta lição explica esses termos sem fórmulas, e mostra por que cada um é disputado.</p>
<h2>Os termos que mais aparecem</h2>
<table><thead><tr><th>Termo</th><th>O que é</th><th>Onde você sente</th></tr></thead><tbody>
<tr><td><strong>PIB</strong></td><td>A soma de tudo o que o país produz em um ano. “Crescer 2%” significa produzir 2% a mais</td><td>Emprego e renda. Mas o PIB não diz como a riqueza é dividida, nem conta o que não tem preço, como o trabalho doméstico</td></tr>
<tr><td><strong>Inflação</strong></td><td>A alta geral e contínua dos preços. No Brasil, o índice oficial é o IPCA, medido pelo IBGE</td><td>O mesmo dinheiro compra menos. Pesa mais sobre quem vive de salário e não tem como se proteger</td></tr>
<tr><td><strong>Juros (Selic)</strong></td><td>A taxa básica, definida a cada 45 dias pelo Banco Central. Serve de referência para todos os outros juros</td><td>Juro alto encarece crédito e financiamento, e freia a inflação. Juro baixo estimula consumo e investimento, e pode alimentar a inflação</td></tr>
<tr><td><strong>Déficit e superávit</strong></td><td>Déficit é quando o governo gasta mais do que arrecada no ano; superávit é o contrário. O “resultado primário” é essa conta sem os juros da dívida</td><td>Déficits seguidos aumentam a dívida, e a dívida é paga com impostos, inflação ou corte de gastos</td></tr>
<tr><td><strong>Dívida pública</strong></td><td>Tudo o que o governo deve a quem comprou seus títulos: bancos, fundos, pessoas e o próprio país, por meio do Tesouro Direto</td><td>Quanto maior a dívida e a desconfiança, maiores os juros que o país paga, e menos sobra para serviços</td></tr>
<tr><td><strong>Câmbio</strong></td><td>O preço do dólar em reais. Desde 1999, flutua conforme o mercado, com intervenções do Banco Central</td><td>Dólar alto encarece importados, combustível e trigo, e favorece quem exporta</td></tr>
<tr><td><strong>Desemprego</strong></td><td>Quem procurou trabalho e não achou, medido pela Pnad Contínua do IBGE</td><td>Não conta quem desistiu de procurar nem quem está em trabalho informal ou com menos horas do que queria</td></tr>
</tbody></table>
<h2>Como as peças se ligam</h2>
<p>Quase tudo está conectado, e por isso não existe decisão sem custo:</p>
<ul>
<li><strong>Gastar mais pode aquecer a economia</strong> e criar empregos, sobretudo em recessão. Mas, se o governo gasta muito acima do que arrecada, a dívida cresce, os credores cobram juros maiores e a inflação pode subir.</li>
<li><strong>Subir juros reduz a inflação</strong>, porque desestimula o consumo. Mas também freia o crescimento, aumenta o desemprego e encarece a dívida pública, já que boa parte dela é corrigida pela Selic.</li>
<li><strong>Cortar impostos deixa mais dinheiro no bolso</strong> e pode estimular negócios. Mas reduz a arrecadação, e alguém decide o que deixa de ser pago, ou a dívida cresce.</li>
<li><strong>Imprimir dinheiro para pagar contas</strong> gera inflação, como o Brasil viveu até o Plano Real, em 1994, quando os preços chegaram a subir mais de 2.000% em um ano.</li>
</ul>
<div class="nota"><strong>“Não existe almoço grátis.”</strong> A frase, popularizada pelo economista Milton Friedman, resume o ponto: todo benefício é pago por alguém, agora ou depois. A pergunta política não é se há custo, e sim quem paga, quem ganha e se vale a pena. Quem promete tudo ao mesmo tempo, sem dizer de onde sai, não está fazendo economia. Veja o <a href="perigo-do-maniqueismo.html">perigo de simplificar</a>.</div>
<h2>Por que esquerda e direita brigam por isso</h2>
<table><thead><tr><th>Tema</th><th>Ênfase mais comum à esquerda</th><th>Ênfase mais comum à direita</th><th>O que os dados podem responder</th></tr></thead><tbody>
<tr><td>Gasto público</td><td>Investir em saúde, educação e renda estimula a economia e reduz desigualdade</td><td>Gasto demais gera dívida, juros e inflação, que punem os pobres</td><td>Que gasto tem mais retorno, e em que momento do ciclo</td></tr>
<tr><td>Impostos</td><td>Cobrar mais de quem tem mais, sobre renda e patrimônio</td><td>Cobrar menos para estimular produção e emprego</td><td>Quem paga hoje, e o efeito de cada mudança. Veja <a href="imposto-e-roubo.html">imposto é roubo?</a></td></tr>
<tr><td>Juros</td><td>Juros altos travam o país e enriquecem rentistas</td><td>Juros são consequência de gasto e desconfiança; a autonomia do Banco Central protege a moeda</td><td>Qual juro segura a inflação com menor custo, e o que fez o juro subir</td></tr>
<tr><td>Salário mínimo</td><td>Aumentar protege os mais pobres e movimenta o comércio</td><td>Aumentar demais destrói empregos formais e pressiona a Previdência</td><td>O efeito real sobre o emprego varia conforme o tamanho do aumento</td></tr>
</tbody></table>
<p>Parte dessas divergências é sobre <a href="valores-e-decisoes.html">valores</a>: quanto pesa a igualdade diante da liberdade de empreender. Outra parte é sobre fatos, e aí os estudos ajudam, mesmo sem dar certezas. Os economistas concordam mais do que parece em algumas coisas, como os danos da hiperinflação e os ganhos do comércio, e discordam muito em outras, como o tamanho ideal do Estado.</p>
<h2>Regras fiscais do Brasil</h2>
<ul>
<li><strong>Lei de Responsabilidade Fiscal (2000):</strong> limita gastos com pessoal e dívida de União, estados e municípios, e exige transparência.</li>
<li><strong>Teto de gastos (2016 a 2023):</strong> congelou o crescimento real das despesas federais por anos. Foi substituído pelo <strong>arcabouço fiscal</strong> (2023), que deixa o gasto crescer um pouco acima da inflação, conforme a arrecadação.</li>
<li><strong>Meta de inflação:</strong> definida pelo governo, hoje em 3% ao ano, com tolerância de 1,5 ponto para cima ou para baixo. O Banco Central, autônomo desde 2021, usa os juros para persegui-la.</li>
</ul>
<h2>Como não ser enganado com números</h2>
<ol class="roteiro">
<li><strong>Pergunte o período e a comparação.</strong> “A gasolina subiu” significa quanto, desde quando, e comparado com a inflação?</li>
<li><strong>Separe nominal de real.</strong> Um salário que sobe 5% com inflação de 5% não subiu nada.</li>
<li><strong>Desconfie de “recorde”.</strong> Em um país que cresce, quase tudo bate recorde em valor absoluto. Olhe a proporção do PIB ou o valor por pessoa.</li>
<li><strong>Olhe a fonte original:</strong> IBGE, Banco Central e Tesouro publicam os dados. Veja o <a href="https://www.tesourotransparente.gov.br/" target="_blank" rel="noopener">Tesouro Transparente</a>.</li>
<li><strong>Cuidado com a causa.</strong> O governo da vez leva a culpa e o crédito por coisas que dependem do preço do petróleo, da China, do clima e das decisões anteriores.</li>
</ol>
<p>Para aprofundar, veja os debates sobre <a href="debates/impostos.html">impostos</a>, <a href="debates/previdencia.html">Previdência</a> e <a href="debates/desemprego.html">desemprego</a>, e a lição sobre <a href="politicas-publicas.html">orçamento</a>. Os termos estão no <a href="glossario-economico.html">glossário de economia</a>, e os números do Brasil comparados aos de outros países, nos <a href="indicadores.html">indicadores internacionais</a>.</p>
''', fontes=[('IBGE Explica: inflação', 'https://www.ibge.gov.br/explica/inflacao.php'), ('Banco Central: taxa Selic', 'https://www.bcb.gov.br/controleinflacao/taxaselic'), ('Tesouro Transparente', 'https://www.tesourotransparente.gov.br/'), ('Lei de Responsabilidade Fiscal (Wikipédia)', 'https://pt.wikipedia.org/wiki/Lei_de_Responsabilidade_Fiscal'), ('Plano Real (Wikipédia)', 'https://pt.wikipedia.org/wiki/Plano_Real'), ('Arcabouço fiscal (Wikipédia)', 'https://pt.wikipedia.org/wiki/Novo_arcabou%C3%A7o_fiscal')]),

dict(slug='perigo-do-populismo', grupo=PI, titulo='O perigo do populismo', resumo='“O povo puro contra a elite corrupta”, com um líder que fala por todos. Existe à esquerda e à direita, nasce de problemas reais e costuma terminar atacando quem limita o poder.', corpo='''
<p class="abre">Populismo não é “fazer política para o povo”. É um jeito de fazer política que divide a sociedade em dois grupos, o povo puro e a elite corrupta, e apresenta um líder como a única voz verdadeira do povo. Quem discorda deixa de ser adversário e vira parte da elite, do sistema ou dos inimigos da nação. Esse estilo existe em qualquer ponto do espectro.</p>
<h2>O que define o populismo</h2>
<p>O cientista político Cas Mudde o descreve como uma “ideologia fina”: não diz o que fazer com a economia ou os costumes, e por isso se combina com qualquer coisa, do socialismo ao nacionalismo. Jan-Werner Müller acrescenta o traço mais perigoso: a pretensão de que <strong>só o líder representa o povo</strong>. Se o povo é um só e o líder fala por ele, quem perde para o líder não pode ter vencido de verdade.</p>
<table><thead><tr><th>Marca</th><th>Como aparece</th></tr></thead><tbody>
<tr><td>Povo contra elite</td><td>“Eles”, os políticos, os banqueiros, a imprensa, os juízes, as universidades, contra “nós”</td></tr>
<tr><td>O líder como voz do povo</td><td>“Eu sou vocês.” Partido, programa e equipe importam menos do que a pessoa</td></tr>
<tr><td>Antipluralismo</td><td>Quem discorda não é parte do povo. Imprensa crítica “mente”, tribunais “perseguem”, oposição “trai”</td></tr>
<tr><td>Soluções simples</td><td>Problemas complexos têm um culpado e uma resposta de uma frase</td></tr>
<tr><td>Mobilização permanente</td><td>Governa-se em campanha, com um inimigo sempre à vista</td></tr>
</tbody></table>
<h2>À esquerda e à direita</h2>
<table><thead><tr><th>Populismo de esquerda</th><th>Populismo de direita</th></tr></thead><tbody>
<tr><td>A elite é econômica: os ricos, os bancos, o “mercado”, o imperialismo</td><td>A elite é cultural e política: a imprensa, os intelectuais, os juízes, o “sistema”</td></tr>
<tr><td>O povo são os trabalhadores e os pobres</td><td>O povo é a nação, a família tradicional, “o cidadão de bem”</td></tr>
<tr><td>Exemplos estudados: Perón na Argentina, Chávez e Maduro na Venezuela</td><td>Exemplos estudados: Orbán na Hungria, Trump nos EUA, Erdoğan na Turquia</td></tr>
</tbody></table>
<p>Os pesquisadores divergem sobre quem merece o rótulo e em que grau, e ele costuma ser usado como xingamento contra qualquer adversário. No Brasil, Getúlio Vargas, Jânio Quadros e Fernando Collor são os casos clássicos, e o debate acadêmico aplica o termo, em medidas diferentes, a lideranças recentes de campos opostos. O teste útil não é o rótulo, e sim as marcas da tabela acima: a pessoa trata a oposição como ilegítima? Ataca quem pode fiscalizá-la?</p>
<h2>Por que atrai</h2>
<ul>
<li><strong>Os problemas são reais.</strong> Desigualdade, corrupção, serviços ruins e políticos que não ouvem ninguém. O populismo nasce onde a representação falhou, e é um sintoma antes de ser uma causa.</li>
<li><strong>Dá voz a quem se sentia ignorado</strong>, e muitas vezes aponta falhas que o “establishment” preferia não ver.</li>
<li><strong>É simples e emocional.</strong> Um culpado e um salvador são mais fáceis de entender do que juros, coalizões e comissões. Veja a <a href="politica-do-medo.html">política do medo</a> e o <a href="perigo-do-messianismo.html">messianismo</a>.</li>
</ul>
<h2>Por que é perigoso</h2>
<ul>
<li><strong>Corrói os freios.</strong> Se o líder é o povo, tribunais, imprensa, Congresso e oposição são obstáculos à vontade popular. É o caminho descrito por Levitsky e Ziblatt em <em>Como as democracias morrem</em>: a democracia é desmontada por dentro, com aparência de legalidade.</li>
<li><strong>Não aceita perder.</strong> Derrota eleitoral vira fraude, e crítica vira conspiração. Veja o <a href="perigo-de-questionar-a-democracia.html">perigo de questionar a democracia</a>.</li>
<li><strong>Promete o que não entrega.</strong> As soluções simples não resolvem os problemas complexos, e a frustração é redirecionada para novos inimigos.</li>
<li><strong>Divide para governar.</strong> Uma sociedade em que metade vê a outra metade como inimiga perde a capacidade de resolver qualquer coisa junto. Veja o <a href="perigo-do-tribalismo.html">tribalismo</a>.</li>
</ul>
<h2>Popular não é populista</h2>
<table><thead><tr><th>Política popular</th><th>Política populista</th></tr></thead><tbody>
<tr><td>Defende os interesses da maioria, com programa e dados</td><td>Fala em nome do “povo” contra quem discorda</td></tr>
<tr><td>Aceita a oposição e as instituições, mesmo quando perde</td><td>Trata a oposição como inimiga e as instituições como obstáculo</td></tr>
<tr><td>Explica custos e limites</td><td>Promete tudo e culpa a elite quando não entrega</td></tr>
<tr><td>Depende de partido, equipe e programa</td><td>Depende da pessoa do líder</td></tr>
</tbody></table>
<p>Há quem veja um lado positivo: para o filósofo Ernesto Laclau, o populismo é a forma como demandas ignoradas se juntam e entram na política. Mesmo quem aceita essa leitura reconhece o risco quando a mobilização se volta contra os limites do poder.</p>
<h2>Como se proteger</h2>
<ol class="roteiro"><li><strong>Troque “quem” por “o quê”.</strong> Qual é a proposta, quanto custa, quem paga?</li><li><strong>Veja como o líder trata quem o fiscaliza.</strong> Esse é o sinal mais confiável.</li><li><strong>Desconfie de “o povo quer”.</strong> O povo são milhões de pessoas que discordam entre si.</li><li><strong>Cobre a entrega</strong>, e não só o discurso.</li><li><strong>Leve a sério a insatisfação</strong> que alimenta o populismo. Combatê-la é melhor do que ridicularizar quem a sente.</li></ol>
<p>Veja também a vertente do <a href="vertentes/populismo.html">populismo</a> e a lição sobre <a href="atores-malevolentes.html">atores malevolentes</a>, que explica como esse estilo pode servir a pessoas com traços perigosos.</p>
''', fontes=[('Populismo (Wikipédia)', 'https://pt.wikipedia.org/wiki/Populismo'), ('Populism: A Very Short Introduction', 'https://www.google.com/search?tbm=bks&q=Mudde+Kaltwasser+Populism+A+Very+Short+Introduction'), ('Jan-Werner Müller, autor de What Is Populism? (Wikipédia)', 'https://en.wikipedia.org/wiki/Jan-Werner_M%C3%BCller'), ('Como as democracias morrem', 'https://pt.wikipedia.org/wiki/How_Democracies_Die'), ('A razão populista (Laclau)', 'https://www.google.com/search?tbm=bks&q=Laclau+A+raz%C3%A3o+populista')]),

dict(slug='corrupcao', grupo=EI, titulo='Corrupção: por que existe e o que funciona contra ela', resumo='Não é só falta de caráter: é uma conta de incentivos. O que é corrupção, o que ela custa, o que os dados dizem sobre combatê-la e por que o “salvador” não resolve.', corpo='''
<p class="abre">Corrupção é usar um cargo ou uma função pública para obter vantagem privada. Explicá-la como “falta de caráter” é cômodo, mas não ajuda a combatê-la: pessoas comuns se corrompem quando a vantagem é grande, o risco é pequeno e ninguém está olhando. Por isso, o combate eficaz mexe nos incentivos, e não só nas pessoas.</p>
<h2>As formas mais comuns</h2>
<table><thead><tr><th>Tipo</th><th>Como funciona</th></tr></thead><tbody>
<tr><td><strong>Propina</strong></td><td>Pagamento para obter contrato, licença, decisão ou vista grossa</td></tr>
<tr><td><strong>Desvio</strong></td><td>Dinheiro público que vai para bolsos privados, por obra superfaturada ou serviço não prestado</td></tr>
<tr><td><strong>Fraude em licitação</strong></td><td>Empresas combinam preços entre si, ou o edital é feito sob medida para uma delas</td></tr>
<tr><td><strong>Caixa dois</strong></td><td>Dinheiro de campanha não declarado, que esconde quem financia quem</td></tr>
<tr><td><strong>Nepotismo e apadrinhamento</strong></td><td>Cargos para parentes e aliados, sem critério. O STF proibiu o nepotismo em 2008</td></tr>
<tr><td><strong>Tráfico de influência e porta giratória</strong></td><td>Vender acesso a quem decide, ou sair do governo para a empresa que se regulava</td></tr>
<tr><td><strong>Corrupção “legal”</strong></td><td>Emendas sem critério, privilégios aprovados por lei e benefícios fiscais sob medida. Não dá cadeia, e custa muito</td></tr>
</tbody></table>
<h2>Por que ela existe</h2>
<p>O economista Robert Klitgaard resumiu em uma fórmula: <strong>corrupção = monopólio + poder de decidir − prestação de contas</strong>. Onde uma pessoa decide sozinha, sem regras claras e sem ninguém conferindo, a corrupção prospera. Outros fatores:</p>
<ul>
<li><strong>Impunidade:</strong> no Brasil, processos duram anos, recursos se acumulam e prescrevem. A certeza da punição pesa mais do que o tamanho da pena.</li>
<li><strong>Burocracia:</strong> cada exigência desnecessária é uma oportunidade de cobrar para “facilitar”.</li>
<li><strong>Campanhas caras:</strong> quem gasta muito para se eleger precisa de quem pague, e cobra depois.</li>
<li><strong>Cultura do jeitinho:</strong> quando a pequena corrupção é normal, como a carteirada e a propina ao guarda, a grande parece só uma questão de escala.</li>
<li><strong>Normalização pelo grupo:</strong> “todo mundo faz”, “é assim que funciona”, “o outro lado faz pior”.</li>
</ul>
<h2>O que ela custa</h2>
<p>Não é só o dinheiro desviado. A obra superfaturada é também a obra que não fica pronta, o remédio que não chega e a ponte que cai. A corrupção afasta investimento, porque ninguém quer competir com quem paga propina. E destrói a confiança: quando as pessoas acham que tudo é roubo, deixam de cobrar, e a desistência protege os corruptos. Veja <a href="perigo-de-ser-despolitizado.html">o perigo de ser despolitizado</a>.</p>
<h2>No Brasil, em vários lados</h2>
<ul>
<li><strong>Mensalão (2005):</strong> pagamento a parlamentares por apoio ao governo Lula; o STF condenou os envolvidos em 2012.</li>
<li><strong>Petrolão e Lava Jato (a partir de 2014):</strong> empreiteiras e dirigentes da Petrobras pagavam propina a partidos de vários campos. A operação recuperou bilhões e prendeu empresários e políticos, mas também cometeu abusos: em 2021, o STF anulou as condenações de Lula e considerou o juiz Sergio Moro parcial. Combater a corrupção não autoriza violar as regras do processo.</li>
<li><strong>Orçamento secreto (2020 a 2022):</strong> emendas bilionárias distribuídas sem transparência sobre quem indicava o dinheiro. O STF as considerou inconstitucionais em 2022.</li>
<li><strong>Casos locais:</strong> a maior parte da corrupção acontece em prefeituras e governos estaduais, longe das manchetes, em merenda, saúde e obras.</li>
</ul>
<p>No Índice de Percepção da Corrupção da Transparência Internacional, o Brasil teve 34 pontos em 100 em 2024 e ficou na 107ª posição entre 180 países. O índice mede percepção, e não casos provados, mas acompanha a tendência ao longo dos anos.</p>
<h2>O que funciona, segundo a experiência</h2>
<table><thead><tr><th>Medida</th><th>Por que funciona</th></tr></thead><tbody>
<tr><td><strong>Transparência obrigatória</strong></td><td>Portal da Transparência, Lei de Acesso à Informação (2011) e dados abertos deixam o cidadão e a imprensa conferirem</td></tr>
<tr><td><strong>Compras eletrônicas e regras claras</strong></td><td>O pregão eletrônico reduziu o espaço para combinação de preços. Menos poder de decidir sozinho, menos corrupção</td></tr>
<tr><td><strong>Órgãos de controle independentes</strong></td><td>Tribunais de Contas, Controladoria-Geral da União, Ministério Público e Polícia Federal com autonomia e orçamento</td></tr>
<tr><td><strong>Imprensa livre</strong></td><td>Quase todo grande caso começou com uma reportagem. Veja <a href="como-ler-a-midia-tradicional.html">como ler o noticiário</a></td></tr>
<tr><td><strong>Punição certa e rápida</strong></td><td>Acordos de leniência, delação premiada com regras e processos mais curtos, com direito de defesa garantido</td></tr>
<tr><td><strong>Filtro na entrada</strong></td><td>A Lei da Ficha Limpa (2010), de iniciativa popular, impede candidaturas de condenados por órgãos colegiados</td></tr>
<tr><td><strong>Menos burocracia e menos cargos de confiança</strong></td><td>Cada carimbo a menos é uma propina a menos; concursos reduzem o apadrinhamento</td></tr>
<tr><td><strong>Proteção a quem denuncia</strong></td><td>Canais seguros e proteção contra retaliação</td></tr>
</tbody></table>
<h2>O que não funciona</h2>
<ul>
<li><strong>O salvador.</strong> “Só ele é honesto” é o começo de muitos escândalos, porque o honesto sem controle deixa de ser conferido. Veja o <a href="perigo-do-messianismo.html">messianismo</a>.</li>
<li><strong>Moralismo seletivo.</strong> Quem só vê a corrupção do outro lado não combate corrupção: usa o tema como arma. Faça o <a href="ferramentas/teste-de-troca.html">teste de troca</a>.</li>
<li><strong>“Vale tudo contra os corruptos.”</strong> Processos sem defesa e vazamentos seletivos acabam anulados e desacreditam o próprio combate.</li>
<li><strong>Achar que tudo é corrupção.</strong> O orçamento tem limites mesmo sem desvio nenhum, e a corrupção não explica cada serviço ruim. Veja o <a href="perigo-do-maniqueismo.html">perigo de simplificar</a>.</li>
</ul>
<h2>O que você pode fazer</h2>
<ol class="roteiro"><li>Não vote em condenados e em quem responde a processos graves, de qualquer partido. Consulte o <a href="https://divulgacandcontas.tse.jus.br/" target="_blank" rel="noopener">DivulgaCandContas</a>.</li><li>Olhe as emendas e as contas da sua cidade no <a href="https://portaldatransparencia.gov.br/" target="_blank" rel="noopener">Portal da Transparência</a>.</li><li>Cobre o seu lado com a mesma régua que usa para o outro.</li><li>Não pratique a pequena corrupção: ela é a escola da grande.</li><li>Apoie imprensa e órgãos de controle quando investigam quem você apoia.</li></ol>
''', fontes=[('Transparência Internacional Brasil', 'https://transparenciainternacional.org.br/'), ('Índice de Percepção da Corrupção 2024', 'https://www.transparency.org/en/cpi/2024'), ('Controlling Corruption (Klitgaard)', 'https://www.google.com/search?tbm=bks&q=Klitgaard+Controlling+Corruption'), ('Corrupção no Brasil (Wikipédia)', 'https://pt.wikipedia.org/wiki/Corrup%C3%A7%C3%A3o_no_Brasil'), ('Lei da Ficha Limpa (Wikipédia)', 'https://pt.wikipedia.org/wiki/Lei_da_Ficha_Limpa'), ('Portal da Transparência', 'https://portaldatransparencia.gov.br/')]),

dict(slug='como-ler-a-midia-tradicional', grupo=DR, titulo='Como ler a grande mídia com senso crítico', resumo='Jornais e emissoras têm método, correção e responsabilidade. Também têm dono, linha editorial, anunciantes e erros históricos. Como aproveitar o que fazem bem sem engolir tudo.', corpo='''
<p class="abre">A lição sobre a <a href="perigo-da-midia-alternativa.html">mídia alternativa extremista</a> mostra o risco de se informar por veículos de torcida. Mas a grande mídia também merece leitura crítica. Ela não é um bloco único, não é neutra e já errou feio. Ao mesmo tempo, tem algo que a maioria dos canais de internet não tem: método, responsabilidade legal e correção pública. O objetivo não é escolher um lado entre “a mídia mente” e “a mídia é imparcial”. É aprender a ler.</p>
<h2>O que ela faz melhor</h2>
<ul>
<li><strong>Apuração com método:</strong> ouvir os envolvidos, conferir documentos, checar antes de publicar. Não é garantia, mas é uma regra que pode ser cobrada.</li>
<li><strong>Responsabilidade:</strong> veículos têm nome, endereço, editor e CNPJ. Quem é difamado pode processar, e isso impõe cuidado.</li>
<li><strong>Correção pública:</strong> erros são corrigidos, com registro. Compare com um vídeo que simplesmente some.</li>
<li><strong>Investigação cara:</strong> meses de trabalho de repórteres, que revelaram do mensalão ao orçamento secreto. Veja <a href="corrupcao.html">corrupção</a>.</li>
<li><strong>Pluralidade interna:</strong> colunistas de linhas diferentes no mesmo jornal, o que raramente existe em canais de um dono só.</li>
</ul>
<h2>Os limites e os vieses</h2>
<table><thead><tr><th>Limite</th><th>O que significa na prática</th></tr></thead><tbody>
<tr><td><strong>Tem dono</strong></td><td>Poucas famílias e grupos controlam a maior parte da audiência de TV, rádio e jornal no Brasil. Interesses do dono, de seus negócios e de sua posição política podem pesar na cobertura</td></tr>
<tr><td><strong>Tem linha editorial</strong></td><td>Todo veículo escolhe o que cobre, com que destaque e com que palavras. Isso é legítimo, desde que seja visível e não contamine a notícia</td></tr>
<tr><td><strong>Depende de dinheiro</strong></td><td>Anunciantes, assinantes e verba pública de publicidade. Governos de vários partidos já usaram a publicidade oficial para premiar aliados</td></tr>
<tr><td><strong>Tem pressa</strong></td><td>A concorrência por cliques leva a manchetes que o texto não sustenta e a erros que depois são corrigidos em letra pequena</td></tr>
<tr><td><strong>Falso equilíbrio</strong></td><td>Dar o mesmo peso a um consenso científico e a uma opinião isolada, para parecer neutro, distorce a realidade</td></tr>
<tr><td><strong>Bolha de redação</strong></td><td>Jornalistas vivem em grandes cidades, com formação parecida, e podem não enxergar o que o resto do país vê</td></tr>
<tr><td><strong>Pauta por conveniência</strong></td><td>O que aparece depende do que é fácil de cobrir e do que rende audiência. O crime na capital ganha mais espaço do que a fome no interior</td></tr>
</tbody></table>
<h2>Os erros que a própria mídia reconhece</h2>
<ul>
<li><strong>Apoio ao golpe de 1964:</strong> os principais jornais apoiaram a deposição de João Goulart. A Globo publicou em 2013 um editorial reconhecendo que o apoio editorial à ditadura foi um erro.</li>
<li><strong>O debate de 1989:</strong> a edição do último debate entre Collor e Lula exibida no Jornal Nacional favoreceu Collor, segundo críticos de dentro e de fora da emissora. O caso está na seção de erros do site Memória Globo.</li>
<li><strong>Escola Base (1994):</strong> donos de uma escola em São Paulo foram acusados de abuso de crianças com base em uma investigação policial frágil. A imprensa publicou como fato. Eram inocentes, e tiveram a vida destruída.</li>
<li><strong>Cobertura policial:</strong> versões da polícia publicadas como verdade, sem ouvir o outro lado, sobretudo quando as vítimas são pobres e negras.</li>
</ul>
<p>Reconhecer esses erros não leva à conclusão de que “tudo é mentira”. Leva à conclusão de que a leitura precisa de critério, com qualquer fonte.</p>
<h2>Como ler o noticiário</h2>
<ol class="roteiro">
<li><strong>Separe notícia de opinião.</strong> Editorial, coluna e análise são opinião assumida. Reportagem deve ter fatos verificáveis. Muitos veículos marcam a diferença, e vale aprender a ver.</li>
<li><strong>Leia além da manchete.</strong> Com frequência, o título promete mais do que o texto entrega. Veja o que o texto diz de fato, e o que a fonte citada disse.</li>
<li><strong>Procure a fonte original.</strong> O estudo, o documento, a íntegra da fala, o dado do IBGE. Quase sempre há um link ou um nome para buscar.</li>
<li><strong>Compare veículos de linhas diferentes.</strong> Se dois jornais com posições opostas relatam o mesmo fato, ele provavelmente aconteceu. Onde eles divergem, está a interpretação.</li>
<li><strong>Note o enquadramento.</strong> “Governo gasta” ou “governo investe”? “Protesto” ou “baderna”? “Reforma” ou “desmonte”? A escolha das palavras já é uma posição. Veja <a href="palavras-em-disputa.html">palavras em disputa</a>.</li>
<li><strong>Pergunte quem não foi ouvido.</strong> Uma reportagem com uma só fonte é uma versão.</li>
<li><strong>Veja o que o veículo faz quando erra.</strong> Corrige com destaque, ou apaga em silêncio? Esse é o melhor termômetro de confiabilidade.</li>
</ol>
<div class="nota"><strong>“A mídia” não existe no singular.</strong> Há jornais, emissoras, agências, sites e portais com donos, linhas e qualidades diferentes. Generalizar é o primeiro passo para só acreditar em quem confirma o que você já pensa. Veja as <a href="camaras-de-eco.html">câmaras de eco</a> e a lição sobre <a href="checagem-de-fatos.html">checagem de fatos</a>.</div>
<h2>Confiança no Brasil</h2>
<p>O Reuters Institute mede todo ano a confiança nas notícias. No Brasil, ela caiu ao longo da última década, e hoje menos da metade das pessoas diz confiar na maior parte do noticiário. Parte disso se deve a erros reais, e parte a campanhas sistemáticas de descrédito, que servem a quem prefere não ser fiscalizado. Os dois fatores existem, e distinguir um do outro é parte da leitura crítica.</p>
''', fontes=[('Media Ownership Monitor Brasil', 'https://brazil.mom-gmr.org/'), ('O Globo: “Apoio editorial ao golpe de 64 foi um erro” (2013)', 'https://oglobo.globo.com/brasil/apoio-editorial-ao-golpe-de-64-foi-um-erro-9771604'), ('Caso Escola Base (Wikipédia)', 'https://pt.wikipedia.org/wiki/Caso_Escola_Base'), ('Falso equilíbrio (Wikipédia)', 'https://en.wikipedia.org/wiki/False_balance'), ('Reuters Institute: Digital News Report, Brasil', 'https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025/brazil'), ('Eleição presidencial de 1989 (Wikipédia)', 'https://pt.wikipedia.org/wiki/Elei%C3%A7%C3%A3o_presidencial_no_Brasil_em_1989')]),

dict(slug='pesquisas-eleitorais', grupo=DR, titulo='Como ler uma pesquisa eleitoral', resumo='Pesquisa é fotografia, não previsão. O que significam amostra, margem de erro e votos válidos, por que elas erram e como reconhecer uma pesquisa falsa.', corpo='''
<p class="abre">Toda eleição vem com uma enxurrada de pesquisas, e com a mesma briga: “a pesquisa está comprada”, “a pesquisa errou”, “a pesquisa manipula o eleitor”. Pesquisa séria é uma ferramenta útil e limitada. Para usá-la bem, é preciso entender o que ela mede, e o que não mede.</p>
<h2>Como funciona</h2>
<p>Ninguém pergunta a 150 milhões de eleitores. O instituto entrevista uma <strong>amostra</strong>, em geral entre mil e três mil pessoas, escolhida para representar o eleitorado em sexo, idade, renda, escolaridade e região. Se a amostra é bem feita, o resultado se aproxima do total, com uma margem de incerteza conhecida. É o mesmo princípio de provar a sopa com uma colher: funciona se a panela foi mexida.</p>
<table><thead><tr><th>Termo</th><th>O que significa</th></tr></thead><tbody>
<tr><td><strong>Margem de erro</strong></td><td>O quanto o resultado pode variar para cima ou para baixo. Com 2 pontos de margem, um candidato com 40% pode ter entre 38% e 42%. Dois candidatos com 2 pontos de diferença estão em <strong>empate técnico</strong></td></tr>
<tr><td><strong>Nível de confiança</strong></td><td>Em geral 95%: se a pesquisa fosse repetida muitas vezes, em 19 de cada 20 o resultado real estaria dentro da margem. Ou seja, 1 em 20 pode ficar fora, sem erro do instituto</td></tr>
<tr><td><strong>Votos totais e votos válidos</strong></td><td>Totais incluem brancos, nulos e indecisos. Válidos excluem esses. Na eleição, quem vence no primeiro turno precisa de mais da metade dos <em>válidos</em>. Comparar totais de uma pesquisa com válidos de outra é um erro comum</td></tr>
<tr><td><strong>Estimulada e espontânea</strong></td><td>Na estimulada, o entrevistado vê a lista de nomes. Na espontânea, responde sem lista, e os números são bem menores</td></tr>
<tr><td><strong>Rejeição</strong></td><td>Em quem o eleitor “não votaria de jeito nenhum”. Muitas vezes diz mais sobre o segundo turno do que a intenção de voto</td></tr>
<tr><td><strong>Registro no TSE</strong></td><td>Toda pesquisa divulgada precisa ser registrada com antecedência, informando quem pagou, a amostra, a margem e o questionário. Pesquisa sem registro é irregular</td></tr>
</tbody></table>
<h2>Por que elas erram</h2>
<ul>
<li><strong>Quem não responde.</strong> Se eleitores de um candidato recusam mais a entrevista, ou mentem, a amostra fica torta. É a explicação mais aceita para erros recentes nos EUA e no Brasil.</li>
<li><strong>Gente que decide na véspera.</strong> Pesquisa de uma semana antes não captura quem mudou de ideia no sábado.</li>
<li><strong>Ponderação.</strong> O instituto ajusta a amostra para refletir o eleitorado, e cada ajuste é uma escolha que pode errar, sobretudo com escolaridade e renda.</li>
<li><strong>Método.</strong> Entrevista presencial, por telefone e pela internet alcançam públicos diferentes.</li>
<li><strong>Pesquisas de verdade também ficam fora da margem</strong> em cerca de 1 a cada 20 vezes, por pura estatística.</li>
</ul>
<p>Em 2022, as principais pesquisas subestimaram a votação de Jair Bolsonaro no primeiro turno, e em 2018 houve erro semelhante com candidatos de outros campos em disputas estaduais. Isso mostra os limites do método, e não que as pesquisas sejam inventadas: institutos que erram muito perdem clientes, e seus resultados são comparados publicamente.</p>
<h2>Pesquisa falsa e pesquisa de torcida</h2>
<p>O que circula nas redes como “pesquisa” muitas vezes não é uma. Enquete de site ou de perfil, em que qualquer pessoa vota quantas vezes quiser, mede só quem foi mobilizado para votar. Pesquisa “paralela”, “interna” ou de instituto que ninguém conhece, divulgada sem registro, costuma ser propaganda. E pesquisa encomendada por partido pode ser séria, mas o contratante precisa aparecer, e é bom saber quem é.</p>
<h2>Como ler bem</h2>
<ol class="roteiro">
<li><strong>Veja a tendência, não a pesquisa isolada.</strong> Uma oscilação de 2 pontos dentro da margem não é notícia. Vários institutos apontando a mesma direção, sim. Agregadores de pesquisas ajudam.</li>
<li><strong>Confira o registro no TSE:</strong> quem pagou, quantos entrevistados, quando, com que margem.</li>
<li><strong>Compare o comparável:</strong> válidos com válidos, estimulada com estimulada, mesmo instituto com mesmo instituto.</li>
<li><strong>Olhe a data da coleta,</strong> não a da divulgação.</li>
<li><strong>Lembre que pesquisa não é previsão.</strong> É um retrato do momento, com borrão.</li>
<li><strong>Não vote pela pesquisa.</strong> O “voto útil” é uma escolha legítima, mas baseada em uma fotografia que pode estar errada. Veja <a href="como-votar-bem.html">como votar bem</a>.</li>
</ol>
<div class="nota"><strong>Pesquisa muda o eleitor?</strong> Há evidência de um pequeno efeito de “ir com o vencedor” e de voto útil, e por isso alguns países proíbem a divulgação nos últimos dias. O Brasil permite até o dia da eleição. O efeito existe, mas é menor do que a reclamação de quem está atrás sugere. Veja o <a href="vieses/bandwagon-effect.html">efeito de adesão</a>.</div>
''', fontes=[('TSE: pesquisas eleitorais', 'https://www.tse.jus.br/eleicoes/pesquisa-eleitoral'), ('Pesquisa eleitoral (Wikipédia)', 'https://pt.wikipedia.org/wiki/Pesquisa_eleitoral'), ('Margem de erro (Wikipédia)', 'https://pt.wikipedia.org/wiki/Margem_de_erro'), ('Amostragem (Wikipédia)', 'https://pt.wikipedia.org/wiki/Amostragem_(estat%C3%ADstica)'), ('Biblioteca de Dados: estatística para leigos', 'https://data.biblioverse.org/')]),
]

META_REVISAO = {
 'como-uma-lei-e-feita': (['fundamentos', 'brasil'], ('O que acontece quando o presidente veta um projeto?', ['O projeto morre', 'O Congresso pode derrubar o veto por maioria absoluta', 'O STF decide'], 1, 'O veto volta ao Congresso, que pode mantê-lo ou derrubá-lo em sessão conjunta.')),
 'o-que-e-um-partido': (['fundamentos', 'eleicoes', 'brasil'], ('De onde vem a maior parte do dinheiro das campanhas hoje?', ['De empresas', 'Dos fundos públicos partidário e eleitoral', 'Da venda de produtos'], 1, 'Doações de empresas são proibidas desde 2015. O dinheiro público é distribuído pelas cúpulas dos partidos.')),
 'economia-para-entender-politica': (['economia', 'fundamentos'], ('Um salário que sobe 5% com inflação de 5%…', ['Aumentou 5%', 'Não mudou em poder de compra', 'Caiu 5%'], 1, 'O aumento nominal foi comido pela inflação. Compare sempre o valor real.')),
 'perigo-do-populismo': (['perigos', 'ideologia'], ('Qual é o traço mais perigoso do populismo, segundo Müller?', ['Defender os pobres', 'Afirmar que só o líder representa o povo', 'Fazer comícios'], 1, 'Se só o líder é o povo, quem discorda não é legítimo, e os limites ao poder viram obstáculos.')),
 'corrupcao': (['perigos', 'brasil'], ('Segundo a fórmula de Klitgaard, a corrupção cresce quando há…', ['Monopólio e poder de decidir, sem prestação de contas', 'Muitos jornalistas', 'Eleições frequentes'], 0, 'Quem decide sozinho, sem regra clara e sem ninguém conferindo, tem mais oportunidade de se corromper.')),
 'como-ler-a-midia-tradicional': (['desinformacao', 'mente'], ('Qual é o melhor sinal de confiabilidade de um veículo?', ['Ter muita audiência', 'Corrigir erros em público e mostrar as fontes', 'Concordar com você'], 1, 'Método e correção pública são o que permite conferir o trabalho, de qualquer veículo.')),
 'pesquisas-eleitorais': (['desinformacao', 'eleicoes'], ('Dois candidatos com 41% e 39%, margem de 2 pontos, estão…', ['Com vantagem clara do primeiro', 'Em empate técnico', 'Com erro do instituto'], 1, 'A diferença cabe dentro da margem de erro. Pesquisa é fotografia com borrão, não previsão.')),
}

# Analogia, explicação para criança e aprofundamento das lições novas.
BASICO_REVISAO = {
'como-uma-lei-e-feita': dict(
 analogia='Fazer uma lei é como aprovar uma reforma no prédio. Alguém propõe, uma comissão de moradores analisa o projeto, a assembleia vota, o outro bloco também precisa concordar, e o síndico pode recusar. Se o projeto quebrar uma regra da convenção, o conselho derruba. Parece lento, e é para ser: ninguém quer um muro derrubado na pressa.',
 crianca='Para mudar uma regra da escola, não basta um aluno querer. Ele escreve a ideia, um grupo discute e melhora, a turma vota, a outra turma também vota, e a diretora pode dizer não. Se a regra nova for contra o regulamento da escola, ela não vale. É assim que uma lei é feita, só que para o país inteiro.',
 fundo='''<h2>Maioria simples, absoluta e qualificada</h2>
<table><thead><tr><th>Tipo</th><th>O que exige</th><th>Usada para</th></tr></thead><tbody>
<tr><td>Simples</td><td>Mais da metade dos presentes, desde que haja quórum</td><td>Leis ordinárias</td></tr>
<tr><td>Absoluta</td><td>Mais da metade de todos os membros: 257 deputados e 41 senadores</td><td>Leis complementares e derrubada de veto</td></tr>
<tr><td>Qualificada</td><td>3/5 de todos os membros: 308 deputados e 49 senadores</td><td>Emendas à Constituição</td></tr>
</tbody></table>
<h2>O que a Constituição não deixa mudar</h2>
<p>As chamadas cláusulas pétreas não podem ser abolidas nem por emenda: a forma federativa, o voto direto, secreto, universal e periódico, a separação dos Poderes e os direitos e garantias individuais. Uma proposta que tentasse acabar com eleições seria barrada antes de ser votada. Só uma nova Assembleia Constituinte poderia refazer tudo, e o Brasil já teve sete constituições.</p>
<h2>Medida provisória: o atalho e o risco</h2>
<p>A MP foi feita para urgências reais, como uma calamidade. Na prática, presidentes de todos os partidos a usaram para governar sem esperar o Congresso, e o Congresso aproveita para incluir os jabutis. Desde 2001, uma MP tranca a pauta da casa em que está depois de 45 dias, o que força a votação, e perde a validade se não for votada em 120 dias.</p>''',
 fontes=[('Cláusulas pétreas (Wikipédia)', 'https://pt.wikipedia.org/wiki/Cl%C3%A1usula_p%C3%A9trea'), ('Medida provisória (Wikipédia)', 'https://pt.wikipedia.org/wiki/Medida_provis%C3%B3ria')]),
'o-que-e-um-partido': dict(
 analogia='Um partido é como uma escola de samba: tem nome, cores, enredo, diretoria e dinheiro para o desfile. Quem quer desfilar precisa entrar em uma. Algumas têm história e comunidade. Outras existem só para disputar a verba e o espaço na avenida, e trocam de enredo conforme a conveniência.',
 crianca='Para o jogo da turma, as crianças formam times. Cada time tem um nome, combina um jeito de jogar e escolhe quem entra. Ninguém joga sozinho. Partidos são times para a política. O problema é quando o time só quer o prêmio e esquece de jogar direito.',
 fundo='''<h2>Sistemas partidários pelo mundo</h2>
<table><thead><tr><th>Modelo</th><th>Como funciona</th><th>Exemplos</th></tr></thead><tbody>
<tr><td>Bipartidário</td><td>Dois grandes partidos dominam, por causa do voto distrital</td><td>EUA, Reino Unido em boa parte da história</td></tr>
<tr><td>Multipartidário moderado</td><td>Quatro a seis partidos relevantes, que formam coalizões</td><td>Alemanha, Espanha</td></tr>
<tr><td>Multipartidário fragmentado</td><td>Muitos partidos, coalizões amplas e instáveis</td><td>Brasil, Israel, Itália em certos períodos</td></tr>
<tr><td>Partido único</td><td>Só um partido pode governar; os outros são proibidos ou decorativos</td><td>China, Cuba, Coreia do Norte</td></tr>
</tbody></table>
<p>Nenhum modelo é perfeito. O bipartidarismo dá clareza e tende a polarizar. A fragmentação dá diversidade e dificulta governar. As regras eleitorais, mais do que a cultura, explicam a diferença. Veja as <a href="melhorar-a-democracia.html">ideias para melhorar a democracia</a>.</p>
<h2>Partido não é dono do seu voto</h2>
<p>Você pode votar em pessoas de partidos diferentes para cargos diferentes, e pode mudar de voto a cada eleição. Ter preferência por um partido é legítimo. O risco é o <a href="perigo-do-tribalismo.html">tribalismo</a>: defender o partido como time, inclusive quando ele erra.</p>''',
 fontes=[('Sistema partidário (Wikipédia)', 'https://pt.wikipedia.org/wiki/Sistema_partid%C3%A1rio')]),
}

REFORCO_REVISAO = {
'economia-para-entender-politica': dict(
 analogia='A economia do país é como o orçamento de uma casa grande, com uma diferença: a casa pode pegar emprestado quase sem limite e pode até imprimir o próprio dinheiro. Isso resolve o mês, e cria a conta do ano seguinte. Juros, dívida e inflação são os nomes dessa conta.',
 crianca='Imagine que a sua turma tem um cofrinho para a festa. Se gastar mais do que juntou, precisa pedir emprestado e devolver com um pouco a mais: são os juros. Se alguém inventar de fazer dinheiro de papel para pagar, logo ninguém aceita mais aquele papel, e tudo fica mais caro: é a inflação.',
 fundo='''<h2>Por que a inflação pesa mais sobre os pobres</h2>
<p>Quem tem dinheiro sobrando aplica em títulos corrigidos pela inflação e protege o que tem. Quem vive do salário gasta tudo no mês e vê o dinheiro perder valor entre o pagamento e a compra. Na hiperinflação dos anos 1980 e 1990, os preços mudavam todo dia, e as pessoas corriam ao mercado no dia do pagamento. O Plano Real acabou com isso em 1994, e desde então o controle da inflação é uma das poucas prioridades que quase todos os governos mantiveram.</p>
<h2>O que o Banco Central faz e não faz</h2>
<p>O Banco Central define a Selic e cuida da moeda e dos bancos. Não decide impostos nem gastos, que são do governo e do Congresso. Quando os dois lados puxam em direções opostas, com o governo gastando e o Banco Central freando, a corda é o juro, e quem paga é o país. Desde 2021, a diretoria tem mandato fixo, para que decisões técnicas não mudem a cada eleição. Há quem defenda essa autonomia como proteção, e quem a veja como poder demais nas mãos de quem não foi eleito.</p>
<h2>Crescer para quem?</h2>
<p>O PIB pode crescer com a renda concentrada no topo. Por isso, indicadores como a renda média por pessoa, a pobreza, a desigualdade e o desemprego dizem coisas que o PIB sozinho não diz. Um bom debate econômico olha os vários números juntos.</p>'''),
'perigo-do-populismo': dict(
 analogia='É como um síndico que diz que só ele representa os moradores e que o conselho, a contadora e o vizinho que reclama são todos inimigos do prédio. No começo, ele resolve coisas que ninguém resolvia. Depois, qualquer conferência das contas vira perseguição, e quem discorda é convidado a se mudar.',
 crianca='Imagine um colega que diz: “eu sou a turma inteira, quem não concorda comigo não é da turma”. Ele pode até ter boas ideias, mas assim ninguém mais pode opinar, e a professora que pede para ver o combinado vira inimiga. Uma turma de verdade tem muita gente pensando diferente.'),
'corrupcao': dict(
 analogia='Deixe uma caixa de dinheiro aberta, sem câmera, com uma pessoa só tomando conta e ninguém conferindo as contas. Não é preciso um vilão: basta tempo. Combater a corrupção é menos sobre encontrar santos e mais sobre fechar a caixa, instalar a câmera e contar o dinheiro em público.',
 crianca='Imagine que uma criança guarda o dinheiro da festa sozinha, num lugar que ninguém vê, e ninguém pergunta quanto tem. Mesmo uma criança boa pode acabar pegando um pouco. Se o dinheiro fica num pote transparente e todo mundo confere, fica muito mais difícil. Corrupção se combate assim: com regras e gente olhando.'),
'como-ler-a-midia-tradicional': dict(
 analogia='Um grande jornal é como um restaurante com cozinha profissional e vigilância sanitária. A comida pode ser mal temperada, o dono pode escolher o cardápio, e já houve intoxicações famosas. Mas há regras, inspeção e um nome a zelar, o que não existe na barraca anônima que some depois do erro. Dá para comer nos dois lugares, desde que se saiba onde está.',
 crianca='O jornal da escola é feito por alunos que precisam ouvir os dois lados e corrigir quando erram, porque todo mundo sabe quem escreveu. Isso não quer dizer que ele acerta sempre, nem que conta tudo. Por isso, é bom ler mais de um jornal e perguntar: “quem contou isso, e como eles sabem?”.'),
'pesquisas-eleitorais': dict(
 analogia='Pesquisa eleitoral é como provar a sopa com uma colher para saber se a panela está salgada. Funciona se a sopa foi bem mexida e a colher é limpa. Mas a colher diz como a sopa está agora, não como vai estar depois que alguém puser mais sal, e uma colherada em vinte vai enganar só por azar.',
 crianca='Para saber qual é o sabor de sorvete preferido da escola, você não precisa perguntar a todos: pergunta a algumas crianças de cada turma, meninos e meninas, pequenos e grandes. O resultado chega perto do que a escola inteira pensa, mas pode errar um pouco, e pode mudar se chegar um sabor novo amanhã.'),
}

# Grupos de cada lição e ordem dos grupos em cada nível. Lições sem entrada mantêm o grupo definido no próprio módulo.
GRUPOS = {
 # Iniciante
 'o-que-e-politica': 'O básico', 'perigo-de-ser-despolitizado': 'O básico', 'o-que-esta-por-tras': 'O básico',
 'valores-e-decisoes': 'Valores e escolhas', 'etica-normativa': 'Valores e escolhas',
 'esquerda-e-direita': 'Os lados', 'palavras-em-disputa': 'Os lados', 'sem-binarismo': 'Os lados',
 'democracia': INI, 'como-uma-lei-e-feita': INI, 'o-que-e-um-partido': INI,
 'como-votar-bem': 'Voto e informação', 'checagem-de-fatos': 'Voto e informação',
 # Intermediário
 'contrato-social': CE, 'imposto-e-roubo': CE, 'economia-para-entender-politica': CE, 'politicas-publicas': CE, 'geopolitica': CE, 'globalizacao': CE, 'comparar-projetos': CE, 'bem-comum': CE,
 'vieses-cognitivos': 'Como a mente nos engana', 'mudar-de-ideia': 'Como a mente nos engana', 'testar-visao-moral': 'Como a mente nos engana', 'mente-moralista': 'Como a mente nos engana', 'sofismo': 'Como a mente nos engana', 'perigo-do-maniqueismo': 'Como a mente nos engana', 'perigo-do-tribalismo': 'Como a mente nos engana', 'politica-do-medo': 'Como a mente nos engana', 'perigo-do-fanatismo': 'Como a mente nos engana',
 'teoria-da-ferradura': PI, 'perigo-das-revolucoes': PI, 'perigo-do-reacionarismo': PI, 'perigo-do-ultraconservadorismo': PI, 'perigo-do-messianismo': PI, 'perigo-do-populismo': PI, 'perigo-de-culpar-o-estrangeiro': PI,
 'camaras-de-eco': DR, 'perigo-da-midia-alternativa': DR, 'como-ler-a-midia-tradicional': DR, 'perigo-dos-grupos-de-mensagem': DR, 'perigo-dos-bots': DR, 'cambridge-analytica': DR, 'pesquisas-eleitorais': DR,
 'numero-de-projetos': EI, 'corrupcao': EI, 'estado-e-mercado': EI, 'religiao-e-estado': EI, 'poder-paralelo': EI, 'um-sistema-para-todos': EI, 'regras-e-desobediencia': EI, 'perigo-de-questionar-a-democracia': EI,
 'liberdade-de-expressao': 'Perguntas difíceis', 'respeitar-crencas': 'Perguntas difíceis', 'nem-tudo-e-politico': 'Perguntas difíceis',
 'maiores-estadistas': 'Quem fez história', 'maiores-ativistas': 'Quem fez história', 'america-do-sul-e-ditaduras': 'Quem fez história',
 # Avançado
 'teorias-da-justica': 'Quem conta e o que é justo', 'progresso-moral-e-politico': 'Quem conta e o que é justo', 'sencientismo': 'Quem conta e o que é justo', 'relativismo-e-circulo-moral': 'Quem conta e o que é justo', 'politica-baseada-na-senciencia': 'Quem conta e o que é justo', 'libertarismo-de-coracao-sangrante': 'Quem conta e o que é justo',
}
ORDEM_GRUPOS = {
 'iniciante': ['O básico', 'Valores e escolhas', 'Os lados', INI, 'Voto e informação'],
 'intermediario': [CE, 'Como a mente nos engana', PI, DR, EI, 'Direito e mundo', 'Perguntas difíceis', 'Quem fez história'],
 'avancado': ['Quem chega ao poder', 'Mente, identidade e política', 'Melhorar a democracia', 'O sistema brasileiro', 'Quem conta e o que é justo', 'Riscos do futuro'],
}

NOVAS_AVANCADO = [
dict(slug='pragmatismo-politico', grupo='Melhorar a democracia', titulo='Pragmatismo como postura política', resumo='Julgar ideias pelo que produzem, e não pela bandeira. De onde vem a postura, quando é virtude, quando vira falta de princípio, e como distinguir uma coisa da outra.', corpo='''
<p class="abre">“Sou pragmático” é uma das frases mais usadas na política, e uma das mais ambíguas. Pode significar alguém que julga cada proposta pelos resultados, aceita acordos e corrige o rumo quando os dados mudam. Pode também ser o nome bonito para quem não tem princípio nenhum e vende o voto a quem pagar mais. Esta lição separa as duas coisas.</p>
<h2>De onde vem a palavra</h2>
<p>O pragmatismo nasceu como corrente filosófica nos Estados Unidos, no fim do século XIX, com Charles Peirce, William James e John Dewey. A ideia central: o sentido e o valor de uma ideia estão nas consequências práticas que ela produz. Uma crença que não muda nada no mundo não vale a discussão. Dewey levou isso à política e à educação: a democracia seria um grande experimento coletivo, em que as regras são hipóteses a serem testadas, avaliadas e corrigidas, e não dogmas.</p>
<p>Na política cotidiana, a palavra ganhou um sentido mais solto: fazer o que funciona, negociar, aceitar o possível em vez de esperar o ideal. Os dois sentidos se encontram em uma pergunta: <strong>o que esta decisão produz, de fato, na vida das pessoas?</strong></p>
<h2>Duas éticas, segundo Weber</h2>
<p>Em <em>A política como vocação</em> (1919), Max Weber distinguiu duas formas de agir na política:</p>
<table><thead><tr><th></th><th>Ética da convicção</th><th>Ética da responsabilidade</th></tr></thead><tbody>
<tr><td>O que guia</td><td>O princípio. Faço o que é certo, aconteça o que acontecer</td><td>As consequências previsíveis. Respondo pelo que minha escolha vai causar</td></tr>
<tr><td>Diante de um acordo</td><td>Ceder é trair</td><td>Ceder em parte pode ser o único jeito de conseguir algo</td></tr>
<tr><td>Risco</td><td>Pureza que não muda nada, ou que destrói tudo em nome do ideal</td><td>Justificar qualquer meio pelo resultado</td></tr>
</tbody></table>
<p>Weber não escolheu uma contra a outra. Disse que o político maduro precisa das duas: convicções firmes e responsabilidade pelas consequências. O pragmatismo saudável é a ética da responsabilidade a serviço de uma convicção, e não no lugar dela.</p>
<h2>Exemplos de pragmatismo que deu certo</h2>
<ul>
<li><strong>Deng Xiaoping</strong>, na China dos anos 1970: “não importa se o gato é branco ou preto, desde que cace ratos”. Abriu a economia sem abandonar o controle político, e tirou centenas de milhões da pobreza. O mesmo pragmatismo manteve a ditadura, o que mostra que ele não substitui valores.</li>
<li><strong>Nelson Mandela</strong> negociou com o regime do apartheid que o prendera por 27 anos, aceitou garantias à minoria branca e evitou uma guerra civil. Foi criticado por aliados mais radicais.</li>
<li><strong>O Plano Real</strong> (1994) combinou economistas de linhas diferentes e abandonou receitas anteriores que não funcionaram, depois de uma década de planos fracassados.</li>
<li><strong>Karl Popper</strong> chamou de “engenharia social gradual” a postura de reformar aos poucos, medir e corrigir, contra a “engenharia utópica” que quer refazer tudo de uma vez. Veja o <a href="perigo-das-revolucoes.html">perigo das revoluções</a> e as <a href="politicas-baseadas-em-evidencias.html">políticas baseadas em evidências</a>.</li>
</ul>
<h2>O que o pragmatismo acerta</h2>
<ul>
<li><strong>Olha o resultado, e não a bandeira.</strong> Uma boa ideia continua boa quando vem do adversário. É o antídoto ao <a href="perigo-do-tribalismo.html">pacote de ideias</a>.</li>
<li><strong>Aceita o possível.</strong> Em uma democracia, ninguém governa sozinho. Quem exige tudo costuma conseguir nada. Veja o <a href="presidencialismo-de-coalizao.html">presidencialismo de coalizão</a>.</li>
<li><strong>Corrige o rumo.</strong> Trata políticas como hipóteses e <a href="mudar-de-ideia.html">muda de ideia</a> diante de evidências.</li>
<li><strong>Desconfia das soluções totais.</strong> Prefere reformas que podem ser desfeitas se derem errado.</li>
<li><strong>Evita o perfeito como inimigo do bom.</strong> Uma lei imperfeita que reduz mortes vale mais do que um projeto ideal que nunca passa.</li>
</ul>
<h2>Quando vira vício</h2>
<table><thead><tr><th>Pragmatismo saudável</th><th>Falso pragmatismo</th></tr></thead><tbody>
<tr><td>Negocia o caminho, e mantém o destino</td><td>Negocia o destino: não há nada que não venda</td></tr>
<tr><td>Cede em parte para conseguir o essencial</td><td>Cede o essencial para ficar no cargo</td></tr>
<tr><td>Troca apoio por agenda, às claras</td><td>Troca apoio por cargos e verbas, às escondidas. É o fisiologismo</td></tr>
<tr><td>Muda de posição por novos fatos, e explica</td><td>Muda de posição por conveniência, e finge que não mudou. Veja o <a href="sofismo.html">sofismo</a></td></tr>
<tr><td>Tem limites que não cruza, mesmo para vencer</td><td>“Os fins justificam os meios”</td></tr>
<tr><td>Diz “ainda não dá” e mostra o plano</td><td>Diz “não dá” para justificar não fazer nada</td></tr>
<tr><td>Pergunta se funciona, e para quem</td><td>Pergunta só se funciona para quem decide</td></tr>
</tbody></table>
<p>No Brasil, “pragmático” virou o adjetivo educado para partidos que apoiam qualquer governo em troca de espaço. Isso não é pragmatismo no sentido de Dewey ou de Weber: não há convicção sendo servida pela responsabilidade, só interesse. A palavra é a mesma, e a coisa é outra. Veja <a href="palavras-em-disputa.html">palavras em disputa</a>.</p>
<h2>Pragmatismo não substitui valores</h2>
<p>“Funciona” é uma resposta incompleta até que se diga <strong>funciona para quê, e para quem</strong>. Uma política pode funcionar muito bem para reduzir o déficit e muito mal para quem perde o atendimento. O pragmatismo é a segunda etapa do raciocínio que a lição sobre <a href="valores-e-decisoes.html">valores e decisões</a> apresenta: depois de decidir o que se quer, buscar com honestidade o que realiza isso. Pular a primeira etapa não torna ninguém neutro. Torna a pessoa refém de quem definiu os objetivos por ela.</p>
<p>Por isso, o pragmático sério tem linhas que não cruza: direitos básicos, regras da democracia, verdade sobre os fatos. Essas linhas não são falta de pragmatismo. São o que impede que ele vire o vale-tudo que a tabela descreve. Veja <a href="testar-visao-moral.html">como testar sua visão moral</a>.</p>
<h2>As críticas</h2>
<ul>
<li><strong>Da esquerda e da direita ideológicas:</strong> o pragmatismo seria a aceitação do mundo como ele é, e grandes mudanças, como a abolição, não vieram de quem só aceitava o possível. A resposta pragmática é que a abolição também foi conquistada por etapas, leis e acordos, e não só por proclamações.</li>
<li><strong>Dos filósofos:</strong> “o que funciona” pode esconder uma teoria da verdade frouxa, em que o útil se confunde com o verdadeiro. Um fato continua sendo fato mesmo quando é inconveniente.</li>
<li><strong>Do próprio Weber:</strong> a responsabilidade pelas consequências pode virar desculpa para tudo, se não houver convicção por trás.</li>
</ul>
<h2>Como praticar</h2>
<ol class="roteiro"><li><strong>Escreva o que você quer</strong>, antes de discutir como. Isso é o que não está em negociação.</li><li><strong>Avalie cada proposta pelo mérito e pela viabilidade</strong>, separados.</li><li><strong>Pergunte “funciona para quem?”</strong>, e inclua quem não está na mesa.</li><li><strong>Prefira o que pode ser medido e desfeito.</strong></li><li><strong>Aceite acordos que avançam</strong>, e recuse os que só mantêm você no jogo.</li><li><strong>Diga quais são seus limites</strong>, em voz alta e antes de precisar deles.</li></ol>
<div class="nota"><strong>Para guardar:</strong> pragmatismo é teimosia nos fins e flexibilidade nos meios. Quando a flexibilidade chega aos fins, o nome certo é outro.</div>
''', fontes=[('Pragmatismo (Wikipédia)', 'https://pt.wikipedia.org/wiki/Pragmatismo'), ('A política como vocação (Wikipédia)', 'https://pt.wikipedia.org/wiki/A_Pol%C3%ADtica_como_Voca%C3%A7%C3%A3o'), ('John Dewey (Wikipédia)', 'https://pt.wikipedia.org/wiki/John_Dewey'), ('A Sociedade Aberta e Seus Inimigos', 'https://pt.wikipedia.org/wiki/A_Sociedade_Aberta_e_Seus_Inimigos'), ('Deng Xiaoping (Wikipédia)', 'https://pt.wikipedia.org/wiki/Deng_Xiaoping'), ('Fisiologismo (Wikipédia)', 'https://pt.wikipedia.org/wiki/Fisiologismo')]),
]
META_REVISAO['pragmatismo-politico'] = (['etica', 'democracia'], ('Para Weber, a ética da responsabilidade pede que o político…', ['Siga a convicção sem olhar as consequências', 'Responda pelas consequências previsíveis das suas escolhas', 'Faça o que der mais votos'], 1, 'Weber queria as duas: convicção firme e responsabilidade pelos resultados. Só a segunda vira vale-tudo; só a primeira vira pureza inútil.'))
REFORCO_REVISAO['pragmatismo-politico'] = dict(
 analogia='Um velejador tem o porto definido e não discute isso com o vento. Mas ajusta a vela, muda o ângulo e às vezes faz zigue-zague para chegar. Pragmatismo é isso: firme no destino, flexível na rota. Quem muda de porto a cada rajada não está velejando, está à deriva.',
 crianca='Você quer que a turma toda brinque junto. Se um jogo não funciona, você tenta outro, sem desistir da ideia de incluir todo mundo. Isso é ser pragmático. Agora, se você trocar a ideia de incluir todos só para ganhar, aí não é mais pragmatismo, é só querer vencer.')
GRUPOS['pragmatismo-politico'] = 'Melhorar a democracia'

# ---------- lições acrescentadas em 2026-11-04: outsiders e mandatos coletivos ----------
OUTSIDER = dict(slug='perigo-do-outsider', grupo=PI, titulo='O mito do outsider', resumo='“Não sou político” virou a promessa mais vendida das eleições. O que é um outsider de verdade, por que ele atrai, o que costuma acontecer depois e as perguntas que separam renovação de marketing.', corpo='''
<p class="abre">A cada eleição aparece alguém que se apresenta como gente de fora: o empresário, o apresentador, o juiz, o influenciador, o militar. A promessa é sempre a mesma: “não sou político, por isso não tenho os vícios deles”. Às vezes é verdade. Com frequência, é só a frase mais eficiente do marketing eleitoral, e a falta de experiência é vendida como se fosse uma qualidade.</p>
<h2>O que é um outsider</h2>
<p>Na ciência política, outsider é quem chega a um cargo alto sem ter feito carreira em partidos ou em cargos eletivos. O oposto é o <em>insider</em>, que subiu degrau por degrau. Entre os dois há uma faixa cinzenta, em que vive a maior parte dos “outsiders” de campanha.</p>
<table><thead><tr><th>Tipo</th><th>Quem é</th><th>Exemplos</th></tr></thead><tbody>
<tr><td><strong>Outsider de fato</strong></td><td>Nunca disputou nem exerceu cargo antes de chegar ao topo</td><td><a href="mundo/volodymyr-zelensky.html">Volodymyr Zelensky</a>, ator, eleito presidente da Ucrânia em 2019; Alberto Fujimori, reitor, eleito no Peru em 1990; <a href="mundo/donald-trump.html">Donald Trump</a>, empresário, eleito em 2016</td></tr>
<tr><td><strong>Outsider de dentro</strong></td><td>Tem carreira política, mas se vende como estranho ao sistema</td><td>Jair Bolsonaro, 28 anos de Câmara; <a href="politicos/fernando-collor.html">Fernando Collor</a>, governador e herdeiro de uma oligarquia de Alagoas; <a href="mundo/emmanuel-macron.html">Emmanuel Macron</a>, ministro que fundou o próprio movimento</td></tr>
<tr><td><strong>Celebridade convertida</strong></td><td>Fama em outra área usada como capital político</td><td><a href="politicos/pablo-marcal.html">Pablo Marçal</a>, coach, em São Paulo, 2024; <a href="mundo/javier-milei.html">Javier Milei</a>, economista de TV, na Argentina, 2023; Jânio Quadros, com a vassoura, em 1960</td></tr>
</tbody></table>
<p>Nenhuma dessas categorias é, por si, boa ou ruim. O que a tabela mostra é que “não sou político” costuma ser slogan, e não biografia. Vale conferir a ficha antes de acreditar na frase.</p>
<h2>Por que o outsider atrai</h2>
<ul>
<li><strong>Os partidos perderam a confiança.</strong> Quando o eleitor acha que são todos iguais, quem não é de nenhum parece a única opção limpa. Veja <a href="o-que-e-um-partido.html">para que servem os partidos</a>.</li>
<li><strong>Corrupção e escândalos</strong> transformam experiência em suspeita: quem esteve lá dentro “deve ter se sujado”.</li>
<li><strong>A antipolítica</strong> promete resolver problemas “com gestão” ou “com bom senso”, sem a negociação lenta que a democracia exige.</li>
<li><strong>As redes dispensam a estrutura.</strong> Antes, era preciso partido, tempo de TV e militância para ser conhecido. Hoje, um perfil com milhões de seguidores substitui parte disso.</li>
<li><strong>Os porteiros falharam.</strong> Steven Levitsky e Daniel Ziblatt mostram que, por décadas, os partidos barraram candidatos despreparados ou perigosos. Quando deixaram de filtrar, outsiders passaram a chegar direto ao topo.</li>
</ul>
<h2>O que costuma acontecer depois</h2>
<table><thead><tr><th>Caso</th><th>O que aconteceu</th></tr></thead><tbody>
<tr><td><strong>Jânio Quadros</strong>, Brasil, 1960</td><td>Eleito com a vassoura contra a corrupção, renunciou sete meses depois, sem base no Congresso, e abriu a crise que levou ao golpe de 1964</td></tr>
<tr><td><strong>Fernando Collor</strong>, Brasil, 1989</td><td>“Caçador de marajás”, de um partido criado para a eleição. Confiscou a poupança, perdeu o apoio e sofreu impeachment em 1992</td></tr>
<tr><td><strong>Alberto Fujimori</strong>, Peru, 1990</td><td>Venceu um escritor famoso como o “desconhecido”. Dois anos depois, fechou o Congresso em um autogolpe. Governou dez anos e foi condenado por crimes contra a humanidade</td></tr>
<tr><td><strong>Donald Trump</strong>, EUA, 2016</td><td>Governou em conflito com o próprio partido e as instituições, e não aceitou a derrota de 2020. Foi reeleito em 2024</td></tr>
<tr><td><strong>Volodymyr Zelensky</strong>, Ucrânia, 2019</td><td>Eleito contra a corrupção, virou líder de guerra em 2022, com apoio amplo. O balanço ainda está em aberto</td></tr>
<tr><td><strong>Javier Milei</strong>, Argentina, 2023</td><td>Sem bancada própria, governa por decreto e por acordos com os partidos que atacava, com inflação em queda e custo social alto</td></tr>
</tbody></table>
<p>O padrão não é “outsider sempre dá errado”. É outro: quem chega sem partido, sem bancada e sem equipe descobre que não consegue governar sozinho, e tem dois caminhos. Ou negocia com a “velha política” que prometeu destruir, ou ataca as instituições que o limitam. No Brasil, o primeiro caminho tem nome: veja o <a href="presidencialismo-de-coalizao.html">presidencialismo de coalizão</a>.</p>
<h2>Os perigos</h2>
<ul>
<li><strong>Inexperiência vendida como virtude.</strong> Em qualquer outro emprego, nunca ter feito o trabalho é uma desvantagem. Governar um país é um dos trabalhos mais difíceis que existem.</li>
<li><strong>Sem partido, sem freio interno.</strong> O partido também é quem diz “não” ao líder. O outsider costuma criar uma legenda de aluguel ou um movimento que só obedece a ele.</li>
<li><strong>Da antipolítica ao ataque às instituições.</strong> Quem foi eleito contra “o sistema” tende a tratar Congresso, Justiça e imprensa como parte do problema quando eles o contrariam. Veja o <a href="perigo-de-questionar-a-democracia.html">perigo de questionar a democracia</a>.</li>
<li><strong>Personalismo.</strong> O outsider é, por definição, uma pessoa e não um programa. É a porta de entrada mais comum do <a href="perigo-do-messianismo.html">messianismo</a>.</li>
<li><strong>Simplificação.</strong> “É só ter vontade” e “é só gestão” escondem a complexidade de cada problema. Veja o <a href="perigo-do-maniqueismo.html">perigo de simplificar</a>.</li>
<li><strong>Quem está por trás.</strong> Toda campanha sem partido tem financiadores e estrategistas. Quem não os mostra, esconde.</li>
</ul>
<h2>O que há de legítimo</h2>
<p>Partidos fechados, carreiras de quarenta anos e cúpulas que escolhem candidatos entre si produzem a demanda por gente de fora. Renovação é saudável, e muitos outsiders trouxeram pautas que ninguém defendia e eleitores que ninguém ouvia. O problema não é vir de fora. É vender a falta de experiência como qualidade, não dizer como pretende governar e tratar as regras como coisa de político.</p>
<table><thead><tr><th>Renovação de verdade</th><th>Marketing de outsider</th></tr></thead><tbody>
<tr><td>Tem equipe, plano e aliados nomeados</td><td>“Eu resolvo”, sem dizer com quem</td></tr>
<tr><td>Explica o que fez antes, inclusive fora da política</td><td>Apaga o passado, ou o passado político</td></tr>
<tr><td>Aceita as regras e os limites do cargo</td><td>Promete o que o cargo não pode fazer. Veja <a href="cargos.html">o que cada cargo faz</a></td></tr>
<tr><td>Critica práticas específicas</td><td>Ataca “os políticos” em bloco, e logo entra em um partido deles</td></tr>
<tr><td>Vai para dentro de um partido e disputa nele</td><td>Cria uma sigla de aluguel ou troca de partido a cada eleição</td></tr>
</tbody></table>
<h2>Perguntas antes de votar em um outsider</h2>
<ol class="roteiro">
<li><strong>O que ele fez na vida?</strong> Empresa, carreira ou fama dizem algo sobre como lida com dinheiro, pessoas e regras.</li>
<li><strong>Com quem vai governar?</strong> Sem bancada, de quem virão os votos no Congresso ou na Câmara?</li>
<li><strong>Quem é a equipe?</strong> Um bom governo são centenas de pessoas, não uma.</li>
<li><strong>Quem financia e quem aconselha?</strong> Consulte o <a href="https://divulgacandcontas.tse.jus.br/" target="_blank" rel="noopener">DivulgaCandContas</a>.</li>
<li><strong>Ele aceita perder?</strong> O que disse sobre urnas, tribunais e imprensa quando foi contrariado?</li>
<li><strong>A mudança é de pessoas ou de práticas?</strong> Trocar o nome e manter o método não é renovação.</li>
</ol>
<div class="nota"><strong>Para guardar:</strong> “não sou político” é uma informação sobre o currículo, não sobre o caráter. Quem vai ocupar um cargo político se torna político no primeiro dia. A pergunta é que tipo de político vai ser, e isso se descobre olhando o que a pessoa já fez, e não o que ela diz que não é.</div>
''', fontes=[('Como as democracias morrem', 'https://pt.wikipedia.org/wiki/How_Democracies_Die'), ('The Rise of Outsiders in Latin America, 1980-2010 (Miguel Carreras)', 'https://www.google.com/search?tbm=bks&q=Carreras+The+Rise+of+Outsiders+in+Latin+America'), ('Fernando Collor (Wikipédia)', 'https://pt.wikipedia.org/wiki/Fernando_Collor'), ('Alberto Fujimori (Wikipédia)', 'https://pt.wikipedia.org/wiki/Alberto_Fujimori'), ('Jânio Quadros (Wikipédia)', 'https://pt.wikipedia.org/wiki/J%C3%A2nio_Quadros'), ('Antipolítica (Wikipédia)', 'https://pt.wikipedia.org/wiki/Antipol%C3%ADtica')])
META_REVISAO['perigo-do-outsider'] = (['perigos', 'eleicoes'], ('O que costuma acontecer com um outsider eleito sem partido e sem bancada?', ['Governa sozinho, como prometeu', 'Precisa negociar com os partidos que atacava, ou passa a atacar as instituições', 'Perde o cargo automaticamente'], 1, 'Sem base, ninguém governa. Os dois caminhos mais comuns são o acordo com a “velha política” e o conflito com quem o limita.'))
REFORCO_REVISAO['perigo-do-outsider'] = dict(
 analogia='É como contratar para pilotar o avião alguém cuja principal qualidade é nunca ter sido piloto, porque “os pilotos estão todos viciados”. Pode até ser uma pessoa ótima. Mas o avião continua exigindo saber pilotar, e, na primeira turbulência, ou ela chama um piloto de verdade ou culpa a torre de controle.',
 crianca='Imagine que alguém quer ser o capitão do time dizendo: “eu nunca joguei futebol, por isso não tenho os vícios dos jogadores”. Pode ser uma pessoa legal, mas o jogo continua sendo futebol. Antes de escolher, vale perguntar o que ela sabe fazer e com quem vai jogar.')
GRUPOS['perigo-do-outsider'] = PI

COLETIVO = dict(slug='mandatos-coletivos', grupo='Melhorar a democracia', titulo='Candidaturas coletivas e mandatos compartilhados', resumo='Um grupo se candidata junto, mas só uma pessoa tem o mandato na lei. O que é, de onde veio, o que promete, os riscos e como avaliar um mandato coletivo.', corpo='''
<p class="abre">Em uma candidatura coletiva, um grupo de pessoas disputa a eleição junto e promete exercer o mandato em conjunto. Na urna e na lei, porém, só uma delas é a candidata: as outras são “cocandidatas” por um acordo político, sem cargo nem voto na Câmara. É uma inovação brasileira recente, que tenta resolver um problema real de representação, e que ainda não tem regra própria.</p>
<h2>Como funciona na prática</h2>
<ol class="passos">
<li><strong>Uma pessoa registra a candidatura</strong> no TSE, como qualquer outra. É a titular: só ela aparece na lista de eleitos, vota no plenário e responde perante a lei.</li>
<li><strong>O grupo assina um compromisso</strong>, em geral público, com as regras do mandato: como as decisões são tomadas, como os votos em plenário são definidos, como se divide o salário e o que acontece se alguém sair.</li>
<li><strong>Os demais entram no gabinete</strong>, muitas vezes como assessores pagos com a verba de gabinete, e dividem o trabalho: projetos, emendas, atendimento, articulação.</li>
<li><strong>As decisões são coletivas</strong> por acordo, mas a palavra final, na lei, é sempre da titular. Se ela discordar do grupo, nada a obriga.</li>
</ol>
<h2>De onde veio</h2>
<table><thead><tr><th>Quando</th><th>O que aconteceu</th></tr></thead><tbody>
<tr><td>2002</td><td>Na Suécia, o partido Demoex elege um vereador em Vallentuna que votava conforme decisões online dos filiados. Na Argentina, o Partido de la Red (2013) propôs o mesmo</td></tr>
<tr><td>2016</td><td>Em Alto Paraíso de Goiás, um vereador é eleito com o compromisso de decidir junto com um grupo de moradores: é considerado o primeiro mandato coletivo do Brasil</td></tr>
<tr><td>2018</td><td>A Bancada Ativista elege uma deputada estadual em São Paulo com nove cocandidatas, e as Juntas elegem uma deputada em Pernambuco com cinco. As duas entram em assembleias legislativas</td></tr>
<tr><td>2020</td><td>Centenas de candidaturas coletivas disputam as eleições municipais, e algumas vencem em capitais, em geral ligadas a mulheres, pessoas negras, periferias e pessoas LGBT</td></tr>
<tr><td>2022 e 2024</td><td>O modelo se repete nas eleições estaduais e municipais, com rachas públicos em alguns mandatos e a continuidade de outros</td></tr>
</tbody></table>
<h2>O que diz a lei</h2>
<p>Nada, até agora. A legislação eleitoral só conhece a candidatura individual. O TSE já afirmou que o mandato pertence a quem foi registrado e que o coletivo é um arranjo político, sem efeito jurídico. Uma proposta de emenda à Constituição apresentada em 2017 na Câmara tenta reconhecer o mandato compartilhado, mas não foi votada. Enquanto isso, cada tribunal regional decide caso a caso sobre o uso de nomes coletivos na urna.</p>
<h2>O que promete</h2>
<ul>
<li><strong>Mais gente representada.</strong> Uma cadeira pode levar ao parlamento várias trajetórias: uma mulher negra da periferia, uma pessoa trans, um morador de rua, um agricultor. Veja o <a href="debates/representatividade.html">debate sobre representatividade</a>.</li>
<li><strong>Menos personalismo.</strong> A decisão é do grupo, e não de um nome. É uma resposta ao <a href="perigo-do-messianismo.html">messianismo</a> e ao <a href="perigo-do-outsider.html">culto à pessoa</a>.</li>
<li><strong>Campanha mais barata.</strong> Grupos sem dinheiro dividem o custo e a exposição de uma única candidatura.</li>
<li><strong>Mais trabalho feito.</strong> Várias pessoas com mandato político, e não só uma, acompanham comissões, bairros e pautas.</li>
<li><strong>Transparência interna.</strong> Os melhores mandatos publicam suas regras e suas decisões, o que poucos gabinetes tradicionais fazem.</li>
</ul>
<h2>Os riscos</h2>
<ul>
<li><strong>Insegurança jurídica.</strong> Quem responde por um voto errado ou por um gasto irregular é só a titular. Os demais não podem ser cobrados pelo eleitor nem pela Justiça.</li>
<li><strong>Quando o grupo racha, a cadeira fica com uma pessoa.</strong> Já houve rompimentos públicos em mandatos coletivos, e o eleitor que votou no grupo descobriu que tinha votado em um nome.</li>
<li><strong>O eleitor pode não saber em quem está votando.</strong> Quem decide de fato: o grupo, a titular ou um partido?</li>
<li><strong>Pode ser só marketing.</strong> Um candidato com “cocandidatos” que são, na prática, assessores comuns usa a ideia sem o conteúdo.</li>
<li><strong>Dinheiro público para o grupo.</strong> Pagar os cocandidatos com verba de gabinete é legal, porque são assessores, mas críticos veem aí um uso da estrutura pública para sustentar um projeto eleitoral.</li>
<li><strong>Diluição da responsabilidade.</strong> Se a decisão foi “do coletivo”, ninguém errou. A responsabilização individual é uma das proteções da democracia representativa.</li>
</ul>
<h2>Um debate em aberto</h2>
<table><thead><tr><th>A favor de regulamentar</th><th>Contra, ou com cautela</th></tr></thead><tbody>
<tr><td>Dar segurança jurídica ao que já existe na prática</td><td>A Constituição liga o mandato à pessoa eleita, e mudar isso afeta todo o sistema</td></tr>
<tr><td>Ampliar a representação de grupos sub-representados</td><td>Grupos podem ser representados por partidos, listas e cotas, sem dividir uma cadeira</td></tr>
<tr><td>Reduzir o personalismo</td><td>O eleitor precisa saber quem responde por cada voto</td></tr>
<tr><td>Experimentar formas novas de democracia</td><td>Experimentos devem ser avaliados antes de virar regra. Veja <a href="politicas-baseadas-em-evidencias.html">políticas baseadas em evidências</a></td></tr>
</tbody></table>
<h2>Como avaliar um mandato coletivo</h2>
<ol class="roteiro">
<li><strong>As regras do grupo são públicas?</strong> Como decidem, e o que acontece em caso de divergência?</li>
<li><strong>Quem é a titular, e o que ela fez antes?</strong> Na lei, é nela que você vota.</li>
<li><strong>Os cocandidatos têm trajetória própria</strong>, ou são nomes de preenchimento?</li>
<li><strong>Como votou o mandato</strong> nas pautas decisivas? Veja <a href="numero-de-projetos.html">o que olhar em um mandato</a>.</li>
<li><strong>O coletivo presta contas</strong> do que fez e de como gastou a verba de gabinete?</li>
</ol>
<div class="nota"><strong>Para guardar:</strong> o mandato coletivo é uma promessa política apoiada em uma cadeira individual. Vale pelo que o grupo faz, e não pela ideia. Ele compartilha o trabalho; a responsabilidade, por enquanto, a lei não deixa compartilhar. Veja outras <a href="melhorar-a-democracia.html">ideias para melhorar a democracia</a>.</div>
''', fontes=[('Mandato coletivo (Wikipédia)', 'https://pt.wikipedia.org/wiki/Mandato_coletivo'), ('Candidatura coletiva (Wikipédia)', 'https://pt.wikipedia.org/wiki/Candidatura_coletiva'), ('Bancada Ativista (Wikipédia)', 'https://pt.wikipedia.org/wiki/Bancada_Ativista'), ('RAPS: Rede de Ação Política pela Sustentabilidade', 'https://www.raps.org.br/'), ('Demoex (Wikipédia)', 'https://en.wikipedia.org/wiki/Demoex')])
META_REVISAO['mandatos-coletivos'] = (['democracia', 'eleicoes'], ('Em uma candidatura coletiva, quem tem o mandato perante a lei?', ['Todo o grupo, em partes iguais', 'Só a pessoa registrada como candidata', 'O partido'], 1, 'A lei só conhece a candidatura individual. O coletivo é um compromisso político, sem efeito jurídico.'))
REFORCO_REVISAO['mandatos-coletivos'] = dict(
 analogia='É como uma banda que se inscreve em um festival que só aceita artistas solo. Um músico assina o contrato e recebe o cachê, e o grupo combina entre si como dividir tudo e decidir o repertório. Enquanto a banda se entende, funciona. Se brigar, quem assinou fica com o palco.',
 crianca='Imagine que só uma criança pode ser a representante da turma, mas ela combina com quatro amigos que vão decidir tudo juntos. Isso pode ser ótimo, porque mais gente participa. Mas, se os amigos discordarem, quem foi escolhida é quem decide, porque foi nela que a turma votou.')
GRUPOS['mandatos-coletivos'] = 'Melhorar a democracia'

# ---------- biblioteca: seção sobre vertentes e figuras (2026-11-04) ----------
# Livros já cadastrados que mudam para a seção "Sobre vertentes e figuras".
RENIVEL = {
 'O Negócio do Jair: a história proibida do clã Bolsonaro': 'Vertentes',
 'Jornalismo Wando: os personagens bizarros que explicam a nova política': 'Vertentes',
 'A Elite do Atraso: da escravidão a Bolsonaro': 'Vertentes',
 'Cartografia da extrema direita': 'Vertentes',
 'Mulheres e extrema direita no Brasil': 'Vertentes',
 'O Populismo Reacionário': 'Vertentes',
 'A Extrema Direita Hoje': 'Vertentes',
}
# Livros novos da seção: (título, autor, descrição). O link é gerado no build.
LIVROS_VERTENTES = [
 ('Os Sentidos do Lulismo: reforma gradual e pacto conservador', 'André Singer', 'A análise que deu nome ao lulismo: redução da pobreza sem confronto com o capital, e a base entre os mais pobres.'),
 ('O Brasil Dobrou à Direita: uma radiografia da eleição de Bolsonaro em 2018', 'Jairo Nicolau', 'Quem votou em quem, e por quê, na eleição que consolidou o antipetismo como força eleitoral.'),
 ('A Organização: a Odebrecht e o esquema de corrupção que chocou o mundo', 'Malu Gaspar', 'Reportagem sobre a maior empreiteira do país e as propinas pagas a políticos de vários partidos.'),
 ('A Privataria Tucana', 'Amaury Ribeiro Jr.', 'Investigação sobre as privatizações do governo FHC. Contestada pelos citados, e vale ler junto com as respostas.'),
 ('O Cadete e o Capitão: a vida de Jair Bolsonaro no quartel', 'Luiz Maklouf Carvalho', 'Reportagem sobre os anos de Bolsonaro no Exército, com documentos dos processos militares.'),
 ('A Miséria do Estado', 'Denis Rosenfield', 'Crítica liberal, de um filósofo ligado ao pensamento liberal-conservador, ao crescimento do Estado e ao patrimonialismo brasileiro.'),
]
