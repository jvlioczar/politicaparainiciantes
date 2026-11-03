"""Lição extra, temas e teste rápido de cada lição. tema: chaves de TEMAS. quiz: (pergunta, opções, índice certo, explicação)."""
TEMAS = {'fundamentos': 'Fundamentos', 'etica': 'Ética e valores', 'ideologia': 'Ideologias', 'democracia': 'Democracia', 'eleicoes': 'Voto e eleições', 'desinformacao': 'Desinformação', 'mente': 'Mente e vieses', 'perigos': 'Perigos', 'economia': 'Estado e economia', 'brasil': 'Brasil'}

NOVA = dict(slug='numero-de-projetos', grupo='Os perigos', titulo='O perigo de avaliar políticos por projetos aprovados', resumo='“Aprovou 50 projetos” não diz se fez bem ou mal. Veja que interesses defende e como vota.', corpo='''
<p class="abre">“Fulano aprovou 50 projetos.” Parece prova de bom trabalho, mas o número sozinho não diz o que os projetos fazem, nem a quem servem. É como avaliar um médico pelo número de receitas, sem perguntar se os pacientes melhoraram.</p>
<h2>Por que o número engana</h2>
<ul>
<li><strong>Quantidade não é conteúdo.</strong> Um projeto pode dar nome a uma rua ou criar um “dia de” alguma coisa. Outro pode mudar a vida de milhões. Na contagem, valem o mesmo.</li>
<li><strong>Lei ruim também conta.</strong> Quem aprova muitos projetos que favorecem um setor às custas de todos sobe no ranking e piora o país.</li>
<li><strong>Aprovar depende de poder, não só de mérito.</strong> Ajuda estar na base do governo, em um partido grande ou em bons cargos. Um oposicionista pode ter boas ideias e ver todas barradas.</li>
<li><strong>O Executivo pesa muito.</strong> Figueiredo e Limongi mostraram que, no Brasil pós-1988, o governo domina a agenda e é autor de boa parte das leis aprovadas. Assim, parlamentares têm poucas leis em seu nome, mesmo trabalhando muito.</li>
<li><strong>Autoria esconde o trabalho real.</strong> O relator muitas vezes reescreve o texto. Quem barrou um projeto ruim não ganha ponto nenhum.</li>
<li><strong>Vira incentivo errado.</strong> Se o eleitor premia o número, o político apresenta projetos em massa, muitos só para a foto.</li>
</ul>
<h2>Compare dois deputados</h2>
<table><thead><tr><th></th><th>Deputado A</th><th>Deputada B</th></tr></thead><tbody>
<tr><td>Projetos aprovados</td><td><strong>32</strong></td><td><strong>2</strong></td></tr>
<tr><td>O que aprovaram</td><td>28 homenagens e nomes de vias; 4 benefícios a um setor que financiou a campanha</td><td>Regras para reduzir a mortalidade materna; transparência em emendas</td></tr>
<tr><td>Como votou</td><td>Contra a transparência</td><td>A favor, inclusive contra o próprio partido</td></tr>
<tr><td>Fiscalização</td><td>Nenhuma</td><td>Relatou uma CPI e barrou um gasto irregular</td></tr>
</tbody></table>
<p class="legenda">Exemplo fictício. No ranking de quantidade, A ganha de longe.</p>
<h2>O que olhar no lugar</h2>
<ol class="roteiro">
<li><strong>Que interesses defende?</strong> Quem financiou a campanha e quem ganha com suas pautas? Veja no <a href="https://divulgacandcontas.tse.jus.br/" target="_blank" rel="noopener">DivulgaCandContas</a>.</li>
<li><strong>Como vota?</strong> É o dado mais importante. O voto mostra de que lado a pessoa fica quando há conflito. Veja na <a href="https://www.camara.leg.br/busca-portal/votacoes" target="_blank" rel="noopener">Câmara</a>, no <a href="https://www12.senado.leg.br/" target="_blank" rel="noopener">Senado</a> e em <a href="ferramentas/como-votaram.html">como os partidos votaram</a>.</li>
<li><strong>O que propõe?</strong> Leia as propostas, inclusive as que não passaram. Elas resolvem um problema real? Com quais evidências?</li>
<li><strong>Para onde vão suas emendas?</strong> Dinheiro público também revela prioridades.</li>
<li><strong>Fiscaliza?</strong> CPIs, relatorias e pedidos de informação contam.</li>
<li><strong>É coerente?</strong> O que disse na campanha bate com o que fez no mandato?</li>
</ol>
<div class="nota"><strong>Para guardar:</strong> a pergunta não é “quantos projetos aprovou?”, e sim “a favor de quem, e com que efeito?”. Vale o mesmo para rankings de políticos e notas prontas: veja quais critérios usam, porque todo critério carrega valores.</div>
''', fontes=[('Executivo e Legislativo na nova ordem constitucional', 'https://www.google.com/search?tbm=bks&q=Figueiredo+Limongi+Executivo+e+Legislativo+na+nova+ordem+constitucional'), ('Portal da Câmara: votações', 'https://www.camara.leg.br/busca-portal/votacoes'), ('TSE: DivulgaCandContas', 'https://divulgacandcontas.tse.jus.br/'), ('Politize!', 'https://www.politize.com.br/')])

DESPOLITIZADO = dict(slug='perigo-de-ser-despolitizado', titulo='O perigo de ser despolitizado', resumo='Parece que as decisões políticas não afetam seu dia a dia. Elas afetam, do café da manhã à hora de dormir.', corpo='''
<p class="abre">“Não gosto de política, ela não muda nada na minha vida.” A frase é comum e compreensível. O problema é que a política continua decidindo sobre a sua vida, mesmo que você não acompanhe.</p>
<p>Ela parece distante porque quase nunca aparece com etiqueta. Ninguém vê uma lei na conta de luz ou um voto no preço do ônibus. Vê só o resultado, e pensa que “é assim mesmo”.</p>
<h2>Um dia comum</h2>
<table><thead><tr><th>Quando</th><th>O que você vive</th><th>A decisão por trás</th></tr></thead><tbody>
<tr><td>Ao acordar</td><td>Água na torneira, esgoto, luz</td><td>Regras de saneamento e energia, tarifas e concessões</td></tr>
<tr><td>No café</td><td>Preço do pão e do leite</td><td>Impostos sobre consumo, juros, câmbio, política agrícola</td></tr>
<tr><td>No caminho</td><td>Ônibus, buraco, segurança</td><td>Tarifa e obras da prefeitura; policiamento do estado</td></tr>
<tr><td>No trabalho</td><td>Salário mínimo, férias, FGTS</td><td>Leis trabalhistas votadas no Congresso</td></tr>
<tr><td>Na escola</td><td>Vaga, merenda, currículo</td><td>Orçamento e regras municipais, estaduais e federais</td></tr>
<tr><td>Na saúde</td><td>Posto, vacina, remédio</td><td>SUS, Anvisa, verba para cada área</td></tr>
<tr><td>À noite</td><td>Internet, redes sociais, notícias</td><td>Regras de telecomunicações e decisões sobre plataformas</td></tr>
<tr><td>No futuro</td><td>Aposentadoria, clima, dívida</td><td>Reformas e escolhas feitas agora</td></tr>
</tbody></table>
<h2>“Política e futebol não se discutem”: um tremendo engano</h2>
<p>Poucas frases são tão repetidas no Brasil, e poucas fazem tanto mal. Ela costuma vir com boa intenção, para evitar briga no almoço de domingo. Mas confunde duas coisas: <strong>brigar</strong> e <strong>discutir</strong>.</p>
<ul>
<li><strong>Política se discute porque decide a vida de todos.</strong> Você não pode trocar de país como troca de assunto. Se não dá para conversar sobre impostos, saúde e escola, como decidir juntos?</li>
<li><strong>O silêncio não é neutro.</strong> Quando a maioria se cala, as decisões ficam com quem tem dinheiro, cargo ou lobby. A frase protege quem prefere não ser questionado.</li>
<li><strong>Política não é torcida.</strong> O time do coração é escolhido por amor e não precisa de argumento. Um voto afeta os outros e precisa de razões. Tratar político como time é justamente o que impede a conversa: veja o <a href="perigo-do-tribalismo.html">tribalismo</a>.</li>
<li><strong>Até o futebol é político.</strong> Estádios da Copa de 2014 usaram dinheiro público, leis regulam clubes e dívidas, e a ditadura explorou o tricampeonato de 1970. A Democracia Corintiana mostrou o caminho oposto, com jogadores votando e pedindo eleições diretas.</li>
</ul>
<p>A frase certa seria outra: <strong>política se discute, mas com respeito.</strong> Dá para ouvir, perguntar “por que você pensa assim?”, admitir que não sabe e encerrar a conversa quando esquentar.</p>
<h2>Quem sai ganhando quando você não olha</h2>
<ul>
<li><strong>Grupos organizados não se ausentam.</strong> Setores com lobby acompanham cada vírgula. Se o cidadão comum sai de cena, sobra quem tem interesse direto.</li>
<li><strong>Sem cobrança, o mau político fica mais barato.</strong> Quem não é vigiado corre menos risco.</li>
<li><strong>“São todos iguais” ajuda os piores.</strong> Se não há diferença, ninguém é punido por fazer mal.</li>
<li><strong>Quem menos tem costuma pagar mais.</strong> Quem tem dinheiro paga escola, saúde e segurança privadas. Quem não tem depende mais das decisões públicas.</li>
</ul>
<p>A pandemia mostrou isso com clareza: compra de vacinas, auxílio emergencial e regras para escolas viraram, em semanas, questão de renda, saúde e vida.</p>
<h2>O que despolitizado não quer dizer</h2>
<p>Você não precisa ter partido, brigar na internet nem acompanhar todas as notícias. Cansar-se do tema é legítimo, sobretudo com tanto ódio no debate. Politizar-se também não é virar torcedor: <a href="perigo-do-messianismo.html">isso traz outros perigos</a>.</p>
<h2>O mínimo que já muda muito</h2>
<ol class="roteiro"><li>Escolha um tema que te afeta e acompanhe só ele.</li><li>Pesquise antes de votar, inclusive para vereador e deputado. Use a <a href="ferramentas/ficha-do-candidato.html">ficha do candidato</a>.</li><li>Saiba <a href="cargos.html">quem cobrar</a> por cada problema.</li><li>Olhe uma fonte confiável por semana. Veja <a href="acompanhar.html">onde acompanhar</a>.</li><li>Participe de algo perto: conselho da escola, associação de bairro ou audiência pública.</li></ol>
<div class="nota"><strong>Para guardar:</strong> você pode não se interessar por política, mas as decisões políticas continuarão se interessando por você.</div>
''', fontes=[('Democracia Corintiana (Wikipédia)', 'https://pt.wikipedia.org/wiki/Democracia_Corintiana'), ('Politize!', 'https://www.politize.com.br/'), ('Toda Política: cidadania', 'https://www.todapolitica.com/'), ('Agência Senado', 'https://www12.senado.leg.br/noticias'), ('Tudo que você precisa saber para votar', 'https://julismo.wordpress.com/2018/08/16/tudo-que-voce-precisa-saber-para-votar-da-melhor-forma-possivel/')])

NEM_TUDO = dict(slug='nem-tudo-e-politico', grupo='Perguntas difíceis', titulo='Nem tudo é político', resumo='Muita coisa tem um lado político, mas gostar de azul não é uma posição de governo. Por que tanta gente diz o contrário?', corpo='''
<p class="abre">“Tudo é político” virou frase pronta. Ela guarda uma verdade importante, mas, levada ao pé da letra, é falsa. Se tudo é político, a palavra deixa de distinguir qualquer coisa.</p>
<h2>O que não é político</h2>
<ul>
<li><strong>Preferências estéticas:</strong> gostar mais de azul do que de verde, ou de um acorde, de uma pintura ou do sabor da manga.</li>
<li><strong>Decisões pessoais:</strong> que caminho fazer até o trabalho, que livro ler hoje, com quem passar o domingo.</li>
<li><strong>Fatos do mundo:</strong> a água ferver ou uma estrela existir não depende de opinião política. O que fazemos com esse conhecimento é outra história.</li>
<li><strong>Experiências íntimas:</strong> sentir saudade, achar um pôr do sol bonito.</li>
</ul>
<p>Política, como vimos, é a forma de decidir o que vale para todos: envolve poder, regras coletivas e disputa sobre elas. Quem prefere azul não está reivindicando que os outros sejam obrigados a preferir azul.</p>
<h2>Um teste de três perguntas</h2>
<ol class="roteiro"><li><strong>Envolve regra ou decisão coletiva?</strong> Lei, orçamento, norma, instituição.</li><li><strong>Há disputa de poder ou de recursos?</strong> Alguém ganha ou perde por causa disso?</li><li><strong>Afeta quem não escolheu?</strong> Tem efeito sobre outras pessoas ou seres?</li></ol>
<p>Se a resposta for não às três, é difícil chamar de político.</p>
<h2>O contexto muda as coisas</h2>
<table><thead><tr><th>A mesma coisa</th><th>Não é política quando…</th><th>Passa a ser quando…</th></tr></thead><tbody>
<tr><td>Camisa amarela</td><td>Você gostou da cor</td><td>É usada como símbolo em um ato</td></tr>
<tr><td>Uma música</td><td>Você ouve porque é bonita</td><td>Um governo a censura</td></tr>
<tr><td>O que comer</td><td>Você prefere manga a uva</td><td>Discute-se subsídio, rotulagem ou o sofrimento de animais</td></tr>
<tr><td>Ter filhos</td><td>É uma escolha do casal</td><td>Discute-se creche ou licença-maternidade</td></tr>
</tbody></table>
<p>Ter uma <em>dimensão</em> política não torna algo inteiro político. Uma comida tem preço, regulação e impacto, e também tem sabor. Uma coisa não apaga a outra.</p>
<h2>Por que as pessoas dizem isso</h2>
<ul>
<li><strong>“O pessoal é político.”</strong> A expressão ficou conhecida no feminismo dos anos 1960 e 1970, em texto de Carol Hanisch. Mostrava que problemas tratados como privados, como violência doméstica e divisão do trabalho em casa, tinham causas e soluções coletivas. Foi uma descoberta valiosa.</li>
<li><strong>A neutralidade pode esconder escolhas.</strong> Muitas vezes, quem diz “isso não é político” só está defendendo a situação atual como se fosse natural. A frase serve para lembrar isso.</li>
<li><strong>Tudo tem regras em volta.</strong> O ar, a comida e a internet são regulados. Daí é fácil saltar de “tudo é afetado pela política” para “tudo é político”.</li>
<li><strong>Identidade.</strong> Com a polarização, gostos viram sinal de time: carro, cerveja e cantor passam a indicar um lado.</li>
<li><strong>Atenção e mobilização.</strong> Redes premiam conflito. Para quem milita, politizar mais temas também aumenta o engajamento.</li>
<li><strong>Atalho retórico.</strong> Às vezes, a frase encerra a conversa sem que se explique qual é a relação política naquele caso específico.</li>
</ul>
<h2>Por que vale manter o limite</h2>
<ul>
<li><strong>Protege a liberdade.</strong> Regimes totalitários tentaram politizar a arte, a família e a vida privada. A ideia de que há uma esfera privada é uma proteção contra isso. Hannah Arendt dedicou boa parte de sua obra a essa distinção entre público e privado.</li>
<li><strong>Protege as relações.</strong> Se o gosto de alguém vira prova de caráter, amizades e famílias viram campo de batalha.</li>
<li><strong>Protege a própria política.</strong> Quando tudo é urgente e político, sobra menos atenção para o que é, de fato, decisão coletiva.</li>
</ul>
<div class="nota"><strong>Equilíbrio:</strong> os dois erros existem. Dizer que “isso não é político” para fugir de uma questão coletiva real, como foi feito com a violência doméstica, e dizer que “tudo é político” para julgar o gosto dos outros. Quando ouvir a frase, peça o elo: “qual é a regra, o poder ou o efeito coletivo aqui?”.</div>
<p>Esse limite não contradiz o <a href="perigo-de-ser-despolitizado.html">perigo de ser despolitizado</a>: as decisões políticas afetam quase toda a sua vida, e nem por isso cada parte da sua vida é uma decisão política.</p>
''', fontes=[('The Personal Is Political', 'https://en.wikipedia.org/wiki/The_personal_is_political'), ('A condição humana', 'https://pt.wikipedia.org/wiki/Hannah_Arendt'), ('Binarismo político', 'https://julismo.wordpress.com/2016/03/09/binarismo-politico/')])

META = {
 'nem-tudo-e-politico': (['fundamentos', 'ideologia'], ('Qual destes não é, por si só, político?', ['A regra de quem paga imposto', 'Preferir azul a verde', 'A censura de uma música'], 1, 'Sem regra, poder ou efeito coletivo, é só um gosto pessoal.')),
 'perigo-de-ser-despolitizado': (['fundamentos', 'perigos'], ('Quem ganha quando o cidadão comum para de acompanhar a política?', ['Ninguém, porque nada muda', 'Grupos organizados com interesses diretos', 'Só a oposição'], 1, 'As decisões continuam sendo tomadas, com menos gente olhando.')),
 'o-que-e-politica': (['fundamentos'], ('De onde vem a palavra “política”?', ['Do latim “politus”, educado', 'Do grego “pólis”, a cidade', 'Do francês “politesse”'], 1, 'Pólis era a cidade-Estado grega; “politiká”, os assuntos dela.')),
 'o-que-esta-por-tras': (['fundamentos', 'etica'], ('Qual pista revela mais sobre os interesses de um político?', ['O slogan da campanha', 'Os votos e quem financiou', 'O número de seguidores'], 1, 'Discurso é fácil. Votos e dinheiro deixam registro público.')),
 'valores-e-decisoes': (['etica', 'fundamentos'], ('“O salário mínimo maior reduz empregos?” é uma pergunta…', ['De valor', 'De fato', 'De opinião, sem resposta'], 1, 'É empírica: estudos ajudam a responder, ainda que o resultado varie com o contexto.')),
 'etica-normativa': (['etica'], ('“Uma política é boa se melhora a vida dos afetados” é típico do…', ['Consequencialismo', 'Deontologia', 'Relativismo'], 0, 'O consequencialismo avalia pelos resultados.')),
 'esquerda-e-direita': (['ideologia'], ('De onde vêm os termos esquerda e direita?', ['Da Guerra Fria', 'Da Revolução Francesa', 'Do Império Romano'], 1, 'Dos lugares em que os deputados sentavam na assembleia francesa de 1789.')),
 'palavras-em-disputa': (['ideologia', 'etica'], ('“Quem passa fome não é livre” usa qual ideia de liberdade?', ['Liberdade negativa', 'Liberdade positiva', 'Liberdade de mercado'], 1, 'Liberdade positiva é ter condições reais de escolher.')),
 'democracia': (['democracia'], ('Só fazer eleições torna um país uma democracia?', ['Sim', 'Não, ela exige direitos, imprensa livre e tribunais independentes', 'Só se houver dois turnos'], 1, 'Ditaduras também fazem eleições.')),
 'como-votar-bem': (['eleicoes', 'brasil'], ('Votos em branco e nulos…', ['Vão para o 1º colocado', 'Anulam a eleição se passarem de 50%', 'Não entram nos votos válidos'], 2, 'Ficam de fora da conta. Essas duas lendas são recorrentes.')),
 'checagem-de-fatos': (['desinformacao'], ('Qual a primeira atitude diante de um conteúdo que te deu muita raiva?', ['Compartilhar logo', 'Respirar e checar', 'Procurar quem concorda'], 1, 'Emoção forte é o combustível da desinformação.')),
 'sem-binarismo': (['ideologia', 'mente'], ('O que ajuda em um debate polarizado?', ['Vencer a qualquer custo', 'Explicar a posição do outro de um jeito que ele aceitaria', 'Só debater com quem concorda'], 1, 'Mostra que você entendeu antes de discordar.')),
 'vieses-cognitivos': (['mente'], ('No estudo de Westen (2006), partidários…', ['Viam as contradições nos dois lados', 'Viam mais as do adversário', 'Não viam nenhuma'], 1, 'E minimizavam as do próprio candidato. É o raciocínio motivado.')),
 'mente-moralista': (['mente', 'etica'], ('Para Haidt, o que vem primeiro no julgamento moral?', ['A razão', 'A intuição', 'A lei'], 1, 'O elefante (intuição) anda, e o condutor (razão) justifica.')),
 'teoria-da-ferradura': (['ideologia'], ('Onde a teoria da ferradura acerta mais?', ['Os extremos têm as mesmas ideias', 'Os extremos podem partilhar métodos autoritários', 'O centro sempre tem razão'], 1, 'Métodos parecidos não significam fins iguais.')),
 'comparar-projetos': (['economia'], ('Qual pergunta testa melhor uma promessa?', ['Quem é o candidato?', 'Por qual mecanismo funciona e quem paga?', 'Ela parece bonita?'], 1, 'Sem mecanismo e custo, é só slogan.')),
 'bem-comum': (['etica'], ('O “véu da ignorância” é de qual filósofo?', ['Rawls', 'Nozick', 'Burke'], 0, 'Rawls pede que escolhamos regras sem saber em que posição nasceremos.')),
 'politicas-publicas': (['economia', 'brasil'], ('Qual lei define quanto entra e sai no ano?', ['PPA', 'LDO', 'LOA'], 2, 'A LOA é o orçamento anual.')),
 'perigo-das-revolucoes': (['perigos', 'ideologia'], ('Por que revoluções costumam concentrar poder?', ['Porque quem toma o poder pela força raramente o devolve', 'Porque sempre há rei', 'Porque não há problemas reais'], 0, 'A injustiça pode ser real, e o novo poder, pior.')),
 'perigo-do-reacionarismo': (['perigos', 'ideologia'], ('O que distingue reacionário de conservador?', ['O reacionário quer voltar atrás e reverter conquistas', 'São sinônimos', 'O conservador quer revolução'], 0, 'O conservador prefere mudar devagar.')),
 'perigo-do-messianismo': (['perigos'], ('Qual é um sinal de alerta?', ['Criticar seu candidato', 'Não conseguir citar um erro grave dele', 'Ler o plano de governo'], 1, 'Político é funcionário público, não salvador.')),
 'perigo-do-maniqueismo': (['perigos', 'mente'], ('O maniqueísmo divide o mundo em…', ['Bem absoluto e mal absoluto', 'Ricos e pobres', 'Norte e sul'], 0, 'E contra o “mal absoluto” parece valer tudo.')),
 'perigo-do-fanatismo': (['perigos'], ('O que protege contra o fanatismo?', ['Mais certeza', 'Saber que fatos fariam você mudar', 'Evitar quem discorda'], 1, 'Ter convicção é bom, mas sem imunidade a evidências.')),
 'numero-de-projetos': (['perigos', 'brasil'], ('O que diz mais sobre um parlamentar?', ['O número de leis aprovadas', 'Como vota e a quem suas pautas beneficiam', 'A quantidade de discursos'], 1, 'O número sozinho não mostra conteúdo nem interesses.')),
 'estado-e-mercado': (['economia', 'perigos'], ('Qual a pergunta útil sobre estatizar ou privatizar?', ['Qual lado é melhor sempre?', 'Nesse setor, qual arranjo entrega mais a quem precisa?', 'O que meu partido diz?'], 1, 'Depende do setor, da regulação e do contexto.')),
 'religiao-e-estado': (['perigos', 'democracia'], ('Estado laico significa…', ['Proibir religião', 'Não adotar nem perseguir crenças', 'Governo ateu'], 1, 'Ele protege quem crê e quem não crê.')),
 'poder-paralelo': (['perigos', 'brasil'], ('O que é “captura” do governo?', ['Quando quem não foi eleito dirige decisões', 'Um tipo de eleição', 'Prisão de um ministro'], 0, 'Mercado, mídia e crime podem capturar eleitos.')),
 'um-sistema-para-todos': (['perigos', 'economia'], ('Por que copiar um sistema de outro país pode falhar?', ['Depende de história, instituições e tamanho', 'Leis não funcionam fora', 'Só funciona em países pequenos'], 0, 'Pergunte o que tornava aquilo possível lá.')),
 'regras-e-desobediencia': (['perigos', 'democracia'], ('Qual destes é desobediência civil?', ['Invadir prédios para anular uma eleição', 'Protesto público e não violento contra lei injusta', 'Sonegar para ganhar mais'], 1, 'É pública, não violenta e busca corrigir uma injustiça.')),
 'perigo-de-questionar-a-democracia': (['perigos', 'democracia'], ('Qual é uma crítica saudável?', ['“Fechem o STF”', '“O STF errou nesta decisão”', '“Só um golpe resolve”'], 1, 'Criticar decisões faz parte; abolir os freios, não.')),
 'liberdade-de-expressao': (['democracia', 'etica'], ('O paradoxo da tolerância é de…', ['Mill', 'Popper', 'Rawls'], 1, 'Tolerância ilimitada pode destruir a própria tolerância.')),
 'respeitar-crencas': (['etica', 'mente'], ('Qual a distinção central?', ['Respeitar pessoas não é considerar toda ideia correta', 'Toda crença é igualmente verdadeira', 'Crenças não têm efeitos'], 0, 'Pessoas merecem respeito; ideias, exame.')),
 'atores-malevolentes': (['perigos'], ('Qual NÃO faz parte da Tétrade Sombria?', ['Sadismo', 'Maquiavelismo', 'Populismo'], 2, 'Populismo é estilo político. Os quatro traços são narcisismo, maquiavelismo, psicopatia e sadismo.')),
 'fanatismo-ideologico': (['perigos', 'ideologia'], ('Os autores tratam o fanatismo como…', ['Um contínuo', 'Exclusivo de um lado', 'Coisa do passado'], 0, 'Formas leves ficam próximas de vieses comuns.')),
 'direta-ou-epistocracia': (['democracia'], ('Quem defende a epistocracia?', ['Jason Brennan', 'Rousseau', 'Norberto Bobbio'], 0, 'Brennan, em Against Democracy.')),
 'melhorar-a-democracia': (['democracia', 'eleicoes'], ('No voto preferencial, você…', ['Vota em um só', 'Ordena os candidatos', 'Vota duas vezes'], 1, 'Isso reduz o voto útil.')),
 'politicas-baseadas-em-evidencias': (['economia', 'democracia'], ('Qual é a evidência mais fraca?', ['Revisão sistemática', 'Experimento aleatorizado', 'Caso e opinião'], 2, 'Casos são ilustrativos, mas não provam efeito.')),
 'sencientismo': (['etica'], ('Qual o critério do sencientismo?', ['Ser humano', 'Poder sentir', 'Ser racional'], 1, 'Quem pode sofrer conta moralmente.')),
 'teorias-da-justica': (['etica', 'economia'], ('“É justo o que resulta de trocas voluntárias” é de…', ['Rawls', 'Nozick', 'Sen'], 1, 'Nozick, em Anarquia, Estado e Utopia.')),
 'presidencialismo-de-coalizao': (['brasil', 'democracia'], ('Quem criou o termo “presidencialismo de coalizão”?', ['Sérgio Abranches', 'FHC', 'Ulysses Guimarães'], 0, 'Abranches, em 1988.')),
}
