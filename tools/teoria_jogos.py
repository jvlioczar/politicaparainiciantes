"""Lição Avançada de novembro de 2026: teoria dos jogos, economia comportamental e cooperação humana aplicadas à
política. Mesmo formato de costumes_transito.py, com a camada didática no fim. Grupo próprio no nível Avançado."""
GTJ = 'Cooperação e conflito'
W = 'https://pt.wikipedia.org/wiki/'

LICOES_TJ = [
dict(slug='teoria-dos-jogos', grupo=GTJ, titulo='Teoria dos jogos: ganha-ganha, ganha-perde e perde-perde', resumo='Dilema do prisioneiro, tragédia dos comuns e economia comportamental: por que cooperar é difícil, e como as regras certas tornam a cooperação possível.', corpo='''
<p class="abre">Muita coisa na política parece irracional: países que se arruínam numa guerra comercial, estados que perdem arrecadação para atrair a mesma fábrica, partidos que preferem ver o país pior a dar uma vitória ao adversário. A teoria dos jogos ajuda a entender esses casos. Ela estuda situações em que o resultado de cada um depende também do que os outros fazem, e mostra uma coisa incômoda: pessoas racionais, cada uma buscando o melhor para si, podem chegar juntas a um resultado ruim para todas. A boa notícia é que ela também mostra como sair dessa armadilha.</p>
<h2>Três tipos de jogo</h2>
<table><thead><tr><th>Tipo</th><th>O que acontece</th><th>Exemplo</th></tr></thead><tbody>
<tr><td><strong>Ganha-ganha (soma positiva)</strong></td><td>A cooperação cria valor novo, e os dois lados saem melhor</td><td>Comércio voluntário, vacinação, ciência compartilhada, acordos que reduzem custos para todos</td></tr>
<tr><td><strong>Ganha-perde (soma zero)</strong></td><td>O que um ganha, o outro perde; o total não muda</td><td>Uma cadeira no Senado, um jogo de futebol, a divisão de um orçamento já fixo</td></tr>
<tr><td><strong>Perde-perde (soma negativa)</strong></td><td>O conflito destrói valor, e os dois lados saem pior</td><td>Guerras, guerras comerciais, guerra fiscal entre estados, campanhas de difamação mútua</td></tr>
</tbody></table>
<p>Um erro político comum é tratar como soma zero um jogo que é de soma positiva. Pesquisas de psicologia mostram que muita gente pensa assim espontaneamente: se o imigrante ganha, eu perco; se outro país cresce, nós encolhemos. Às vezes é verdade, mas muitas vezes não é, e esse pensamento alimenta políticas que acabam em perde-perde.</p>
<h2>O dilema do prisioneiro</h2>
<p>Dois suspeitos são presos e interrogados separados. Se os dois ficam calados, pegam pena leve. Se um delata e o outro cala, o delator sai livre e o outro pega pena alta. Se os dois delatam, ambos pegam pena média. Para cada um, delatar parece sempre melhor, não importa o que o outro faça. Resultado: os dois delatam e ficam pior do que se tivessem cooperado.</p>
<p>O mesmo desenho aparece na política o tempo todo:</p>
<ul>
<li><strong>Guerra fiscal:</strong> cada estado dá isenção de imposto para atrair empresas. Se todos dão, a empresa vai para onde iria de qualquer jeito, e todos perdem arrecadação. A reforma tributária de 2023 tentou acabar com esse jogo ao cobrar o imposto no destino.</li>
<li><strong>Corrida armamentista:</strong> cada país se arma porque o outro se arma, e ambos gastam fortunas sem ficar mais seguros.</li>
<li><strong>Campanhas sujas:</strong> se um candidato ataca e o outro não, o atacante pode ganhar; se os dois atacam, a política inteira perde credibilidade.</li>
<li><strong>Guerras tarifárias:</strong> cada país sobe a tarifa para proteger a própria indústria, e o comércio entre eles encolhe para os dois lados.</li>
</ul>
<p>O ponto de chegada em que ninguém quer mudar sozinho é chamado de equilíbrio de Nash, em homenagem ao matemático John Nash, Nobel de Economia em 1994. O dilema mostra que um equilíbrio pode ser estável e, ainda assim, ruim para todos.</p>
<h2>A tragédia dos comuns</h2>
<p>Em 1968, o ecólogo Garrett Hardin descreveu um pasto aberto a todos: cada pastor ganha ao pôr mais uma vaca, mas o custo do pasto desgastado é dividido entre todos. Cada um age de forma sensata, e o pasto acaba. O mesmo vale para a pesca, a água, a floresta, o clima e até a confiança nas instituições. É a lógica do lixo jogado na rua, da lição <a href="para-o-bem-e-para-o-mal.html">Para o bem e para o mal</a>.</p>
<p>Hardin achava que só havia duas saídas: privatizar ou deixar o Estado controlar. A cientista política Elinor Ostrom, primeira mulher a ganhar o Nobel de Economia, em 2009, estudou comunidades pelo mundo e mostrou uma terceira: grupos que criam as próprias regras, fiscalizam uns aos outros, punem de forma gradual e resolvem conflitos localmente conseguem cuidar de bens comuns por séculos.</p>
<h2>Como a cooperação nasce</h2>
<ul>
<li><strong>Jogo repetido:</strong> quando as pessoas se encontram de novo, trapacear hoje custa a confiança de amanhã. Em torneios de computador organizados pelo cientista político Robert Axelrod, por volta de 1980, a estratégia vencedora foi uma das mais simples: cooperar no primeiro lance e depois repetir o que o outro fez, o “olho por olho”. Ela é gentil, retalia e perdoa.</li>
<li><strong>Reputação:</strong> se todos sabem quem trapaceou, trapacear fica caro. Por isso transparência e imprensa livre importam.</li>
<li><strong>Regras e contratos:</strong> um terceiro que faz valer os acordos, como a Justiça, transforma o dilema em cooperação. É a ideia central do <a href="contrato-social.html">contrato social</a>.</li>
<li><strong>Punição de quem trapaceia:</strong> em experimentos de bens públicos, as contribuições tendem a cair com o tempo; quando os participantes podem punir quem não contribui, mesmo pagando por isso, a cooperação volta a subir.</li>
<li><strong>Identidade compartilhada:</strong> cooperamos mais com quem sentimos como “nós”. Isso ajuda dentro do grupo, e atrapalha quando o outro lado vira inimigo, como mostra a lição sobre o <a href="perigo-do-tribalismo.html">tribalismo</a>.</li>
</ul>
<h2>O que a economia comportamental acrescenta</h2>
<p>A teoria clássica supõe pessoas frias e calculistas. Os experimentos mostram outra coisa. No jogo do ultimato, uma pessoa propõe como dividir um dinheiro e a outra aceita ou recusa; se recusar, ninguém leva nada. Pela lógica fria, deveria aceitar qualquer valor. Na prática, ofertas muito baixas costumam ser recusadas: as pessoas aceitam perder dinheiro para punir o que veem como injusto. O senso de justiça é parte do jogo.</p>
<p>Daniel Kahneman, Nobel em 2002, mostrou como vieses distorcem decisões, e Richard Thaler, Nobel em 2017, como pequenos empurrões no desenho das escolhas, os <em>nudges</em>, mudam comportamentos, como a adesão automática a um plano de previdência. Para a política, a lição é dupla: as pessoas cooperam mais do que a teoria fria prevê, e reagem com força ao que percebem como injustiça. Veja a lição sobre <a href="vieses-cognitivos.html">vieses cognitivos</a>.</p>
<h2>Como usar isso para ler a política</h2>
<ol>
<li><strong>Pergunte que jogo é:</strong> o problema é de soma zero de verdade, ou alguém está vendendo como disputa algo que todos poderiam ganhar?</li>
<li><strong>Procure o dilema:</strong> se todos agem de forma sensata e o resultado é ruim, o problema é de regras, não só de caráter.</li>
<li><strong>Veja quem faz cumprir o acordo:</strong> sem fiscalização, sanção ou reputação em jogo, promessas de cooperação tendem a falhar.</li>
<li><strong>Desconfie de quem vive do perde-perde:</strong> há políticos que ganham com a polarização, mesmo quando o país perde.</li>
</ol>
<p>Veja também <a href="presidencialismo-de-coalizao.html">presidencialismo de coalizão</a>, um jogo repetido de negociação, e o debate sobre <a href="debates/clima.html">clima</a>, a maior tragédia dos comuns do nosso tempo.</p>
''', fontes=[('Teoria dos jogos (Wikipédia)', W + 'Teoria_dos_jogos'), ('Dilema do prisioneiro (Wikipédia)', W + 'Dilema_do_prisioneiro'), ('Tragédia dos comuns (Wikipédia)', W + 'Trag%C3%A9dia_dos_comuns'), ('Elinor Ostrom (Wikipédia)', W + 'Elinor_Ostrom'), ('Jogo do ultimato (Wikipédia)', W + 'Jogo_do_ultimato'), ('Economia comportamental (Wikipédia)', W + 'Economia_comportamental')]),
]

META_TJ = {
 'teoria-dos-jogos': (['economia', 'mente'], ('Todos os estados de uma região dão isenção de imposto para atrair a mesma fábrica, e ela vai para onde iria de qualquer jeito. Que jogo é esse?', ['Ganha-ganha: todos atraem empresas', 'Um dilema do prisioneiro que vira perde-perde: todos perdem arrecadação', 'Soma zero: um estado ganha o que o outro perde, e o total não muda'], 1, 'Cada estado age de forma sensata, e juntos todos perdem. A saída é mudar a regra do jogo, como fez a reforma tributária ao cobrar o imposto no destino.')),
}

REFORCO_TJ = {
 'teoria-dos-jogos': dict(analogia='Num show lotado, quem fica na ponta dos pés vê melhor. Logo todos ficam na ponta dos pés, ninguém vê melhor do que antes, e todo mundo fica cansado. Cada um fez o que parecia sensato, e o resultado foi pior para todos. A saída não é pedir que cada um sofra sozinho, e sim combinar uma regra: todos com os pés no chão.', crianca='Se cada criança puxa o brinquedo para si, ele quebra e ninguém brinca. Se elas combinam a vez de cada uma, todas brincam. A teoria dos jogos estuda isso: quando brigar faz todos perderem, e como combinar regras para todos ganharem.'),
}

DID_TJ = {
 'teoria-dos-jogos': dict(obj=['Distinguir jogos de soma positiva, soma zero e soma negativa', 'Reconhecer o dilema do prisioneiro e a tragédia dos comuns em situações políticas reais', 'Explicar como repetição, reputação, regras e punição tornam a cooperação possível'], guardar=['Pessoas racionais podem chegar juntas a um resultado ruim para todas, como no dilema do prisioneiro.', 'Bens comuns podem ser cuidados por regras criadas pelas próprias comunidades, como mostrou Elinor Ostrom.', 'Pessoas cooperam mais do que a teoria fria prevê e punem a injustiça mesmo perdendo dinheiro.'], pensar='Pense num conflito político recente. Ele era mesmo de soma zero, ou os dois lados poderiam ter ganhado com um acordo?', pre=['economia-para-entender-politica', 'bem-comum']),
}

DID2_TJ = {
 'teoria-dos-jogos': dict(
  caso=('Dois países vizinhos sobem tarifas um contra o outro, cada um dizendo que protege seus empregos. Um ano depois, as exportações dos dois caíram e os preços subiram.', 'Que tipo de jogo é esse? O que poderia tirá-los dele?', 'É um dilema que virou perde-perde. A saída costuma vir de um acordo com regras e fiscalização, de negociações repetidas que constroem confiança, ou de um árbitro aceito pelos dois, como a Organização Mundial do Comércio.'),
  erro=('“Se o outro ganha, eu perco.”', 'Isso só vale em jogos de soma zero. Comércio, ciência, saúde pública e boa parte da economia são de soma positiva: os dois lados podem sair melhor. Tratar tudo como disputa leva a escolhas em que todos perdem.'),
  ferr='teste-de-troca',
  quiz=[('O que é um equilíbrio de Nash?', ['O resultado mais justo possível', 'Uma situação em que ninguém ganha mudando sozinho de estratégia, mesmo que seja ruim para todos', 'Um acordo assinado entre países'], 1, 'O dilema do prisioneiro mostra que o equilíbrio pode ser estável e ruim.'),
        ('O que Elinor Ostrom mostrou sobre bens comuns?', ['Que só a privatização funciona', 'Que comunidades podem cuidar deles com regras próprias, fiscalização mútua e punições graduais', 'Que eles sempre se esgotam'], 1, 'Foi uma terceira via entre mercado e Estado, e lhe rendeu o Nobel de 2009.')]),
}
