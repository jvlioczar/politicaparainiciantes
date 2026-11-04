"""Bloco “Problemas sociais do Brasil” (novembro de 2026): dívidas, impunidade, os protegidos, golpes, transparência, facções,
milícias, desigualdade e bets. Cada lição segue o padrão do site; a camada didática está em brasil_problemas_did.py."""
PB = 'Problemas sociais do Brasil'
W = 'https://pt.wikipedia.org/wiki/'

LICOES_BR = [
dict(slug='dividas-e-devedores', grupo=PB, titulo='Dívidas: quem deve, quem paga e quem sai ganhando', resumo='Recuperação judicial, Refis, renegociações e o limite de cinco anos no Serasa: quando a segunda chance é justa e quando premia a má gestão.', corpo='''
<p class="abre">Uma parte da sensação de injustiça no Brasil vem das dívidas: a empresa que quebra e continua funcionando, o grande devedor que espera o próximo parcelamento, o nome que sai do cadastro negativo depois de cinco anos. Ao mesmo tempo, quem paga em dia sente que paga pelos outros. As duas percepções têm fundamento, e as regras que as provocam também têm razões. A pergunta útil é qual regra protege quem precisa e qual premia quem escolheu não pagar.</p>
<h2>As regras que mais geram revolta</h2>
<table><thead><tr><th>Regra</th><th>O que diz</th><th>Por que existe</th><th>Onde falha</th></tr></thead><tbody>
<tr><td><strong>Recuperação judicial</strong></td><td>A empresa em crise suspende cobranças por 180 dias e propõe um plano de pagamento, votado pelos credores (Lei 11.101/2005, reformada em 2020)</td><td>Salvar empresas viáveis, empregos e fornecedores; uma falência destrói mais valor do que uma reorganização</td><td>Empresas inviáveis ganham tempo; credores pequenos aceitam descontos de 50% a 90% porque não têm escolha</td></tr>
<tr><td><strong>Refis e parcelamentos tributários</strong></td><td>Programas especiais que perdoam multas e juros de quem deve impostos</td><td>Recuperar parte de dívidas que talvez nunca fossem pagas</td><td>Foram dezenas desde 2000; a Receita Federal já apontou que a expectativa do próximo programa estimula o atraso</td></tr>
<tr><td><strong>Cinco anos no cadastro negativo</strong></td><td>O Código de Defesa do Consumidor (art. 43) proíbe manter a informação negativa por mais de cinco anos</td><td>Dar uma segunda chance; impedir a exclusão permanente do crédito por um problema antigo</td><td>Quem nunca pagou volta ao mercado ao lado de quem pagou em dia</td></tr>
<tr><td><strong>Lei do superendividamento</strong></td><td>Garante um mínimo para viver e permite renegociar todas as dívidas juntas (Lei 14.181/2021)</td><td>Pessoas sem saída deixam de consumir, trabalhar formalmente e pagar qualquer coisa</td><td>Depende de distinguir quem se endividou por necessidade de quem abusou do crédito</td></tr>
</tbody></table>
<h2>Uma correção importante sobre o Serasa</h2>
<p>Sair do cadastro depois de cinco anos não apaga a dívida. Ela continua existindo e pode ser cobrada enquanto não prescreve, o que, para a maioria das dívidas de consumo, também leva cinco anos. O que muda é que a informação deixa de ser usada para negar crédito. Muitos países têm limite parecido: nos Estados Unidos, a informação negativa sai do relatório de crédito em sete anos. A escolha de um prazo é uma escolha moral sobre quanto tempo um erro deve pesar na vida de alguém.</p>
<h2>Má gestão recompensada?</h2>
<p>O caso mais citado é o das Americanas: em janeiro de 2023, a empresa revelou inconsistências contábeis de cerca de R$ 20 bilhões e pediu recuperação judicial com dívidas acima de R$ 40 bilhões. A recuperação manteve a empresa e os empregos, e os credores aceitaram perdas. A investigação sobre a fraude seguiu em paralelo. O exemplo mostra as duas faces: a recuperação protege quem trabalha e vende para a empresa, e não deveria proteger quem fraudou. Quando os responsáveis por uma fraude seguem sem consequência pessoal, a sensação de que a má gestão compensa tem base.</p>
<p>Com os impostos acontece algo parecido. O estoque da dívida ativa da União está na casa dos trilhões de reais, concentrado em poucos grandes devedores, muitos deles empresas que já não existem. A <strong>transação tributária</strong>, criada em 2020, tenta substituir o Refis genérico por acordos caso a caso, com desconto maior para quem de fato não consegue pagar e menor para quem pode.</p>
<h2>Quem paga a conta</h2>
<p>O calote não some: ele entra no preço. Os juros cobrados no Brasil estão entre os mais altos do mundo, e parte da explicação é a inadimplência e a dificuldade de recuperar garantias. Quem paga em dia financia, pelo juro, quem não paga. Isso explica a revolta do bom pagador e também por que o juro alto empurra mais gente para a inadimplência. O rotativo do cartão chegou a passar de 400% ao ano; desde 2024, a lei limita juros e encargos a 100% do valor original da dívida.</p>
<h2>Separar o devedor que precisa do que escolheu</h2>
<ul>
<li><strong>Devedor por necessidade:</strong> perdeu o emprego, adoeceu, teve renda cortada. A renegociação e o limite de cinco anos são o que permite recomeçar, e programas como o Desenrola renegociaram dívidas de milhões de pessoas.</li>
<li><strong>Devedor estratégico:</strong> pode pagar, mas calcula que vale mais a pena esperar o próximo perdão, empurrar o processo ou trocar de CNPJ. Para ele, cada programa genérico é um prêmio.</li>
</ul>
<p>Uma boa política trata os dois de forma diferente: alívio para quem prova que não pode, cobrança firme e sem perdão recorrente para quem pode e não quer. Veja <a href="o-que-esta-por-tras.html">o que está por trás das decisões</a> para entender por que programas genéricos são tão frequentes: quem deve muito se organiza melhor do que quem paga em dia.</p>
''', fontes=[('Recuperação judicial (Wikipédia)', W + 'Recupera%C3%A7%C3%A3o_judicial'), ('Lei 11.101/2005 (Planalto)', 'https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2005/lei/l11101.htm'), ('Código de Defesa do Consumidor, art. 43 (Planalto)', 'https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm'), ('Lei do superendividamento (Planalto)', 'https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14181.htm'), ('Caso Americanas (Wikipédia)', W + 'Americanas')]),

dict(slug='impunidade', grupo=PB, titulo='Impunidade: por que tantos crimes ficam sem resposta', resumo='Homicídios não esclarecidos, processos que prescrevem, mortes no trânsito, menores, violência doméstica e ruas inseguras: o que é fato e o que é mito.', corpo='''
<p class="abre">O Brasil tem a terceira maior população carcerária do mundo e, ao mesmo tempo, uma sensação generalizada de impunidade. As duas coisas são verdade: o país prende muito, e prende mal. A maior parte dos presos responde por tráfico ou crimes contra o patrimônio, enquanto a maioria dos homicídios nunca chega a um culpado. Entender esse paradoxo é o primeiro passo para discutir segurança sem slogan.</p>
<h2>Onde a impunidade é maior</h2>
<ul>
<li><strong>Homicídios:</strong> segundo o Instituto Sou da Paz, só cerca de um terço dos homicídios do país é esclarecido, com diferenças enormes entre estados. Em países como o Reino Unido, a taxa passa de 80%. Sem investigação, a punição não depende da lei: depende de sorte.</li>
<li><strong>Golpes e crimes pequenos:</strong> estelionatos já passam de 1,9 milhão de registros por ano, e a maioria nunca é investigada. Veja <a href="golpes-e-fraudes.html">golpes e fraudes</a>.</li>
<li><strong>Processos longos:</strong> recursos sucessivos e prazos de prescrição fazem casos expirarem antes da decisão final. Desde 2019, o STF só permite a prisão após o fim de todos os recursos, com exceções, como as condenações do júri, que podem ser executadas logo (decisão de 2024).</li>
<li><strong>Reparação do dano:</strong> o juiz pode fixar uma indenização mínima para a vítima na sentença, mas ela raramente é paga. A vítima perde duas vezes.</li>
</ul>
<h2>Os casos que mais revoltam, e o que diz a lei</h2>
<table><thead><tr><th>Situação</th><th>O que a lei diz</th><th>Por que parece impune</th></tr></thead><tbody>
<tr><td><strong>Morte no trânsito</strong></td><td>Homicídio culposo na direção: 2 a 4 anos; com embriaguez, 5 a 8 anos (desde 2017). Em casos extremos, como racha, a Justiça pode reconhecer dolo eventual e levar ao júri</td><td>Penas até 4 anos costumam ser trocadas por prestação de serviços; mais de 30 mil pessoas morrem por ano no trânsito</td></tr>
<tr><td><strong>Menores de idade</strong></td><td>Adolescentes de 12 a 17 anos respondem por ato infracional, com medidas que vão até a internação por 3 anos (ECA). A internação é possível já na primeira vez quando há violência ou grave ameaça</td><td>O limite de 3 anos para um homicídio parece pouco, e para atos sem violência, como o tráfico, a internação não é automática</td></tr>
<tr><td><strong>Violência doméstica</strong></td><td>A Lei Maria da Penha (2006) criou medidas protetivas e proibiu penas como cesta básica; desde 2024, o feminicídio é crime próprio, com pena de 20 a 40 anos</td><td>Medidas protetivas sem fiscalização, delegacias especializadas que fecham à noite e subnotificação; cerca de 1.400 mulheres são mortas por ano por serem mulheres</td></tr>
<tr><td><strong>Ruas inseguras</strong></td><td>Roubo e furto têm penas previstas; a polícia militar faz o policiamento, e a civil investiga</td><td>Mais de 40 mil mortes violentas por ano; roubo de celular raramente investigado; a polícia civil não tem pessoal para tudo</td></tr>
</tbody></table>
<p>Uma correção vale para o caso dos menores: a ideia de que um adolescente que comete um crime hediondo “não é punido na primeira passagem” não corresponde à lei. A internação já é possível quando há violência; o debate real é sobre o tempo máximo e sobre a idade, que é o tema do debate sobre <a href="debates/maioridade-penal.html">maioridade penal</a>.</p>
<h2>Por que acontece</h2>
<ul>
<li><strong>A certeza pesa mais que a pena:</strong> a pesquisa sobre dissuasão é consistente. Aumentar penas muda pouco quando a chance de ser pego é baixa. O Brasil costuma responder ao crime aumentando penas, e não aumentando a investigação.</li>
<li><strong>Investigação fraca:</strong> faltam peritos, delegados e banco de dados integrado entre estados. A polícia civil é o elo mais esquecido do sistema.</li>
<li><strong>Prisão sem efeito:</strong> presídios superlotados e controlados por facções devolvem à rua gente mais ligada ao crime do que entrou. Veja <a href="faccoes-e-sistema-prisional.html">facções e sistema prisional</a>.</li>
<li><strong>Seletividade:</strong> o sistema é rápido com o pobre pego em flagrante e lento com quem tem bom advogado e acesso a tribunais superiores. Veja <a href="os-protegidos.html">os protegidos</a>.</li>
</ul>
<h2>O que tende a funcionar</h2>
<p>Investigar homicídios como prioridade, com metas e perícia; integrar dados entre estados; focar a polícia nos lugares e pessoas que concentram a violência; cumprir rápido penas proporcionais em vez de prometer penas enormes que não se cumprem; e reparar a vítima. Experiências como o Pacto pela Vida, em Pernambuco, e programas de redução de homicídios em São Paulo e no Ceará mostram queda quando a investigação melhora, e recaída quando ela é abandonada. Veja <a href="politicas-baseadas-em-evidencias.html">políticas baseadas em evidências</a>.</p>
''', fontes=[('Onde mora a impunidade (Instituto Sou da Paz)', 'https://soudapaz.org/'), ('Anuário Brasileiro de Segurança Pública (FBSP)', 'https://forumseguranca.org.br/'), ('Estatuto da Criança e do Adolescente, art. 122 (Planalto)', 'https://www.planalto.gov.br/ccivil_03/leis/l8069.htm'), ('Lei Maria da Penha (Wikipédia)', W + 'Lei_Maria_da_Penha'), ('Código de Trânsito, art. 302 (Planalto)', 'https://www.planalto.gov.br/ccivil_03/leis/l9503compilado.htm')]),

dict(slug='os-protegidos', grupo=PB, titulo='Os protegidos: dinheiro, farda e foro diante da Justiça', resumo='Por que empresários, militares, juízes e políticos costumam escapar: foro, imunidade, prescrição, justiça militar, anistia, e as exceções recentes.', corpo='''
<p class="abre">A lei é a mesma para todos no papel. Na prática, o caminho entre o crime e a punição muda conforme quem o cometeu. Quem tem dinheiro paga bons advogados e chega aos tribunais superiores; quem tem cargo tem foro especial e imunidade; quem tem farda tem justiça própria e, no passado, anistia. Nem toda diferença é privilégio injustificado, mas várias são, e entender cada uma ajuda a cobrar a mudança certa.</p>
<h2>Dinheiro: o tempo como defesa</h2>
<p>Num processo criminal, o tempo favorece o réu: cada recurso adia a decisão, e o prazo de prescrição corre. Quem tem bons advogados usa todos os recursos possíveis até o STF; quem depende da Defensoria Pública, sobrecarregada, raramente chega lá. Por isso a população carcerária é jovem, pobre e majoritariamente negra, enquanto condenações por crimes financeiros e de corrupção são raras e demoradas.</p>
<ul>
<li><strong>Sonegação:</strong> pagar o imposto devido extingue a punição criminal, a qualquer tempo. O furto de um objeto, mesmo devolvido, não tem a mesma regra.</li>
<li><strong>Delação e leniência:</strong> acordos que reduzem penas em troca de provas e devolução de dinheiro. Revelaram esquemas que nunca seriam descobertos, e também deixaram réus confessos com penas leves.</li>
<li><strong>Anulações:</strong> processos com falhas graves, como os da Lava Jato julgados por juiz considerado parcial pelo STF, foram anulados. Anular por violação das regras é correto; o problema é quando a falha vem do próprio Estado e o resultado é a impunidade de todos.</li>
</ul>
<h2>Cargo: foro, imunidade e a PEC da Blindagem</h2>
<table><thead><tr><th>Proteção</th><th>O que é</th><th>Debate</th></tr></thead><tbody>
<tr><td><strong>Foro por prerrogativa de função</strong></td><td>Autoridades são julgadas por tribunais superiores, como o STF para deputados, senadores e ministros</td><td>Protege o cargo de juízes locais pressionados, e sobrecarrega tribunais que não foram feitos para instruir processos. O STF restringiu o foro em 2018 e o ampliou de novo em 2025 para crimes cometidos no cargo, mesmo depois que o mandato acaba</td></tr>
<tr><td><strong>Imunidade parlamentar</strong></td><td>Deputados e senadores não respondem por opiniões e votos, e só podem ser presos em flagrante de crime inafiançável</td><td>Protege o mandato contra perseguição; vira escudo quando o Congresso protege os seus</td></tr>
<tr><td><strong>PEC da Blindagem</strong></td><td>Em setembro de 2025, a Câmara aprovou exigir autorização do Congresso, em voto secreto, para processar parlamentares</td><td>Depois de protestos em todo o país, o Senado a rejeitou por unanimidade na Comissão de Constituição e Justiça, no mesmo mês</td></tr>
<tr><td><strong>Juízes e promotores</strong></td><td>A pena administrativa máxima para um magistrado é a aposentadoria compulsória, com salário proporcional</td><td>Uma punição que parece prêmio; a perda do cargo exige ação judicial própria</td></tr>
</tbody></table>
<h2>Farda: justiça militar e anistia</h2>
<p>Crimes militares são julgados pela Justiça Militar. Desde 1996, homicídios dolosos de civis cometidos por policiais militares vão ao júri comum; em 2017, uma lei levou à Justiça Militar da União os crimes de militares das Forças Armadas contra civis em operações como as de garantia da lei e da ordem, o que foi criticado por especialistas em direitos humanos. A Lei da Anistia de 1979 perdoou crimes políticos e, segundo o STF em 2010, também os de agentes da ditadura, como tortura, o que a Corte Interamericana de Direitos Humanos considerou incompatível com o direito internacional. Veja <a href="america-do-sul-e-ditaduras.html">a América do Sul e as ditaduras</a>.</p>
<h2>As exceções recentes</h2>
<p>A impunidade dos poderosos não é absoluta. O Mensalão levou políticos e empresários à prisão em 2012; a Lava Jato prendeu donos de grandes empreiteiras; e, em setembro de 2025, o STF condenou um ex-presidente e generais de quatro estrelas por tentativa de golpe de Estado, algo inédito na história do país. Esses casos mostram que a punição é possível, e também que ela depende de instituições com independência e de pressão pública.</p>
<h2>O que mudaria o quadro</h2>
<ul>
<li>Limitar recursos protelatórios e rever prazos de prescrição em crimes contra a administração pública.</li>
<li>Defensoria pública com estrutura comparável à acusação, para que o tempo deixe de ser privilégio de quem paga.</li>
<li>Foro restrito aos crimes no exercício da função, com julgamento em prazo definido.</li>
<li>Perda do cargo como sanção possível para magistrados e membros do Ministério Público.</li>
<li>Transparência total sobre processos contra autoridades. Veja <a href="transparencia-dos-gastos.html">transparência</a>.</li>
</ul>
<p>O debate sobre <a href="debates/estado-protege-a-burguesia.html">se o Estado protege a burguesia</a> discute a pergunta de fundo: essas proteções são desvios a corrigir, ou o sistema funcionando como foi feito?</p>
''', fontes=[('Foro por prerrogativa de função (Wikipédia)', W + 'Foro_por_prerrogativa_de_fun%C3%A7%C3%A3o'), ('Imunidade parlamentar (Wikipédia)', W + 'Imunidade_parlamentar'), ('Lei da Anistia (Wikipédia)', W + 'Lei_da_Anistia'), ('Justiça Militar (Wikipédia)', W + 'Justi%C3%A7a_Militar_do_Brasil'), ('Lei Orgânica da Magistratura (Planalto)', 'https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp35.htm')]),

dict(slug='golpes-e-fraudes', grupo=PB, titulo='Golpes e fraudes: por que o golpista sai na frente', resumo='Pix, contas laranja, falso atendente e lavagem por fintechs: por que o rastreamento falha, o dano raramente volta e o que bancos e Estado devem fazer.', corpo='''
<p class="abre">O golpe virou o crime mais comum do país. O estelionato passa de 1,9 milhão de registros por ano, segundo o Fórum Brasileiro de Segurança Pública, e em vários estados já supera roubos e furtos. O golpista trabalha com vantagem: o dinheiro sai em segundos, passa por dezenas de contas, e a investigação, quando acontece, chega meses depois. A vítima quase nunca recupera o que perdeu.</p>
<h2>Como funcionam os golpes mais comuns</h2>
<table><thead><tr><th>Golpe</th><th>Como funciona</th></tr></thead><tbody>
<tr><td><strong>Falso atendente ou falsa central</strong></td><td>Alguém se passa pelo banco e convence a vítima a transferir para uma “conta segura” ou a instalar um aplicativo de acesso remoto</td></tr>
<tr><td><strong>Falso parente</strong></td><td>Mensagem de um “filho com número novo” pedindo um Pix urgente</td></tr>
<tr><td><strong>Falsa venda e falso boleto</strong></td><td>Loja ou anúncio que não existe; boleto adulterado com outro destinatário</td></tr>
<tr><td><strong>Investimento milagroso</strong></td><td>Pirâmides, “robôs de trading” e criptomoedas com retorno garantido</td></tr>
<tr><td><strong>Conta laranja</strong></td><td>Contas abertas com documentos de terceiros ou alugadas, por onde o dinheiro passa e se divide até sumir</td></tr>
</tbody></table>
<h2>Por que o rastreamento falha</h2>
<ul>
<li><strong>Velocidade:</strong> o Pix foi feito para ser instantâneo, e o golpista divide o valor em várias contas em minutos. Quando a vítima percebe, o dinheiro já foi sacado ou convertido.</li>
<li><strong>Bloqueio limitado:</strong> o Mecanismo Especial de Devolução (MED), criado em 2021, permite bloquear e devolver valores em caso de fraude, mas só alcançava a primeira conta. Uma versão ampliada, anunciada pelo Banco Central em 2025, permite seguir o dinheiro por várias contas em sequência.</li>
<li><strong>Contas fáceis de abrir:</strong> a abertura digital de contas trouxe inclusão e também facilitou contas laranja. A checagem de identidade varia muito entre instituições.</li>
<li><strong>Investigação fragmentada:</strong> o golpista está num estado, a conta em outro, a vítima em um terceiro. Delegacias raramente investigam valores pequenos, e cada caso parece pequeno.</li>
</ul>
<h2>Quando o golpe vira lavagem do crime organizado</h2>
<p>Em agosto de 2025, a Operação Carbono Oculto mostrou o PCC usando postos de combustível, fundos de investimento e fintechs para lavar bilhões de reais, aproveitando contas que misturavam o dinheiro de muitos clientes e escondiam o dono real. Meses antes, em janeiro de 2025, uma norma da Receita Federal que ampliava o acompanhamento de transações foi revogada depois do boato de que o Pix seria taxado. O episódio mostra o dilema: mais controle ajuda a seguir o dinheiro do crime, e precisa ser explicado para não ser confundido com vigilância do cidadão comum.</p>
<h2>Quem responde pelo prejuízo</h2>
<p>O Superior Tribunal de Justiça entende que bancos respondem por fraudes cometidas por terceiros em suas operações, como contas abertas com documentos falsos (Súmula 479). Quando a própria vítima faz a transferência enganada, os tribunais se dividem, e muitas vezes atribuem a culpa à vítima. Desde o Pacote Anticrime de 2019, o estelionato só é investigado se a vítima pedir formalmente, exceto quando ela é idosa, pessoa com deficiência, criança ou o próprio poder público. A fraude eletrônica tem pena de 4 a 8 anos desde 2021, mas pena alta sem investigação tem pouco efeito.</p>
<h2>O que funcionaria melhor</h2>
<ul>
<li><strong>Bloqueio inteligente:</strong> limites e atrasos automáticos para transferências fora do padrão do cliente, como já fazem alguns bancos à noite.</li>
<li><strong>Responsabilidade compartilhada:</strong> a instituição que abriu a conta laranja sem checar deveria responder pelo prejuízo, o que cria incentivo para checar.</li>
<li><strong>Investigação em escala:</strong> reunir casos pequenos do mesmo golpista em uma só investigação, com dados integrados entre estados e o Banco Central.</li>
<li><strong>Seguir o dinheiro do crime:</strong> transparência sobre o dono real de contas e fundos, para que fintechs não virem caminho de lavagem.</li>
<li><strong>Educação contínua:</strong> a regra de ouro é simples: banco não liga pedindo transferência; desligue e ligue você para o número oficial.</li>
</ul>
<p>Veja também <a href="checagem-de-fatos.html">fake news e checagem de fatos</a>: muitos golpes usam as mesmas técnicas de urgência e medo que a desinformação.</p>
''', fontes=[('Anuário Brasileiro de Segurança Pública (FBSP)', 'https://forumseguranca.org.br/'), ('Mecanismo Especial de Devolução (Banco Central)', 'https://www.bcb.gov.br/estabilidadefinanceira/pix'), ('Súmula 479 do STJ', 'https://www.stj.jus.br/'), ('Lei 14.155/2021, fraude eletrônica (Planalto)', 'https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14155.htm'), ('Estelionato (Wikipédia)', W + 'Estelionato')]),

dict(slug='transparencia-dos-gastos', grupo=PB, titulo='Transparência: para onde vai o dinheiro público', resumo='Lei de Acesso à Informação, portais, sigilos de cem anos, orçamento secreto e emendas Pix: o que já é público, o que ainda se esconde e como fiscalizar.', corpo='''
<p class="abre">O Brasil tem leis de transparência entre as mais avançadas do mundo e, ao mesmo tempo, bilhões de reais gastos sem que se saiba direito quem decidiu e para quê. As duas coisas convivem porque a transparência depende de regras e de vontade de cumpri-las, e governos de todos os lados já preferiram o escuro quando o assunto era deles.</p>
<h2>O que já é público</h2>
<table><thead><tr><th>Ferramenta</th><th>O que mostra</th></tr></thead><tbody>
<tr><td><strong>Lei de Responsabilidade Fiscal (2000)</strong></td><td>Obriga governos a publicar relatórios de receita, gasto e dívida, e limita gastos com pessoal</td></tr>
<tr><td><strong>Portal da Transparência (2004)</strong></td><td>Gastos do governo federal, salários de servidores, contratos, cartões corporativos e transferências</td></tr>
<tr><td><strong>Lei de Acesso à Informação (2011)</strong></td><td>Qualquer pessoa pode pedir informações a órgãos públicos, sem justificar; a resposta deve vir em até 20 dias, prorrogáveis por mais 10</td></tr>
<tr><td><strong>Tribunais de Contas e CGU</strong></td><td>Auditam gastos, apontam irregularidades e podem barrar contratos</td></tr>
<tr><td><strong>Dados de organizações civis</strong></td><td>Projetos como o Querido Diário, da Open Knowledge Brasil, e a Fiquem Sabendo tornam pesquisáveis diários oficiais e pedidos de informação</td></tr>
</tbody></table>
<h2>O que ainda se esconde</h2>
<ul>
<li><strong>Sigilos de cem anos:</strong> a lei permite proteger informações pessoais por até cem anos. O dispositivo foi usado de forma ampla para esconder gastos e agendas de autoridades, e governos de lados diferentes recorreram a ele. Informação pessoal é a de um cidadão comum; o gasto de uma autoridade com dinheiro público não deveria caber aí.</li>
<li><strong>Orçamento secreto:</strong> entre 2020 e 2022, as emendas de relator distribuíram dezenas de bilhões de reais sem registro de quem indicava cada valor. O STF as declarou inconstitucionais em dezembro de 2022.</li>
<li><strong>Emendas Pix:</strong> transferências especiais, criadas em 2019, mandam dinheiro direto ao caixa de prefeituras e estados, sem projeto definido. Em 2024, o ministro Flávio Dino suspendeu a execução de emendas até que houvesse rastreabilidade, e o Congresso aprovou regras novas no fim daquele ano. A fiscalização ainda é difícil.</li>
<li><strong>Penduricalhos:</strong> auxílios e verbas indenizatórias fazem salários do topo do funcionalismo ultrapassarem o teto constitucional, de forma pouco visível. Veja o debate sobre <a href="debates/supersalarios.html">supersalários</a>.</li>
<li><strong>Estados e municípios:</strong> a maior parte do gasto em saúde e educação acontece nas prefeituras, onde os portais são mais pobres e a imprensa local mais fraca.</li>
</ul>
<h2>Por que a transparência importa</h2>
<p>Pela fórmula de Klitgaard, a corrupção cresce com o poder de decidir e diminui com a prestação de contas. Veja <a href="corrupcao.html">corrupção</a>. Quase todo grande escândalo começou com um dado público lido por alguém: um jornalista, um auditor, um cidadão. Transparência também melhora o gasto honesto, porque permite comparar o preço de uma obra com outra e cobrar quem gasta mal sem roubar. E protege a democracia: quem não sabe para onde vai o dinheiro não consegue votar sabendo o que escolhe.</p>
<h2>Os argumentos de quem defende sigilo</h2>
<p>Há sigilos legítimos: segurança nacional, investigações em curso, dados de saúde e de pessoas comuns, estratégias de negociação. O problema é a falta de critério e de prazo. A regra boa é a da lei: o público é a regra, o sigilo é a exceção, sempre justificada e com prazo, e nunca para proteger a própria autoridade de constrangimento.</p>
<h2>Como você pode fiscalizar</h2>
<ol class="passos">
<li><strong>Escolha um gasto perto de você:</strong> a merenda da escola, a obra da praça, as emendas do deputado em quem votou.</li>
<li><strong>Procure no portal:</strong> o Portal da Transparência federal, o do seu estado e o da sua prefeitura.</li>
<li><strong>Peça o que não estiver lá:</strong> pela Lei de Acesso, no sistema Fala.BR ou no site do órgão. Não é preciso justificar.</li>
<li><strong>Compare:</strong> o preço por aluno, por quilômetro, por consulta, com cidades parecidas.</li>
<li><strong>Divulgue com cuidado:</strong> dado público é forte; acusação sem prova é fraca. Veja <a href="checagem-de-fatos.html">checagem de fatos</a>.</li>
</ol>
''', fontes=[('Portal da Transparência', 'https://portaldatransparencia.gov.br/'), ('Lei de Acesso à Informação (Planalto)', 'https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'), ('Orçamento secreto (Wikipédia)', W + 'Or%C3%A7amento_secreto'), ('Querido Diário', 'https://queridodiario.ok.org.br/'), ('Fiquem Sabendo', 'https://fiquemsabendo.com.br/')]),

dict(slug='faccoes-e-sistema-prisional', grupo=PB, titulo='Facções: como o tráfico tomou prisões e periferias', resumo='Como PCC e Comando Vermelho nasceram nos presídios, dominam territórios e lavam dinheiro, e o que a evidência diz sobre confronto, prisão e inteligência.', corpo='''
<p class="abre">As maiores facções criminosas do Brasil nasceram dentro de presídios. O Comando Vermelho surgiu em 1979, na prisão da Ilha Grande, no Rio; o Primeiro Comando da Capital, em 1993, em Taubaté, um ano depois do massacre do Carandiru. Hoje estão em todos os estados, controlam territórios onde vivem milhões de pessoas e movimentam negócios que vão do varejo de drogas a combustíveis e fundos de investimento. Entender como isso aconteceu ajuda a entender por que as respostas mais populares costumam falhar.</p>
<h2>A prisão como escritório do crime</h2>
<p>Presídios superlotados, com o Estado ausente das celas, deixam o preso sem proteção. A facção oferece segurança, comida e assistência à família, em troca de lealdade e de serviços quando ele sair. Quem entra por um crime pequeno sai devendo à organização. Em 2015, o STF declarou o sistema prisional um “estado de coisas inconstitucional”, pela violação massiva de direitos, e em 2023 mandou o governo elaborar um plano nacional para mudá-lo.</p>
<ul>
<li><strong>Quem está preso:</strong> o Brasil tem mais de 800 mil pessoas presas, contando a prisão domiciliar. Uma parte grande responde por tráfico, muitas vezes réus primários, sem arma e com pouca droga.</li>
<li><strong>A Lei de Drogas (2006):</strong> não definiu quanto separa o usuário do traficante, e a decisão ficou com o policial e o juiz. O número de presos por tráfico cresceu muito desde então. Em 2024, o STF fixou 40 gramas de maconha como presunção de uso pessoal.</li>
<li><strong>O efeito:</strong> a prisão de varejistas pequenos não reduz o tráfico, porque eles são substituídos no dia seguinte, e alimenta o recrutamento da facção dentro da cadeia.</li>
</ul>
<h2>O domínio das periferias</h2>
<p>Fora da prisão, a facção controla territórios: decide quem entra, cobra “taxas”, julga conflitos no “tribunal do crime” e impõe toques de recolher. Para quem mora ali, a facção é a autoridade mais presente, e o Estado aparece sobretudo na forma de operação policial. Isso cria uma relação ambígua: medo da facção, desconfiança da polícia e pouca escolha.</p>
<h2>O dinheiro</h2>
<p>As facções viraram empresas. O PCC exporta cocaína para a Europa e a África pelos portos, opera no Paraguai e na Bolívia e, segundo a Operação Carbono Oculto, de 2025, lavava bilhões por meio de postos de combustível, fintechs e fundos. Atacar esse dinheiro desorganiza a facção mais do que prender seus soldados.</p>
<h2>Confronto ou inteligência?</h2>
<table><thead><tr><th>Estratégia</th><th>O que se argumenta a favor</th><th>O que a evidência mostra</th></tr></thead><tbody>
<tr><td><strong>Grandes operações</strong></td><td>Retomar territórios, mostrar força, prender líderes</td><td>A operação de outubro de 2025 nos complexos do Alemão e da Penha, no Rio, foi a mais letal da história do país, com mais de 120 mortos, incluindo policiais. Operações assim raramente mudam o controle do território por mais de semanas</td></tr>
<tr><td><strong>Inteligência financeira</strong></td><td>Seguir o dinheiro e bloquear a lavagem</td><td>Ataca o que sustenta a organização; exige cooperação entre Receita, Banco Central, Polícia Federal e Ministério Público</td></tr>
<tr><td><strong>Controle das prisões</strong></td><td>Separar presos por perigo, cortar a comunicação, oferecer trabalho e estudo</td><td>Onde o Estado retoma o presídio, o recrutamento cai; presídios federais isolam líderes</td></tr>
<tr><td><strong>Presença do Estado</strong></td><td>Escola, emprego, saúde, iluminação e polícia de proximidade</td><td>Reduz a dependência da facção, mas leva anos e exige continuidade; as UPPs do Rio mostraram o efeito e o colapso quando faltou</td></tr>
</tbody></table>
<p>A população dessas áreas quer segurança, e muitos apoiam operações duras. O ponto não é escolher entre firmeza e direitos: é perguntar o que de fato diminui o poder da facção. A experiência sugere que a resposta combina asfixiar o dinheiro, retomar o controle das prisões, investigar homicídios e garantir que o Estado chegue com mais do que viaturas. Veja os debates sobre <a href="debates/drogas.html">drogas</a>, <a href="debates/narcoterrorismo.html">narcoterrorismo</a> e <a href="debates/seguranca-publica.html">segurança pública</a>.</p>
''', fontes=[('Primeiro Comando da Capital (Wikipédia)', W + 'Primeiro_Comando_da_Capital'), ('Comando Vermelho (Wikipédia)', W + 'Comando_Vermelho'), ('Anuário Brasileiro de Segurança Pública (FBSP)', 'https://forumseguranca.org.br/'), ('ADPF 347, estado de coisas inconstitucional (STF)', 'https://portal.stf.jus.br/'), ('Lei de Drogas (Planalto)', 'https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11343.htm')]),

dict(slug='milicias', grupo=PB, titulo='Milícias: quando polícia, política e crime se misturam', resumo='De “autodefesa” a máfia: como agentes do Estado viraram donos de território, serviços e votos, o caso Marielle e o que separa a polícia honesta da milícia.', corpo='''
<p class="abre">Milícias são grupos armados formados em grande parte por policiais, ex-policiais, bombeiros e agentes penitenciários, que controlam territórios e cobram por “proteção”. Nasceram no Rio de Janeiro com o discurso de expulsar o tráfico e viraram outra forma de crime organizado, com uma diferença perigosa: estão dentro do Estado. Por isso o tema não é só segurança; é a relação entre polícia, política e crime.</p>
<h2>Como funcionam</h2>
<ul>
<li><strong>Taxa de segurança:</strong> comerciantes e moradores pagam para não serem atacados, pela própria milícia.</li>
<li><strong>Monopólio de serviços:</strong> gás, internet e TV clandestinas, transporte alternativo, água e até grilagem e construção de prédios irregulares. Em 2019, dois prédios construídos pela milícia desabaram na Muzema, no Rio, e mataram 24 pessoas.</li>
<li><strong>Controle do voto:</strong> candidatos ligados ao grupo fazem campanha livre no território, adversários não entram. É o curral eleitoral armado.</li>
<li><strong>Proteção oficial:</strong> membros que estão na polícia sabem das operações, desviam investigações e usam a farda como cobertura.</li>
</ul>
<p>Levantamentos da Universidade Federal Fluminense com o Fogo Cruzado indicaram que, na região metropolitana do Rio, as milícias chegaram a controlar a maior parte da área dominada por grupos armados, mais do que o tráfico. Há grupos semelhantes em outros estados, com nomes diferentes.</p>
<h2>A mistura entre polícia, política e crime</h2>
<p>Em 2008, a CPI das Milícias da Assembleia do Rio, presidida por Marcelo Freixo, pediu o indiciamento de mais de 200 pessoas, entre elas vereadores, deputados e policiais. O caso mais conhecido é o assassinato da vereadora Marielle Franco e do motorista Anderson Gomes, em 2018. O executor confesso, Ronnie Lessa, é ex-policial militar; em 2024, ele e o comparsa Élcio de Queiroz foram condenados, e a Polícia Federal prendeu como suspeitos de mandar matar um deputado federal e um conselheiro do Tribunal de Contas, além de um ex-chefe da Polícia Civil, acusado de atrapalhar a investigação. O caso resume o problema: quem deveria investigar estava, segundo a acusação, do lado de quem mandou matar.</p>
<h2>Por que acontece</h2>
<table><thead><tr><th>Causa</th><th>Como pesa</th></tr></thead><tbody>
<tr><td><strong>Estado ausente</strong></td><td>Onde não há serviço público nem polícia confiável, quem oferece ordem manda, mesmo cobrando caro</td></tr>
<tr><td><strong>Informalidade urbana</strong></td><td>Terrenos sem título, transporte sem regulação e serviços clandestinos são mercados prontos para quem tem armas</td></tr>
<tr><td><strong>Voto como negócio</strong></td><td>Território controlado vira voto garantido, e voto vira proteção política e emendas</td></tr>
<tr><td><strong>Impunidade interna</strong></td><td>Corregedorias fracas e espírito de corpo protegem o policial que cruza a linha</td></tr>
<tr><td><strong>Aplauso social</strong></td><td>O discurso de “limpar” o bairro e o “bandido bom é bandido morto” dão às milícias apoio no começo</td></tr>
</tbody></table>
<h2>Separar a polícia da milícia</h2>
<p>A maioria dos policiais não é miliciana, e policiais estão entre as vítimas da violência: centenas são mortos todo ano, muitos de folga. Tratar a polícia inteira como criminosa é injusto e enfraquece quem trabalha certo. O que distingue uma polícia saudável é o controle: corregedoria independente, Ministério Público atuante no controle externo, câmeras corporais, investigação de mortes em operações e salários que não empurrem para o bico armado. Estudos em São Paulo associaram as câmeras corporais a uma queda forte da letalidade policial.</p>
<h2>O que funciona contra as milícias</h2>
<ul>
<li>Seguir o dinheiro: imóveis, cooperativas de transporte e empresas de fachada.</li>
<li>Regularizar terra, transporte e serviços, para tirar o mercado das mãos do grupo armado.</li>
<li>Investigação por órgãos de fora da polícia local, como Polícia Federal e Ministério Público.</li>
<li>Barrar candidaturas ligadas a grupos armados e proteger o voto em áreas dominadas.</li>
</ul>
<p>Veja também <a href="poder-paralelo.html">mercado, mídia e crime no governo</a> e o debate sobre <a href="debates/desmilitarizacao.html">desmilitarização da polícia</a>.</p>
''', fontes=[('Milícias no Rio de Janeiro (Wikipédia)', W + 'Mil%C3%ADcias_no_Rio_de_Janeiro'), ('Assassinato de Marielle Franco (Wikipédia)', W + 'Assassinato_de_Marielle_Franco'), ('Fogo Cruzado', 'https://fogocruzado.org.br/'), ('Desabamento de prédios na Muzema (Wikipédia)', W + 'Desabamento_de_pr%C3%A9dios_na_Muzema'), ('Anuário Brasileiro de Segurança Pública (FBSP)', 'https://forumseguranca.org.br/')]),

dict(slug='desigualdade-social', grupo=PB, titulo='Desigualdade: o tamanho, as causas e o que funciona', resumo='O Brasil está entre os países mais desiguais do mundo. De onde vem isso, como a desigualdade afeta todos e o que os dados mostram sobre reduzi-la.', corpo='''
<p class="abre">O Brasil está entre os países mais desiguais do mundo. Segundo o World Inequality Lab, os 10% mais ricos ficam com mais da metade da renda nacional, e o índice de Gini, que vai de 0 (todos iguais) a 1 (um só tem tudo), está em torno de 0,5, mesmo depois de cair aos menores níveis da série histórica. Desigualdade não é só diferença de renda: é diferença de chance, de saúde, de segurança e de voz.</p>
<h2>De onde ela vem</h2>
<table><thead><tr><th>Causa</th><th>Como pesa</th></tr></thead><tbody>
<tr><td><strong>Escravidão e terra</strong></td><td>O Brasil foi o último país das Américas a abolir a escravidão, em 1888, sem terra, educação ou indenização para os libertos. A Lei de Terras de 1850 já havia fechado o acesso à terra para quem não podia comprar</td></tr>
<tr><td><strong>Educação tardia</strong></td><td>A escola pública só se universalizou no fim do século XX; a diferença de escolaridade entre ricos e pobres virou diferença de salário</td></tr>
<tr><td><strong>Mercado de trabalho</strong></td><td>Perto de 40% dos trabalhadores estão na informalidade, sem direitos nem previdência</td></tr>
<tr><td><strong>Impostos</strong></td><td>O sistema pesa mais sobre o consumo, que os pobres gastam proporcionalmente mais; desde 1995, dividendos são isentos de imposto de renda</td></tr>
<tr><td><strong>Discriminação</strong></td><td>Pessoas pretas e pardas recebem, em média, pouco mais da metade do rendimento de pessoas brancas, segundo o IBGE; mulheres recebem menos que homens na mesma função</td></tr>
<tr><td><strong>Topo do Estado</strong></td><td>Salários e aposentadorias do topo do funcionalismo e benefícios fiscais para setores organizados concentram renda pública</td></tr>
</tbody></table>
<h2>Por que ela importa, mesmo para quem não é pobre</h2>
<ul>
<li><strong>Desperdício de talento:</strong> quem nasce pobre raramente tem a chance de desenvolver o que sabe fazer; o país perde médicos, engenheiros e artistas que nunca existiram.</li>
<li><strong>Violência:</strong> sociedades mais desiguais tendem a ter mais homicídios, mesmo controlando pela renda média.</li>
<li><strong>Democracia:</strong> quem tem muito mais dinheiro tem muito mais voz, financia campanhas e faz lobby; a desigualdade econômica vira desigualdade política.</li>
<li><strong>Mobilidade baixa:</strong> no Brasil, a renda dos pais prevê fortemente a dos filhos. A meritocracia funciona mal quando a largada é tão diferente. Veja o debate sobre <a href="debates/meritocracia.html">meritocracia</a>.</li>
</ul>
<h2>O que reduziu a desigualdade</h2>
<p>A desigualdade caiu nas décadas de 2000 e 2010, voltou a subir na crise e caiu de novo a partir de 2022. Os fatores mais documentados:</p>
<ul>
<li><strong>Salário mínimo valorizado:</strong> reajustes acima da inflação elevaram a base e as aposentadorias atreladas a ele.</li>
<li><strong>Transferências focalizadas:</strong> o Bolsa Família e o Benefício de Prestação Continuada chegam aos mais pobres a custo baixo em relação ao orçamento; estudos do Ipea mostram efeito grande sobre a pobreza extrema.</li>
<li><strong>Educação:</strong> mais anos de escola reduziram a diferença salarial entre níveis de escolaridade.</li>
<li><strong>Formalização:</strong> emprego com carteira traz salário, previdência e seguro-desemprego.</li>
</ul>
<h2>Onde está a disputa</h2>
<p>Quase ninguém defende a desigualdade extrema; a disputa é sobre meios. A esquerda tende a enfatizar tributação progressiva, salário mínimo e serviços públicos; a direita, crescimento, educação, produtividade e menos burocracia para empreender. As duas têm evidência a favor de parte do que defendem, e os países que reduziram a desigualdade costumam ter combinado crescimento com redistribuição. A reforma do Imposto de Renda aprovada em 2025, que isenta quem ganha até R$ 5 mil por mês e cria um imposto mínimo para rendas muito altas, é o exemplo mais recente dessa disputa. Veja os debates sobre <a href="debates/grandes-fortunas.html">grandes fortunas</a>, <a href="debates/programas-sociais.html">programas sociais</a> e <a href="debates/impostos.html">impostos</a>, e a lição sobre <a href="teorias-da-justica.html">teorias da justiça</a>.</p>
''', fontes=[('World Inequality Database', 'https://wid.world/country/brazil/'), ('Desigualdades sociais por cor ou raça (IBGE)', 'https://www.ibge.gov.br/'), ('Ipea', 'https://www.ipea.gov.br/'), ('Desigualdade econômica no Brasil (Wikipédia)', W + 'Desigualdade_econ%C3%B4mica_no_Brasil'), ('Coeficiente de Gini (Wikipédia)', W + 'Coeficiente_de_Gini')]),

dict(slug='bets', grupo=PB, titulo='Bets: como as apostas viraram problema público', resumo='Legalizadas em 2018 e reguladas em 2025, as casas de aposta cresceram com patrocínio e influenciadores. O que mostram os dados sobre vício, dívida e regulação.', corpo='''
<p class="abre">Em poucos anos, as casas de apostas on-line passaram de quase invisíveis a patrocinadoras de quase todos os grandes clubes de futebol, presença constante em intervalos comerciais e em perfis de influenciadores. Junto com elas vieram relatos de famílias endividadas, de dinheiro do Bolsa Família indo para apostas e de jogos manipulados. As bets viraram um problema de saúde pública e de política ao mesmo tempo.</p>
<h2>Como chegamos aqui</h2>
<ul>
<li><strong>2018:</strong> uma lei legalizou as apostas esportivas de quota fixa, mas deixou a regulamentação para depois. Por anos, as casas operaram de fora do país, sem imposto e sem regra.</li>
<li><strong>2023:</strong> a Lei 14.790 regulamentou o setor e incluiu os jogos on-line de cassino, como o “jogo do tigrinho”.</li>
<li><strong>2025:</strong> desde janeiro, só podem operar empresas autorizadas pelo Ministério da Fazenda, com sede no Brasil, identificação do apostador e proibição de apostas por menores.</li>
</ul>
<h2>O que os dados mostram</h2>
<table><thead><tr><th>Dado</th><th>Fonte</th></tr></thead><tbody>
<tr><td>Brasileiros transferiram cerca de R$ 20 bilhões por mês para casas de apostas via Pix em 2024</td><td>Banco Central, estudo de setembro de 2024</td></tr>
<tr><td>Beneficiários do Bolsa Família enviaram cerca de R$ 3 bilhões a apostas em um único mês</td><td>Banco Central, mesmo estudo</td></tr>
<tr><td>A maior parte do lucro das casas vem de uma minoria que aposta muito e perde muito</td><td>Padrão documentado em vários países</td></tr>
<tr><td>Jogadores aliciados para tomar cartões e manipular resultados</td><td>Operação Penalidade Máxima, do Ministério Público de Goiás, 2023</td></tr>
</tbody></table>
<h2>Por que preocupa</h2>
<ul>
<li><strong>Vício:</strong> o transtorno do jogo é reconhecido como doença. Aplicativos com apostas instantâneas, bônus e notificações são desenhados para manter a pessoa jogando.</li>
<li><strong>Dívida e pobreza:</strong> quem aposta para “sair do aperto” tende a perder justamente o que não tinha. Varejistas relataram queda de consumo atribuída às apostas.</li>
<li><strong>Publicidade:</strong> influenciadores e ídolos do futebol mostram ganhos e escondem perdas; adolescentes são atingidos mesmo com a proibição.</li>
<li><strong>Integridade do esporte:</strong> a aposta em lances específicos facilita a manipulação por poucos jogadores.</li>
<li><strong>Crime:</strong> casas ilegais seguem operando, e o setor já foi usado para lavar dinheiro.</li>
</ul>
<p>Em 2024 e 2025, o Senado fez uma CPI das Bets, que ouviu influenciadores e empresários e terminou sem relatório aprovado. A disputa sobre quanto tributar as casas e quanto limitar a publicidade continuou no Congresso.</p>
<h2>As opções em debate</h2>
<table><thead><tr><th>Opção</th><th>A favor</th><th>Contra</th></tr></thead><tbody>
<tr><td><strong>Proibir</strong></td><td>Corta a oferta legal e a publicidade</td><td>As casas voltam para a ilegalidade, sem imposto nem proteção ao apostador</td></tr>
<tr><td><strong>Regular forte</strong></td><td>Limites de gasto e de tempo, pausa obrigatória, autoexclusão, fim de bônus e restrição de publicidade, como no fumo</td><td>Exige fiscalização e enfrenta o lobby do setor e dos clubes</td></tr>
<tr><td><strong>Regular leve</strong></td><td>Respeita a liberdade do adulto e arrecada</td><td>Deixa o vício e a dívida concentrados em quem já está pior</td></tr>
</tbody></table>
<p>A evidência internacional favorece a regulação forte: a liberdade de apostar o próprio dinheiro merece proteção, mas um produto desenhado para explorar a compulsão, anunciado a quem menos se defende, não oferece escolha livre. Veja o debate sobre <a href="debates/apostas.html">apostas</a> e a lição sobre <a href="vieses-cognitivos.html">vieses cognitivos</a>.</p>
''', fontes=[('Lei 14.790/2023 (Planalto)', 'https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14790.htm'), ('Análise técnica sobre apostas (Banco Central)', 'https://www.bcb.gov.br/'), ('Secretaria de Prêmios e Apostas (Ministério da Fazenda)', 'https://www.gov.br/fazenda/pt-br/composicao/orgaos/secretaria-de-premios-e-apostas'), ('Apostas esportivas no Brasil (Wikipédia)', W + 'Apostas_esportivas'), ('Transtorno do jogo (Wikipédia)', W + 'Jogo_patol%C3%B3gico')]),
]
