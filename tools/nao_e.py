"""Bloco “O que não é…” de cada vertente (novembro de 2026): as concepções erradas e os espantalhos mais comuns sobre
cada corrente, com a correção. Chave: slug da vertente; valor: lista de (o que se diz, o que é de fato).
O build exige uma entrada para toda vertente; build.py renderiza com nao_e_html()."""

NAO_E = {
'liberalismo-classico': [
 ('“Liberal é quem defende o lucro acima das pessoas.”', 'O liberalismo clássico nasceu como defesa do indivíduo contra o poder absoluto do rei e da Igreja. Seu centro são direitos e limites ao Estado; o mercado livre é consequência, não ponto de partida.'),
 ('“Liberal é contra qualquer Estado.”', 'Locke, Smith e Mill defendiam Estado com lei, tribunais, polícia, defesa e, no caso de Smith, obras públicas e educação básica. Quem rejeita o Estado inteiro é o anarcocapitalismo.'),
 ('“Liberal é a mesma coisa que conservador.”', 'Historicamente foram adversários: o liberalismo questionava tradições e privilégios herdados. No Brasil e nos Estados Unidos as palavras se misturaram, mas as origens são opostas.'),
 ('“Liberalismo é a ideologia dos ricos.”', 'Os liberais do século 19 lutaram contra monopólios, corporações de ofício e privilégios aristocráticos, e muitos defenderam o fim da escravidão e o voto ampliado.'),
],
'neoliberalismo': [
 ('“Neoliberal é qualquer política que eu não gosto.”', 'O termo virou xingamento genérico. Em sentido útil, descreve um conjunto específico: privatizações, abertura comercial, controle fiscal e regulação menor, como em Thatcher, Reagan e no Consenso de Washington.'),
 ('“Neoliberalismo quer um Estado fraco.”', 'Muitos neoliberais querem um Estado forte para garantir contratos, moeda estável e ordem, e fraco apenas na produção e na redistribuição. Hayek e os ordoliberais alemães escreveram sobre isso.'),
 ('“Nenhum neoliberal defende proteção social.”', 'Hayek admitia uma renda mínima garantida, e Milton Friedman propôs o imposto de renda negativo, que inspirou programas de transferência de renda.'),
],
'social-liberalismo': [
 ('“Social-liberal é só um socialista envergonhado.”', 'O social-liberal mantém o mercado e a propriedade privada como base. Ele acrescenta que, sem educação, saúde e um mínimo de segurança, a liberdade é só formal.'),
 ('“É a mesma coisa que social-democracia.”', 'Parecem-se nas políticas, mas partem de lugares diferentes: a social-democracia vem do movimento operário e pensa a partir da classe; o social-liberalismo vem do liberalismo e pensa a partir do indivíduo.'),
 ('“Social-liberal quer um Estado gigante.”', 'A proposta é um Estado que garanta pisos, não que dirija a economia. Beveridge, pai do Estado de bem-estar britânico, era liberal.'),
],
'libertarianismo': [
 ('“Libertário é quem quer o caos.”', 'O minarquista defende Estado com polícia, tribunais e defesa. A ordem continua; o que muda é o tamanho do que o Estado pode mandar.'),
 ('“Libertário é de extrema-direita.”', 'A maioria dos libertários é a favor de drogas legalizadas, casamento entre pessoas do mesmo sexo, imigração livre e contra guerras. Isso o separa da direita conservadora.'),
 ('“Libertário não se importa com os pobres.”', 'A aposta libertária é que mercados livres e menos regulação enriquecem os pobres mais rápido. Pode estar errada, mas é um argumento sobre resultados, não indiferença.'),
],
'anarcocapitalismo': [
 ('“Anarcocapitalismo é o liberalismo de sempre, só mais radical.”', 'É uma ruptura: o liberalismo clássico considera o Estado necessário para garantir direitos; o anarcocapitalismo diz que até justiça e segurança podem ser serviços comprados.'),
 ('“Anarcocapitalista quer que o mais forte mande.”', 'A teoria prevê agências de proteção e tribunais privados que competem entre si. Os críticos dizem que isso vira feudalismo; os defensores dizem que a competição evita o abuso.'),
 ('“Anarcocapitalismo é anarquismo.”', 'Os anarquistas clássicos rejeitam o patrão tanto quanto o Estado. Para eles, o anarcocapitalismo mantém a hierarquia que querem abolir, e por isso o recusam como parte da família.'),
],
'conservadorismo': [
 ('“Conservador é quem não quer mudança nenhuma.”', 'Burke, o pai da corrente, defendia que uma sociedade sem meios de mudar não tem meios de se conservar. O que o conservador rejeita é a mudança abrupta e feita de cima, por um plano.'),
 ('“Conservador é a mesma coisa que reacionário.”', 'O reacionário quer voltar a um passado; o conservador quer preservar o que funciona hoje. Burke apoiou a independência americana e condenou a Revolução Francesa.'),
 ('“Conservadorismo é só religião.”', 'Há conservadores religiosos e seculares. Oakeshott e Scruton fundaram sua posição na desconfiança de projetos racionais totais, não na fé.'),
 ('“Conservador defende os ricos.”', 'Conservadores defendem instituições, famílias e comunidades, que incluem sindicatos antigos e igrejas populares. Disraeli, conservador, criou leis de proteção aos trabalhadores.'),
],
'liberal-conservadorismo': [
 ('“É só um nome bonito para a direita.”', 'É uma combinação específica, e com tensão interna: o mercado livre que ele defende dissolve tradições que ele quer preservar. Pensadores da corrente discutem essa contradição abertamente.'),
 ('“Liberal-conservador é contra direitos civis.”', 'Em geral aceita os direitos civis já conquistados e resiste a ampliações rápidas. A posição varia muito entre países e épocas.'),
],
'democracia-crista': [
 ('“Democracia cristã quer um Estado religioso.”', 'Nasceu justamente para que católicos participassem da democracia pluralista, aceitando a separação entre Igreja e Estado. Adenauer e De Gasperi governaram repúblicas laicas.'),
 ('“É só conservadorismo com Bíblia.”', 'A doutrina social da Igreja defende salário justo, sindicatos e limites ao capital. A democracia cristã europeia construiu Estados de bem-estar.'),
 ('“Democrata-cristão é de extrema-direita.”', 'Na Europa, a democracia cristã foi o centro-direita moderado e o principal adversário dos fascismos depois da guerra.'),
],
'reacionarismo': [
 ('“Reacionário é qualquer conservador.”', 'O conservador preserva o presente; o reacionário rejeita o presente e quer restaurar uma ordem passada, real ou idealizada. A diferença é de direção.'),
 ('“Reacionário é sempre religioso.”', 'Há reacionários laicos, que idealizam um passado de hierarquia, honra ou pureza nacional sem apelar a Deus.'),
 ('“Reacionário quer voltar exatamente ao passado.”', 'O passado que ele quer costuma ser uma reconstrução. Pesquisas sobre reacionarismo mostram que a nostalgia seleciona o que agrada e apaga o resto.'),
],
'monarquismo': [
 ('“Monarquista quer um rei absoluto mandando em tudo.”', 'A maioria dos monarquistas de hoje defende a monarquia parlamentar, como no Reino Unido, na Espanha ou no Japão, em que o rei reina e não governa.'),
 ('“Monarquia é incompatível com democracia.”', 'Vários dos países mais democráticos do mundo são monarquias constitucionais, como Noruega, Suécia e Dinamarca. O que decide é a Constituição, não o título do chefe de Estado.'),
 ('“Monarquista é saudosista da escravidão.”', 'Monarquistas brasileiros costumam lembrar que a abolição foi assinada pela princesa Isabel. A crítica mais forte a eles é outra: que o Império também manteve a escravidão por décadas.'),
],
'tradicionalismo': [
 ('“Tradicionalismo é só gostar do antigo.”', 'É uma teoria: a de que a tradição carrega uma verdade que a razão individual não alcança. Por isso, para o tradicionalista, questionar a tradição não é só erro, é perda.'),
 ('“Tradicionalista e conservador são a mesma coisa.”', 'O conservador aceita que tradições mudem devagar e se corrijam. O tradicionalista as vê como fonte de autoridade, não como algo a ser avaliado.'),
],
'ultraconservadorismo': [
 ('“Ultraconservador é todo conservador.”', 'O conservador comum aceita direitos civis já estabelecidos e muda devagar. O ultraconservador quer reverter mudanças sociais e tende a ver adversários como ameaça moral.'),
 ('“Ultraconservadorismo é fascismo.”', 'Pode conviver com a democracia eleitoral e, em geral, não defende violência política nem partido único. A linha é cruzada quando passa a rejeitar a democracia liberal.'),
],
'neoconservadorismo': [
 ('“Neocon é só um conservador mais novo.”', 'A corrente nasceu de ex-esquerdistas americanos nos anos 1960 e 1970 e tem uma marca própria: política externa ativa para espalhar a democracia, inclusive pela força.'),
 ('“Neocon é isolacionista.”', 'É o oposto. Os neoconservadores apoiaram as guerras do Iraque e do Afeganistão; os isolacionistas da direita, como parte do trumpismo, os combatem.'),
 ('“Neocon é contra o Estado de bem-estar.”', 'Muitos aceitam o Estado de bem-estar e criticam apenas seus excessos. A diferença para o libertarianismo é grande nesse ponto.'),
],
'direita-radical': [
 ('“Direita radical é fascismo.”', 'A direita radical aceita eleições e disputa o poder pelo voto, embora tensione a democracia liberal. O fascismo a rejeita e usa violência organizada. A fronteira pode ser cruzada, mas não é a mesma coisa.'),
 ('“Toda direita é radical.”', 'A direita moderada, como o liberal-conservadorismo e a democracia cristã, aceita as regras do jogo e a alternância de poder sem contestá-las.'),
],
'bolsonarismo': [
 ('“Bolsonarismo é só o eleitor de Bolsonaro.”', 'Mais da metade do país votou nele em 2018. O bolsonarismo, como movimento, é um núcleo mais estreito, organizado em torno do líder, do antipetismo e da desconfiança das instituições.'),
 ('“Bolsonarismo é fascismo.”', 'Tem traços comuns, como o culto ao líder e a hostilidade a adversários, mas disputou e perdeu eleições e não tem partido único nem milícia de partido. O termo mais usado por pesquisadores é direita radical ou populismo de direita.'),
 ('“Bolsonarista é tudo igual.”', 'Há liberais na economia, militares, evangélicos e conservadores de costumes com interesses diferentes, e brigas públicas entre eles.'),
],
'fascismo': [
 ('“Fascista é qualquer um de direita de quem eu discordo.”', 'O fascismo é algo específico: nação acima de tudo, líder único, partido único, violência política como método e fim da democracia. Chamar de fascista quem só é conservador esvazia a palavra.'),
 ('“O fascismo era de esquerda, porque era socialista.”', 'Mussolini veio do socialismo, mas o fascismo se definiu contra ele: esmagou sindicatos, partidos de esquerda e a luta de classes, e se aliou a industriais e proprietários.'),
 ('“Fascismo é só autoritarismo.”', 'Há ditaduras sem fascismo. O fascismo mobiliza massas, cultua a violência e a guerra e quer refazer o ser humano, não só mantê-lo quieto.'),
],
'nazismo': [
 ('“O nazismo era socialista, está no nome.”', 'O “socialismo” do nome era propaganda. Hitler proibiu partidos e sindicatos socialistas, mandou seus líderes a campos de concentração e privatizou empresas estatais. O centro do nazismo era a raça, não a classe.'),
 ('“Nazismo é só fascismo alemão.”', 'O racismo biológico e o projeto de extermínio o distinguem. O fascismo italiano, no início, não era antissemita.'),
 ('“Nazista é quem defende fronteiras ou ordem.”', 'Isso dilui um crime histórico. Nazismo envolve hierarquia de raças, Estado totalitário e genocídio.'),
],
'integralismo': [
 ('“Integralismo foi só um partido nacionalista.”', 'Foi o maior movimento fascista fora da Europa, com uniforme, saudação e milícia. Seu líder, Plínio Salgado, admirava Mussolini.'),
 ('“Integralismo é catolicismo político.”', 'Usava a religião, mas a Igreja nunca o adotou, e muitos católicos o combateram. O lema “Deus, Pátria e Família” era mobilização, não doutrina da Igreja.'),
],
'militarismo-autoritario': [
 ('“Todo militar é autoritário.”', 'A corrente é uma ideia política, não uma profissão. Muitos militares defendem a democracia e a subordinação das Forças Armadas ao poder civil.'),
 ('“A ditadura de 1964 foi uma ‘revolução’ para salvar o país do comunismo.”', 'O golpe derrubou um presidente eleito e o regime cassou, torturou e matou opositores, inclusive não comunistas. O risco comunista era real como tema de propaganda, não como ameaça de tomada do poder.'),
 ('“O autoritarismo militar é sempre de direita.”', 'No Brasil e no Cone Sul foi de direita, mas houve regimes militares de esquerda, como o de Velasco Alvarado no Peru e o egípcio de Nasser.'),
],
'ultranacionalismo': [
 ('“Ultranacionalista é quem ama o país.”', 'Patriotismo é gostar do próprio país. Ultranacionalismo é colocá-lo acima de qualquer valor, inclusive dos direitos de quem é de fora ou de quem é visto como estranho dentro dele.'),
 ('“Nacionalismo e ultranacionalismo são o mesmo.”', 'O nacionalismo comum convive com direitos iguais e com outras nações. O ultranacionalismo tende à superioridade e ao conflito.'),
],
'extrema-direita': [
 ('“Extrema-direita é todo mundo à direita do centro.”', 'A definição usada por pesquisadores é mais estreita: rejeição da democracia liberal ou da igualdade de direitos, em nome da nação, da ordem ou de uma hierarquia natural. Conservadores comuns não entram nela.'),
 ('“Extrema-direita e extrema-esquerda são iguais.”', 'Compartilham métodos, como o culto ao líder e a intolerância, mas os fins se opõem: uma quer hierarquia e nação, a outra quer igualdade e fim das classes. A teoria da ferradura descreve a semelhança nos meios, não nos objetivos.'),
],
'centrismo': [
 ('“Centrista é quem não tem opinião.”', 'O centrismo moderno tem um programa: mercado regulado, proteção social e reformas graduais. Blair e Clinton tinham políticas claras, e muitas foram polêmicas.'),
 ('“Centro é o meio exato entre esquerda e direita.”', 'O centro muda de lugar conforme o país e a época. O que é centro na Suécia pode ser esquerda nos Estados Unidos.'),
 ('“Centrista é sempre moderado nos costumes.”', 'Há centristas liberais e conservadores nos costumes. A posição econômica não decide a posição moral.'),
],
'social-democracia': [
 ('“Social-democracia é socialismo.”', 'Hoje, a social-democracia aceita o capitalismo e quer regulá-lo e redistribuir seus frutos. O socialismo quer substituí-lo. As duas correntes se separaram no século 20.'),
 ('“Social-democracia é comunismo disfarçado.”', 'Os social-democratas foram, na Europa, os adversários mais firmes dos partidos comunistas, inclusive na Guerra Fria.'),
 ('“Os países nórdicos são socialistas.”', 'São economias de mercado com empresas privadas, livre comércio e Estados de bem-estar amplos. Os próprios governos nórdicos recusam o rótulo de socialismo.'),
],
'trabalhismo': [
 ('“Trabalhismo é marxismo.”', 'O trabalhismo britânico nasceu de sindicatos e de cristãos sociais, não de Marx. O trabalhismo de Vargas foi explicitamente anticomunista.'),
 ('“Trabalhismo é só populismo de Vargas.”', 'Vargas o usou, mas a corrente inclui Brizola, Darcy Ribeiro e um programa próprio: direitos do trabalho, Estado protetor e nacionalismo econômico.'),
],
'desenvolvimentismo': [
 ('“Desenvolvimentista é de esquerda.”', 'A ditadura militar foi desenvolvimentista, e Juscelino também. A corrente combina com governos de direita e de esquerda; o que a define é o papel do Estado na industrialização.'),
 ('“Desenvolvimentismo é só gastar dinheiro público.”', 'Seu centro é planejar a economia para mudar a estrutura produtiva. Os críticos apontam que isso protegeu empresas ineficientes; os defensores, que criou a indústria brasileira.'),
],
'lulismo': [
 ('“Lulismo é socialismo.”', 'O lulismo governou com bancos lucrando, agronegócio crescendo e sem mexer na estrutura da propriedade. Sua marca é reduzir a pobreza sem confrontar o capital.'),
 ('“Lulismo é só o PT.”', 'O cientista político André Singer cunhou o termo para um pacto com os mais pobres que passa por cima do partido e das classes médias que fundaram o PT.'),
 ('“Lulismo é petismo.”', 'O petismo é a identificação com o partido; o lulismo, com o líder e com um modo de governar. Há lulistas que não gostam do PT e petistas que criticam Lula.'),
],
'socialismo-democratico': [
 ('“Socialismo democrático é a União Soviética com voto.”', 'A corrente nasceu contra o modelo soviético: recusa partido único, censura e polícia política, e aposta em reformas aprovadas pelo voto e reversíveis por ele.'),
 ('“É a mesma coisa que social-democracia.”', 'A social-democracia quer regular o capitalismo; o socialismo democrático quer superá-lo. Compartilham o método democrático, não o objetivo.'),
 ('“Socialista democrático quer estatizar tudo.”', 'Muitos defendem cooperativas, empresas de trabalhadores e propriedade social, não controle estatal centralizado.'),
],
'marxismo': [
 ('“Marxismo é a ditadura da União Soviética.”', 'Marx morreu em 1883, décadas antes da Revolução Russa. Há marxistas que criticam o modelo soviético desde o começo, como Rosa Luxemburgo e os conselhistas.'),
 ('“Marxismo quer que todos ganhem igual.”', 'Marx criticou o “igualitarismo grosseiro”. A fórmula dele para a sociedade futura era “de cada um segundo sua capacidade, a cada um segundo suas necessidades”, que supõe diferenças.'),
 ('“Marx queria abolir toda propriedade.”', 'O alvo era a propriedade dos meios de produção, como fábricas e terras, não os bens pessoais. O Manifesto Comunista diz isso de forma explícita.'),
 ('“Marxismo cultural controla as universidades.”', 'A expressão vem de uma teoria conspiratória. Há professores marxistas, como há liberais e conservadores, mas não existe um plano coordenado, e a maior parte da obra de Marx é sobre economia, não cultura.'),
],
'comunismo': [
 ('“Comunismo é o Estado controlando tudo.”', 'Na teoria de Marx, comunismo é o estágio final, sem Estado e sem classes. O Estado que controla tudo era, para ele, uma fase de transição, e muitos comunistas dizem que ela nunca foi superada em lugar nenhum.'),
 ('“Comunismo e socialismo são a mesma coisa.”', 'Na tradição marxista, socialismo é a etapa intermediária, ainda com Estado; comunismo é o fim do caminho. No uso comum, as palavras se misturam.'),
 ('“Comunista quer tirar sua casa e seu carro.”', 'O comunismo mira a propriedade dos meios de produção. Em regimes comunistas, bens pessoais continuaram existindo; o que não havia era empresa privada.'),
],
'marxismo-leninismo': [
 ('“Marxismo-leninismo é o único marxismo.”', 'É uma versão: a do partido de vanguarda que toma e exerce o poder. Trotskistas, conselhistas, eurocomunistas e marxistas acadêmicos rejeitam partes dela.'),
 ('“Stalin aplicou o que Lenin queria.”', 'É disputado. Lenin, no fim da vida, pediu que Stalin fosse afastado do cargo de secretário-geral; stalinistas e antistalinistas dentro do marxismo leem a continuidade de forma oposta.'),
 ('“Marxista-leninista nega os crimes de Stalin.”', 'Alguns negam; muitos partidos comunistas, inclusive o soviético em 1956, reconheceram os crimes e o culto à personalidade.'),
],
'trotskismo': [
 ('“Trotskista é stalinista disfarçado.”', 'Trótski foi o maior opositor de Stalin e foi assassinado a mando dele. O trotskismo nasceu da crítica à burocracia soviética.'),
 ('“Trotskismo é democracia dentro do marxismo.”', 'Trótski também defendeu o partido único e reprimiu a revolta de Kronstadt em 1921. A crítica dele ao stalinismo não era liberal.'),
 ('“Trotskista quer revolução agora, a qualquer custo.”', 'A “revolução permanente” é uma tese sobre a ligação entre revoluções nacionais e internacionais, não um chamado a insurreições a qualquer momento.'),
],
'maoismo': [
 ('“Maoísmo é só o marxismo da China.”', 'É uma variante com ideias próprias: a revolução parte do campo, a guerra popular prolongada e a revolução cultural contra a burocracia. A China atual se diz marxista, mas abandonou boa parte disso.'),
 ('“Mao modernizou a China sem custo.”', 'O Grande Salto Adiante causou uma fome que matou dezenas de milhões de pessoas, e a Revolução Cultural perseguiu e matou intelectuais e quadros. O próprio Partido Comunista reconheceu os erros em 1981.'),
],
'ecossocialismo': [
 ('“Ecossocialismo é ambientalismo com bandeira vermelha.”', 'É uma tese específica: a de que a crise ecológica vem da lógica de crescimento do capitalismo e só se resolve mudando o sistema. Ambientalistas liberais discordam dela.'),
 ('“Socialismo foi bom para o meio ambiente.”', 'O ecossocialismo nasceu também da crítica ao desastre ambiental soviético, como o mar de Aral. Ele rejeita o produtivismo dos dois sistemas.'),
],
'teologia-da-libertacao': [
 ('“Teologia da Libertação é marxismo com batina.”', 'Usa ferramentas da análise social, inclusive marxistas, mas sua base é bíblica: os profetas, o Êxodo e o Evangelho lidos a partir dos pobres. O Vaticano criticou o uso do marxismo, não a opção pelos pobres.'),
 ('“A Igreja condenou a Teologia da Libertação.”', 'Houve críticas e punições a alguns teólogos nos anos 1980, mas a “opção preferencial pelos pobres” foi assumida pelos bispos latino-americanos e pelo papa Francisco.'),
],
'extrema-esquerda': [
 ('“Extrema-esquerda é todo mundo à esquerda do centro.”', 'O PT, a social-democracia e o socialismo democrático aceitam a democracia liberal e a disputa eleitoral. O que marca a extrema-esquerda é a busca de ruptura, em geral vendo a democracia liberal como insuficiente.'),
 ('“Extrema-esquerda é sempre violenta.”', 'Há grupos que defendem a luta armada e outros que atuam só pela organização, pela greve e pelo voto. O termo descreve o objetivo, não necessariamente o método.'),
],
'anarquismo': [
 ('“Anarquia é bagunça e violência.”', 'Na teoria política, anarquismo é uma sociedade organizada sem poder imposto, com acordos voluntários e decisões coletivas. Os anarquistas dizem que a palavra foi sequestrada pelo senso comum.'),
 ('“Anarquista é contra qualquer regra.”', 'É contra a regra imposta por quem está acima. Comunidades anarquistas tiveram assembleias, normas e até tribunais populares, como na Catalunha de 1936.'),
 ('“Anarquismo é individualismo.”', 'As correntes principais, como o anarcocomunismo e o anarcossindicalismo, são coletivistas. O individualismo anarquista existe, mas é minoritário.'),
],
'anarcocomunismo': [
 ('“Anarcocomunismo é comunismo soviético sem Estado.”', 'Os anarcocomunistas combateram os bolcheviques, que os reprimiram, como no caso de Makhno na Ucrânia. Para Kropotkin, o Estado era o principal obstáculo ao comunismo.'),
 ('“Sem dinheiro ninguém trabalharia.”', 'Kropotkin argumentou com exemplos de cooperação voluntária e de trabalho por reconhecimento. Os críticos acham insuficiente para uma sociedade grande; os defensores apontam comunidades que funcionaram por anos.'),
],
'anarcossindicalismo': [
 ('“É só sindicalismo radical.”', 'O sindicato, aqui, não é só instrumento de luta: é o modelo da sociedade futura, que seria gerida pelos trabalhadores organizados por ofício e por local.'),
 ('“Anarcossindicalismo nunca saiu do papel.”', 'A CNT espanhola chegou a ter mais de um milhão de membros, e coletivizou fábricas e terras durante a Guerra Civil, antes de ser derrotada.'),
],
'mutualismo': [
 ('“Mutualismo é capitalismo.”', 'Proudhon, seu criador, escreveu que “a propriedade é um roubo”, referindo-se à renda sem trabalho. O mutualismo quer mercado sem juros, sem renda da terra e sem patrão.'),
 ('“Mutualismo é comunismo.”', 'Mantém mercado, preços e posse individual do que se usa e produz. Os anarcocomunistas o criticam justamente por isso.'),
],
'populismo': [
 ('“Populismo é fazer política para o povo.”', 'Na ciência política, populismo é uma forma de ver a política: um “povo puro” contra uma “elite corrupta”, com um líder que diz encarnar o povo. Governar para a maioria não é populismo; dizer que quem discorda não é povo, sim.'),
 ('“Populismo é de esquerda.”', 'Há populismo de esquerda, como o chavismo, e de direita, como Trump e Orbán. O conteúdo varia; a forma é a mesma.'),
 ('“Populista é quem dá benefício social.”', 'Programas sociais existem em governos de todo tipo. O que define o populismo é o discurso de povo contra elite, não a política pública.'),
],
'nacionalismo': [
 ('“Nacionalismo é sempre de direita.”', 'Houve nacionalismos de esquerda, como os anticoloniais da África e da Ásia e o nacionalismo econômico de Vargas e Brizola.'),
 ('“Nacionalismo é xenofobia.”', 'O nacionalismo cívico define a nação pela cidadania e pelas instituições, e pode ser aberto a imigrantes. O nacionalismo étnico, que define pela origem, é o que tende à exclusão.'),
 ('“Nacionalismo é natural e antigo.”', 'As nações modernas foram construídas nos séculos 18 e 19, com escola, exército e imprensa. Antes, a lealdade era ao rei, à religião ou à região.'),
],
'ambientalismo': [
 ('“Ambientalista é contra o progresso.”', 'A maioria defende outra forma de progresso, com energia limpa, cidades melhores e tecnologia. A disputa é sobre que crescimento, não sobre crescer ou não.'),
 ('“Ambientalismo é de esquerda.”', 'Há conservadores ambientalistas, que veem a natureza como herança a preservar, e liberais que apostam em mercado de carbono. A pauta cruza o espectro.'),
 ('“Ambientalista quer que todos virem vegetarianos e andem a pé.”', 'As propostas centrais são coletivas: matriz energética, regulação, desmatamento e transporte público. O comportamento individual é parte menor do debate.'),
],
'feminismo': [
 ('“Feminismo é o contrário do machismo.”', 'O machismo afirma a superioridade dos homens; o feminismo pede igualdade de direitos e de tratamento. O contrário do machismo seria uma superioridade das mulheres, que o feminismo não defende.'),
 ('“Feminista odeia homens.”', 'Há correntes que criticam o patriarcado como sistema, não os homens como pessoas, e boa parte do feminismo discute como o sistema também prejudica homens.'),
 ('“O feminismo já venceu, não serve mais.”', 'Mulheres votam e trabalham, mas ganham menos pelo mesmo trabalho, são minoria nos parlamentos e são a maior parte das vítimas de violência doméstica.'),
],
'comunitarismo': [
 ('“Comunitarismo é coletivismo autoritário.”', 'Os comunitaristas, como Sandel e Taylor, são democratas e defendem direitos. A crítica deles é que o liberalismo esquece que as pessoas se formam em comunidades.'),
 ('“Comunitarista é conservador.”', 'Há comunitaristas de esquerda, que valorizam sindicatos, bairros e movimentos sociais como comunidades que dão sentido e poder às pessoas.'),
],
'cosmopolitismo': [
 ('“Cosmopolita quer acabar com os países.”', 'A maioria defende que as fronteiras existam, mas que não decidam quanto uma vida vale. Propõe deveres além das fronteiras, não o fim delas.'),
 ('“Cosmopolitismo é globalismo das elites.”', '“Globalismo” é um termo de teoria da conspiração. O cosmopolitismo é uma tese moral antiga, dos estoicos a Kant: todo ser humano merece a mesma consideração.'),
],
'senciocracia': [
 ('“Sencientismo é dar voto a animais.”', 'É dar peso aos interesses de quem pode sofrer e desfrutar, nas decisões que os afetam. Animais seriam representados, como já são crianças e pessoas incapazes, não eleitores.'),
 ('“É colocar animais acima de humanos.”', 'A proposta é consideração igual para interesses iguais, não inversão de hierarquia. Humanos continuam contando; o que muda é que os outros também contam.'),
 ('“É um nome novo para o veganismo.”', 'O veganismo é uma prática individual. O sencientismo é um critério para a política: que seres entram na conta quando o Estado decide.'),
],
'autoritarismo': [
 ('“Autoritarismo é a mesma coisa que ditadura militar.”', 'Há autoritarismos civis, eleitos e com parlamento, que esvaziam os freios aos poucos, como a Hungria de Orbán e a Venezuela de Maduro.'),
 ('“Autoritarismo é totalitarismo.”', 'O autoritário quer obediência e deixa a vida privada em paz; o totalitário quer controlar tudo, inclusive o pensamento. Franco era autoritário; Hitler e Stalin, totalitários.'),
 ('“Governo forte é governo autoritário.”', 'Um governo pode ser forte e eficiente dentro das regras. Autoritário é o que escapa dos freios: Justiça, imprensa, oposição e eleições limpas.'),
],
'totalitarismo': [
 ('“Totalitarismo é só uma ditadura muito dura.”', 'Hannah Arendt mostrou que é um tipo próprio: ideologia total, mobilização de massas, terror contra inimigos inventados e destruição da vida privada. Muitas ditaduras duras não chegam a isso.'),
 ('“Só existe totalitarismo de esquerda” ou “só de direita”.', 'Os dois casos clássicos são o nazismo e o stalinismo. A estrutura é parecida; o conteúdo da ideologia é oposto.'),
],
'teocracia': [
 ('“Teocracia é qualquer governo de religiosos.”', 'Há políticos religiosos em democracias laicas. Teocracia é quando a lei e o governo se subordinam a uma doutrina religiosa e a seus intérpretes.'),
 ('“Fundamentalista é todo crente praticante.”', 'Fundamentalismo é uma leitura literal e inegociável do texto sagrado, aplicada à política. A maioria dos fiéis não é fundamentalista.'),
 ('“Teocracia é coisa só do islã.”', 'Houve teocracias cristãs, como a Genebra de Calvino e os Estados Pontifícios, e há projetos teocráticos em várias religiões hoje.'),
],
'progressismo': [
 ('“Progressista é só quem apoia a pauta de costumes.”', 'O progressismo começou como uma confiança na ciência e na reforma para melhorar a sociedade. Inclui saúde pública, educação e combate à corrupção, não só costumes.'),
 ('“Progressismo é esquerda econômica.”', 'Há progressistas liberais na economia. O que define a corrente é a crença em que a sociedade pode melhorar por reformas, não a posição sobre o mercado.'),
 ('“Progressista acha que tudo que é novo é bom.”', 'O progressismo clássico pedia evidências e reformas testadas. A caricatura do “novo pelo novo” é o espantalho mais comum.'),
],
'petismo': [
 ('“Petista é comunista.”', 'O PT governou com o mercado, pagou a dívida e fez alianças com o centro. Suas políticas são social-democratas; o programa socialista do início foi abandonado nos anos 1990.'),
 ('“Petista vota no PT porque recebe Bolsa Família.”', 'Pesquisas mostram que a identidade petista é anterior aos programas e inclui classe média, sindicalistas e professores. Reduzir o voto dos pobres a compra é a tese que o antipetismo usa, não um dado.'),
 ('“O PT é o único partido corrupto.”', 'O PT teve escândalos grandes, como o mensalão e o petrolão. Mas as mesmas investigações alcançaram partidos de quase todo o espectro, como mostram os dossiês dos partidos neste site.'),
 ('“Petismo é lulismo.”', 'O petismo é a identificação com o partido; o lulismo, com o líder e com um modo de governar. Há petistas que criticam Lula e lulistas que não gostam do PT.'),
],
'antipetismo': [
 ('“Antipetista é bolsonarista.”', 'O antipetismo é mais antigo e mais amplo: inclui tucanos, liberais e parte da esquerda que rompeu com o PT. O bolsonarismo capturou parte dele, não todo.'),
 ('“Antipetista é rico que odeia pobre.”', 'A rejeição ao PT é mais alta nas rendas mais altas, mas é grande também entre evangélicos de baixa renda e no interior do Sul e do Centro-Oeste. Não é uma classe, é uma identidade.'),
 ('“Antipetismo é só a reação da elite à inclusão dos pobres.”', 'É uma das explicações, mas o antipetismo cresceu sobretudo depois do mensalão e da Lava Jato, em resposta a escândalos reais. Explicá-lo só por preconceito é o espantalho que o petismo usa.'),
 ('“Ser contra o PT é ser contra a democracia.”', 'Rejeitar um partido é um direito democrático. O problema aparece quando a rejeição aceita qualquer meio, inclusive golpe, para impedir que ele governe.'),
],
'antibolsonarismo': [
 ('“Antibolsonarista é petista.”', 'A frente de 2022 incluiu Alckmin, Marina Silva, Simone Tebet, Fernando Henrique Cardoso e liberais que nunca votaram no PT. O antibolsonarismo é mais largo que qualquer partido.'),
 ('“Chamar o bolsonarismo de fascismo é só xingamento.”', 'Para parte dos antibolsonaristas é mesmo exagero, e eles preferem “extrema-direita” ou “populismo autoritário”. Os que usam “protofascismo” apontam traços específicos: culto ao líder, elogio à ditadura, inimigos internos e desprezo pela verdade. É um diagnóstico contestável, não um palavrão.'),
 ('“Antibolsonarista é contra toda a direita.”', 'A tese central é que o bolsonarismo não é uma direita comum. Muitos antibolsonaristas apoiaram candidatos de direita, como Tebet e Alckmin, justamente para separar os dois.'),
 ('“Antibolsonarismo é defender a censura do STF.”', 'Há antibolsonaristas que criticaram decisões do STF, como as de derrubar perfis e prender por discurso. O que une o campo é a defesa das urnas e da Constituição, não a aprovação de cada decisão.'),
],
}
