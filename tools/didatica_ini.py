"""Camada didática extra (padrão do Ética Para Iniciantes) para o nível Iniciante: caso de abertura, erro comum, ferramenta para praticar
e duas perguntas extras por lição. E[slug] = dict(caso=(situação, pergunta, resposta), erro=(erro comum, correção), ferr=slug|None, quiz=[(q, ops, idx, expl), (q, ops, idx, expl)])."""
E_INI = {
'o-que-e-politica': dict(
 caso=('O síndico do seu prédio decide, sem assembleia, trocar a empresa de segurança. A taxa sobe para todos.', 'Isso é política? Quem decidiu, quem foi ouvido, quem paga?', 'É política: uma decisão que vale para todos, tomada por alguém com poder, com uma conta a pagar. A lição mostra que a política começa muito antes da urna e tem sempre as mesmas três perguntas.'),
 erro=('“Política é coisa de político.”', 'Política é a disputa sobre o que vale para todos, e acontece no condomínio, na escola e no trabalho. O político é só quem a faz profissionalmente; você a faz todo dia, inclusive quando não participa.'),
 ferr='quem-faz-o-que',
 quiz=[('Qual das três é a pergunta sobre legitimidade?', ['Quem tem força para impor a decisão?', 'Quem tem o direito reconhecido de decidir, e por quê?', 'Quanto custa a decisão?'], 1, 'Poder é poder impor; autoridade é o direito reconhecido; legitimidade é o que faz as pessoas aceitarem a autoridade.'),
       ('“O Estado brasileiro” e “o governo Lula” são…', ['A mesma coisa', 'Coisas diferentes: o Estado permanece; o governo passa', 'Sinônimos de nação'], 1, 'Confundir os dois leva a tratar a crítica ao governo como ataque ao país, e vice-versa.')]),
'perigo-de-ser-despolitizado': dict(
 caso=('“Não acompanho política, não me afeta.” Você acorda, toma água tratada, pega um ônibus com tarifa definida pela prefeitura e paga imposto no café.', 'Quantas decisões públicas aconteceram antes das 9 da manhã? Quem decidiu cada uma?', 'Dezenas: tarifa, saneamento, imposto, regra de trânsito, horário da escola. Não acompanhar não tira você delas; só tira a sua voz. A lição mostra quem ganha com o seu afastamento.'),
 erro=('“Ser despolitizado é ser neutro.”', 'Não há neutralidade: as decisões continuam valendo para você, e quem mais ganha com o afastamento do eleitor comum é quem tem interesse concentrado e dinheiro para pressionar.'),
 ferr=None,
 quiz=[('Quem mais ganha quando a maioria deixa de acompanhar política?', ['Ninguém', 'Grupos com interesse concentrado, que seguem pressionando enquanto os outros não olham', 'O eleitor comum, que fica em paz'], 1, 'Benefício concentrado organiza; custo espalhado adormece.'),
       ('Qual é o “mínimo que já muda muito”, segundo a lição?', ['Filiar-se a um partido', 'Saber em quem votou, ler uma checagem e olhar como seu deputado vota', 'Ir a todas as manifestações'], 1, 'Três hábitos pequenos tiram a pessoa da condição de massa de manobra.')]),
'o-que-esta-por-tras': dict(
 caso=('Um deputado vota contra um imposto sobre agrotóxicos e diz que é “pelo consumidor”.', 'Antes de acreditar ou desconfiar, que pergunta você faz? O que você procuraria?', 'Quem financiou a campanha, quem ganha de forma concentrada com o voto e quem paga de forma espalhada. Discurso é o que aparece; incentivo é o que explica. A lição ensina a ler incentivos sem cair no cinismo.'),
 erro=('“São todos iguais, só pensam em si.”', 'O cinismo total é tão errado quanto a ingenuidade: incentivos explicam padrões, não tudo, e há diferenças mensuráveis entre políticos. Quem diz “são todos iguais” deixa de fiscalizar, e isso é o que os piores querem.'),
 ferr='como-votaram',
 quiz=[('“Benefício concentrado, custo espalhado” explica por que…', ['Todo mundo se organiza', 'Os poucos que ganham muito se organizam, e os muitos que perdem pouco nem percebem', 'Impostos são altos'], 1, 'É o padrão por trás de subsídios, isenções e regulações feitas sob medida.'),
       ('Qual é a melhor pista sobre o que um político defende?', ['O que diz em entrevista', 'Como vota e quem o financia', 'Quantos seguidores tem'], 1, 'Votações e financiamento são públicos e deixam rastro; o discurso é barato.')]),
'valores-e-decisoes': dict(
 caso=('Dois amigos discutem a maioridade penal. Um diz “deve cair para 16, é justo”; o outro, “reduzir não diminui o crime”.', 'Eles estão discordando da mesma coisa? O que falta para a conversa andar?', 'Um fala de valor (o que devemos querer) e o outro de fato (o que funciona). Separar as duas camadas é o primeiro passo de qualquer debate político, e a lição dá o método em três camadas: valor, meio, evidência.'),
 erro=('“Os dados decidem a política.”', 'Dados resolvem a parte factual (o que funciona para chegar lá); a parte moral (o que queremos) precisa de argumento. Quem diz que os dados decidem tudo está escondendo o valor que escolheu.'),
 ferr='valor-ou-fato',
 quiz=[('“Reduzir a jornada aumenta a produtividade.” Isso é…', ['Um valor', 'Um fato, que se checa com evidência', 'Uma opinião sem resposta'], 1, 'Pode ser verdadeiro ou falso; a evidência decide. “Trabalhadores merecem mais tempo livre” seria o valor.'),
       ('A guilhotina de Hume diz que…', ['Fatos não existem', 'Do que é não se tira sozinho o que deve ser; falta sempre uma premissa de valor', 'Valores não se discutem'], 1, 'Todo argumento político tem uma premissa de valor, explícita ou escondida.')]),
'etica-normativa': dict(
 caso=('Uma prefeitura quer remover à força moradores de uma área de risco para evitar mortes numa enchente.', 'Que pergunta faz quem olha o resultado? E quem olha os direitos? E quem olha o caráter de quem decide?', '“Quantas vidas serão salvas?”, “há um direito que a remoção forçada viola?”, “que governante faz isso, e como?”. As três perguntas coexistem; a diferença é qual decide quando colidem. É o ponto focal de cada família.'),
 erro=('“Consequencialismo é não ter princípios; deontologia é não olhar o resultado.”', 'Cada família tem um ponto focal, não uma exclusividade: o consequencialista cuidadoso valoriza regras, e o deontologista olha resultados dentro dos limites. A caricatura é o erro mais comum.'),
 ferr='valor-ou-fato',
 quiz=[('Qual pergunta é típica da ética das virtudes diante de uma lei?', ['Quanto bem ela produz?', 'Que direito ela protege ou viola?', 'Que tipo de governante e de sociedade ela forma?'], 2, 'O foco é no caráter de quem age e no que a prática faz com as pessoas.'),
       ('O círculo moral pergunta…', ['Qual teoria está certa', 'Quem entra na conta: só eleitores, todos os humanos, todos os que sentem?', 'Quanto custa a política'], 1, 'A resposta muda o veredito de todas as outras perguntas; animais e gerações futuras são os casos de teste.')]),
'esquerda-e-direita': dict(
 caso=('Uma candidata defende privatizar estatais e, ao mesmo tempo, legalizar o aborto.', 'Ela é de esquerda ou de direita? O rótulo único dá conta?', 'Não: ela é à direita no eixo econômico e progressista no de costumes. Um eixo só não basta, e a lição mostra as quatro combinações e por que o rótulo orienta sem substituir o exame de cada proposta.'),
 erro=('“Esquerda é bondade; direita é maldade”, ou o contrário.', 'Os dois lados têm valores legítimos (igualdade e proteção de um lado; liberdade e ordem de outro) e os dois produziram catástrofes quando foram ao extremo. O que vale é o argumento e a evidência de cada proposta.'),
 ferr='comparador',
 quiz=[('De onde vêm os termos esquerda e direita?', ['Da Bíblia', 'Da posição dos deputados na assembleia francesa de 1789', 'Da Revolução Russa'], 1, 'Quem apoiava o rei sentava à direita; quem queria mudanças, à esquerda. O sentido mudou muito desde então.'),
       ('“Moderado” é sinônimo de “certo”?', ['Sim, o meio é sempre melhor', 'Não: o meio entre duas posições pode ser errado, e uma posição extrema pode ter razão; o que decide é o argumento', 'Sim, porque evita conflito'], 1, 'A falácia do meio-termo é tão comum quanto a do extremo.')]),
'palavras-em-disputa': dict(
 caso=('“Esse governo tira a nossa liberdade”, diz alguém sobre a lei do cinto de segurança.', 'Antes de concordar ou discordar, que pergunta você faz?', '“O que você quer dizer com liberdade?” Não ser impedido de nada, ou poder viver bem e com segurança? Os dois lados usam a mesma palavra para coisas diferentes, e quem define a palavra já ganhou metade do debate.'),
 erro=('“Liberdade e conservar têm um sentido óbvio.”', 'Liberdade pode ser ausência de interferência ou capacidade real de agir; conservar pode ser manter instituições que funcionam ou blindar privilégios. Pedir definição antes de discutir evita a maior parte das brigas vazias.'),
 ferr='que-truque-e-esse',
 quiz=[('Liberdade negativa é…', ['Liberdade ruim', 'Não ser impedido por outros de fazer algo', 'Poder de fato fazer algo, com os meios necessários'], 1, 'A positiva é a capacidade real; a disputa política é sobre qual das duas o Estado deve garantir.'),
       ('O “truque de trocar a palavra” consiste em…', ['Usar sinônimos', 'Redefinir um termo no meio da discussão para vencer sem argumentar', 'Falar outra língua'], 1, 'Quem controla o sentido da palavra controla o veredito; a defesa é pedir a definição.')]),
'sem-binarismo': dict(
 caso=('Numa discussão de família, alguém diz: “quem vota nesse partido é burro ou mau”.', 'O que essa frase faz com a conversa? O que as pesquisas dizem sobre como cada lado imagina o outro?', 'Transforma o debate em embate: a meta vira vencer, não entender. As pesquisas mostram que os dois lados exageram o quanto o outro é radical. A lição dá formas de discordar sem odiar.'),
 erro=('“Discordar de verdade exige tratar o outro como inimigo.”', 'Discordar é parte da democracia; tratar o adversário como inimigo é o que a destrói. Dá para discordar com firmeza e ainda reconhecer o outro como alguém que quer o bem, com valores diferentes.'),
 ferr='teste-de-troca',
 quiz=[('Qual é a diferença entre embate e debate?', ['Nenhuma', 'No embate a meta é vencer; no debate, entender', 'O debate é mais longo'], 1, 'Quem entra para vencer não escuta; quem entra para entender às vezes muda e às vezes muda o outro.'),
       ('O que as pesquisas mostram sobre como cada lado imagina o outro?', ['Que acertam', 'Que os dois lados exageram o quanto o outro é radical', 'Que a esquerda acerta mais'], 1, 'O “outro lado” imaginado é mais extremo do que o real, nos dois lados.')]),
'democracia': dict(
 caso=('Um país tem eleições regulares, mas o governo controla a TV, prende jornalistas e troca juízes à vontade.', 'É uma democracia? O que falta?', 'Falta o que precisa existir junto com a eleição: imprensa livre, tribunais independentes, direitos protegidos, troca pacífica de poder. A lição lista os componentes e mostra como democracias morrem hoje: pelas mãos de eleitos.'),
 erro=('“Democracia é o governo da maioria.”', 'A maioria não pode tudo: sem direitos protegidos para minorias, a eleição vira instrumento de opressão. Democracia é eleição mais limites ao poder de quem venceu.'),
 ferr='quem-faz-o-que',
 quiz=[('Como as democracias costumam morrer hoje?', ['Por golpes militares', 'Por eleitos que, pouco a pouco, capturam tribunais, imprensa e regras eleitorais', 'Por invasões'], 1, 'Levitsky e Ziblatt: a erosão vem de dentro, com aparência de legalidade.'),
       ('Por que democracias costumam dar resultados melhores?', ['Porque são mais ricas', 'Porque informação livre e troca de poder corrigem erros que autocracias escondem', 'Porque têm mais partidos'], 1, 'Sen: nenhuma grande fome do século XX aconteceu numa democracia com imprensa livre.')]),
'como-uma-lei-e-feita': dict(
 caso=('Um deputado anuncia: “aprovei a lei que acaba com a fila do SUS”. Você procura e descobre que o projeto passou numa comissão da Câmara.', 'A lei existe? Quanto falta? Quem ainda pode barrar?', 'Falta muito: plenário, Senado, sanção ou veto, e ainda o STF se contrariar a Constituição. A lição mostra o caminho inteiro e por que “aprovar” costuma ser uma etapa, não o fim.'),
 erro=('“Se foi aprovada na Câmara, virou lei.”', 'Um projeto passa por comissões, dois plenários, sanção e pode ser derrubado pelo Supremo. Cada etapa tem um responsável, e saber qual permite cobrar a pessoa certa.'),
 ferr='quem-faz-o-que',
 quiz=[('Uma medida provisória…', ['É uma lei definitiva', 'Vale na hora, mas perde efeito se o Congresso não a aprovar em até 120 dias', 'Só vale depois do Congresso'], 1, 'É o instrumento de urgência do presidente, e um dos mais criticados por uso excessivo.'),
       ('Uma emenda constitucional precisa de…', ['Maioria simples', 'Três quintos dos deputados e dos senadores, em dois turnos em cada casa', 'Sanção do presidente'], 1, 'Por isso mudar a Constituição é difícil de propósito.')]),
'o-que-e-um-partido': dict(
 caso=('Um amigo diz que vai votar “na pessoa, não no partido”.', 'Isso é possível no Brasil? O que o voto na pessoa faz com o partido dela?', 'Ninguém se elege sem partido, e o voto num deputado ajuda a eleger outros do mesmo partido (o quociente). A lição mostra o que partidos fazem, de onde vem o dinheiro e como avaliá-los.'),
 erro=('“Partidos são todos iguais; só a pessoa importa.”', 'Partidos votam em bloco na maior parte das vezes, recebem fundo público e decidem quem entra na lista. Votar na pessoa sem olhar o partido é entregar metade do voto a quem você não escolheu.'),
 ferr='arvore-dos-partidos',
 quiz=[('De onde vem a maior parte do dinheiro dos partidos brasileiros hoje?', ['Doações de empresas', 'Fundos públicos (partidário e eleitoral)', 'Mensalidades de filiados'], 1, 'Doações empresariais foram proibidas em 2015; o dinheiro público passou a dominar.'),
       ('Por que o Brasil tem tantos partidos?', ['Porque o povo é dividido', 'Por regras que facilitaram a criação e o acesso a fundos e tempo de TV; a cláusula de desempenho tenta reduzir', 'Por tradição'], 1, 'Incentivos institucionais, não ideologia, explicam a fragmentação.')]),
'como-votar-bem': dict(
 caso=('Faltam dois dias para a eleição e você só decidiu o voto para presidente.', 'E os outros cinco votos? O que dá para fazer em duas horas?', 'Dá para conhecer a história, ler as propostas, checar os números e olhar como o candidato a deputado vota. A lição dá o roteiro, e lembra que o voto para o Legislativo é o que mais decide o seu dia a dia.'),
 erro=('“Meu voto para deputado não muda nada.”', 'É o que mais muda: deputados fazem as leis e o orçamento, e o seu voto conta para a chapa inteira. A conta do quociente eleitoral é o que a lição explica.'),
 ferr='ficha-do-candidato',
 quiz=[('Qual é a armadilha mais comum na hora de votar?', ['Ler demais', 'Escolher pelo carisma ou pela promessa impossível, sem checar história e números', 'Votar em branco'], 1, 'A lição lista as armadilhas e dá um antídoto para cada uma.'),
       ('O que acontece com o voto num deputado que não se elege?', ['É perdido', 'Pode ajudar a eleger outro candidato do mesmo partido ou federação', 'Vai para o mais votado'], 1, 'É o sistema proporcional: o voto conta para a legenda.')]),
'checagem-de-fatos': dict(
 caso=('Chega no grupo da família um áudio dizendo que uma vacina causa uma doença grave, “confirmado por médicos”.', 'O que você faz nos próximos dois minutos?', 'Procura a fonte, busca o título numa agência de checagem, olha a data e desconfia da emoção. A lição dá o teste de dois minutos e mostra por que a mentira viraliza mais do que a verdade.'),
 erro=('“Se veio de alguém que confio, é verdade.”', 'Confiança na pessoa não é evidência sobre o conteúdo: quem encaminha também foi enganado. Boatos viajam justamente por redes de confiança.'),
 ferr='que-truque-e-esse',
 quiz=[('Por que a mentira viraliza mais do que a verdade?', ['Porque é mais bem escrita', 'Porque mexe com emoção (medo, raiva, nojo) e é mais nova e surpreendente', 'Porque os algoritmos a preferem por lei'], 1, 'Estudos mostram que notícias falsas se espalham mais rápido e mais longe no Twitter, movidas por emoção.'),
       ('Qual é o primeiro passo do teste de dois minutos?', ['Compartilhar e perguntar', 'Procurar a fonte original e a data', 'Responder com raiva'], 1, 'Sem fonte e sem data, o conteúdo não merece encaminhamento.')]),
}
