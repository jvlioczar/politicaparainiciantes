"""Lições avançadas: genética e política, inteligência e viés, estereótipos, relativismo, identitarismo, política da senciência, riscos-s e riscos-x, libertarismo de coração sangrante. Também a lição sobre a América do Sul e as ditaduras."""
def bl(a, c): return f'<div class="ajuda"><section class="analogia"><h3>Uma analogia</h3><p>{a}</p></section><section class="crianca"><h3>Explicando para uma criança</h3><p>{c}</p></section></div>'
MP, QC, RF = 'Mente, identidade e política', 'Quem conta', 'Riscos do futuro'
AV_NOVAS = [
dict(slug='genetica-e-politica', grupo=MP, titulo='Genética e comportamento político', resumo='Estudos com gêmeos sugerem que os genes influenciam parte das nossas inclinações políticas. Influenciar não é determinar.', corpo='''
<p class="abre">Por que irmãos criados na mesma casa podem votar de forma tão diferente? Uma linha de pesquisa chamada genopolítica sugere que parte da resposta está nos genes: eles influenciariam traços de personalidade que nos inclinam a posições mais conservadoras ou mais progressistas.</p>
''' + bl('Os genes funcionam como o terreno de uma casa: um terreno inclinado facilita certas construções, mas é o arquiteto, a família, a cidade e as escolhas que definem a casa. Ninguém nasce com um voto escrito no DNA.', 'Algumas crianças nascem mais curiosas por coisas novas, e outras gostam mais das coisas do jeito de sempre. Isso vem um pouco de como nascemos e muito do que vivemos. Quando crescem, isso pode influenciar o que pensam sobre política, mas cada um ainda pode pensar e mudar.') + '''
<h2>O que os estudos encontraram</h2>
<p>A ferramenta principal são os estudos com gêmeos. Gêmeos idênticos compartilham quase todos os genes, e os fraternos, cerca de metade. Se os idênticos são mais parecidos politicamente do que os fraternos, isso sugere uma influência genética.</p>
<ul>
<li><strong>Alford, Funk e Hibbing (2005)</strong> chamaram a atenção para o tema na ciência política americana.</li>
<li><strong>Revisões de muitos estudos</strong> estimam que cerca de 40% da variação nas atitudes políticas, em média, se associa a diferenças genéticas. O restante vem sobretudo das experiências próprias de cada pessoa, e a criação comum na família pesa menos do que se imaginava.</li>
<li><strong>Nenhum “gene da direita” ou “da esquerda”</strong> foi encontrado: grandes análises de DNA não acharam variantes isoladas com efeito relevante. Se há influência, ela vem de milhares de genes com efeitos minúsculos.</li>
<li><strong>Traços intermediários:</strong> a explicação mais aceita é que os genes influenciam a personalidade, como a abertura a experiências e a sensibilidade a ameaças, e esses traços influenciam as escolhas políticas.</li>
</ul>
<h2>Os cuidados</h2>
<table><thead><tr><th>Interpretação errada</th><th>O que os dados permitem dizer</th></tr></thead><tbody>
<tr><td>“Nasceu conservador, vai morrer conservador”</td><td>Há uma inclinação, e pessoas mudam com a vida, a informação e a convivência</td></tr>
<tr><td>“40% de cada pessoa é genético”</td><td>A estimativa vale para diferenças entre pessoas em uma população, e não para um indivíduo</td></tr>
<tr><td>“Então o outro lado é biologicamente inferior”</td><td>Não há base para isso, e esse tipo de leitura já alimentou o racismo científico</td></tr>
<tr><td>“Discutir não adianta”</td><td>Argumentos, contexto e grupos continuam importando</td></tr>
</tbody></table>
<p>Os estudos também têm limites conhecidos: os gêmeos idênticos podem ser tratados de forma mais parecida, a maioria dos dados vem de países ricos, e o que é “conservador” muda entre países e épocas. Um estudo famoso que associava reações físicas ao medo com posições conservadoras não se confirmou quando foi repetido.</p>
<div class="nota"><strong>Para que isso serve:</strong> entender que parte das diferenças políticas tem raízes profundas pode aumentar a tolerância. O outro lado não é necessariamente burro ou mau, e pode ter um temperamento diferente. Mas isso não torna todas as posições igualmente boas: elas continuam sendo avaliadas por argumentos e evidências. Veja <a href="mente-moralista.html">por que boas pessoas se dividem</a>.</div>
''', fontes=[('Genopolitics (Wikipédia)', 'https://en.wikipedia.org/wiki/Genopolitics'), ('Genetic influences on political ideologies: twin analyses of 19 measures', 'https://research.ceu.edu/en/publications/genetic-influences-on-political-ideologies-twin-analyses-of-19-me/'), ('Genetic and Environmental Influences on Sociopolitical Attitudes', 'https://bioone.org/journals/politics-and-the-life-sciences/volume-37/issue-2/pls.2018.17/Genetic-and-Environmental-Influences-on-Sociopolitical-Attitudes/10.1017/pls.2018.17.full')]),

dict(slug='inteligencia-nao-protege', grupo=MP, titulo='Inteligência a serviço da crença', resumo='Ensinar lógica e dar informação pode tornar as pessoas mais hábeis em defender o que já acreditam. Por isso, também é preciso ensinar humildade.', corpo='''
<p class="abre">Seria ótimo se mais conhecimento sempre levasse a menos erros políticos. Mas vários estudos sugerem algo incômodo: pessoas mais inteligentes e informadas também podem ser melhores em justificar o que já pensavam, encontrando falhas só nos argumentos contrários.</p>
''' + bl('Ensinar lógica é como dar uma ferramenta melhor a um advogado. Ele não fica automaticamente mais justo, e sim mais eficiente em defender o cliente. Se o cliente é a nossa própria opinião, a ferramenta pode servir para blindá-la.', 'Imagine uma criança que aprende muitas palavras difíceis e passa a usá-las para ganhar toda briga com os irmãos, mesmo quando está errada. Saber muito é ótimo, mas também é preciso querer descobrir a verdade, e não só ganhar.') + '''
<h2>O que dizem as pesquisas</h2>
<table><thead><tr><th>Estudo</th><th>O que sugeriu</th></tr></thead><tbody>
<tr><td>Taber e Lodge (2006)</td><td>Pessoas com mais conhecimento político avaliaram argumentos de forma mais enviesada, aceitando os favoráveis e atacando os contrários. É o chamado efeito da sofisticação</td></tr>
<tr><td>Kahan e colegas, “Motivated Numeracy”</td><td>Pessoas boas em matemática interpretaram melhor os dados, exceto quando o resultado contrariava sua posição política. Estudos posteriores nem sempre repetiram esse resultado</td></tr>
<tr><td>Keith Stanovich, sobre o “viés do meu lado”</td><td>A tendência a favorecer o próprio lado aparece em pessoas de todos os níveis de inteligência, e ser inteligente não protege dela</td></tr>
<tr><td>Mercier e Sperber, teoria argumentativa</td><td>A razão teria evoluído sobretudo para convencer e se justificar, e funciona melhor quando discutimos com quem discorda</td></tr>
</tbody></table>
<p>Os resultados são debatidos, e nem todos se replicaram. Mas o quadro geral é consistente: inteligência e informação não são vacinas contra o viés. Veja também <a href="vieses-cognitivos.html">como os vieses afetam seu julgamento</a>.</p>
<h2>Por que isso acontece</h2>
<ul><li><strong>Raciocínio motivado:</strong> o cérebro trabalha como advogado da identidade, e não como juiz.</li><li><strong>Mais munição:</strong> quem sabe mais tem mais argumentos e mais facilidade para desconfiar de dados incômodos.</li><li><strong>Identidade:</strong> mudar de posição pode custar amigos e reputação. Veja o <a href="perigo-do-tribalismo.html">tribalismo</a>.</li><li><strong>Confiança:</strong> quem é bom em argumentar tende a confiar mais nas próprias conclusões.</li></ul>
<h2>Então, o que ensinar?</h2>
<p>Lógica e informação continuam essenciais. O ponto é que não bastam. Pesquisas sobre pensamento ativo e aberto e sobre humildade intelectual apontam para outros hábitos:</p>
<ol class="roteiro"><li><strong>Curiosidade sobre o outro lado,</strong> que alguns estudos associam a menos polarização.</li><li><strong>Buscar a falha no próprio argumento,</strong> e não só no alheio.</li><li><strong>Fazer previsões verificáveis,</strong> que mostram quando erramos.</li><li><strong>Discutir em grupos diversos,</strong> onde a razão funciona melhor.</li><li><strong>Separar identidade de opinião:</strong> mudar de ideia não é trair quem você é. Veja <a href="mudar-de-ideia.html">mudar de ideia</a>.</li></ol>
<div class="nota alerta"><strong>Vale para quem lê esta página:</strong> é fácil usar este conhecimento para explicar por que os outros estão errados. Use-o primeiro em você.</div>
''', fontes=[('Motivated Numeracy', 'https://doi.org/10.1017/bpp.2016.2'), ('Overcoming ideology-consistent biases', 'https://core-cms.cambridgecore.org/core/services/aop-cambridge-core/content/view/B3D6045989A0C65419E8EC8F66BB50F8/S1930297524000445a.pdf/overcoming-ideology-consistent-biases-does-it-help-to-make-things-easier.pdf'), ('Myside bias (Wikipédia)', 'https://en.wikipedia.org/wiki/Myside_bias'), ('The Enigma of Reason', 'https://www.google.com/search?tbm=bks&q=Mercier+Sperber+The+Enigma+of+Reason')]),

dict(slug='estereotipo-preconceito-discriminacao', grupo=MP, titulo='Estereótipo, preconceito e discriminação na política', resumo='Pensar, sentir e agir: três coisas diferentes, que se alimentam e que a política pode reforçar ou combater.', corpo='''
<p class="abre">As três palavras costumam ser usadas como sinônimos, mas descrevem coisas diferentes. Separá-las ajuda a entender como a política pode piorar ou melhorar a vida de grupos inteiros.</p>
''' + bl('Pense em uma fila de emprego. O estereótipo é a ideia que o selecionador tem na cabeça, o preconceito é o incômodo que ele sente, e a discriminação é a vaga negada. Só a última aparece na estatística, mas as três trabalham juntas.', 'Achar que “toda menina gosta de rosa” é um estereótipo. Não gostar de alguém só porque é diferente é preconceito. Não deixar essa pessoa brincar é discriminação. Cada pessoa é única, e todo mundo merece a chance de brincar.') + '''
<h2>As três diferenças</h2>
<table><thead><tr><th></th><th>O que é</th><th>Exemplo</th></tr></thead><tbody>
<tr><td><strong>Estereótipo</strong></td><td>Uma <strong>crença</strong>: atribuir os mesmos traços a todos de um grupo</td><td>“Político é tudo ladrão”, “nordestino é preguiçoso”</td></tr>
<tr><td><strong>Preconceito</strong></td><td>Uma <strong>atitude</strong>, sobretudo emocional, em relação ao grupo</td><td>Desconfiança ou desprezo antes de conhecer a pessoa</td></tr>
<tr><td><strong>Discriminação</strong></td><td>Uma <strong>ação</strong> que prejudica alguém por pertencer ao grupo</td><td>Negar emprego, aluguel ou atendimento</td></tr>
</tbody></table>
<h2>De onde vêm</h2>
<ul>
<li><strong>Atalhos mentais:</strong> Gordon Allport descreveu os estereótipos como uma “lei do menor esforço”. Simplificam o mundo, e resistem a mudar.</li>
<li><strong>Grupos mínimos:</strong> nos experimentos de Henri Tajfel, pessoas divididas por sorteio já favoreciam o próprio grupo. Pertencer a um grupo eleva a autoestima, e o “nós” facilmente vira “contra eles”. Veja o <a href="vieses/in-group-bias.html">favoritismo de grupo</a>.</li>
<li><strong>Conformidade e cultura:</strong> aprendemos preconceitos com a família, a mídia e o grupo, e por isso também podemos desaprendê-los.</li>
</ul>
<h2>Onde entra a política</h2>
<table><thead><tr><th>Como a política piora</th><th>Como a política ajuda</th></tr></thead><tbody>
<tr><td>Discursos que generalizam e culpam grupos. Veja <a href="perigo-de-culpar-o-estrangeiro.html">o perigo de culpar o estrangeiro</a></td><td>Leis contra discriminação e meios de denunciar</td></tr>
<tr><td>Leis que já discriminaram, como a escravidão, as leis de segregação ou a proibição do voto feminino</td><td>Igualdade de direitos e de acesso</td></tr>
<tr><td>Abordagens policiais seletivas</td><td>Dados, controle e protocolos claros</td></tr>
<tr><td>Uso eleitoral do medo</td><td>Escolas, cidades e espaços que promovem convivência</td></tr>
</tbody></table>
<p>O contato entre grupos costuma reduzir o preconceito: uma grande revisão de 515 estudos encontrou essa associação. Estudos mais rigorosos e recentes mostram efeitos menores, sobretudo para preconceito racial, e por isso o contato ajuda, mas não basta sozinho.</p>
<div class="nota alerta"><strong>Estereótipos políticos também existem:</strong> “todo eleitor do outro lado é burro, fascista ou comunista” é um estereótipo como qualquer outro. E a maioria das pessoas exagera o quanto o outro lado é radical. Veja <a href="sem-binarismo.html">sair do nós contra eles</a>.</div>
<h2>Como reconhecer em si mesmo</h2>
<ol class="roteiro"><li>Estou julgando a pessoa, ou o grupo dela?</li><li>Eu diria o mesmo de alguém do meu grupo que fizesse isso?</li><li>Conheço pessoas desse grupo de verdade, ou só pela tela?</li><li>Essa regra trataria alguém pior pelo que ele é, e não pelo que fez?</li></ol>
''', fontes=[('Preconceito, estereótipo e discriminação: diferenças e semelhanças', 'https://socientifica.com.br/preconceito-estereotipo-e-discriminacao-diferencas-e-semelhancas'), ('What we have learned since Pettigrew and Tropp', 'https://doi.org/10.1017/BPP.2018.25'), ('Contact hypothesis (Wikipédia)', 'https://en.wikipedia.org/wiki/Contact_hypothesis')]),

dict(slug='relativismo-e-circulo-moral', grupo=QC, titulo='Por que é difícil ser relativista diante da inclusão', resumo='Se toda moral fosse relativa, a abolição não teria sido um avanço. A expansão do círculo moral segue um princípio: a imparcialidade.', corpo='''
<p class="abre">“Cada cultura tem sua moral, e ninguém pode julgar.” A frase soa tolerante. Mas, levada a sério, ela impede dizer que a escravidão era errada, que proibir mulheres de votar era injusto ou que perseguir minorias é mal. Por isso, quase ninguém consegue ser relativista até o fim.</p>
''' + bl('Imagine um termômetro em que cada pessoa decide o número. Ninguém poderia dizer que está mais quente hoje do que ontem. O relativismo moral faz algo parecido com o certo e o errado: se tudo depende de quem olha, não existe melhorar nem piorar.', 'Se cada criança pudesse inventar a regra que quisesse, e ninguém pudesse dizer que bater no colega é errado, a escola viraria uma bagunça injusta. Algumas regras valem para todos, como não machucar os outros.') + '''
<h2>O que é relativismo moral</h2>
<p>É a ideia de que o certo e o errado dependem da cultura ou da pessoa, sem um critério que valha para todos. Há uma verdade nele: culturas diferem, e devemos ter humildade antes de julgar. Mas há dois problemas sérios:</p>
<ul>
<li><strong>Não permite progresso:</strong> se a moral de cada época fosse correta por definição, a abolição e o voto feminino não seriam avanços, apenas mudanças. Veja <a href="progresso-moral-e-politico.html">progresso moral</a>.</li>
<li><strong>Silencia as vítimas:</strong> quem sofre dentro de uma cultura também faz parte dela. Dizer “é a cultura deles” costuma dar razão a quem tem mais poder.</li>
</ul>
<h2>Tolerância não é relativismo</h2>
<table><thead><tr><th>Tolerância</th><th>Relativismo</th></tr></thead><tbody>
<tr><td>Respeita pessoas e convive com diferenças</td><td>Nega que se possa julgar qualquer prática</td></tr>
<tr><td>Admite que podemos estar errados</td><td>Diz que ninguém está errado</td></tr>
<tr><td>Tem limites, como o dano a outros</td><td>Não tem critério para limites</td></tr>
</tbody></table>
<p>Na prática, quem defende o relativismo costuma defendê-lo como algo bom, o que já é um juízo moral que pretende valer para todos.</p>
<h2>A imparcialidade e o círculo que se expande</h2>
<p>Se não é tudo relativo, qual é o critério? Um dos mais fortes é a <a href="testar-visao-moral.html">imparcialidade</a>: casos iguais devem ser tratados de forma igual, a menos que haja uma diferença relevante. É ela que explica a expansão do círculo moral:</p>
<table><thead><tr><th>Já ficou de fora</th><th>Por quê</th><th>A diferença era relevante?</th></tr></thead><tbody>
<tr><td>Escravizados</td><td>Cor e origem</td><td>Não muda a capacidade de sofrer, pensar e querer</td></tr>
<tr><td>Mulheres</td><td>Sexo</td><td>Não muda a capacidade de decidir e participar</td></tr>
<tr><td>Pessoas LGBT</td><td>Orientação e identidade</td><td>Não prejudica ninguém</td></tr>
<tr><td>Estrangeiros</td><td>Local de nascimento</td><td>É <a href="perigo-de-culpar-o-estrangeiro.html">loteria da vida</a></td></tr>
<tr><td>Animais</td><td>Espécie</td><td>A dor continua sendo dor. Veja o <a href="sencientismo.html">sencientismo</a></td></tr>
</tbody></table>
<p>Incluir minorias, então, não é um favor nem um capricho de um lado político. É a aplicação coerente de um princípio que quase todos já aceitam: não tratar alguém pior por uma característica que não tem relação com o que está em jogo.</p>
<h2>As objeções sérias</h2>
<ul><li><strong>Quem decide o que é relevante?</strong> É uma pergunta difícil, e por isso pede argumentos públicos, e não só a vontade de quem manda.</li><li><strong>Universalismo já serviu ao colonialismo:</strong> é verdade. Mas a resposta a uma imposição injusta é uma imparcialidade mais coerente, e não o relativismo.</li><li><strong>Deveres especiais:</strong> temos laços com família e comunidade. Isso permite cuidar mais dos próximos, mas não tratar os outros como se não contassem.</li></ul>
''', fontes=[('Moral relativism (Wikipédia)', 'https://en.wikipedia.org/wiki/Moral_relativism'), ('The Expanding Circle', 'https://www.google.com/search?tbm=bks&q=Peter+Singer+The+Expanding+Circle'), ('Imparcialidade (Wikipédia)', 'https://en.wikipedia.org/wiki/Impartiality')]),

dict(slug='critica-ao-identitarismo', grupo=MP, titulo='A crítica ao identitarismo e ao pós-modernismo', resumo='A luta por reconhecimento trouxe direitos. Mas, quando a identidade vira o único critério, surgem riscos. E o identitarismo existe à esquerda e à direita.', corpo='''
<p class="abre">Movimentos por direitos de mulheres, negros, indígenas e pessoas LGBT conquistaram avanços enormes. Ao mesmo tempo, cresceu uma crítica ao chamado identitarismo: quando a identidade do grupo se torna o critério principal de tudo, inclusive do que é verdade e de quem pode falar. Essa crítica vem da direita, e também de dentro da própria esquerda.</p>
''' + bl('Uma lanterna ajuda a ver o que estava no escuro: injustiças que muitos não enxergavam. Mas se você só olha pela lanterna, deixa de ver o resto da sala. A identidade é uma lanterna útil, e um péssimo substituto para a luz toda.', 'Imagine uma turma em que, em vez de ouvir a ideia de cada criança, todo mundo decide só olhando de que grupo ela é. Algumas crianças nunca seriam ouvidas, e outras ganhariam sempre. Ouvir quem sofre é importante, e ouvir a ideia de todos também.') + '''
<h2>De onde vem: o pós-modernismo</h2>
<p>Pensadores como Jean-François Lyotard, Jacques Derrida e Michel Foucault questionaram as “grandes narrativas”, a neutralidade da ciência e a relação entre conhecimento e poder. Isso ajudou a revelar preconceitos escondidos em discursos que se diziam neutros. Críticos dizem que, levado ao extremo, esse ceticismo vira relativismo, em que tudo é discurso e poder, e nada é simplesmente verdadeiro.</p>
<h2>O que a política de identidade acertou</h2>
<ul><li>Mostrou que regras aparentemente neutras podem prejudicar grupos.</li><li>Deu voz a quem era ignorado, inclusive pela esquerda tradicional.</li><li>Ajudou a conquistar direitos, como no casamento igualitário e no combate ao racismo.</li><li>A ideia de interseccionalidade mostrou que uma mulher negra pode sofrer discriminações que nem o feminismo nem o movimento negro viam sozinhos.</li></ul>
<h2>As principais críticas</h2>
<table><thead><tr><th>Crítica</th><th>Em resumo</th></tr></thead><tbody>
<tr><td>Fragmentação</td><td>Divide a sociedade em grupos rivais, e torna mais difícil construir maiorias por causas comuns</td></tr>
<tr><td>Esquece a classe</td><td>Críticos de esquerda dizem que a desigualdade econômica perdeu espaço para disputas simbólicas</td></tr>
<tr><td>Lugar de fala absoluto</td><td>Quando só quem pertence ao grupo pode falar, o argumento perde para a identidade de quem fala</td></tr>
<tr><td>Hierarquia de vítimas</td><td>Uma disputa sobre quem sofre mais pode substituir a busca por soluções</td></tr>
<tr><td>Cancelamento e punição</td><td>Exposição pública e linchamento virtual no lugar do debate</td></tr>
<tr><td>Relativismo sobre fatos</td><td>Se toda verdade é “de um grupo”, fica difícil contestar mentiras</td></tr>
<tr><td>Reação contrária</td><td>Pode alimentar o ressentimento que a extrema-direita explora</td></tr>
</tbody></table>
<p>No Brasil, essas críticas aparecem em autores e comentaristas de vários campos, como Francisco Bosco e Vladimir Safatle, ambos ligados à esquerda. Nos EUA, o caso Sokal, em 1996, quando um físico publicou um artigo de propósito sem sentido em uma revista pós-moderna, virou símbolo do debate.</p>
<div class="nota"><strong>Cuidado com os dois exageros:</strong> “identitarismo” virou xingamento usado para desqualificar qualquer luta por direitos. E também há quem trate toda crítica como preconceito. A pergunta útil é concreta: essa medida reduz uma injustiça real, e trata cada pessoa pelos seus atos e argumentos?</div>
<h2>O identitarismo também é de direita</h2>
<p>A palavra costuma ser usada só contra a esquerda, mas a lógica de organizar a política em torno de quem a pessoa é, e não do que ela propõe, existe dos dois lados. O próprio termo nasceu à direita: o Movimento Identitário, surgido na França nos anos 2000, é de extrema-direita e defende a identidade étnica e cultural “europeia” contra imigrantes. No Brasil, a direita construiu identidades de grupo tão fortes quanto as da esquerda: o “cidadão de bem”, a “família tradicional”, o patriota, o evangélico, o armamentista, o “agro”. Quem está fora delas vira “eles”.</p>
<table><thead><tr><th>Mecanismo</th><th>Na esquerda</th><th>Na direita</th></tr></thead><tbody>
<tr><td>Quem pode falar</td><td>“Só quem pertence ao grupo tem lugar de fala”</td><td>“Só o cidadão de bem opina; artista e professor não”</td></tr>
<tr><td>Hierarquia de vítimas</td><td>Disputa sobre qual minoria sofre mais</td><td>“O cristão é o perseguido de hoje”, “o homem branco é o novo alvo”</td></tr>
<tr><td>Cancelamento</td><td>Linchamento virtual de quem erra uma palavra</td><td>Boicote a marcas, artistas e empresas por propaganda ou opinião</td></tr>
<tr><td>Verdade do grupo</td><td>Relativismo: cada identidade tem a sua verdade</td><td>Negar fatos que incomodam o grupo, da vacina à urna</td></tr>
<tr><td>Símbolos</td><td>Pronomes, nomes e bandeiras como teste de lealdade</td><td>Camisa da seleção, bandeira e arma como teste de lealdade</td></tr>
</tbody></table>
<p>A diferença, para muitos analistas, não está no mecanismo, e sim no ponto de partida: a política de identidade das minorias nasceu de exclusões reais e documentadas; a identidade de direita costuma ser a reação de uma maioria que se sente ameaçada pela perda de um lugar que tinha. Os dois podem virar tribalismo, e os dois alimentam um ao outro. Veja o <a href="vertentes/nacionalismo.html">nacionalismo</a>, o <a href="vertentes/bolsonarismo.html">bolsonarismo</a> e a lição sobre <a href="perigo-do-tribalismo.html">o perigo do tribalismo</a>.</p>
<h2>Uma saída: a universalidade</h2>
<p>Muitos críticos propõem defender direitos de minorias pela mesma régua que vale para todos: igualdade, dignidade e imparcialidade. Assim, a luta contra o racismo ou a homofobia não depende de quem você é, e sim de princípios que qualquer pessoa pode aceitar. Veja <a href="relativismo-e-circulo-moral.html">o relativismo e o círculo moral</a> e <a href="debates/identidade-lgbt.html">o debate sobre identidade e direitos LGBTQIA+</a>.</p>
<div class="cta"><a class="btn alt" href="https://www.youtube.com/watch?v=aOEFh_SpB18" target="_blank" rel="noopener">Vídeo: Safatle e a esquerda identitária</a><a class="btn alt" href="https://www.youtube.com/watch?v=Z0Sr2Qz17Vs" target="_blank" rel="noopener">Vídeo: entrevista com Francisco Bosco</a><a class="btn alt" href="https://www.youtube.com/watch?v=8jE_fTY21e8" target="_blank" rel="noopener">Vídeo: Pós-modernidade, Lyotard e Derrida</a></div>
''', fontes=[('A desconstrução do pós-modernismo', 'https://juliocesar.medium.com/a-desconstru%C3%A7%C3%A3o-do-p%C3%B3s-modernismo-fc787151fa8'), ('Vídeo: Vladimir Safatle fala sobre a esquerda identitária', 'https://www.youtube.com/watch?v=aOEFh_SpB18'), ('Vídeo: O ativismo identitário e o debate público', 'https://www.youtube.com/watch?v=Z0Sr2Qz17Vs'), ('Vídeo: Pós-modernidade, Lyotard e Derrida', 'https://www.youtube.com/watch?v=8jE_fTY21e8'), ('Identity politics (Wikipédia)', 'https://en.wikipedia.org/wiki/Identity_politics'), ('Caso Sokal (Wikipédia)', 'https://pt.wikipedia.org/wiki/Caso_Sokal')]),

dict(slug='politica-baseada-na-senciencia', grupo=QC, titulo='Política baseada na senciência', resumo='Se o que importa é poder sentir, como seriam leis, orçamentos e instituições que levassem isso a sério?', corpo='''
<p class="abre">A <a href="sencientismo.html">lição sobre sencientismo</a> discute quem deve contar. Esta lição dá o passo seguinte: como seria uma política que levasse a senciência a sério, nas leis, nos orçamentos e nas instituições? A ideia rompe com o antropocentrismo, a visão de que só os humanos importam.</p>
''' + bl('Durante séculos, as cidades foram planejadas como se só existissem carros, e os pedestres que se virassem. Quando passamos a pensar nos pedestres, surgiram calçadas e faixas. Uma política da senciência faz o mesmo: lembra que existem outros seres sentindo os efeitos de cada decisão.', 'Quando a cidade decide algo, como derrubar uma árvore ou construir uma estrada, quem mora ali sente: pessoas, e também passarinhos, cachorros e outros bichos. Uma boa regra pensa em todo mundo que pode sentir dor ou medo.') + '''
<h2>De onde vem a ideia</h2>
<ul><li><strong>Antiguidade:</strong> pensadores como Pitágoras, Plutarco e Porfírio já ligavam a capacidade de sentir à consideração moral.</li><li><strong>Jeremy Bentham (1789):</strong> a pergunta não é se podem raciocinar ou falar, mas se podem sofrer.</li><li><strong>Século XX:</strong> autores como J. Howard Moore, Peter Singer e outros desenvolveram a crítica ao especismo.</li><li><strong>Hoje:</strong> teorias políticas como as de Cochrane, Donaldson e Kymlicka, Vinding e Adenitire e Fasel propõem instituições concretas. Uma proposta teórica, a senciocracia, imagina um governo que represente todos os seres sencientes.</li></ul>
<h2>Como apareceria na prática</h2>
<table><thead><tr><th>Área</th><th>Exemplos de políticas</th></tr></thead><tbody>
<tr><td>Constituição e leis</td><td>Reconhecer a senciência, proibir crueldade evitável e dar peso aos interesses dos animais nas leis</td></tr>
<tr><td>Representação</td><td>Defensorias, conselhos ou parlamentares com mandato para representar quem não vota</td></tr>
<tr><td>Orçamento</td><td>Medir o impacto de subsídios e obras sobre animais, e financiar alternativas</td></tr>
<tr><td>Alimentação</td><td>Transição para sistemas com menos sofrimento, com apoio aos trabalhadores e produtores</td></tr>
<tr><td>Ambiente e saúde</td><td>Incluir os animais afetados em enchentes, queimadas e epidemias</td></tr>
<tr><td>Ciência</td><td>Pesquisar quem é senciente e métodos sem testes dolorosos</td></tr>
<tr><td>Cidades</td><td>Castração, adoção e proteção de animais de rua. Veja o <a href="debates/animais-de-rua.html">debate</a></td></tr>
</tbody></table>
<h2>Os desafios</h2>
<ul><li><strong>Como medir?</strong> Há incerteza sobre o grau de sofrimento de cada espécie. A resposta comum é agir com cautela, e não ignorar.</li><li><strong>Até onde?</strong> Insetos, peixes, animais selvagens e futuras mentes digitais desafiam os limites do círculo.</li><li><strong>Resistência cultural e econômica:</strong> exige transição justa, sem abandonar quem depende dessas atividades.</li><li><strong>Diferença do ambientalismo:</strong> o ambientalismo pensa em espécies e ecossistemas, e o sencientismo, em cada indivíduo que sente. Às vezes, os dois concordam, e às vezes, não.</li></ul>
<div class="nota">Uma política da senciência não exige que todos virem vegetarianos amanhã. Exige que o sofrimento de quem não pode votar entre na conta, com o peso que merece. Veja os <a href="debates/direitos-animais.html">direitos dos animais</a>.</div>
''', fontes=[('O estabelecimento e a possível queda do antropocentrismo', 'https://medium.com/novo-iluminismo/o-estabelecimento-e-a-poss%C3%ADvel-queda-do-antropocentrismo-c9ab3ba1b9d7'), ('Vegpedia: Sencientismo', 'https://vegpedia.com/sencientismo'), ('Vegpedia: Senciocracia', 'https://vegpedia.com/senciocracia'), ('Sentientist Politics: A Theory of Global Inter-Species Justice', 'https://global.oup.com/academic/product/sentientist-politics-9780198789802')]),

dict(slug='riscos-s-e-x', grupo=RF, titulo='Políticas para prevenir riscos-s e riscos-x', resumo='Alguns riscos poderiam acabar com a humanidade, e outros, criar sofrimento em escala gigantesca. A política pode ajudar a evitá-los.', corpo='''
<p class="abre">A maioria das decisões políticas olha para os próximos quatro anos. Mas algumas ameaças poderiam afetar todo o futuro: uma pandemia projetada, uma guerra nuclear, uma inteligência artificial fora de controle. Pesquisadores chamam de <strong>riscos-x</strong> os riscos existenciais, que podem acabar com a humanidade ou destruir seu potencial, e de <strong>riscos-s</strong> os riscos de sofrimento em escala astronômica, muito maior do que todo o sofrimento que já existiu.</p>
''' + bl('Um prédio pode passar décadas sem pegar fogo, e ainda assim instalamos extintores e saídas de emergência. Não porque o incêndio é provável amanhã, mas porque, se acontecer, o dano é enorme e irreversível. Riscos-x e riscos-s são incêndios em escala de civilização.', 'Os adultos colocam grade na janela e guardam remédios no alto, mesmo achando que nada vai acontecer, porque um acidente poderia ser muito grave. Alguns cientistas estudam perigos muito grandes para o mundo todo, para que nunca aconteçam.') + '''
<h2>As duas categorias</h2>
<table><thead><tr><th></th><th>Riscos-x (existenciais)</th><th>Riscos-s (de sofrimento)</th></tr></thead><tbody>
<tr><td>O que é</td><td>Extinção humana ou perda permanente do futuro</td><td>Sofrimento em escala muito maior do que o atual, por muito tempo</td></tr>
<tr><td>Exemplos discutidos</td><td>Guerra nuclear, pandemia projetada, IA desalinhada, colapso climático extremo</td><td>Regimes totalitários permanentes com tecnologia avançada, IA que cause sofrimento, exploração de seres sencientes em escala imensa, inclusive mentes digitais</td></tr>
<tr><td>Quem estuda</td><td>Pesquisadores de risco existencial, como Toby Ord, em <em>The Precipice</em></td><td>Grupos como o Center for Reducing Suffering e o Center on Long-Term Risk</td></tr>
</tbody></table>
<p>O Center for Reducing Suffering distingue riscos-s acidentais, causados por agentes que querem fazer mal e naturais. O foco no sofrimento extremo se liga às ideias de <a href="politica-baseada-na-senciencia.html">política baseada na senciência</a> e de Magnus Vinding.</p>
<h2>Políticas que ajudam</h2>
<table><thead><tr><th>Área</th><th>Exemplos</th></tr></thead><tbody>
<tr><td>Inteligência artificial</td><td>Testes de segurança, transparência, limites ao uso militar e cooperação internacional. Veja o <a href="debates/inteligencia-artificial.html">debate sobre IA</a></td></tr>
<tr><td>Biossegurança</td><td>Vigilância de pandemias, controle de pesquisas perigosas e de síntese de DNA</td></tr>
<tr><td>Armas nucleares</td><td>Redução de arsenais, canais de comunicação e tratados</td></tr>
<tr><td>Instituições</td><td>Evitar a concentração permanente de poder e manter freios e contrapesos. Veja o <a href="fanatismo-ideologico.html">fanatismo ideológico</a> e os <a href="atores-malevolentes.html">atores malevolentes</a></td></tr>
<tr><td>Círculo moral</td><td>Garantir que seres sencientes, inclusive animais e futuras mentes digitais, sejam considerados antes que tecnologias poderosas se consolidem</td></tr>
<tr><td>Representação do futuro</td><td>Comissões e metas de longo prazo, como as que alguns países criaram para as próximas gerações</td></tr>
</tbody></table>
<h2>As críticas</h2>
<ul><li><strong>Especulação:</strong> as probabilidades são muito incertas, e às vezes apenas palpites.</li><li><strong>Problemas de hoje:</strong> focar no futuro distante pode desviar recursos de quem sofre agora.</li><li><strong>Uso do medo:</strong> riscos enormes podem justificar vigilância e concentração de poder, que também são perigosos. Veja a <a href="politica-do-medo.html">política do medo</a>.</li><li><strong>Quem decide:</strong> o debate é concentrado em poucos países e instituições.</li></ul>
<div class="nota">Muitas medidas fazem sentido mesmo para quem não aceita as projeções mais dramáticas: prevenir pandemias, conter armas e regular tecnologias perigosas também protege as pessoas de hoje.</div>
''', fontes=[('S-risks: Why they are the worst existential risks, and how to prevent them', 'https://longtermrisk.org/s-risks-talk-eag-boston-2017/'), ('80,000 Hours: s-risks', 'https://80000hours.org/problem-profiles/s-risks/'), ('Center for Reducing Suffering', 'https://centerforreducingsuffering.org/'), ('Global catastrophic risk (Wikipédia)', 'https://en.wikipedia.org/wiki/Global_catastrophic_risk'), ('The Precipice', 'https://en.wikipedia.org/wiki/The_Precipice:_Existential_Risk_and_the_Future_of_Humanity')]),

dict(slug='libertarismo-de-coracao-sangrante', grupo=QC, titulo='O libertarismo de coração sangrante', resumo='Uma corrente liberal defende mercados livres justamente por, e para, os mais pobres. E aceita que a justiça social importa.', corpo='''
<p class="abre">Costuma-se imaginar que quem defende mercado livre não se importa com os pobres, e que quem se importa com os pobres desconfia do mercado. O chamado <em>bleeding heart libertarianism</em>, ou libertarismo de coração sangrante, recusa essa divisão: defende a liberdade econômica e a propriedade, e também afirma que uma sociedade justa deve ser avaliada pelo que faz pelos que estão pior.</p>
''' + bl('Pense em uma ponte. Uns querem que o governo construa e cobre pedágio, e outros, que empresas compitam para construir. Os liberais de coração sangrante dizem: o que importa é quem consegue atravessar, sobretudo os mais pobres. Se a competição levar mais gente para o outro lado, ótimo, e se não levar, é preciso repensar.', 'Imagine uma feira em que todo mundo pode vender e comprar. Algumas pessoas acham que isso é bom porque cada um é livre. Outras perguntam se as crianças mais pobres também conseguem comprar comida. Essa ideia tenta juntar as duas coisas: liberdade e cuidado com quem tem menos.') + '''
<h2>De onde vem</h2>
<p>O nome ganhou força a partir de 2011, com um blog de filósofos acadêmicos, como Matt Zwolinski e Jason Brennan. John Tomasi, em <em>Free Market Fairness</em>, tentou unir Rawls e Hayek: a liberdade econômica seria um direito básico, e a justiça social, um critério para avaliar instituições. A ideia tem raízes antigas: Adam Smith escreveu sobre a dignidade dos trabalhadores, e Hayek aceitou uma renda mínima garantida.</p>
<h2>O que defendem</h2>
<table><thead><tr><th>Ideia</th><th>Na prática</th></tr></thead><tbody>
<tr><td>Mercados livres ajudam os pobres</td><td>Abrir comércio, facilitar abrir negócios e reduzir barreiras para quem quer trabalhar</td></tr>
<tr><td>Privilégios prejudicam os pobres</td><td>Atacar subsídios a grandes empresas, cartórios, licenças e monopólios. Veja o <a href="debates/subsidios.html">debate sobre subsídios</a></td></tr>
<tr><td>Renda básica em vez de burocracia</td><td>Alguns defendem transferir dinheiro direto, em vez de programas complexos. Veja os <a href="debates/programas-sociais.html">programas sociais</a></td></tr>
<tr><td>Liberdade de imigrar</td><td>Abrir fronteiras seria uma das formas mais fortes de reduzir a pobreza mundial</td></tr>
<tr><td>Contra a guerra às drogas</td><td>A proibição pune sobretudo pobres e minorias</td></tr>
<tr><td>Moradia acessível</td><td>Reduzir regras que impedem construir e encarecem o aluguel</td></tr>
</tbody></table>
<h2>As críticas</h2>
<ul><li><strong>De outros libertários:</strong> justiça social seria um conceito vago, que abriria espaço para mais Estado. Nozick lembrava que importa como a riqueza foi obtida, e não só o resultado.</li><li><strong>Da esquerda:</strong> mercados não bastam para corrigir desigualdades de origem, como a da <a href="perigo-de-culpar-o-estrangeiro.html">loteria da vida</a>, e o poder econômico também ameaça a liberdade.</li><li><strong>Empírica:</strong> muito depende de dados sobre o que de fato ajuda os pobres, e eles variam por país e política. Veja <a href="politicas-baseadas-em-evidencias.html">políticas baseadas em evidências</a>.</li></ul>
<div class="nota">O valor da proposta está no critério que ela aceita: julgar instituições pelo efeito sobre quem está pior. Esse critério une liberais, social-democratas e outros, e permite discutir os meios com dados. Veja as <a href="teorias-da-justica.html">teorias da justiça</a> e a vertente do <a href="vertentes/social-liberalismo.html">social-liberalismo</a>.</div>
''', fontes=[('Bleeding-heart libertarianism (Wikipédia)', 'https://en.wikipedia.org/wiki/Bleeding-heart_libertarianism'), ('Free Market Fairness', 'https://www.google.com/search?tbm=bks&q=Tomasi+Free+Market+Fairness'), ('Arguing About Political Philosophy', 'https://www.google.com/search?tbm=bks&q=Arguing+About+Political+Philosophy+Zwolinski')]),
]
META_AV = {
 'genetica-e-politica': (['mente', 'ideologia'], ('O que os estudos com gêmeos sugerem?', ['Que existe um gene da direita', 'Que os genes influenciam parte das inclinações, sem determinar o voto', 'Que a criação não importa nada'], 1, 'A estimativa média é de cerca de 40% da variação, sem um gene único, e com muita influência das experiências.')),
 'inteligencia-nao-protege': (['mente', 'desinformacao'], ('Ser mais inteligente protege contra o viés político?', ['Sim, sempre', 'Não necessariamente: pode até ajudar a justificar o que já se pensa', 'Só quem é pouco inteligente tem viés'], 1, 'Estudos sugerem que o viés do próprio lado aparece em todos os níveis de inteligência.')),
 'estereotipo-preconceito-discriminacao': (['mente', 'etica'], ('Qual é a diferença entre preconceito e discriminação?', ['Nenhuma', 'Preconceito é uma atitude, e discriminação, uma ação', 'Discriminação é só pensar mal de alguém'], 1, 'O estereótipo é uma crença, o preconceito, uma atitude, e a discriminação, uma ação.')),
 'relativismo-e-circulo-moral': (['etica'], ('Por que o relativismo moral tem dificuldade com a abolição?', ['Porque não permite dizer que foi um avanço', 'Porque a escravidão era boa', 'Porque todos concordavam'], 0, 'Se toda moral de época fosse correta, abolir a escravidão seria só uma mudança, e não um progresso.')),
 'critica-ao-identitarismo': (['ideologia', 'democracia'], ('Qual é a alternativa proposta por muitos críticos do identitarismo?', ['Ignorar as minorias', 'Defender direitos com princípios universais de igualdade e imparcialidade', 'Proibir movimentos sociais'], 1, 'A ideia é defender direitos de todos com a mesma régua.')),
 'politica-baseada-na-senciencia': (['etica', 'democracia'], ('O que diferencia o sencientismo do ambientalismo?', ['Nada', 'O foco em cada indivíduo que pode sentir, e não só em espécies e ecossistemas', 'O sencientismo ignora animais'], 1, 'Às vezes os dois concordam, e às vezes, não.')),
 'riscos-s-e-x': (['democracia', 'perigos'], ('O que é um risco-s?', ['Um risco de sofrimento em escala muito maior do que o atual', 'Um risco econômico pequeno', 'Uma sigla de partido'], 0, 'Os riscos-x ameaçam o futuro da humanidade, e os riscos-s, criar sofrimento em escala astronômica.')),
 'libertarismo-de-coracao-sangrante': (['ideologia', 'economia'], ('Qual é o critério central dessa corrente?', ['Mercados livres, sem se importar com os pobres', 'Avaliar instituições pelo efeito sobre quem está pior', 'Estatizar a economia'], 1, 'Ela defende mercados livres justamente pelos mais pobres.')),
}
SUL = dict(slug='america-do-sul-e-ditaduras', grupo='Quem fez história', titulo='A América do Sul e as ditaduras', resumo='Golpes, Operação Condor e transições: por que o continente viveu tantas ditaduras, e o que ficou disso.', corpo='''
<p class="abre">Entre as décadas de 1960 e 1980, quase toda a América do Sul viveu sob ditaduras, a maioria militar e de direita. Antes e depois, houve também caudilhos e regimes autoritários de vários tipos, inclusive de esquerda. Entender esse passado ajuda a reconhecer os sinais de alerta no presente.</p>
''' + bl('É como uma vizinhança em que, em poucos anos, quase todas as casas trocaram a fechadura por cadeados controlados por guardas armados. Os guardas ainda conversavam entre si e trocavam informações sobre os moradores que reclamavam. Foi o que aconteceu com a Operação Condor.', 'Há muito tempo, em vários países perto do Brasil, grupos de militares tomaram o poder e não deixavam as pessoas votar nem falar o que pensavam. Muita gente foi presa e machucada. Hoje, lembramos disso para que nunca mais aconteça.') + '''
<h2>Uma onda de golpes</h2>
<table><thead><tr><th>País</th><th>Período</th><th>Marca</th></tr></thead><tbody>
<tr><td>Paraguai</td><td>1954-1989</td><td>Ditadura de <a href="mundo/alfredo-stroessner.html">Stroessner</a>, a mais longa</td></tr>
<tr><td>Brasil</td><td>1964-1985</td><td>Golpe contra João Goulart, AI-5 e tortura. Veja a <a href="historia.html">história</a></td></tr>
<tr><td>Bolívia</td><td>Vários governos militares, entre 1964 e 1982</td><td>Golpes sucessivos</td></tr>
<tr><td>Uruguai</td><td>1973-1985</td><td>Um dos maiores números de presos políticos por habitante</td></tr>
<tr><td>Chile</td><td>1973-1990</td><td>Golpe de <a href="mundo/augusto-pinochet.html">Pinochet</a> contra Allende</td></tr>
<tr><td>Argentina</td><td>1976-1983</td><td>Junta de <a href="mundo/jorge-videla.html">Videla</a> e milhares de desaparecidos</td></tr>
<tr><td>Peru</td><td>1968-1980, e depois Fujimori nos anos 1990</td><td>Ditadura militar de esquerda nacionalista, e depois um autogolpe civil</td></tr>
</tbody></table>
<h2>Por que tantas ditaduras?</h2>
<ul><li><strong>Guerra Fria:</strong> o medo do comunismo, depois da Revolução Cubana, levou elites e militares a apoiar golpes. Os EUA apoiaram vários deles.</li><li><strong>Desigualdade e crises:</strong> inflação, conflitos sociais e reformas que assustavam proprietários.</li><li><strong>Militares como “salvadores”:</strong> uma tradição de Forças Armadas que se viam como tutoras da nação. Veja o <a href="perigo-do-messianismo.html">messianismo</a>.</li><li><strong>Instituições frágeis:</strong> partidos, Justiça e imprensa com pouca força para resistir.</li><li><strong>Guerrilhas e violência política</strong> serviram de justificativa, embora a repressão tenha atingido muito além dos grupos armados.</li></ul>
<h2>A Operação Condor</h2>
<p>Nos anos 1970, ditaduras do Cone Sul, entre elas as do Chile, Argentina, Uruguai, Paraguai, Bolívia e Brasil, cooperaram para perseguir opositores além das fronteiras, com sequestros, troca de presos e assassinatos.</p>
<h2>Transição, memória e justiça</h2>
<table><thead><tr><th>País</th><th>Como lidou com o passado</th></tr></thead><tbody>
<tr><td>Argentina</td><td>Julgou as juntas militares e, depois de anistias revogadas, condenou centenas de agentes</td></tr>
<tr><td>Chile</td><td>Comissões da verdade e julgamentos, enquanto Pinochet seguiu influente por anos</td></tr>
<tr><td>Brasil</td><td>Lei da Anistia de 1979, que também protegeu agentes do Estado, e a Comissão Nacional da Verdade, em 2014</td></tr>
<tr><td>Uruguai</td><td>Lei que impediu julgamentos, mantida em plebiscitos, e depois revista em parte</td></tr>
</tbody></table>
<h2>E hoje?</h2>
<p>O risco atual raramente vem de tanques. Vem de líderes eleitos que atacam tribunais, imprensa e eleições. Há exemplos à direita e à esquerda, como a Venezuela de Maduro, que deixou de ser uma democracia. No Brasil, a tentativa de golpe e os ataques de 8 de janeiro de 2023 mostraram que o perigo não ficou no passado. Veja <a href="perigo-de-questionar-a-democracia.html">o perigo de questionar a democracia</a>.</p>
<div class="nota"><strong>Às vítimas:</strong> nossa memória e nossas condolências aos mortos, desaparecidos, torturados e exilados das ditaduras sul-americanas, e às famílias que ainda buscam respostas.</div>
''', fontes=[('Operação Condor (Wikipédia)', 'https://pt.wikipedia.org/wiki/Opera%C3%A7%C3%A3o_Condor'), ('Comissão Nacional da Verdade', 'https://pt.wikipedia.org/wiki/Comiss%C3%A3o_Nacional_da_Verdade'), ('Ditaduras militares na América do Sul (Wikipédia)', 'https://pt.wikipedia.org/wiki/Ditadura_militar')])
META_SUL = (['democracia', 'brasil'], ('O que foi a Operação Condor?', ['Uma cooperação entre ditaduras para perseguir opositores além das fronteiras', 'Um plano econômico', 'Uma operação contra o narcotráfico'], 0, 'Ditaduras do Cone Sul trocaram informações e presos, e sequestraram e mataram opositores.'))
