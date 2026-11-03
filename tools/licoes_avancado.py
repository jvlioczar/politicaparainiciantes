"""Lições do nível Avançado."""
from licoes_iniciante import VINDING
ALTHAUS = ('Reducing long-term risks from malevolent actors (2020)', 'https://longtermrisk.org/reducing-long-term-risks-from-malevolent-actors/')
FANAT = ('Long-term risks from ideological fanaticism (2026)', 'https://www.lesswrong.com/posts/sFewetPnb8KJgcER7/long-term-risks-from-ideological-fanaticism-1')

AVANCADO = [
dict(slug='atores-malevolentes', grupo='Quem chega ao poder', titulo='Atores malevolentes e a Tétrade Sombria', resumo='Narcisismo, maquiavelismo, psicopatia e sadismo: quando traços sombrios chegam ao poder.', corpo='''
<p class="abre">Parte dos piores danos políticos da história veio de pessoas com traços de personalidade específicos, que chegaram a posições de enorme poder. A pesquisa chama esse conjunto de Tétrade Sombria.</p>
<table><thead><tr><th>Traço</th><th>Descrição</th><th>Na política</th></tr></thead><tbody>
<tr><td>Narcisismo</td><td>Grandiosidade, necessidade de admiração, fragilidade à crítica</td><td>Culto à imagem; culpa sempre é dos outros</td></tr>
<tr><td>Maquiavelismo</td><td>Manipulação calculada, os outros como meios</td><td>Mentira estratégica e alianças descartáveis</td></tr>
<tr><td>Psicopatia</td><td>Falta de empatia e de remorso, impulsividade</td><td>Indiferença às vítimas das próprias decisões</td></tr>
<tr><td>Sadismo</td><td>Prazer no sofrimento alheio</td><td>Crueldade como política e espetáculo</td></tr>
</tbody></table>
<p>O populismo não é um traço de personalidade, e sim um estilo político (“povo puro contra elite corrupta”, com o líder como voz do povo). Combinado a esses traços, pode ser explosivo, porque oferece a quem os tem uma justificativa para atacar limites institucionais.</p>
<h2>O argumento</h2>
<p>David Althaus e Tobias Baumann propõem reduzir a influência de atores malevolentes no longo prazo. A linha é próxima do trabalho de Magnus Vinding e Tobias Baumann, cofundadores do Center for Reducing Suffering, que colocam a redução de riscos de sofrimento extremo no centro. A preocupação é que esses traços parecem super-representados em cargos de poder, e tecnologias futuras dariam a essas pessoas ainda mais poder.</p>
<h2>Como evitar</h2>
<ul><li><strong>Limites de poder:</strong> mandatos, freios e contrapesos e imprensa livre valem mais do que escolher a pessoa certa.</li><li><strong>Avaliar conduta:</strong> crueldade, mentira persistente e desprezo pela lei devem pesar mais do que carisma.</li><li><strong>Filtros partidários:</strong> partidos sérios são a primeira barreira, como lembram Levitsky e Ziblatt.</li><li><strong>Pesquisa:</strong> medidas mais difíceis de manipular; a proposta é controversa.</li></ul>
<div class="nota alerta"><strong>Cautela:</strong> ninguém diagnostica à distância. Psiquiatras têm regras contra isso, e “psicopata” virou xingamento fácil. Avalie condutas públicas. E lembre-se: a própria ideia de “filtrar líderes” poderia ser usada para perseguir adversários.</div>
''', fontes=[ALTHAUS, ('Center for Reducing Suffering', 'https://centerforreducingsuffering.org/'), ('Tétrade Sombria (Wikipédia)', 'https://en.wikipedia.org/wiki/Dark_triad')]),

dict(slug='fanatismo-ideologico', grupo='Quem chega ao poder', titulo='Fanatismo ideológico no longo prazo', resumo='Por que certa combinação de certeza absoluta e crueldade pode ser o grande risco do futuro.', corpo='''
<p class="abre">Em 2026, David Althaus e colegas publicaram uma análise longa sobre fanatismo ideológico. A tese: esse fanatismo foi motor de várias das piores atrocidades, e pode ser ainda mais perigoso com tecnologia avançada.</p>
<h2>Do que se trata</h2>
<p>Os autores tratam-no como um contínuo. As características centrais são pensamento em preto e branco, certeza dogmática, ódio aos de fora e disposição à violência. Formas leves estão próximas de fenômenos humanos comuns.</p>
<h2>Os argumentos</h2>
<ul>
<li><strong>Passado:</strong> estimam que foi motor importante de oito das dez maiores atrocidades desde 1800, entre elas a Segunda Guerra e os regimes de Stálin, Mao e Hitler.</li>
<li><strong>Presente:</strong> movimentos desse tipo controlam hoje uma fração pequena do PIB mundial, e têm dificuldade para formar coalizões amplas e entender o mundo com precisão.</li>
<li><strong>Futuro:</strong> a preocupação é a combinação com IA e outras tecnologias poderosas, que permitiriam consolidar regimes por muito tempo.</li>
</ul>
<h2>O que isso muda para a política comum</h2>
<p>O texto sugere que o ambiente de ideias importa: valorizar a dúvida, o pluralismo e as instituições. Isso liga a discussão ao <a href="vieses-cognitivos.html">raciocínio motivado</a> e ao <a href="perigo-do-fanatismo.html">perigo do fanatismo</a> do dia a dia.</p>
<p class="legenda">Trata-se de um ensaio em fórum de pesquisa, com estimativas assumidamente incertas, não de um artigo revisado por pares.</p>
''', fontes=[FANAT, ('Versão no EA Forum', 'https://forum.effectivealtruism.org/posts/EDBQPT65XJsgszwmL/long-term-risks-from-ideological-fanaticism')]),

dict(slug='direta-ou-epistocracia', grupo='Melhorar a democracia', titulo='Democracia direta × epistocracia', resumo='Dar mais poder a todos, ou mais peso a quem sabe mais? Duas respostas opostas à crise da representação.', corpo='''
<p class="abre">As duas propostas partem da insatisfação com a democracia representativa, mas caminham em direções opostas.</p>
<table><thead><tr><th></th><th>Democracia direta</th><th>Epistocracia</th></tr></thead><tbody>
<tr><td>Ideia</td><td>Cidadãos decidem temas importantes sem intermediários</td><td>Quem tem mais conhecimento político tem mais peso</td></tr>
<tr><td>Quem defende</td><td>Tradição participativa, Suíça como exemplo</td><td>Jason Brennan, em <em>Against Democracy</em></td></tr>
<tr><td>A favor</td><td>Legitimidade, menos captura por elites</td><td>Eleitores são desinformados e decisões têm vítimas</td></tr>
<tr><td>Contra</td><td>Temas complexos em plebiscito, manipulação, risco a minorias, como no Brexit</td><td>Quem decide quem sabe? Testes foram usados para excluir negros nos EUA; o conhecimento é desigual por classe e raça; especialistas têm vieses</td></tr>
</tbody></table>
<h2>Caminhos do meio</h2>
<ul>
<li><strong>Assembleias de cidadãos:</strong> pessoas sorteadas estudam um tema e deliberam. A Irlanda usou esse modelo para temas como casamento igualitário e aborto, depois levados a referendo.</li>
<li><strong>Democracia líquida:</strong> você vota diretamente ou delega seu voto.</li>
<li><strong>Democracia deliberativa:</strong> James Fishkin testa sondagens em que as pessoas mudam de opinião após estudar.</li>
<li><strong>Informação melhor:</strong> agências independentes de avaliação, sem retirar o voto de ninguém.</li>
</ul>
<div class="nota">O consenso é escasso. O risco histórico de excluir pessoas do voto é real, e talvez o caminho mais seguro seja qualificar a informação de todos, em vez de tirar poder de alguns.</div>
''', fontes=[('Against Democracy', 'https://en.wikipedia.org/wiki/Against_Democracy'), ('Democracia direta (Wikipédia)', 'https://pt.wikipedia.org/wiki/Democracia_direta'), VINDING]),

dict(slug='melhorar-a-democracia', grupo='Melhorar a democracia', titulo='Ideias para melhorar a democracia', resumo='Voto preferencial, direitos universais, cosmopolitismo, evidências. Um cardápio com prós e contras.', corpo='''
<p class="abre">Democracia não é um objeto pronto. As regras podem mudar, e algumas mudanças alteram o tipo de político que vence.</p>
<table><thead><tr><th>Ideia</th><th>O que é</th><th>A favor</th><th>Contra</th></tr></thead><tbody>
<tr><td>Voto preferencial</td><td>Você ordena os candidatos</td><td>Reduz o “voto útil” e premia quem é aceitável para muitos</td><td>Mais complexo de explicar</td></tr>
<tr><td>Voto por aprovação</td><td>Você marca todos que aceita</td><td>Simples; favorece moderados</td><td>Pouco testado em grandes eleições</td></tr>
<tr><td>Distrital misto</td><td>Metade por distrito, metade por lista</td><td>Aproxima eleitor e representante</td><td>Pode fortalecer caciques locais</td></tr>
<tr><td>Sorteio cívico</td><td>Cidadãos sorteados deliberam</td><td>Representa quem nunca se candidataria</td><td>Falta de experiência e de responsabilização</td></tr>
<tr><td>Políticas baseadas em evidências</td><td>Avaliar antes e depois</td><td>Menos dinheiro em ideias que não funcionam</td><td>Dados têm limite e não resolvem valores</td></tr>
<tr><td>Direitos universais</td><td>Direitos que nenhuma maioria pode tirar</td><td>Protegem minorias</td><td>Disputa sobre a lista de direitos e quem os interpreta</td></tr>
<tr><td>Cosmopolitismo</td><td>Instituições e deveres além das fronteiras</td><td>Clima, pandemias e guerra são globais</td><td>Distância do eleitor e risco de perda de soberania</td></tr>
<tr><td>Sencientismo</td><td>Representar os interesses de todos os seres sencientes</td><td>Inclui quem sofre e não vota</td><td>Difícil de desenhar; resistência cultural</td></tr>
<tr><td>Instituições de longo prazo</td><td>Comissões do futuro, metas de Estado</td><td>Corrige o imediatismo</td><td>Podem perder poder ou legitimidade</td></tr>
</tbody></table>
<h2>O que dá para fazer hoje</h2>
<p>Comece pelo que depende menos de reformas: educação midiática, dados abertos, votar nas eleições locais, participar de conselhos e fiscalizar.</p>
''', fontes=[VINDING, ('Voto preferencial (Wikipédia)', 'https://pt.wikipedia.org/wiki/Voto_preferencial'), ('Politize!', 'https://www.politize.com.br/')]),

dict(slug='politicas-baseadas-em-evidencias', grupo='Melhorar a democracia', titulo='Políticas baseadas em evidências', resumo='Tratar leis como hipóteses: testar, medir e corrigir. De onde vem a ideia, como funciona, seus limites e por que os políticos resistem.', corpo='''
<p class="abre">A ideia é simples: tratar políticas públicas como hipóteses. Em vez de adotar um programa porque soa bem, testá-lo, medir os resultados e manter o que funciona. O Nobel de Economia de 2019 premiou Banerjee, Duflo e Kremer por experimentos assim contra a pobreza.</p>
<div class="ajuda"><section class="analogia"><h3>Uma analogia</h3><p>Um remédio novo não chega à farmácia só porque o fabricante jura que é bom. Ele é testado: um grupo toma o remédio, outro não, e alguém compara os resultados. Se fizer mal, sai de cena. Leis e programas também afetam a vida de milhões de pessoas, mas muitas vezes são aplicados sem esse teste. Políticas baseadas em evidências tentam levar esse cuidado para o governo.</p></section><section class="crianca"><h3>Explicando para uma criança</h3><p>Sua turma quer saber se as plantas crescem mais com música. Vocês pegam vasos iguais, sorteiam quais ficam com música e cuidam de todos do mesmo jeito. Depois, medem. Assim ninguém precisa brigar sobre quem acha o quê: dá para olhar o resultado. Com as regras de uma cidade, os adultos podem fazer algo parecido. Só que as plantas não dizem o que é mais justo: isso ainda é preciso conversar.</p></section></div>
<h2>De onde vem a ideia</h2>
<table><thead><tr><th>Quando</th><th>O que aconteceu</th></tr></thead><tbody>
<tr><td>1747</td><td>O médico James Lind compara tratamentos entre marinheiros com escorbuto, e as frutas cítricas se destacam. É um marco inicial dos testes comparativos.</td></tr>
<tr><td>Anos 1960 e 1970</td><td>O psicólogo Donald Campbell defende, em “Reforms as Experiments” (1969), que reformas sociais sejam avaliadas como experimentos. Os EUA testam uma renda garantida com famílias reais.</td></tr>
<tr><td>1972</td><td>O médico Archie Cochrane critica, em <em>Effectiveness and Efficiency</em>, a falta de provas para muitos tratamentos.</td></tr>
<tr><td>Anos 1990</td><td>Surge o termo “medicina baseada em evidências”, e a Colaboração Cochrane passa a reunir os estudos em revisões sistemáticas.</td></tr>
<tr><td>1997</td><td>O México lança o Progresa, de transferência de renda, e o avalia com sorteio na ordem de entrada das comunidades. Foi o primeiro grande experimento de política social em um país de renda baixa ou média, e ajudou a espalhar esse tipo de programa.</td></tr>
<tr><td>1999</td><td>O governo Blair, no Reino Unido, adota o discurso de “o que importa é o que funciona” no documento <em>Modernising Government</em>. A expressão ganha o mundo. Na mesma época, nasce a Colaboração Campbell, para fazer nas políticas sociais o que a Cochrane fazia na saúde.</td></tr>
<tr><td>Anos 2000 e 2010</td><td>Surgem o J-PAL (2003), a rede britânica What Works e, nos EUA, a Evidence Act (2018).</td></tr>
<tr><td>2019 a 2021</td><td>No Brasil, o decreto 9.834/2019 cria o CMAP, conselho de monitoramento e avaliação. A Emenda Constitucional 109/2021 coloca a avaliação de políticas públicas entre as obrigações da administração pública.</td></tr>
</tbody></table>
<p>Ou seja: a ideia veio em boa parte da medicina, foi levada às ciências sociais e virou programa de governo. Isso explica sua força e também um dos debates: a sociedade é mais complicada do que um ensaio clínico.</p>
<h2>A hierarquia das evidências</h2>
<ol><li><strong>Revisões sistemáticas</strong> reúnem muitos estudos, inclusive os que não deram o resultado esperado.</li><li><strong>Experimentos aleatorizados:</strong> grupos sorteados recebem ou não a política. O sorteio torna os grupos parecidos, então a diferença tende a vir da política.</li><li><strong>Experimentos naturais:</strong> comparações aproveitando uma mudança real, como uma lei em um estado e não em outro.</li><li><strong>Correlações simples:</strong> úteis, mas não provam causa. Cidades com mais policiais podem ter mais crimes porque a polícia foi enviada a elas.</li><li><strong>Casos e opiniões:</strong> o nível mais fraco, ainda que ajudem a formular perguntas.</li></ol>
<p>A ordem é uma regra prática, e não uma lei. Um experimento natural bem feito pode valer mais que um experimento ruim, e para perguntas sobre por que algo acontece, entrevistas e estudos qualitativos são indispensáveis.</p>
<h2>O ciclo na prática</h2>
<ol class="passos"><li><strong>Definir o problema</strong> e o que seria sucesso, antes de começar.</li><li><strong>Ver o que já se sabe</strong> em outros lugares.</li><li><strong>Testar em escala menor</strong>, com grupo de comparação, quando for possível.</li><li><strong>Medir custos e efeitos</strong>, inclusive os indesejados.</li><li><strong>Publicar, mesmo se der errado.</strong></li><li><strong>Decidir:</strong> ampliar, ajustar ou encerrar.</li></ol>
<h2>Exemplos</h2>
<table><thead><tr><th>Caso</th><th>O que se aprendeu</th></tr></thead><tbody>
<tr><td><strong>Scared Straight</strong> (EUA)</td><td>Levar jovens para visitar presídios parecia óbvio, e o programa era popular. Revisões de experimentos concluíram que ele não reduz a criminalidade e pode até aumentá-la. A intuição estava errada.</td></tr>
<tr><td><strong>Progresa</strong> (México)</td><td>A avaliação sustentou a continuidade do programa mesmo após a troca de governo, e o modelo inspirou outros países.</td></tr>
<tr><td><strong>Bolsa Família</strong> (Brasil)</td><td>Um estudo na <em>The Lancet</em> (2013), com municípios, associou maior cobertura do programa a menos mortes de crianças, sobretudo por causas ligadas à pobreza, como a diarreia. Não foi um experimento com sorteio, e isso limita a certeza.</td></tr>
<tr><td><strong>Vermífugos</strong> (Quênia)</td><td>Um estudo famoso indicou que o tratamento melhorava a frequência escolar. Reanálises geraram a chamada “guerra dos vermes”. Um só estudo, por melhor que seja, raramente encerra a questão.</td></tr>
</tbody></table>
<h2>Os limites</h2>
<ul><li><strong>Valores:</strong> dados dizem o que acontece, não o que importa. Se um programa reduz o crime, mas fere direitos, a decisão continua sendo moral. Veja a <a href="etica-normativa.html">ética normativa</a>.</li><li><strong>Validade externa:</strong> o resultado em Minas pode não se repetir no Pará.</li><li><strong>Grandes mudanças:</strong> não dá para sortear uma constituição, um câmbio ou uma guerra.</li><li><strong>Longo prazo:</strong> os efeitos demoram a aparecer, e os testes costumam acabar antes.</li><li><strong>Ética:</strong> nem tudo pode virar experimento. Sortear costuma ser mais aceitável quando as vagas são escassas ou a implantação é gradual.</li><li><strong>O que se mede:</strong> o que é fácil de medir pode roubar a atenção do que importa.</li></ul>
<h2>As críticas</h2>
<ul><li><strong>Experimentos não são mágicos.</strong> Angus Deaton e Nancy Cartwright, em artigo de 2018, argumentam que o sorteio não garante, sozinho, conclusão confiável nem resultado aplicável a outro lugar.</li><li><strong>Tecnocracia.</strong> “A ciência mostra” pode encerrar debates que deveriam ser democráticos, e quem encomenda o estudo escolhe a pergunta.</li><li><strong>Foco no pequeno.</strong> É mais fácil testar um ajuste do que uma mudança estrutural, o que pode desviar a atenção de questões maiores, como poder e desigualdade.</li><li><strong>Falsa bala de prata.</strong> Uma sátira famosa no <em>BMJ</em> (2003) nota que nunca houve teste aleatorizado do paraquedas. Exigir sempre o padrão máximo pode ser absurdo.</li></ul>
<div class="nota alerta"><strong>Evidência baseada na política:</strong> o caminho inverso é decidir primeiro e encomendar depois o estudo que confirma. Desconfie quando só os resultados favoráveis aparecem. Por isso, muitos autores preferem falar em políticas <em>informadas</em> por evidências: os dados ajudam a decidir, mas não decidem sozinhos.</div>
<h2>Por que resistem</h2>
<p>Avaliar significa poder ser desmentido. Um programa querido pode não funcionar, o resultado costuma aparecer depois da eleição e encerrar um programa contraria quem depende dele. Avaliações independentes, públicas e obrigatórias ajudam, como as de órgãos como o Ipea. No Brasil, porém, pesquisadores do próprio Ipea ainda descreveram esse movimento como incipiente.</p>
<h2>Como cobrar isso de um político</h2>
<ol class="roteiro"><li>Que problema esta proposta resolve, e como saberemos se funcionou?</li><li>Onde já foi testada, e o que aconteceu?</li><li>Com o que foi comparada?</li><li>Quanto custa, e o que deixa de ser feito com esse dinheiro?</li><li>Quem vai avaliar, e o resultado será público?</li></ol>
<p>Use também o guia para <a href="comparar-projetos.html">comparar projetos</a>.</p>
''', fontes=[('21 afirmações sobre práticas baseadas em evidências', 'https://www.instagram.com/p/DfMp11CAC3G/'), ('Evidence-based policy (Wikipédia)', 'https://en.wikipedia.org/wiki/Evidence-based_policy'), ('Linha do tempo da avaliação de impacto (CGD)', 'https://www.cgdev.org/sites/default/files/impact-evaluation-timeline.pdf'), ('Donald T. Campbell (Wikipédia)', 'https://en.wikipedia.org/wiki/Donald_T._Campbell'), ('Archie Cochrane (Wikipédia)', 'https://en.wikipedia.org/wiki/Archie_Cochrane'), ('Cochrane: revisão sobre o Scared Straight', 'https://www.cochrane.org/evidence/CD002796_scared-straight-and-other-juvenile-awareness-programs-preventing-juvenile-delinquency'), ('Effect of a conditional cash transfer programme on childhood mortality (The Lancet, 2013)', 'https://doi.org/10.1016/S0140-6736(13)60715-1'), ('Worm wars (Wikipédia)', 'https://en.wikipedia.org/wiki/Worm_wars'), ('Understanding and misunderstanding randomized controlled trials (2018)', 'https://doi.org/10.1016/j.socscimed.2017.12.005'), ('Parachute use to prevent death and major trauma (BMJ)', 'https://www.bmj.com/content/327/7429/1459'), ('Ministério da Fazenda: CMAP e EC 109', 'https://www.gov.br/fazenda/pt-br/orgaos/secretaria-de-avaliacao-planejamento-energia-e-loteria/pdfs-webinar/2021-07-15-decisoes-baseadas-em-evidencias-app-gg.pdf'), ('J-PAL', 'https://www.povertyactionlab.org/'), ('Nobel de Economia de 2019', 'https://www.nobelprize.org/prizes/economic-sciences/2019/summary/'), ('Ipea', 'https://www.ipea.gov.br/'), VINDING]),

dict(slug='sencientismo', grupo='Quem conta', titulo='Inclusão moral e sencientismo', resumo='Se pode sofrer, conta. O círculo moral cresceu ao longo da história, e talvez não tenha terminado de crescer.', corpo='''
<p class="abre">Escravizados, mulheres e estrangeiros já ficaram fora do círculo de quem “conta”. Peter Singer chama esse processo de expansão do círculo. O sencientismo propõe o critério: <strong>quem pode sentir, conta</strong>.</p>
<p>Raça, sexo e espécie não mudam o fato de que dor é dor. Discriminar com base em espécie é chamado de especismo. A Declaração de Cambridge (2012) reconheceu que muitos animais possuem os substratos neurológicos da consciência, e a Declaração de Nova York (2024) ampliou o debate a mais grupos.</p>
<h2>O que isso faz com a política</h2>
<ul><li>Bilhões de animais vivem e morrem na pecuária industrial, com subsídios públicos.</li><li>Quem sofre e não vota fica sem representação: animais, bebês, futuras gerações.</li><li>Uma política inclusiva pensa em proteger todos os animais até onde os humanos e o Estado puderem alcançar.</li><li>Questões ambientais e de saúde também devem incluir os animais afetados por elas, e não apenas os humanos. Uma enchente, uma queimada ou uma epidemia atingem também quem não é humano, e isso exige uma visão politicamente inclusiva.</li></ul>
<h2>Ir além da espécie humana</h2>
<p>Humanos não são os únicos que têm interesses. Compartilhamos com muitos animais o interesse em não sentir dor nem medo, em viver, em ter comida e abrigo, em cuidar dos filhotes e em manter laços. Se esses interesses importam em nós, o que justifica ignorá-los em outro corpo? A espécie, assim como a cor ou o país, vem da <a href="perigo-de-culpar-o-estrangeiro.html">loteria da vida</a>. Quatro obras levam essa pergunta para dentro da teoria política:</p>
<table><thead><tr><th>Obra</th><th>Autores</th><th>Ideia central</th></tr></thead><tbody>
<tr><td><em>Zoopolis: A Political Theory of Animal Rights</em></td><td>Sue Donaldson e Will Kymlicka</td><td>Os direitos dependem da relação de cada grupo de animais com a nossa sociedade</td></tr>
<tr><td><em>Sentientist Politics: A Theory of Global Inter-Species Justice</em></td><td>Alasdair Cochrane</td><td>Uma democracia cosmopolita para todos os seres sencientes</td></tr>
<tr><td><em>Reasoned Politics</em></td><td>Magnus Vinding</td><td>Reduzir o sofrimento, sobretudo o extremo, com razão e evidências</td></tr>
<tr><td><em>Animals and the Constitution: Towards Sentience-Based Constitutionalism</em></td><td>John Adenitire e Raffael Fasel</td><td>Constituições baseadas no respeito aos interesses de todos os seres sencientes governados</td></tr>
</tbody></table>
<h3>Donaldson e Kymlicka: animais como membros da comunidade política</h3>
<p>Em <em>Zoopolis</em> (2011), os autores vão além da pergunta sobre o que não se pode fazer aos animais, e perguntam qual é a nossa relação política com eles. Propõem três grupos:</p>
<table><thead><tr><th>Animais</th><th>Exemplos</th><th>Situação proposta</th></tr></thead><tbody>
<tr><td>Domesticados</td><td>Cães, gatos, vacas e galinhas</td><td><strong>Cidadania:</strong> nós os trouxemos para a nossa sociedade, e eles devem ter seus interesses levados em conta</td></tr>
<tr><td>Que vivem perto de nós</td><td>Pombos e ratos urbanos</td><td><strong>Residência:</strong> não são cidadãos plenos, mas têm direito de existir e de não ser tratados como praga</td></tr>
<tr><td>Selvagens</td><td>Animais em seus habitats</td><td><strong>Soberania:</strong> comunidades que têm direito ao próprio território, sem invasão humana</td></tr>
</tbody></table>
<p>A proposta inclui também direitos positivos, e não só a proteção contra danos. Críticos questionam se animais podem mesmo ser cidadãos, e se a ideia de soberania deixa animais selvagens sem ajuda diante do sofrimento na natureza.</p>
<h3>Alasdair Cochrane: justiça entre espécies, no mundo todo</h3>
<p>Em <em>Animal Rights Without Liberation</em>, Cochrane separa dois interesses: a maioria dos animais tem interesse forte em não sofrer, mas não necessariamente um interesse intrínseco em liberdade. Em <em>Sentientist Politics</em> (2018), propõe uma “democracia cosmopolita sencientista”: instituições que levem em conta os interesses de todos os seres sencientes, com representantes específicos para quem não pode votar, em vários níveis, do local ao global. Ele fala em direitos sencientes, e não só em direitos humanos. Ao contrário de <em>Zoopolis</em>, baseia os direitos nos interesses de cada indivíduo, e não em grupos.</p>
<h3>Magnus Vinding: reduzir o sofrimento</h3>
<p>Em <em>Reasoned Politics</em>, Vinding defende a redução do sofrimento, sobretudo o extremo, como valor central, e inclui os não humanos. O livro une ética, política e evidências, e termina com um manifesto para um partido hipotético, a Aliança da Razão e da Compaixão.</p>
<h3>Adenitire e Fasel: a Constituição também para os animais</h3>
<p>Em <em>Animals and the Constitution</em> (2025), os autores criticam a teoria constitucional por olhar só para os humanos. Propõem um constitucionalismo baseado na senciência, que respeite os interesses de todos os seres sencientes governados, e repensam quatro princípios: direitos fundamentais, proporcionalidade, Estado de direito e democracia. Citam debates reais, como votações sobre direitos de primatas na Suíça e propostas de carta de direitos para animais na Finlândia.</p>
<div class="nota"><strong>Eles discordam entre si:</strong> sobre o que os direitos devem ser, sobre liberdade e sobre o mundo selvagem. Mas partem de uma mesma ideia: uma política justa não termina na fronteira da espécie humana.</div>
<h2>Objeções</h2>
<ul><li><strong>“Só humanos têm direitos.”</strong> Bebês e pessoas com deficiência cognitiva grave não têm razão ou contrato, e têm direitos. O que os fundamenta?</li><li><strong>“É cultural e econômico.”</strong> Argumento histórico contra toda reforma moral; ainda assim, a transição precisa cuidar dos trabalhadores.</li><li><strong>“Como medir?”</strong> Há incerteza sobre graus de sofrimento. Ela é motivo para pesquisa, não para desconsiderar.</li></ul>
<div class="cta"><a class="btn alt" href="https://ethicalfood.biblioverse.org/pt/" target="_blank" rel="noopener">Guia de Alimentos Éticos</a></div>
''', fontes=[('Zoopolis: A Political Theory of Animal Rights', 'https://willkymlicka.ca/publications/books/animals'), ('Sentientist Politics: A Theory of Global Inter-Species Justice', 'https://global.oup.com/academic/product/sentientist-politics-9780198789802'), ('Animals and the Constitution: Towards Sentience-Based Constitutionalism', 'https://academic.oup.com/book/59826'), ('Declaração de Nova York sobre Consciência Animal', 'https://sites.google.com/nyu.edu/nydeclaration/declaration'), ('Declaração de Cambridge', 'https://en.wikipedia.org/wiki/Animal_consciousness'), VINDING]),

dict(slug='teorias-da-justica', grupo='Quem conta', titulo='Teorias da justiça para a política', resumo='Rawls, Nozick, utilitaristas, prioritaristas e suficientistas: como dividir o que é de todos?', corpo='''
<p class="abre">Dividir recursos e direitos é a questão central da filosofia política. Cada teoria dá uma resposta com consequências práticas.</p>
<table><thead><tr><th>Teoria</th><th>Regra</th><th>Crítica comum</th></tr></thead><tbody>
<tr><td>Utilitarismo</td><td>Maximizar o bem-estar total</td><td>Pode sacrificar poucos em nome de muitos</td></tr>
<tr><td>Rawls (maximin)</td><td>Desigualdade só se beneficiar quem está pior</td><td>Pode exagerar a prioridade ao pior caso</td></tr>
<tr><td>Prioritarismo</td><td>Benefícios valem mais para quem está pior</td><td>Quanto mais, exatamente?</td></tr>
<tr><td>Suficientismo</td><td>Garantir o suficiente; acima disso, tanto faz</td><td>Onde fica a linha?</td></tr>
<tr><td>Libertarismo (Nozick)</td><td>É justo o que resulta de trocas voluntárias</td><td>Ignora o ponto de partida e quem não tem nada</td></tr>
<tr><td>Capacidades (Sen, Nussbaum)</td><td>O que as pessoas conseguem ser e fazer</td><td>Lista difícil de fechar</td></tr>
<tr><td>Comunitarismo</td><td>Justiça depende da comunidade e de suas tradições</td><td>Pode legitimar injustiças locais</td></tr>
<tr><td>Focada no sofrimento</td><td>Priorizar a redução do sofrimento, sobretudo o extremo</td><td>Pode subestimar outros bens</td></tr>
</tbody></table>
<h2>As três que mais aparecem nos debates</h2>
<p><strong>Rawls</strong> propõe dois princípios, em ordem. Primeiro, liberdades básicas iguais para todos, que nenhum ganho econômico justifica reduzir. Segundo, as desigualdades só são aceitáveis se os cargos e as posições estiverem abertos a todos em igualdade de oportunidades, e se beneficiarem quem está em pior situação. É o chamado princípio da diferença: um país pode ter ricos, desde que isso melhore a vida dos mais pobres em comparação com as alternativas. Veja o <a href="contrato-social.html">contrato social</a>.</p>
<p><strong>Nozick</strong> responde que a justiça não está no desenho final da distribuição, e sim na história de cada bem: é justo o que foi adquirido sem fraude nem violência e trocado de forma voluntária. Redistribuir pelo Estado seria tratar as pessoas como meios para o bem-estar de outras. Ele admite corrigir injustiças passadas, o que abre uma porta enorme, já que boa parte da riqueza do mundo tem origem em conquista e escravidão. Veja <a href="imposto-e-roubo.html">imposto é roubo?</a>.</p>
<p><strong>Sen e Nussbaum</strong> mudam a pergunta: não interessa só quanto dinheiro alguém tem, e sim o que ela consegue de fato ser e fazer com ele. Uma pessoa com deficiência, ou que mora onde não há escola, precisa de mais recursos para ter as mesmas capacidades. É a base do Índice de Desenvolvimento Humano, que combina renda, saúde e educação.</p>
<h2>Onde isso aparece na política brasileira</h2>
<table><thead><tr><th>Política</th><th>Lógica predominante</th><th>A crítica vem de</th></tr></thead><tbody>
<tr><td>SUS universal e gratuito</td><td>Suficientismo e igualdade: um mínimo garantido a todos, sem olhar renda</td><td>Quem prefere focalizar o gasto em quem não pode pagar</td></tr>
<tr><td>Bolsa Família</td><td>Prioritarismo: cada real vale mais para quem tem menos</td><td>Libertários (coerção) e quem teme dependência</td></tr>
<tr><td>Cotas em universidades</td><td>Igualdade de oportunidades e correção de injustiças passadas</td><td>Quem defende o critério exclusivo do mérito. Veja o <a href="debates/cotas.html">debate</a></td></tr>
<tr><td>Imposto progressivo e sobre grandes fortunas</td><td>Rawls e prioritarismo</td><td>Nozick: a riqueza obtida de forma justa pertence a quem a obteve</td></tr>
<tr><td>Redução de burocracia para abrir empresas</td><td>Libertarismo e liberalismo: liberdade de trocar e empreender</td><td>Quem teme menos proteção ao trabalhador e ao consumidor</td></tr>
<tr><td>Proteção legal aos animais</td><td>Ética focada no sofrimento e sencientismo</td><td>Quem restringe a justiça aos humanos. Veja <a href="sencientismo.html">sencientismo</a></td></tr>
</tbody></table>
<p>Quase ninguém segue uma teoria só. A maioria das pessoas aceita um mínimo para todos, alguma recompensa ao mérito e alguma correção da sorte. O que as teorias fazem é obrigar a dizer onde cada princípio termina e o outro começa, e é aí que as disputas políticas de verdade acontecem.</p>
<div class="cta"><a class="btn" href="https://ethicstest.biblioverse.org/" target="_blank" rel="noopener">Descubra sua visão no Teste de Visão Moral</a></div>
''', fontes=[('Teste de Visão Moral: mapa', 'https://ethicstest.biblioverse.org/map.html'), ('Uma teoria da justiça', 'https://pt.wikipedia.org/wiki/Uma_Teoria_da_Justi%C3%A7a'), ('Anarquia, Estado e Utopia', 'https://en.wikipedia.org/wiki/Anarchy,_State,_and_Utopia'), ('Capability approach (Wikipédia)', 'https://en.wikipedia.org/wiki/Capability_approach'), VINDING]),

dict(slug='presidencialismo-de-coalizao', grupo='O sistema brasileiro', titulo='Presidencialismo de coalizão e Centrão', resumo='Por que o presidente do Brasil precisa negociar tanto, e o que isso produz.', corpo='''
<p class="abre">O cientista político Sérgio Abranches cunhou em 1988 o termo “presidencialismo de coalizão”: o presidente é eleito por milhões, mas seu partido nunca tem maioria no Congresso. Para governar, monta alianças com vários partidos.</p>
<h2>A moeda</h2>
<ul><li><strong>Ministérios e cargos:</strong> partidos entram na base em troca de postos.</li><li><strong>Emendas:</strong> verbas para as bases dos parlamentares.</li><li><strong>Agenda:</strong> partes do programa são negociadas.</li></ul>
<p>Isso dá estabilidade, mas gera toma-lá-dá-cá. Sem base, presidentes caem ou ficam paralisados: Collor (1992) e Dilma (2016) sofreram impeachment em meio à perda de apoio.</p>
<h2>O Centrão</h2>
<p>O nome surgiu na Constituinte de 1987-88. Hoje designa partidos, como PP, Republicanos, PL, União e outros, que tendem a apoiar quem está no governo em troca de espaço, com menos rigidez ideológica. A composição varia. Com o crescimento das emendas impositivas, o Congresso ganhou mais força sobre o orçamento, e alguns falam em “semipresidencialismo informal”.</p>
<h2>As regras dos partidos</h2>
<table><thead><tr><th>Regra</th><th>O que faz</th></tr></thead><tbody>
<tr><td>Cláusula de barreira</td><td>Quem não atinge votos mínimos para a Câmara perde fundo partidário e tempo de TV. Em 2026, o requisito foi de 2,5% dos votos válidos, entre outras condições.</td></tr>
<tr><td>Fim das coligações proporcionais</td><td>Desde 2020 partidos não podem se coligar para eleições de vereador e deputado.</td></tr>
<tr><td>Federações</td><td>Desde 2021 partidos podem atuar juntos por no mínimo quatro anos, como se fossem um só.</td></tr>
<tr><td>Fundo eleitoral</td><td>Financiamento público de campanhas, após o STF proibir doações de empresas em 2015.</td></tr>
</tbody></table>
<p>Essas regras explicam muitas fusões recentes, como União Brasil e PRD, e as federações. O número de partidos no Congresso vem caindo.</p>
''', fontes=[('Presidencialismo de coalizão', 'https://pt.wikipedia.org/wiki/Presidencialismo_de_coaliz%C3%A3o'), ('Congresso em Foco', 'https://www.congressoemfoco.com.br/'), ('Centrão (Wikipédia)', 'https://pt.wikipedia.org/wiki/Centr%C3%A3o')]),
]
