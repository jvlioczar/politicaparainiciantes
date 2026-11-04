"""Camada didática de cada lição: objetivos (o que você vai aprender), pontos para guardar, uma pergunta para pensar
e lições que ajudam ter lido antes. Também traz seções extras para as lições mais curtas.
Cada entrada: slug -> dict(obj=[3], guardar=[3], pensar='...', pre=[slugs])."""

D = {
# ---------- Iniciante ----------
'o-que-e-politica': dict(
 obj=['Definir política como a disputa sobre o que vale para todos, e não só como eleição', 'Separar poder, autoridade e legitimidade', 'Distinguir Estado, governo e nação'],
 guardar=['Política é decidir o que vale para todos: quem decide, o que se decide e quem paga a conta.', 'Ela acontece no condomínio, na escola e no trabalho, não só na urna.', 'Estado é permanente; governo passa; nação é o povo que se reconhece como tal.'],
 pensar='Pense na última regra que mudou no seu prédio, escola ou trabalho: quem decidiu, quem foi ouvido e quem pagou a conta?', pre=[]),
'perigo-de-ser-despolitizado': dict(
 obj=['Enxergar as decisões políticas escondidas em um dia comum', 'Identificar quem ganha quando a maioria deixa de acompanhar', 'Diferenciar desconfiança saudável de desistência'],
 guardar=['Não acompanhar política não te tira dela: as decisões continuam valendo para você.', 'Quem mais ganha com o afastamento do eleitor comum é quem tem interesse concentrado e dinheiro para pressionar.', 'O mínimo já muda muito: saber em quem votou, ler uma checagem, olhar como seu deputado vota.'],
 pensar='Liste três coisas que você fez hoje e tente descobrir que decisão pública está por trás de cada uma.', pre=['o-que-e-politica']),
'o-que-esta-por-tras': dict(
 obj=['Ler incentivos: o que recompensa cada atitude de um político', 'Reconhecer o padrão de benefício concentrado e custo espalhado', 'Investigar interesses sem cair no cinismo de que “são todos iguais”'],
 guardar=['Discurso é o que aparece; incentivo é o que explica.', 'Quando poucos ganham muito e muitos perdem pouco, os poucos se organizam e os muitos nem percebem.', 'Desconfiar é útil; achar que tudo é farsa só protege quem se beneficia do silêncio.'],
 pensar='Escolha uma votação recente no Congresso e pergunte: quem ganha de forma concentrada e quem paga de forma espalhada?', pre=['o-que-e-politica']),
'valores-e-decisoes': dict(
 obj=['Separar a pergunta moral (o que queremos) da pergunta factual (o que funciona)', 'Reconhecer a guilhotina de Hume: fatos não decidem valores sozinhos', 'Analisar uma proposta em três camadas: valor, meio e evidência'],
 guardar=['Todo debate político tem duas perguntas dentro: o que devemos querer e o que funciona para chegar lá.', 'Dados resolvem a parte factual; valores precisam de argumento moral.', 'A maior parte das brigas mistura as duas camadas, e por isso ninguém se entende.'],
 pensar='Pegue uma frase política que você ouviu esta semana e separe: o que nela é valor, e o que é fato que dá para checar?', pre=['o-que-e-politica']),
'etica-normativa': dict(
 obj=['Reconhecer as três famílias da ética: consequências, deveres e caráter', 'Ver como cada uma pesa diferente ao julgar uma lei', 'Perguntar quem entra na conta: o círculo moral'],
 guardar=['Consequencialismo olha o resultado; deontologia, o dever e o direito; ética das virtudes, o caráter de quem age.', 'Ponto focal não é exclusividade: quase todo mundo mistura as três.', 'A pergunta sobre quem conta, o círculo moral, muda a resposta de todas as outras.'],
 pensar='Diante de uma lei que beneficia a maioria mas prejudica uma minoria, qual pergunta você faria primeiro: o resultado total, o direito violado ou o que isso diz de quem a aprovou?', pre=['valores-e-decisoes']),
'esquerda-e-direita': dict(
 obj=['Saber de onde vêm os rótulos e o que cada lado costuma valorizar', 'Usar mais de um eixo: economia e costumes', 'Entender por que o rótulo orienta, mas não substitui olhar cada proposta'],
 guardar=['Os termos nasceram na assembleia francesa de 1789 e mudam de sentido conforme a época e o país.', 'Um eixo só não basta: alguém pode ser liberal na economia e conservador nos costumes, ou o contrário.', 'Moderado não é sinônimo de certo, e extremo não é sinônimo de errado: o que vale é o argumento.'],
 pensar='Onde você se colocaria em cada um dos dois eixos? A resposta é a mesma para todos os temas?', pre=['valores-e-decisoes']),
'palavras-em-disputa': dict(
 obj=['Perceber que liberdade e conservar têm sentidos diferentes para cada lado', 'Pedir definição antes de concordar ou discordar', 'Reconhecer o truque de trocar a palavra para vencer o debate'],
 guardar=['Liberdade pode ser ausência de interferência ou capacidade real de agir: os dois lados usam a mesma palavra.', 'Antes de discutir, pergunte: o que você quer dizer com isso?', 'Quem controla o sentido da palavra já ganhou metade da discussão.'],
 pensar='Quando alguém diz “defendo a liberdade”, de que liberdade você acha que está falando? E se fosse alguém do outro lado?', pre=['esquerda-e-direita']),
'sem-binarismo': dict(
 obj=['Reconhecer quando um debate virou jogo de torcida', 'Encontrar pontos em comum que a polarização esconde', 'Praticar formas de discordar sem odiar'],
 guardar=['Em um embate, a meta é vencer; em um debate, é entender.', 'Exageramos o quanto o outro lado é radical, e as pesquisas mostram isso nos dois lados.', 'Discordar é parte da democracia; tratar o adversário como inimigo é o que a destrói.'],
 pensar='Lembre da última discussão política que você teve: você queria entender a outra pessoa ou vencê-la?', pre=['esquerda-e-direita']),
'democracia': dict(
 obj=['Listar o que precisa existir junto com a eleição para haver democracia', 'Reconhecer como democracias morrem hoje, pelas mãos de eleitos', 'Entender por que a maioria não pode tudo'],
 guardar=['Eleição sozinha não basta: ditaduras também fazem eleições.', 'Democracia inclui direitos, imprensa livre, tribunais independentes e alternância pacífica.', 'Direitos básicos existem para não depender da maioria do momento.'],
 pensar='Se um governo que você apoia ganhasse a eleição e depois enfraquecesse os tribunais e a imprensa, você consideraria isso aceitável?', pre=['o-que-e-politica']),
'como-uma-lei-e-feita': dict(
 obj=['Seguir o caminho de um projeto, da proposta à sanção', 'Saber quem pode barrar uma lei: comissões, plenário, veto e STF', 'Diferenciar maioria simples, absoluta e qualificada'],
 guardar=['Uma lei passa por comissões e pelos plenários das duas casas, pode ser vetada e ainda derrubada pelo STF.', 'Nem toda regra é lei: decretos, portarias e medidas provisórias seguem caminhos próprios.', 'Mudar a Constituição exige três quintos em duas votações em cada casa, e as cláusulas pétreas nem assim.'],
 pensar='Pense em uma lei que você gostaria que existisse: por onde ela teria de passar, e em que ponto seria mais fácil barrá-la?', pre=['democracia']),
'o-que-e-um-partido': dict(
 obj=['Entender o que um partido faz antes, durante e depois da eleição', 'Saber de onde vem o dinheiro dos partidos', 'Avaliar um partido por mais do que o nome e o discurso'],
 guardar=['No Brasil ninguém se elege sem partido: ele escolhe candidatos, organiza a campanha e forma blocos no Congresso.', 'O dinheiro vem sobretudo de fundos públicos, distribuídos pelas cúpulas partidárias.', 'Para avaliar um partido, veja como ele votou, com quem se alia e quem o financia.'],
 pensar='Você sabe de que partido são o deputado e o senador em quem votou? E como esse partido votou nos últimos projetos importantes?', pre=['democracia']),
'como-votar-bem': dict(
 obj=['Aplicar quatro passos: história, propostas, números e pensar além de si', 'Entender como votos viram cadeiras no Legislativo', 'Evitar as armadilhas mais comuns na hora de votar'],
 guardar=['Votar bem é conhecer a história, ler a proposta, checar o número e pensar em quem não é você.', 'Seu voto para deputado conta para o partido e para a federação, não só para a pessoa.', 'O trabalho não acaba na urna: acompanhar o eleito faz parte do voto.'],
 pensar='Para o próximo voto, que fonte você consultaria para checar a história do candidato antes de olhar a propaganda?', pre=['o-que-e-um-partido', 'checagem-de-fatos']),
'checagem-de-fatos': dict(
 obj=['Aplicar o teste de dois minutos antes de compartilhar', 'Reconhecer os tipos mais comuns de desinformação', 'Saber onde checar, com as principais agências'],
 guardar=['Mentira viraliza porque mexe com a emoção: raiva e medo fazem compartilhar sem pensar.', 'Antes de compartilhar, pare, procure a fonte original e veja se as agências já checaram.', 'Compartilhar sem checar faz de você parte da corrente, mesmo sem intenção.'],
 pensar='Qual foi a última notícia política que você compartilhou? Você conseguiria dizer de onde ela veio originalmente?', pre=[]),

# ---------- Intermediário ----------
'contrato-social': dict(
 obj=['Entender por que obedecemos a leis que nunca assinamos', 'Diferenciar Hobbes, Locke, Rousseau e Rawls', 'Conhecer as críticas: ninguém assinou esse contrato'],
 guardar=['A autoridade do governo vem de um acordo, real ou hipotético, em que trocamos algo por proteção e direitos.', 'Hobbes quer ordem contra o caos; Locke, proteção de direitos; Rousseau, a vontade geral; Rawls, regras justas sob o véu da ignorância.', 'A ideia é uma ferramenta para avaliar governos, não um documento histórico.'],
 pensar='Que condição faria você considerar que o “contrato” foi quebrado pelo Estado?', pre=['democracia']),
'imposto-e-roubo': dict(
 obj=['Separar imposto de roubo com argumentos jurídicos e filosóficos', 'Conhecer a melhor versão do argumento contrário', 'Fazer perguntas melhores: quem paga, quanto e para quê'],
 guardar=['Imposto é a contrapartida do contrato social: paga o que é de todos.', 'Isso não torna todo imposto justo: ele pode ser mal distribuído e mal usado.', 'A pergunta útil não é “imposto sim ou não”, e sim quem paga, quanto e o que volta.'],
 pensar='Se você pudesse mudar um único imposto no Brasil, qual seria, e quem passaria a pagar mais ou menos?', pre=['contrato-social']),
'economia-para-entender-politica': dict(
 obj=['Entender PIB, inflação, juros, dívida e déficit sem fórmulas', 'Ver como essas peças se ligam e por que esquerda e direita brigam por elas', 'Não ser enganado por números: nominal e real, estoque e fluxo'],
 guardar=['Inflação corrói o salário; juros altos a contêm, mas freiam a economia e encarecem a dívida.', 'Déficit é o buraco do ano; dívida é o acumulado. Confundir os dois é comum e conveniente.', 'Um número sem comparação, sem período e sem a inflação descontada não diz nada.'],
 pensar='Quando ouvir “o governo gastou um recorde”, que três perguntas você faria antes de acreditar?', pre=['valores-e-decisoes']),
'geopolitica': dict(
 obj=['Entender como geografia, recursos e alianças explicam decisões de países', 'Diferenciar realismo e liberalismo nas relações internacionais', 'Situar o Brasil no jogo entre potências'],
 guardar=['Países agem por posição, recursos e segurança, não só por ideologia.', 'Realistas veem um jogo de poder; liberais apostam em instituições e comércio. Os dois enxergam parte do quadro.', 'O Brasil é grande, distante das principais tensões e dependente de exportar: isso molda sua diplomacia.'],
 pensar='Escolha uma decisão recente da diplomacia brasileira: ela se explica melhor por valores ou por interesse e posição?', pre=[]),
'globalizacao': dict(
 obj=['Entender o que circula na globalização e com que velocidade', 'Avaliar quem ganhou e quem perdeu', 'Conhecer as críticas de esquerda e de direita'],
 guardar=['A globalização tirou centenas de milhões da pobreza, sobretudo na Ásia, e deixou regiões industriais para trás.', 'Ela tem altos e baixos: avança, recua e muda de forma.', 'As críticas vêm dos dois lados: desigualdade e empregos, de um; soberania e identidade, de outro.'],
 pensar='Olhe a etiqueta de três coisas que você usa hoje: o que o Brasil ganha e o que perde com cada uma vindo de fora?', pre=['economia-para-entender-politica']),
'divisao-internacional-do-trabalho': dict(
 obj=['Distinguir divisão internacional do trabalho, modelo primário-exportador e teoria da dependência', 'Ler os números da pauta exportadora brasileira', 'Separar o que a evidência confirma do que ela contesta'],
 guardar=['Exportar matéria-prima não condena um país: Austrália, Canadá e Noruega mostram isso.', 'O problema é depender de poucos produtos sem agregar valor, pesquisa e instituições.', 'A desindustrialização precoce é real no Brasil, e as causas estão em disputa.'],
 pensar='Se exportar commodities não é o problema em si, o que explicaria a diferença entre o Brasil e a Austrália?', pre=['globalizacao', 'economia-para-entender-politica']),
'blocos-economicos': dict(
 obj=['Diferenciar os tipos de integração: zona de livre comércio, união aduaneira, mercado comum', 'Saber o que o BRICS não é e o que a OCDE não é', 'Entender o que o Brasil ganha e perde em cada clube'],
 guardar=['BRICS é um fórum político com um banco, não um mercado comum.', 'OCDE é um clube de boas regras, não um bloco comercial.', 'O Mercosul é uma união aduaneira incompleta, e isso explica boa parte das brigas sobre ele.'],
 pensar='Quando um político diz “sair do Mercosul” ou “entrar na OCDE”, que efeito concreto ele está prometendo?', pre=['globalizacao']),
'comparar-projetos': dict(
 obj=['Passar cada proposta pelas mesmas perguntas: o que, quanto, quem paga, que evidência', 'Comparar duas propostas passo a passo', 'Reconhecer promessas para desconfiar'],
 guardar=['Promessa sem custo e sem fonte de dinheiro não é proposta.', 'Compare projetos pelas mesmas perguntas, e não pelo discurso.', '“Vou acabar com” e “vou dobrar” pedem a pergunta: como, e com o dinheiro de onde?'],
 pensar='Pegue uma promessa de campanha de que você gostou e tente responder: quanto custa, quem paga e o que já se sabe sobre isso?', pre=['valores-e-decisoes', 'economia-para-entender-politica']),
'bem-comum': dict(
 obj=['Usar quatro lentes para pensar no bem comum', 'Entender por que o imediatismo vence e o longo prazo perde', 'Reconhecer bens públicos e o problema do carona'],
 guardar=['Teste de Rawls: se você não soubesse em que posição nasceria, aceitaria essa regra?', 'O bem comum inclui quem está pior, o básico para todos e quem ainda vai nascer.', 'Bens públicos pedem regras coletivas, porque o carona se beneficia sem pagar.'],
 pensar='Qual política que você apoia beneficia principalmente você? Ela passaria no teste do véu da ignorância?', pre=['valores-e-decisoes', 'contrato-social']),
'politicas-publicas': dict(
 obj=['Entender o ciclo de uma política pública, da agenda à avaliação', 'Conhecer as três leis do orçamento e por que sobra pouco para decidir', 'Saber de onde vem o dinheiro e onde fiscalizar'],
 guardar=['Política pública é a resposta concreta do Estado a um problema, e passa por um ciclo que pode falhar em cada etapa.', 'A maior parte do orçamento já está comprometida antes de qualquer decisão.', 'As emendas parlamentares cresceram e hoje são parte central da disputa pelo dinheiro.'],
 pensar='Escolha um problema da sua cidade: em que etapa do ciclo ele está travado, na agenda, na decisão ou na execução?', pre=['como-uma-lei-e-feita', 'economia-para-entender-politica']),
'vieses-cognitivos': dict(
 obj=['Reconhecer o raciocínio motivado no estudo de Westen', 'Entender por que temos vieses', 'Ver como eles atuam em uma eleição'],
 guardar=['Vemos a contradição do adversário na hora, e desculpamos a do nosso lado.', 'Vieses não são burrice: são atalhos que todo cérebro usa.', 'O antídoto é o hábito: aplicar ao seu lado a régua que usa no outro.'],
 pensar='Quando foi a última vez que você criticou publicamente um erro de alguém do seu próprio lado?', pre=['sem-binarismo']),
'mudar-de-ideia': dict(
 obj=['Separar as razões boas das razões ruins para mudar de posição', 'Reconhecer o bom ceticismo e suas falsificações', 'Praticar a revisão das próprias crenças'],
 guardar=['Mudar diante de argumento melhor ou evidência forte é honestidade; ceder à pressão não é.', 'Duvidar de tudo menos do próprio líder não é ceticismo.', 'Nenhuma conclusão é definitiva, e isso vale também para as suas.'],
 pensar='Qual foi a última opinião política que você mudou? O que te fez mudar?', pre=['vieses-cognitivos']),
'testar-visao-moral': dict(
 obj=['Aplicar três testes de imparcialidade: véu da ignorância, regra de ouro e universalidade', 'Perceber quando uma regra só parece boa porque favorece seu grupo', 'Conhecer os limites desses testes'],
 guardar=['Se a regra só parece boa enquanto você está do lado certo dela, não é um princípio: é um interesse.', 'Universalidade: você aceitaria a mesma regra aplicada pelo seu adversário?', 'Os testes não dão resposta final, mas revelam parcialidade com rapidez.'],
 pensar='Pegue a posição política que você mais defende e passe-a pelos três testes. Ela sobrevive aos três?', pre=['valores-e-decisoes', 'mudar-de-ideia']),
'mente-moralista': dict(
 obj=['Entender a metáfora do elefante e do condutor', 'Conhecer os fundamentos morais e os paladares de cada lado', 'Usar isso para conversar, sem concluir que descrever é aprovar'],
 guardar=['Julgamos primeiro por intuição; a razão costuma chegar depois, para justificar.', 'Progressistas pesam mais cuidado e justiça; conservadores distribuem o peso também por lealdade, autoridade e santidade.', 'Entender o paladar do outro ajuda a conversar, e não obriga a concordar.'],
 pensar='Pense em uma posição do outro lado que te parece absurda: que fundamento moral ela pode estar protegendo?', pre=['vieses-cognitivos', 'etica-normativa']),
'perigo-do-maniqueismo': dict(
 obj=['Reconhecer o maniqueísmo e por que ele é tão atraente', 'Admitir que existe mal de verdade sem dividir o mundo em luz e trevas', 'Pensar além do preto e branco em problemas complexos'],
 guardar=['Dividir o mundo em bem absoluto e mal absoluto simplifica, e por isso vende.', 'Problemas complexos não têm solução de uma frase.', 'Reconhecer o mal real não exige tratar todo adversário como monstro.'],
 pensar='Em que tema você tem mais dificuldade de admitir que o outro lado possa ter um ponto?', pre=['sem-binarismo']),
'perigo-do-fanatismo': dict(
 obj=['Identificar os sinais do fanatismo: certeza absoluta, inimigo total, vontade de punir', 'Diferenciar convicção de fanatismo', 'Saber como conversar com quem está nesse caminho'],
 guardar=['Fanático é quem não admite estar errado e aceita qualquer meio contra quem discorda.', 'Convicção firme convive com dúvida e com limites; fanatismo, não.', 'Ninguém sai do fanatismo por humilhação: sai por vínculo e por dúvida plantada aos poucos.'],
 pensar='Que evidência faria você mudar de ideia sobre a sua causa mais importante? Se não existe nenhuma, o que isso diz?', pre=['perigo-do-maniqueismo']),
'sofismo': dict(
 obj=['Reconhecer os truques de quem quer vencer sem ter razão', 'Diferenciar mentira, embromação e cinismo, com Frankfurt', 'Defender-se dos vendedores de ideias'],
 guardar=['Quando o objetivo é vencer, a verdade vira ferramenta: usada quando ajuda, descartada quando atrapalha.', 'O embromador não mente: é indiferente à verdade, o que pode ser pior.', 'Mudar de ideia com argumento não é sofisma; mudar conforme a plateia, sim.'],
 pensar='Lembre de um político que você admira: ele já mudou de discurso conforme a plateia? Você notou na hora?', pre=['checagem-de-fatos', 'palavras-em-disputa']),
'perigo-do-tribalismo': dict(
 obj=['Reconhecer o pacote de ideias que cada tribo vende', 'Entender o que as pesquisas mostram sobre pertencimento e opinião', 'Avaliar ideia por ideia, pelo mérito e pela viabilidade'],
 guardar=['Tribalismo é escolher o grupo primeiro e as opiniões depois.', 'Não há razão lógica para quem pensa X sobre impostos pensar Y sobre armas: o pacote é social, não racional.', 'Teste: há alguma posição em que você discorda do seu lado? Se não há, o pacote está pensando por você.'],
 pensar='Liste suas posições em cinco temas: quantas você examinou de verdade, e quantas vieram no pacote?', pre=['sem-binarismo', 'vieses-cognitivos']),
'politica-do-medo': dict(
 obj=['Entender como medo, raiva e nojo desligam a análise', 'Reconhecer a receita do alarmismo', 'Separar alerta honesto de manipulação'],
 guardar=['Quem está com medo procura proteção e pensa menos: por isso o medo é tão usado.', 'Alarmismo tem inimigo sob medida, urgência permanente e nenhuma proposta checável.', 'Nem todo medo é manipulação: o alerta honesto vem com dados, proporção e solução.'],
 pensar='Qual foi a última mensagem política que te deu medo? Ela trazia um dado checável ou só um inimigo?', pre=['checagem-de-fatos', 'vieses-cognitivos']),
'teoria-da-ferradura': dict(
 obj=['Entender o que a teoria da ferradura percebe bem', 'Saber o que ela não explica', 'Reconhecer seu uso errado para desqualificar adversários'],
 guardar=['Os extremos se parecem nos métodos: culto ao líder, inimigo total, desprezo por limites.', 'Nas ideias e nos projetos, continuam opostos.', 'Usar a ferradura para chamar qualquer crítico de extremista é o uso errado dela.'],
 pensar='Pense em um grupo de extrema-esquerda e um de extrema-direita que você conheça: em que se parecem e em que são opostos?', pre=['esquerda-e-direita']),
'perigo-das-revolucoes': dict(
 obj=['Reconhecer o padrão que se repete nas revoluções', 'Entender por que costumam concentrar poder', 'Fazer as perguntas certas antes de apoiar uma ruptura'],
 guardar=['Toda revolução começa com injustiça real; o perigo é acreditar que dá para redesenhar a sociedade do zero.', 'Quem toma o poder pela força precisa de força para mantê-lo, e por isso concentra.', 'Ruptura contra uma ditadura é diferente de ruptura contra uma democracia que desagrada.'],
 pensar='Que garantias você exigiria de um movimento que promete “refazer tudo” antes de apoiá-lo?', pre=['democracia']),
'perigo-do-reacionarismo': dict(
 obj=['Distinguir conservador, reacionário e ultraconservador', 'Entender por que a nostalgia de uma era de ouro funciona', 'Perceber que a tentação existe também na esquerda'],
 guardar=['Conservador quer mudar devagar; reacionário quer voltar atrás.', 'A era de ouro prometida nunca existiu como é lembrada: era melhor para alguns.', 'A nostalgia funciona porque o passado não tem incerteza; o futuro tem.'],
 pensar='Qual época você acha que “era melhor”? Melhor para quem, e o que você está deixando de fora?', pre=['esquerda-e-direita']),
'perigo-do-ultraconservadorismo': dict(
 obj=['Entender o erro de confundir antigo com bom', 'Ver como isso atinge, em grau menor, o conservadorismo comum', 'Separar o que vale manter do que precisa mudar'],
 guardar=['Uma tradição não é boa por ser antiga, nem ruim por ser antiga: precisa ser avaliada pelo que faz.', 'O conservadorismo acerta ao desconfiar de mudanças rápidas e ao valorizar o que já funciona.', 'Teste: a tradição protege alguém, ou protege o poder de alguém?'],
 pensar='Escolha uma tradição que você valoriza: qual é a melhor razão para mantê-la, além de ser antiga?', pre=['perigo-do-reacionarismo']),
'perigo-do-messianismo': dict(
 obj=['Reconhecer os sinais de alerta da idolatria política', 'Entender a porta de entrada: o outsider salvador', 'Admirar sem virar massa de manobra'],
 guardar=['Político é funcionário público, não salvador.', 'Quem tem um “mito” para de fiscalizar e passa a defender o indefensável.', 'Admirar é reconhecer acertos; idolatrar é não enxergar erros.'],
 pensar='Existe algum político de quem você defenderia qualquer atitude? O que ele teria de fazer para você deixar de apoiá-lo?', pre=['perigo-do-tribalismo']),
'perigo-do-populismo': dict(
 obj=['Definir populismo: povo puro contra elite corrupta, com um líder que fala por todos', 'Reconhecê-lo à esquerda e à direita', 'Diferenciar popular de populista'],
 guardar=['Populismo é um jeito de fazer política, não uma ideologia: existe à esquerda e à direita.', 'Seu traço mais perigoso é dizer que só ele representa o povo, e que por isso quem discorda não é povo.', 'Ser popular e falar simples não é populismo; atacar quem limita o poder é.'],
 pensar='Pense em um líder que você considera populista e em um que você apoia: os dois usam a ideia de que “só eu represento o povo”?', pre=['perigo-do-messianismo', 'democracia']),
'perigo-do-outsider': dict(
 obj=['Definir o que é um outsider de verdade', 'Entender por que atrai e o que costuma acontecer depois', 'Fazer as perguntas que separam renovação de marketing'],
 guardar=['“Não sou político” é uma promessa, não uma qualificação.', 'Sem partido e sem bancada, o outsider eleito precisa do mesmo Congresso que criticava.', 'Pergunte: o que ele já fez, com quem se aliou e o que faria sem maioria.'],
 pensar='Que experiência você exigiria de alguém para cuidar da sua saúde? E para cuidar do orçamento de um país?', pre=['perigo-do-messianismo']),
'perigo-de-culpar-o-estrangeiro': dict(
 obj=['Confrontar “eles são criminosos” e “roubam empregos” com os dados', 'Entender a loteria da vida e por que não há povos superiores', 'Separar amor ao país de desprezo pelo outro'],
 guardar=['Imigrantes, em geral, cometem menos crimes do que os nativos e ocupam vagas que ninguém queria.', 'Onde você nasceu é sorte, não mérito.', 'Discutir imigração é legítimo; usar o estrangeiro como bode expiatório é o truque mais antigo da política.'],
 pensar='Se você tivesse nascido no país mais pobre do mundo, que regras de imigração acharia justas?', pre=['politica-do-medo']),
'camaras-de-eco': dict(
 obj=['Entender como a radicalização acontece em grupos fechados', 'Reconhecer o caminho gradual, do red pill ao extremo', 'Saber como sair e como ajudar alguém'],
 guardar=['Câmara de eco é o lugar onde só se ouve quem pensa igual, e por isso tudo parece cada vez mais verdadeiro.', 'A radicalização é gradual: cada passo parece pequeno.', 'Ninguém sai de uma câmara de eco por ser ridicularizado; sai por manter vínculos fora dela.'],
 pensar='Nos seus grupos e feeds, quantas pessoas discordam de você com frequência? Se a resposta é nenhuma, o que isso significa?', pre=['perigo-do-tribalismo']),
'perigo-da-midia-alternativa': dict(
 obj=['Distinguir mídia independente séria de mídia de torcida', 'Reconhecer as técnicas mais comuns de distorção', 'Aplicar um teste rápido de confiabilidade'],
 guardar=['Mídia alternativa não é o problema; mídia a serviço de um extremo é.', 'Sinais: só erra para um lado, nunca corrige, trata o adversário como inimigo.', 'O teste: o veículo já publicou algo ruim sobre o próprio lado?'],
 pensar='Escolha o canal de notícias que você mais consome: quando foi a última vez que ele criticou o lado que defende?', pre=['checagem-de-fatos']),
'como-ler-a-midia-tradicional': dict(
 obj=['Reconhecer o que a grande mídia faz melhor: método, correção e responsabilidade', 'Conhecer seus limites: dono, linha editorial, anunciantes', 'Ler o noticiário separando fato, análise e opinião'],
 guardar=['A grande mídia tem o que os canais de torcida não têm: método, correção pública e responsabilidade legal.', 'Ela também tem dono, linha editorial e erros históricos: ler com senso crítico não é desprezar.', 'Separe reportagem de editorial e de coluna: são gêneros diferentes no mesmo site.'],
 pensar='Abra um grande jornal e identifique uma reportagem, um editorial e uma coluna: você consegue ver a diferença de gênero?', pre=['perigo-da-midia-alternativa']),
'perigo-dos-grupos-de-mensagem': dict(
 obj=['Entender por que o boato no grupo é tão forte', 'Conhecer os dados sobre disparo em massa', 'Agir diante de um “compartilhe antes que apaguem”'],
 guardar=['A mensagem chega sem autor, sem data e sem correção, pela mão de quem você confia.', '“Compartilhe antes que apaguem” é o sinal mais claro de boato.', 'Responder no grupo com a checagem ajuda mais do que sair dele.'],
 pensar='Quem é a pessoa do seu grupo da família que mais compartilha boatos? Qual seria o jeito de ajudá-la sem humilhar?', pre=['checagem-de-fatos']),
'perigo-dos-bots': dict(
 obj=['Entender o que bots fazem e o que os estudos mostram', 'Saber por que o problema está piorando com a IA', 'Desconfiar sem achar que todo discordante é robô'],
 guardar=['Bots criam a impressão de que “todo mundo” pensa assim.', 'Nem todo discordante é robô: chamar gente real de bot é outra forma de não ouvir.', 'Sinais: conta recente, só republica, ativa 24 horas, perfil genérico.'],
 pensar='Quando um assunto “bomba” nas redes, como você diferencia mobilização real de amplificação artificial?', pre=['checagem-de-fatos']),
'cambridge-analytica': dict(
 obj=['Saber o que aconteceu com os dados de 87 milhões de pessoas', 'Avaliar se a manipulação funcionou mesmo', 'Proteger os seus dados'],
 guardar=['O vazamento foi real; o poder de manipular, bem menor do que o anunciado.', 'A investigação britânica não encontrou prova de que o perfil psicológico funcionasse.', 'A lição fica: seus dados valem dinheiro, e as campanhas os querem.'],
 pensar='Que dados sobre você uma campanha conseguiria só com o que está público nas suas redes?', pre=['perigo-dos-bots']),
'pesquisas-eleitorais': dict(
 obj=['Entender amostra, margem de erro e votos válidos', 'Saber por que as pesquisas erram', 'Reconhecer uma pesquisa falsa ou de torcida'],
 guardar=['Pesquisa é fotografia do momento, não previsão.', 'Dentro da margem de erro, dois candidatos estão empatados, mesmo que um apareça na frente.', 'Pesquisa séria tem registro no TSE, metodologia pública e instituto com histórico.'],
 pensar='Na próxima pesquisa que vir, procure: quantos entrevistados, qual margem, quando foi feita e quem pagou.', pre=['checagem-de-fatos']),
'numero-de-projetos': dict(
 obj=['Entender por que o número de projetos engana', 'Comparar dois deputados além da contagem', 'Saber o que olhar no lugar'],
 guardar=['Aprovar 50 projetos não diz se eram bons, nem a quem serviam.', 'Olhe como votou, que interesses defende, que emendas enviou e para quem.', 'Projeto de dia comemorativo e lei que muda a vida das pessoas contam igual na estatística.'],
 pensar='Você sabe como o seu deputado votou nos três projetos mais importantes do ano?', pre=['como-votar-bem']),
'corrupcao': dict(
 obj=['Entender a corrupção como uma conta de incentivos, com a fórmula de Klitgaard', 'Conhecer as formas mais comuns e o custo real', 'Saber o que funciona e o que não funciona contra ela'],
 guardar=['Corrupção = monopólio + poder de decidir − prestação de contas.', 'O custo não é só o dinheiro: é a obra que não fica pronta e a confiança que acaba.', 'Salvadores não resolvem; transparência, controle e certeza de punição, sim.'],
 pensar='Pense em um órgão público que você conhece: onde há decisão concentrada, pouca regra e ninguém olhando?', pre=['o-que-esta-por-tras', 'politicas-publicas']),
'estado-e-mercado': dict(
 obj=['Conhecer os custos de Estado demais e de privatização demais', 'Diferenciar falhas de mercado e falhas de governo', 'Fazer as perguntas certas, setor por setor'],
 guardar=['Estado e mercado são ferramentas: a pergunta útil é qual serve melhor neste setor.', 'Mercado falha por monopólio, externalidade e informação desigual; governo, por captura, imediatismo e rigidez.', 'Os países com melhores indicadores combinam mercado forte com Estado capaz.'],
 pensar='Escolha um serviço da sua cidade: há concorrência real? Quem atende quem não dá lucro? Quem fiscaliza?', pre=['economia-para-entender-politica', 'esquerda-e-direita']),
'religiao-e-estado': dict(
 obj=['Entender o que é Estado laico e o que não é', 'Conhecer três modelos de laicidade', 'Separar a fé legítima na política do uso eleitoral da religião'],
 guardar=['Laicidade não é ateísmo de Estado: é o que permite que cada um pratique, ou não, sua fé.', 'Religiosos podem votar e se candidatar; o problema é transformar dogma em lei que obriga quem não crê.', 'Teste: você aceitaria a mesma regra se viesse de outra religião?'],
 pensar='Qual lei de inspiração religiosa você aceitaria se fosse proposta por uma religião que não é a sua?', pre=['democracia']),
'poder-paralelo': dict(
 obj=['Entender a captura do governo por mercado, mídia e crime', 'Ver como ela acontece sem parecer crime', 'Saber o que protege: transparência, imprensa plural, instituições autônomas'],
 guardar=['Um governo pode ser eleito e dirigido por quem não recebeu voto.', 'A captura costuma ser legal: doação, lobby às escondidas, porta giratória, verba publicitária.', 'Lobby às claras é direito; lobby escondido e acesso desigual é captura.'],
 pensar='Que interesse organizado você acha que tem mais acesso ao governo da sua cidade do que você?', pre=['o-que-esta-por-tras', 'corrupcao']),
'um-sistema-para-todos': dict(
 obj=['Entender o que muda de país para país', 'Aprender com outros países sem copiar', 'Recusar também a desculpa de que “o Brasil é diferente”'],
 guardar=['“Na Suécia funciona” é argumento fraco sem perguntar o que tornava isso possível lá.', 'Instituições, confiança, tamanho e história mudam o resultado de qualquer sistema.', 'Ideias viajam quando são adaptadas: o Bolsa Família veio em parte do Progresa mexicano.'],
 pensar='Pense em um modelo estrangeiro que você admira: que condição ele exige que o Brasil ainda não tem?', pre=[]),
'regras-e-desobediencia': dict(
 obj=['Entender por que lei não é sinônimo de justiça', 'Definir desobediência civil e o que não é', 'Saber quando é legítimo desobedecer'],
 guardar=['Escravidão e apartheid eram legais: obedecer sem pensar pode tornar você cúmplice.', 'Desobediência civil é pública, não violenta, busca o bem comum e aceita a consequência.', 'Invadir prédios para anular uma eleição é o contrário de desobediência civil.'],
 pensar='Que lei atual você acha injusta o bastante para desobedecer às claras e aceitar a punição?', pre=['democracia']),
'perigo-de-questionar-a-democracia': dict(
 obj=['Separar crítica saudável de questionamento perigoso', 'Reconhecer como democracias acabam hoje', 'Ouvir as críticas que a democracia precisa ouvir'],
 guardar=['Criticar a democracia é parte dela; o perigo é o salto da crítica para a ruptura.', 'Sinais de Levitsky e Ziblatt: rejeitar regras, negar a legitimidade do adversário, tolerar violência, restringir direitos.', 'Responder a toda crítica com “é golpismo” também confunde discordância com ameaça.'],
 pensar='Você aceitaria o resultado de uma eleição que seu lado perdesse por margem apertada? Que prova te faria duvidar?', pre=['democracia', 'perigo-das-revolucoes']),
'direito-internacional': dict(
 obj=['Saber de onde vêm as regras entre países: tratados, costume, princípios', 'Conhecer ONU, cortes e OMC, e por que funcionam ou falham', 'Entender como um tratado entra na política brasileira'],
 guardar=['Não há polícia mundial, e mesmo assim a maior parte das regras é cumprida, porque beneficia todos.', 'Sanções e cortes alcançam os fracos e raramente os fortes: o veto protege os cinco.', 'No Brasil, assinar é do Executivo; obrigar o país é do Congresso.'],
 pensar='Se o Brasil fosse condenado por uma corte internacional em um tema que você apoia, acharia que ele deveria cumprir?', pre=['geopolitica']),
'direitos-humanos': dict(
 obj=['Saber de onde vêm os direitos humanos e as gerações de direitos', 'Entender por que “direitos humanos para humanos direitos” inverte o conceito', 'Conhecer as críticas sérias'],
 guardar=['Direitos humanos existem para quem o Estado tem motivo para maltratar: o preso, o suspeito, o manifestante.', 'Direito que depende de merecimento não é direito; é favor, e quem decide o merecimento é quem tem poder.', 'A vítima também tem direitos humanos: punir com processo é o que eles exigem.'],
 pensar='Se um direito só vale para quem se comporta bem, quem decide quem se comportou bem? Você confiaria essa decisão ao governo que mais rejeita?', pre=['democracia', 'contrato-social']),
'direito-ambiental': dict(
 obj=['Conhecer o que a lei diz: Constituição, Código Florestal, licenciamento', 'Entender os princípios: poluidor-pagador, precaução, prevenção', 'Ver por que o desmatamento é uma decisão política'],
 guardar=['O Brasil tem uma das leis ambientais mais avançadas do mundo e uma das piores fiscalizações.', 'O dano ambiental atinge quem não participou da decisão, e por isso o mercado sozinho não cobra a conta.', 'O desmatamento sobe e desce conforme o governo decide fiscalizar: é escolha, não destino.'],
 pensar='Quem paga, hoje, pela poluição do rio mais próximo de você? E quem deveria pagar?', pre=['politicas-publicas']),
'direito-animal': dict(
 obj=['Entender a contradição: coisa no Código Civil, ser que sente nos tribunais', 'Conhecer as decisões do STF: farra do boi, rinha, vaquejada', 'Ver a fronteira: os animais de produção'],
 guardar=['A lei protege o que tem nome e ignora o que tem número.', 'Os tribunais já reconhecem a senciência; o Código Civil ainda chama o animal de bem móvel.', 'Resolver a contradição é uma decisão política que o país adia.'],
 pensar='Por que a mesma sociedade que pune maus-tratos a um cão aceita o que acontece com bilhões de galinhas?', pre=['etica-normativa']),
'guerra-ao-terror': dict(
 obj=['Conhecer a linha do tempo, de 2001 à retirada do Afeganistão', 'Fazer a conta: custo, mortes e resultados', 'Extrair as lições sobre medo, poder e liberdades'],
 guardar=['Guerra a um método não termina: ninguém assina a rendição.', 'Direitos suspensos em uma emergência não voltam sozinhos.', 'Cada medida foi vendida como temporária e necessária: o medo justifica tudo.'],
 pensar='Que medida “temporária” de segurança você aceitaria hoje, e que garantia teria de que ela acabaria?', pre=['politica-do-medo']),
'liberdade-de-expressao': dict(
 obj=['Conhecer as posições: Mill, Popper, modelo americano e europeu', 'Entender o que a lei brasileira protege e pune', 'Fazer as perguntas certas sobre limites e sobre quem os define'],
 guardar=['Quase ninguém defende liberdade total: ameaça, fraude e calúnia são crimes em quase todo lugar.', 'A pergunta não é se há limites, e sim onde e quem decide, inclusive se fosse o seu adversário decidindo.', 'Hoje o problema não é falar, é ser amplificado: isso muda o debate.'],
 pensar='Que discurso você gostaria de ver proibido? Agora imagine o poder de proibir nas mãos de quem você mais rejeita.', pre=['democracia', 'respeitar-crencas']),
'respeitar-crencas': dict(
 obj=['Separar respeito à pessoa de exame da ideia', 'Conhecer a ética da crença, de Clifford a James', 'Entender o paradoxo da tolerância sem usá-lo para calar discordantes'],
 guardar=['Pessoas merecem respeito; crenças merecem exame.', 'Sinceridade não absolve: quem compartilha boato sem checar responde pelo efeito.', 'Popper não manda calar ideias intolerantes: o limite é a recusa do debate e a violência.'],
 pensar='Qual crença sua você nunca examinou de verdade? Como reagiria se alguém a questionasse com respeito?', pre=['checagem-de-fatos']),
'nem-tudo-e-politico': dict(
 obj=['Aplicar o teste de três perguntas para saber se algo é político', 'Ver como o contexto muda as coisas', 'Entender por que tanta gente diz que tudo é político'],
 guardar=['Político é o que envolve regra coletiva, disputa de poder e efeito sobre quem não escolheu.', 'Ter uma dimensão política não torna algo inteiro político.', '“O pessoal é político” foi uma descoberta valiosa; “tudo é político” é o exagero dela.'],
 pensar='Pense em algo de que você gosta e que virou sinal de time nas redes: o que nele é político e o que é só gosto?', pre=['o-que-e-politica']),
'maiores-estadistas': dict(
 obj=['Conhecer os critérios: visão, crise, limites e custo humano', 'Separar influência de grandeza', 'Ver o legado e a sombra de cada um'],
 guardar=['Estadista é quem governa pensando além da próxima eleição e aceita limites.', 'Influência não é grandeza: Hitler e Stálin foram muito influentes.', 'Todos têm sombra: Washington teve escravizados; Churchill, a fome de Bengala; Mandela, a desigualdade que seguiu.'],
 pensar='Qual governante brasileiro vivo você incluiria na lista? Qual seria a sombra dele?', pre=['democracia']),
'maiores-ativistas': dict(
 obj=['Conhecer quem mudou leis sem ter cargo', 'Ver além do mito: o que costuma ficar de fora', 'Saber o que funciona: a pesquisa sobre resistência não violenta'],
 guardar=['Muitos direitos que parecem óbvios foram conquistados por gente ridicularizada, presa ou morta.', 'Heróis têm falhas: Gandhi, King e Suu Kyi mostram isso.', 'Chenoweth e Stephan: campanhas não violentas tiveram cerca do dobro de sucesso das violentas.'],
 pensar='Que regra de hoje você acha que daqui a 50 anos será vista como as pessoas hoje veem a escravidão?', pre=['regras-e-desobediencia']),
'america-do-sul-e-ditaduras': dict(
 obj=['Conhecer a onda de golpes dos anos 1960 a 1980', 'Entender por que houve tantas ditaduras', 'Comparar como cada país lidou com o passado'],
 guardar=['Quase toda a América do Sul viveu ditaduras, a maioria militar e de direita, com apoio dos EUA na Guerra Fria.', 'A Operação Condor foi a cooperação entre ditaduras para perseguir opositores além das fronteiras.', 'A Argentina julgou; o Brasil anistiou, inclusive agentes do Estado, e só fez a Comissão da Verdade em 2014.'],
 pensar='Por que o Brasil, diferentemente da Argentina, nunca julgou os agentes da ditadura? O que isso muda hoje?', pre=['democracia', 'perigo-de-questionar-a-democracia']),

# ---------- Avançado ----------
'atores-malevolentes': dict(
 obj=['Conhecer a Tétrade Sombria: narcisismo, maquiavelismo, psicopatia e sadismo', 'Entender por que esses traços chegam ao poder', 'Avaliar conduta pública sem diagnosticar à distância'],
 guardar=['Basta uma pessoa assim com a chave do cofre para causar um estrago enorme: por isso existem limites ao poder.', 'Freios e contrapesos valem mais do que escolher a pessoa certa.', 'Ninguém diagnostica à distância: observe crueldade, mentira persistente e rejeição de limites.'],
 pensar='Que sinal de conduta, e não de ideologia, faria você deixar de votar em alguém do seu próprio lado?', pre=['perigo-do-messianismo', 'perigo-do-populismo']),
'fanatismo-ideologico': dict(
 obj=['Entender a tese de Althaus sobre o fanatismo como motor de atrocidades', 'Conhecer a tríade: certeza absoluta, ódio ao de fora, disposição à violência', 'Avaliar o risco de bloqueio (lock-in) com tecnologia avançada'],
 guardar=['O fanatismo foi motor de oito das dez maiores atrocidades desde 1800, segundo a estimativa dos autores.', 'O risco novo é o bloqueio: vigilância e IA tornando um regime quase impossível de remover.', 'É um ensaio com incertezas assumidas, não um artigo revisado por pares.'],
 pensar='Que instituição de hoje você acha mais importante para impedir que um regime se torne permanente?', pre=['perigo-do-fanatismo', 'atores-malevolentes']),
'genetica-e-politica': dict(
 obj=['Entender o que os estudos com gêmeos sugerem', 'Conhecer os cuidados: influenciar não é determinar', 'Usar isso para aumentar a tolerância, não para desqualificar'],
 guardar=['Cerca de 40% da variação das atitudes políticas se associa a genes, em média, por meio de traços de personalidade.', 'Não existe gene da esquerda ou da direita: são milhares de efeitos minúsculos.', 'A estimativa vale para diferenças entre pessoas, não para um indivíduo, e pessoas mudam.'],
 pensar='Se parte da diferença entre você e seu adversário vem de temperamento, isso muda como você o trata?', pre=['mente-moralista']),
'inteligencia-nao-protege': dict(
 obj=['Conhecer as pesquisas sobre sofisticação e viés', 'Entender por que mais informação pode blindar crenças', 'Saber o que ensinar além da lógica: humildade e curiosidade'],
 guardar=['Pessoas mais informadas podem ser melhores em justificar o que já pensavam.', 'A razão funciona como advogado da identidade, e funciona melhor em grupos que discordam.', 'Use este conhecimento primeiro em você, não para explicar por que os outros estão errados.'],
 pensar='Faça uma previsão política verificável para os próximos seis meses e anote. O que fará se errar?', pre=['vieses-cognitivos', 'mudar-de-ideia']),
'estereotipo-preconceito-discriminacao': dict(
 obj=['Distinguir estereótipo (crença), preconceito (atitude) e discriminação (ação)', 'Entender de onde vêm: atalhos, grupos mínimos, cultura', 'Ver como a política piora ou ajuda'],
 guardar=['Estereótipo é o que se pensa; preconceito, o que se sente; discriminação, o que se faz.', 'Pessoas divididas por sorteio já favorecem o próprio grupo: o “nós” vira “contra eles” com facilidade.', '“Todo eleitor do outro lado é burro” é um estereótipo como qualquer outro.'],
 pensar='Que estereótipo sobre o eleitor do outro lado você carrega? Quantas pessoas desse grupo você conhece de verdade?', pre=['perigo-do-tribalismo']),
'critica-ao-identitarismo': dict(
 obj=['Entender o que a política de identidade acertou', 'Conhecer as críticas, inclusive de dentro da esquerda', 'Avaliar a saída pela universalidade'],
 guardar=['A identidade é uma lanterna útil e um péssimo substituto para a luz toda.', 'Críticas: fragmentação, esquecimento da classe, lugar de fala absoluto, relativismo sobre fatos.', 'Pergunta útil: a medida reduz uma injustiça real e trata cada pessoa pelos atos e argumentos?'],
 pensar='Em que situação a identidade de quem fala deveria pesar mais do que o argumento? E em qual não deveria pesar nada?', pre=['estereotipo-preconceito-discriminacao']),
'direta-ou-epistocracia': dict(
 obj=['Comparar democracia direta e epistocracia', 'Conhecer os caminhos do meio: assembleias sorteadas, democracia deliberativa', 'Enfrentar o dilema: resultado, processo ou os dois'],
 guardar=['Democracia direta aposta em todos decidirem tudo; epistocracia, em dar mais peso a quem sabe mais.', 'Quem decide quem sabe? Testes de conhecimento já serviram para excluir negros do voto.', 'O caminho mais seguro talvez seja qualificar a informação de todos, não tirar o voto de alguns.'],
 pensar='Você aceitaria que seu voto valesse menos se errasse um teste de conhecimento político? E se fosse o voto do outro?', pre=['democracia', 'melhorar-a-democracia']),
'melhorar-a-democracia': dict(
 obj=['Conhecer o cardápio de reformas, com prós e contras', 'Entender como a regra muda o resultado, com o exemplo do voto preferencial', 'Avaliar uma reforma: quem ganha, se foi testada, se pode ser desfeita'],
 guardar=['Democracia é software: atualiza, mas não se instala uma versão sem ver o que ela quebra.', 'A mesma população produz vencedores diferentes conforme a regra, e nenhuma regra é perfeita.', 'Pergunte sempre quem ganha com a reforma: costuma ser quem a propõe.'],
 pensar='Que reforma eleitoral você apoiaria mesmo sabendo que ela prejudicaria o seu lado na próxima eleição?', pre=['democracia', 'o-que-e-um-partido']),
'politicas-baseadas-em-evidencias': dict(
 obj=['Entender a ideia de tratar leis como hipóteses', 'Conhecer a hierarquia das evidências e o ciclo na prática', 'Ver os limites e por que os políticos resistem'],
 guardar=['Testar, medir e corrigir: um programa não é bom porque soa bem.', 'Revisão sistemática vale mais do que um experimento, que vale mais do que a opinião de um especialista.', 'Evidência diz o que funciona; não diz o que é justo. As duas perguntas continuam separadas.'],
 pensar='Que política você defende com mais convicção? Que evidência existe sobre ela, e você já a procurou?', pre=['valores-e-decisoes', 'comparar-projetos']),
'pragmatismo-politico': dict(
 obj=['Entender a origem filosófica do pragmatismo', 'Diferenciar ética da convicção e ética da responsabilidade, com Weber', 'Separar pragmatismo saudável de falta de princípio'],
 guardar=['Pragmatismo é firme no destino e flexível na rota; quem muda de porto a cada rajada está à deriva.', 'Weber: o político maduro precisa de convicção e de responsabilidade pelas consequências.', 'Pragmatismo não substitui valores: Deng tirou milhões da pobreza e manteve a ditadura.'],
 pensar='Em que ponto um acordo político deixa de ser pragmatismo e vira traição? Como você saberia?', pre=['valores-e-decisoes', 'politicas-baseadas-em-evidencias']),
'mandatos-coletivos': dict(
 obj=['Entender como funciona uma candidatura coletiva na prática e na lei', 'Conhecer a origem e os casos brasileiros', 'Avaliar as promessas e os riscos de um mandato coletivo'],
 guardar=['Na lei, só uma pessoa tem o mandato; o coletivo é um acordo político.', 'A inovação tenta resolver um problema real de representação, e ainda não tem regra própria.', 'Enquanto o grupo se entende, funciona; se briga, quem registrou fica com a cadeira.'],
 pensar='Você votaria em um mandato coletivo? Que regra exigiria no compromisso do grupo antes de confiar?', pre=['o-que-e-um-partido']),
'presidencialismo-de-coalizao': dict(
 obj=['Entender por que o presidente brasileiro precisa negociar tanto', 'Conhecer o Centrão e as regras dos partidos', 'Ver o que mudou com as emendas impositivas'],
 guardar=['O partido do presidente nunca tem maioria: governar exige coalizão, e coalizão custa cargos e emendas.', 'Isso dá estabilidade e gera toma-lá-dá-cá: Collor e Dilma caíram quando perderam a base.', 'Com as emendas impositivas, o Congresso ganhou poder sobre o orçamento e o presidente perdeu moeda.'],
 pensar='Se você fosse presidente com 15% da Câmara, o que aceitaria dar em troca de apoio, e o que não?', pre=['como-uma-lei-e-feita', 'o-que-e-um-partido']),
'progresso-moral-e-politico': dict(
 obj=['Distinguir progresso moral, político e técnico', 'Ver por que nem sempre andam juntos', 'Entender por que nenhum avanço é garantido'],
 guardar=['Progresso moral muda valores; progresso político muda leis e poder. Um pode existir sem o outro.', 'A Lei Áurea veio sem terra, escola ou reparação: a lei mudou, a realidade demorou.', 'A trilha não sobe sempre: 1937 e 1964 foram recuos.'],
 pensar='Que avanço moral você considera definitivo? O que precisaria acontecer para ele recuar?', pre=['etica-normativa']),
'sencientismo': dict(
 obj=['Entender a expansão do círculo moral', 'Conhecer o critério: quem pode sentir, conta', 'Ver o que isso faz com a política, e as objeções'],
 guardar=['Raça, sexo e espécie não mudam o fato de que dor é dor.', 'Quem sofre e não vota fica sem representação: animais, bebês, futuras gerações.', 'Sencientismo é a visão moral; a política baseada na senciência é o passo seguinte.'],
 pensar='Que característica, além da capacidade de sofrer, você usaria para decidir quem conta? Ela resiste ao teste da imparcialidade?', pre=['etica-normativa', 'direito-animal']),
'teorias-da-justica': dict(
 obj=['Comparar utilitarismo, Rawls, Nozick, prioritarismo, suficientismo e capacidades', 'Ver onde cada uma aparece na política brasileira', 'Enfrentar a questão do mérito, da sorte e da herança'],
 guardar=['Rawls: desigualdade só se beneficiar quem está pior. Nozick: justo é o que vem de trocas voluntárias.', 'Sen e Nussbaum mudam a pergunta: não quanto alguém tem, mas o que consegue ser e fazer.', 'SUS, Bolsa Família e imposto progressivo encarnam teorias diferentes, e as críticas vêm de outras.'],
 pensar='Como dividir uma herança entre filhos com necessidades diferentes? Qual teoria você usou sem perceber?', pre=['etica-normativa', 'contrato-social']),
'relativismo-e-circulo-moral': dict(
 obj=['Entender o que é relativismo moral e seus dois problemas', 'Separar tolerância de relativismo', 'Ver como a imparcialidade explica a expansão do círculo'],
 guardar=['Se toda moral fosse relativa, a abolição não teria sido avanço, só mudança.', 'Tolerância respeita pessoas e tem limites; relativismo nega que se possa julgar.', 'Incluir minorias é aplicar um princípio que quase todos aceitam: não tratar pior por uma característica irrelevante.'],
 pensar='Existe alguma prática de outra cultura que você considera errada em qualquer lugar? Qual é o seu critério?', pre=['progresso-moral-e-politico', 'sencientismo']),
'politica-baseada-na-senciencia': dict(
 obj=['Ver de onde vem a ideia, de Bentham às teorias políticas atuais', 'Imaginar como apareceria em leis, orçamentos e representação', 'Conhecer os desafios: medir, até onde, transição'],
 guardar=['Uma política da senciência lembra que outros seres sentem o efeito de cada decisão.', 'Não exige que todos virem vegetarianos amanhã: exige que o sofrimento de quem não vota entre na conta.', 'O ambientalismo pensa em espécies e ecossistemas; o sencientismo, em cada indivíduo que sente.'],
 pensar='Em uma enchente na sua cidade, quem é contado entre as vítimas? Quem deveria ser?', pre=['sencientismo']),
'libertarismo-de-coracao-sangrante': dict(
 obj=['Entender a proposta: mercado livre por, e para, os mais pobres', 'Conhecer o que defendem na prática', 'Ver as críticas de outros libertários e da esquerda'],
 guardar=['Defender o mercado e se importar com os pobres não são opostos nesta corrente.', 'O critério aceito é o de Rawls: julgar instituições pelo efeito sobre quem está pior.', 'Esse critério permite discutir os meios com dados, entre liberais e social-democratas.'],
 pensar='Que privilégio concedido pelo Estado prejudica mais os pobres? Quem defende mantê-lo?', pre=['teorias-da-justica', 'estado-e-mercado']),
'riscos-s-e-x': dict(
 obj=['Distinguir riscos-x (existenciais) e riscos-s (de sofrimento)', 'Conhecer políticas que ajudam: IA, biossegurança, armas, instituições', 'Avaliar as críticas: especulação, uso do medo, quem decide'],
 guardar=['Instalamos extintores sem esperar o incêndio: o dano enorme e irreversível justifica a prevenção.', 'Riscos enormes também podem justificar vigilância e concentração de poder, que são perigosos.', 'Muitas medidas valem mesmo para quem não aceita as projeções: prevenir pandemias e conter armas.'],
 pensar='Quanto do orçamento de hoje você aceitaria gastar em riscos que talvez nunca aconteçam? Como decidiria?', pre=['fanatismo-ideologico', 'politica-baseada-na-senciencia']),
}

# Seções extras para as lições mais curtas: um caso concreto ou um exercício aplicado, acrescentado ao fim do corpo.
EXTRA = {
'perigo-do-fanatismo': '''<h2>Radical não é o mesmo que fanático</h2>
<p>Ideias radicais podem ser certas: os abolicionistas eram radicais para a sua época, e as sufragistas também. O que define o fanatismo não é a distância da opinião em relação à média, e sim o método: a recusa de admitir erro, o inimigo total e a aceitação de qualquer meio. Dá para defender uma ideia radical com argumentos, aceitar críticas e respeitar limites. E dá para defender uma ideia moderada de forma fanática.</p>
<h2>Três perguntas que o fanático não responde</h2>
<table><tr><th>Pergunta</th><th>O que a resposta revela</th></tr>
<tr><td>O que me faria mudar de ideia?</td><td>Se nada, a crença deixou de ser uma conclusão e virou identidade</td></tr>
<tr><td>Que crítica ao meu lado eu aceito?</td><td>Se nenhuma, o lado virou time, e o time não erra</td></tr>
<tr><td>Que limite eu não ultrapassaria pela causa?</td><td>Se nenhum, a causa já justifica qualquer coisa</td></tr></table>
<p>Faça as três perguntas a você mesmo antes de fazê-las a alguém. Quem as responde com honestidade pode ter convicções fortes sem ser fanático.</p>''',
'teoria-da-ferradura': '''<h2>Um teste prático: Stálin e Hitler</h2>
<p>Os dois regimes mais citados pela teoria mostram onde ela acerta e onde erra. Nos métodos, eram quase gêmeos: partido único, polícia política, culto ao líder, campos de prisioneiros, propaganda total e um inimigo interno a ser eliminado. Nas ideias, eram opostos: um abolia a propriedade privada e falava em classe; o outro a mantinha e falava em raça. Um prometia o fim das nações; o outro, a supremacia de uma. Os dois se odiavam e lutaram a guerra mais sangrenta da história entre si, apesar do pacto de 1939.</p>
<p>É por isso que a ferradura funciona como alerta sobre métodos e falha como mapa de ideias. Use-a para reconhecer sinais de autoritarismo em qualquer lado: culto à personalidade, desprezo por limites, violência como ferramenta. Não a use para dizer que um comunista e um fascista “querem a mesma coisa”, porque não querem. E, acima de tudo, não a use para chamar de extremista quem apenas discorda de você.</p>''',
'perigo-do-reacionarismo': '''<h2>Como reconhecer no discurso</h2>
<p>O reacionarismo raramente se apresenta como tal. Ele aparece em frases comuns, e cada uma pede uma pergunta de volta.</p>
<table><tr><th>A frase</th><th>A pergunta</th></tr>
<tr><td>“Antigamente não tinha isso”</td><td>Não tinha, ou não se falava? A violência doméstica “não existia” enquanto não era denunciada</td></tr>
<tr><td>“Era tudo mais simples”</td><td>Simples para quem? Para quem não podia votar, estudar ou escolher com quem casar, não era</td></tr>
<tr><td>“Perdemos nossos valores”</td><td>Quais, e quem os definia? Alguns valores foram perdidos; outros foram trocados por melhores</td></tr>
<tr><td>“Precisamos voltar a ser o que éramos”</td><td>O que, exatamente, seria revertido, e quem perderia direitos com isso?</td></tr></table>
<p>A diferença entre nostalgia e reacionarismo está na resposta. Sentir falta de algo é humano. Querer tirar direitos de outros para recuperar a sensação é política, e merece ser avaliada como qualquer outra proposta.</p>''',
'um-sistema-para-todos': '''<h2>Um exemplo: o voto distrital</h2>
<p>“Nos Estados Unidos e no Reino Unido o eleitor conhece seu deputado, porque cada distrito elege um só.” É verdade, e a proposta de adotar o voto distrital no Brasil volta a cada legislatura. Antes de copiar, vale olhar o que vem junto. Nesses países, o distrito único por cadeira produz, na prática, dois grandes partidos, e um terceiro quase nunca elege ninguém, mesmo com milhões de votos. No Brasil, com dezenas de partidos e um território continental, o mesmo desenho poderia eliminar da Câmara correntes que hoje têm bancada, e dar vantagem a quem controla a política local, inclusive onde o crime manda.</p>
<p>Isso não torna a ideia ruim. Torna necessário perguntar o que ela resolveria aqui, o que quebraria e se há versões intermediárias, como o distrital misto da Alemanha, mais fáceis de testar. É a pergunta desta lição aplicada a um caso: o que tornava isso possível lá, e existe aqui?</p>''',
'religiao-e-estado': '''<h2>Como avaliar uma proposta de inspiração religiosa</h2>
<p>Religiosos têm o mesmo direito de propor leis que qualquer pessoa, e muitas leis boas nasceram de convicções de fé. O que a laicidade pede não é que a fé fique de fora, e sim que a lei tenha razões que valham para todos. Três perguntas ajudam:</p>
<ul><li><strong>Há uma razão pública?</strong> A proposta se sustenta com argumentos sobre dano, direitos ou bem-estar, que alguém sem a mesma fé consiga avaliar? “Deus proíbe” não é um argumento para quem não crê no mesmo Deus.</li>
<li><strong>Ela obriga quem não crê?</strong> Uma regra que organiza a vida dos fiéis é da igreja. Uma regra que obriga todos é do Estado, e precisa de justificativa de Estado.</li>
<li><strong>Você aceitaria a mesma regra de outra religião?</strong> Se um feriado, um símbolo em prédio público ou uma restrição de costume parecem naturais vindos da sua fé e abusivos vindos de outra, o problema não é a regra: é o privilégio.</li></ul>
<p>Uma proposta que passa pelas três perguntas pode ter nascido na igreja e ser lei legítima. Uma que não passa por nenhuma é dogma com força de lei, e costuma terminar mal tanto para o Estado quanto para a religião.</p>''',
'poder-paralelo': '''<h2>Onde olhar</h2>
<p>A captura prefere o escuro, e boa parte do que a ilumina já é público. Alguns lugares para começar:</p>
<ul><li><strong>Quem financiou a campanha:</strong> o sistema DivulgaCand, do TSE, mostra cada doação recebida por cada candidato, e o cruzamento com os votos que ele deu depois é a investigação mais simples que existe.</li>
<li><strong>Quem o político recebe:</strong> as agendas públicas de ministros e de alguns parlamentares mostram com quem se reúnem. Reunião frequente com um setor e nenhuma com os afetados por ele é um sinal.</li>
<li><strong>Para onde vão as emendas:</strong> o Portal da Transparência e o Siga Brasil, do Senado, permitem ver que município e que entidade recebeu cada emenda, e quem é o dono dela.</li>
<li><strong>Quem paga a mídia local:</strong> a verba de publicidade de prefeituras e governos estaduais é pública, e explica muito silêncio editorial.</li>
<li><strong>Quem controla o território:</strong> nas eleições municipais, candidato único em áreas de milícia, ou campanha que não entra em certos bairros, é o sinal mais grave de todos, e o TSE e o Ministério Público recebem denúncias.</li></ul>
<p>Nada disso exige ser jornalista. Exige meia hora e a pergunta desta lição: quem manda de verdade, e por que não aparece?</p>''',
'estado-e-mercado': '''<h2>Um exemplo passo a passo: o ônibus da sua cidade</h2>
<p>Quase toda cidade brasileira tem o transporte por ônibus em concessão: a prefeitura define linhas e tarifa, e empresas privadas operam. Aplique as perguntas desta lição.</p>
<ul><li><strong>Há concorrência real?</strong> Em geral, não. Cada empresa tem o monopólio de suas linhas por 10 ou 20 anos, e as licitações costumam ter um só participante. A concessão troca um monopólio público por um privado, e sem regulação forte o resultado é frota velha e horário ruim.</li>
<li><strong>Quem atende quem não dá lucro?</strong> Linhas de bairro distante, noturnas e de domingo perdem dinheiro. Ou o contrato obriga a operá-las, ou elas somem. É aqui que entra o subsídio público, que já existe na maior parte das capitais.</li>
<li><strong>Quem fiscaliza?</strong> A prefeitura, que também depende das empresas para o serviço funcionar e, em muitos casos, recebeu doações delas. É o risco de captura em escala municipal.</li>
<li><strong>Dá para medir a qualidade?</strong> Sim, e cada vez mais: GPS na frota, pontualidade, lotação e reclamações. Onde isso é público, o contrato pode ser cobrado.</li></ul>
<p>O resultado não é “estatizar” nem “privatizar”. É um arranjo com empresas operando, regras claras, subsídio onde necessário, dados abertos e fiscalização independente. Cidades que combinam essas peças têm transporte melhor, com qualquer bandeira na prefeitura. As que escolhem um lado da briga e esquecem o resto costumam ter o pior dos dois mundos.</p>''',
'bem-comum': '''<h2>Um exemplo: a vacina</h2>
<p>A vacinação reúne, em um só caso, as quatro lentes desta lição. Quem está pior é quem mais depende dela: bebês, idosos e pessoas com doenças, que não se protegem sozinhos. O básico para todos é a cobertura ampla e gratuita, que o SUS garante há décadas. O longo prazo é a imunidade coletiva, que leva anos para construir e meses para perder. E o carona é quem não se vacina porque “todo mundo já se vacinou”: aproveita a proteção dos outros sem pagar o custo, e, se muitos fizerem o mesmo, a proteção desaparece para todos, inclusive para ele.</p>
<p>Por isso a vacina é uma decisão política e não só uma escolha pessoal. Ela passa no teste do véu da ignorância, porque ninguém sabe se nascerá com um sistema imunológico frágil. E mostra por que o imediatismo é perigoso: o sarampo voltou ao Brasil em 2018 depois de quase duas décadas eliminado, exatamente quando a cobertura caiu e o risco parecia distante.</p>''',
'mente-moralista': '''<h2>Um exemplo de conversa</h2>
<p>A mesma política pode ser defendida com paladares morais diferentes, e a pesquisa de Haidt sugere que isso muda a chance de ser ouvido. Pegue a proteção de um rio.</p>
<table><tr><th>Para quem pesa mais</th><th>O argumento que funciona</th></tr>
<tr><td>Cuidado e justiça</td><td>A poluição adoece as crianças da margem e quem paga são os mais pobres, não a fábrica</td></tr>
<tr><td>Lealdade e autoridade</td><td>O rio é patrimônio da cidade há gerações; nossos avós pescavam ali, e temos o dever de entregá-lo aos netos</td></tr>
<tr><td>Santidade e pureza</td><td>Um rio de esgoto é uma profanação de algo que deveria ser limpo e sagrado</td></tr>
<tr><td>Liberdade</td><td>Ninguém tem o direito de impor o próprio lixo à água dos outros</td></tr></table>
<p>Nenhum desses argumentos é falso ou manipulador: cada um aponta uma razão real. Quem só fala em cuidado e justiça convence quem já concordava, e soa estranho para quem pesa a lealdade e a tradição. Entender o paladar do outro não é ceder: é escolher, entre as razões verdadeiras, a que ele consegue ouvir.</p>''',
'geopolitica': '''<h2>Um exemplo: por que o Brasil não escolhe lado</h2>
<p>A China é o maior parceiro comercial do Brasil desde 2009 e compra a maior parte da soja, do minério e do petróleo exportados. Os Estados Unidos são o maior investidor estrangeiro no país, o principal mercado para produtos industrializados e a potência militar do continente. Qualquer governo brasileiro, de qualquer lado, enfrenta a mesma conta: fechar com um dos dois custa caro no outro.</p>
<p>O resultado é a política de não alinhamento automático, que atravessa governos de direita e de esquerda com nomes diferentes. Ela explica por que o Brasil está no BRICS e negocia com a OCDE, por que vota contra a Rússia na ONU e não adere às sanções, por que recebe navios chineses e exercícios militares americanos. Os realistas chamam isso de hedging, o seguro contra apostar errado. Os críticos chamam de indefinição. Os dois têm parte da razão, e o caso serve para ver a lição em ação: posição, recursos e vizinhança pesam mais do que o discurso do momento.</p>''',
}

for _s, _d in D.items():
    assert len(_d['obj']) == 3 and len(_d['guardar']) == 3 and _d['pensar'] and _d['pensar'][-1] in '?.', _s
assert set(EXTRA) <= set(D)
