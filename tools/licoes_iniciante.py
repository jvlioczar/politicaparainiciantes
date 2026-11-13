"""Lições do nível Iniciante. O corpo é HTML; as fontes são pares (rótulo, url)."""
VINDING = ('Reasoned Politics (2022)', 'https://magnusvinding.com/wp-content/uploads/2022/03/reasoned-politics.pdf')

INICIANTE = [
dict(slug='o-que-e-politica', titulo='O que é política?', resumo='A palavra vem de pólis. Política é a disputa sobre o que vale para todos, e nem sempre é feita com boas ideias.', corpo='''
<p class="abre">Política é a disputa e a negociação sobre o que vale para todos em um grupo, quem decide e quem paga a conta.</p>
<p>Essa definição descreve o que a política <strong>é</strong>, e não o que ela deveria ser. Na prática, ela se faz muito com poder, interesses, <a href="perigo-do-tribalismo.html">tribalismo</a> e <a href="vieses-cognitivos.html">tendenciosidade</a>. Muita gente segue um lado ou uma pessoa, mais do que ideias. O ideal, decidir com bons argumentos e pensando em todos, é uma meta a buscar, e não o retrato de como as coisas costumam funcionar.</p>
<p>A palavra vem do grego <em>pólis</em>, a cidade-Estado da Grécia antiga. <em>Politiká</em> eram os assuntos da cidade: as leis, a defesa, os impostos, as obras. Aristóteles chamou o ser humano de “animal político” porque vivemos em comunidade e precisamos combinar regras.</p>
<h2>Ela está mais perto do que parece</h2>
<p>O preço da passagem de ônibus, a merenda da escola, a fila do posto de saúde, a idade para se aposentar e o imposto no pão são decisões políticas. Quem diz “não gosto de política” continua vivendo sob as decisões dela. Só deixa que outros as tomem.</p>
<h2>Política não é só eleição</h2>
<ul>
<li><strong>Política institucional:</strong> governos, parlamentos, tribunais e partidos.</li>
<li><strong>Política cotidiana:</strong> associação de bairro, sindicato, conselho escolar, abaixo-assinado.</li>
<li><strong>Política pública:</strong> o programa concreto que sai do papel, como o SUS ou o Bolsa Família.</li>
</ul>
<h2>As três perguntas de qualquer decisão</h2>
<ol><li><strong>Quem decide?</strong> Um rei, uma elite, eleitos, todo mundo?</li><li><strong>O que está sendo decidido?</strong> E por que isso, e não outra coisa?</li><li><strong>Quem ganha e quem perde?</strong> Quase toda decisão tem os dois lados.</li></ol>
<h2>Boa política e má política</h2>
<p>Toda decisão coletiva é política, mas nem toda política é boa. Política sem pensar no bem comum, movida só por interesses privados e sem considerar os outros, não é boa política: é usar o que é de todos em benefício de poucos. Pode ser legal e eficaz para quem a pratica, e ainda assim ser má política.</p>
<p>Ter interesses é normal: sindicatos, empresas e bairros defendem os seus, e isso faz parte da democracia. O problema é quando o interesse de um grupo passa por cima dos outros, sem levar em conta quem paga a conta. Uma boa pergunta é: <strong>essa decisão se sustenta quando se considera todo mundo que ela afeta, inclusive quem não estava na mesa?</strong> Veja a lição <a href="bem-comum.html">pensar no bem comum</a>.</p>
<div class="nota"><strong>Para guardar:</strong> política é inevitável onde há mais de uma pessoa e recursos limitados. A questão não é ter ou não política, mas fazê-la bem ou mal.</div>
''', fontes=[('Política', 'https://pt.wikipedia.org/wiki/Pol%C3%ADtica_(Arist%C3%B3teles)'), ('Política (Wikipédia)', 'https://pt.wikipedia.org/wiki/Pol%C3%ADtica')]),

dict(slug='o-que-esta-por-tras', titulo='O que está por trás das decisões?', resumo='Há uma parte difícil de enxergar: os interesses, e os valores morais de onde eles vêm.', corpo='''
<p class="abre">O que aparece na política é o discurso e a votação. O que fica escondido é o motivo. Por trás de cada decisão há interesses, e esses interesses nascem dos valores morais de quem decide.</p>
<p>Alguém pode estar na política para ajudar o povo, os mais necessitados, os animais ou a própria família. Pode também estar lá por egocentrismo, para ter mais dinheiro e mais poder. Quase sempre há uma mistura, e quase ninguém admite a parte feia.</p>
<table><thead><tr><th>O que motiva</th><th>Como costuma aparecer</th></tr></thead><tbody>
<tr><td>Ajudar quem está pior</td><td>Foco em saúde, renda e proteção social</td></tr>
<tr><td>Defender um grupo (religião, categoria, região)</td><td>Pautas e verbas dirigidas a esse grupo</td></tr>
<tr><td>Proteger financiadores</td><td>Leis com benefícios para um setor específico</td></tr>
<tr><td>Beneficiar a família</td><td>Nepotismo, parentes em cargos, herança eleitoral</td></tr>
<tr><td>Poder e ego</td><td>Culto à própria imagem, ataques a quem fiscaliza</td></tr>
</tbody></table>
<h2>Como enxergar o invisível</h2>
<ul>
<li><strong>Olhe o que a pessoa faz, não só o que diz.</strong> Votações ficam registradas nos sites da Câmara e do Senado.</li>
<li><strong>Siga o dinheiro.</strong> Doações, emendas e despesas de campanha são públicas no TSE e nos portais de transparência.</li>
<li><strong>Pergunte quem ganha.</strong> Uma lei boa para “o Brasil” pode ser muito boa para um setor em particular.</li>
<li><strong>Compare discurso e passado.</strong> Quem muda de posição explica por quê, ou finge que não mudou?</li>
</ul>
<div class="nota"><strong>Cuidado:</strong> não leia intenção ruim em todo mundo. Cinismo total (“são todos iguais”) também cega, e é útil para quem é pior do que a média.</div>
''', fontes=[VINDING, ('Portal da Câmara: votações', 'https://www.camara.leg.br/busca-portal/votacoes'), ('TSE: DivulgaCandContas', 'https://divulgacandcontas.tse.jus.br/')]),

dict(slug='valores-e-decisoes', titulo='Valores morais × decisões políticas', resumo='Primeiro: o que queremos? Depois: o que funciona? Misturar as duas perguntas gera a maior parte da confusão.', corpo='''
<p class="abre">Todo debate político tem duas perguntas dentro dele. Uma é moral: <em>o que devemos querer?</em> A outra é de fatos: <em>o que funciona para chegar lá?</em></p>
<p>O filósofo Magnus Vinding, no livro <em>Reasoned Politics</em>, chama isso de ideal dos dois passos. Ele observa que o debate público raramente separa valores de fatos, e que essa separação é justamente o que ajuda a pensar com clareza.</p>
<div class="passos"><div><span>1</span><h3>Passo normativo</h3><p>Esclarecer e defender os valores. Reduzir sofrimento? Proteger direitos? Aumentar a liberdade?</p></div><div><span>2</span><h3>Passo empírico</h3><p>Com os valores definidos, investigar quais políticas têm mais chance de realizá-los, segundo as evidências.</p></div></div>
<h2>Um exemplo</h2>
<p>Duas pessoas discutem o salário mínimo. Uma quer aumentá-lo, a outra não. Pode ser que as duas queiram exatamente a mesma coisa, reduzir a pobreza, e discordem só sobre o efeito no emprego. Isso é uma disputa de fatos, que dados podem ajudar a resolver. Ou pode ser que uma valorize a renda dos mais pobres e a outra a liberdade de contratar. Aí é uma disputa de valores, e os dados sozinhos não encerram a conversa.</p>
<table><thead><tr><th>Pergunta</th><th>Tipo</th><th>Como se discute</th></tr></thead><tbody>
<tr><td>O Estado deve garantir saúde para todos?</td><td>Valor</td><td>Argumento moral</td></tr>
<tr><td>Um sistema público reduz a mortalidade evitável?</td><td>Fato</td><td>Estudos e comparações</td></tr>
<tr><td>Animais merecem proteção legal?</td><td>Valor</td><td>Argumento moral</td></tr>
<tr><td>Multas reduzem maus-tratos?</td><td>Fato</td><td>Avaliação de resultados</td></tr>
</tbody></table>
<h2>A ética vem antes da política</h2>
<p>A ética pergunta o que é certo. A política decide o que fazer em conjunto. Toda decisão política já carrega uma resposta ética, mesmo sem dizê-la: quem conta, quanto conta, o que pode ser sacrificado. Por isso a ética é anterior à política: ela fundamenta as decisões. Quem pula essa etapa não fica sem ética. Fica com uma ética que nunca examinou.</p>
<p>Isso não significa que valores sejam intocáveis. Vinding lembra que valores também podem ser discutidos e revistos com bons argumentos.</p>
<div class="nota"><strong>Faça o teste:</strong> no próximo debate, pergunte “discordamos sobre o que queremos ou sobre o que funciona?”. Muita briga diminui aí.</div>
''', fontes=[VINDING]),

dict(slug='etica-normativa', titulo='As grandes teorias da ética', resumo='Consequências, deveres ou caráter: as três famílias que mais moldam como pensamos o certo e o errado.', corpo='''
<p class="abre">A ética normativa é a parte da filosofia que pergunta como devemos agir. Três grandes famílias respondem de formas diferentes, e cada uma dá mais peso a uma pergunta na hora de julgar uma lei ou uma política.</p>
<div class="tres">
<div><h3>Consequencialismo</h3><p><strong>O que pesa mais é o resultado.</strong> Uma política é boa se melhora a vida dos afetados.</p><p class="pol">Na política: “quanto sofrimento isso evita, e de quem?”</p></div>
<div><h3>Deontologia</h3><p><strong>O que pesa mais são os deveres e direitos.</strong> Certas coisas não se fazem, mesmo com bons resultados.</p><p class="pol">Na política: “isso viola um direito?”</p></div>
<div><h3>Ética do caráter</h3><p><strong>O que pesa mais é quem você se torna.</strong> Virtudes e cuidado com os outros.</p><p class="pol">Na política: “que tipo de sociedade isso nos torna?”</p></div>
</div>
<h2>Ponto focal, e não exclusividade</h2>
<p>As três famílias não são caixas fechadas. Quem pende para a deontologia também olha as consequências; quem pende para o consequencialismo também respeita regras, porque regras costumam produzir bons resultados. A diferença está no <strong>ponto focal</strong>: qual consideração ganha quando elas entram em conflito. Um deontologista aceita que a regra de não punir inocentes vale mesmo quando puni-los reduziria o crime; um consequencialista aceita quebrar uma regra se o ganho for grande e certo. Na maior parte dos casos do dia a dia, as três lentes concordam, e é nos casos difíceis que o peso de cada uma aparece.</p>
<h2>Como isso aparece na política</h2>
<p>Quase todo debate político tem as três perguntas dentro, com pesos diferentes para cada pessoa. Veja o mesmo problema pelas três lentes:</p>
<table><thead><tr><th>Decisão</th><th>Pelo resultado</th><th>Pelos direitos e deveres</th><th>Pelo caráter</th></tr></thead><tbody>
<tr><td>Prender um suspeito perigoso antes do julgamento</td><td>Quantos crimes isso evita, e quantos inocentes serão presos?</td><td>A presunção de inocência vale mesmo para quem parece culpado</td><td>Que tipo de sociedade prende por suspeita?</td></tr>
<tr><td>Vacinação obrigatória</td><td>Quantas vidas salva, comparada à adesão voluntária?</td><td>O Estado pode impor um procedimento no corpo de alguém? E a pessoa pode expor os outros?</td><td>O que uma pessoa cuidadosa faria pelos vizinhos?</td></tr>
<tr><td>Imposto maior sobre os mais ricos</td><td>O que o dinheiro produz em saúde e escola, e o que o imposto desestimula?</td><td>Há direito ao que se ganhou? Há dever de sustentar quem está pior?</td><td>Que relação com a riqueza queremos como sociedade?</td></tr>
<tr><td>Torturar um suspeito para obter uma informação</td><td>Um consequencialista rígido perguntaria se funciona; a evidência diz que não</td><td>Nunca, em nenhum caso: é o exemplo clássico de limite absoluto</td><td>Quem tortura deixa de ser o tipo de pessoa que diz defender</td></tr>
<tr><td>Proteger animais em fazendas industriais</td><td>Quanto sofrimento é evitado, a que custo?</td><td>Seres que sentem têm interesses que criam deveres?</td><td>O que a crueldade tolerada faz com quem a tolera?</td></tr>
</tbody></table>
<p>Repare em dois padrões. Constituições democráticas são, em geral, <strong>deontológicas no limite e consequencialistas no resto</strong>: fixam direitos que nenhuma maioria pode tirar, e deixam as políticas serem julgadas pelos resultados. E as frases de efeito da política costumam ser lentes mal usadas: “os fins justificam os meios” é consequencialismo sem contar os meios como consequência; “regra é regra” é deontologia sem perguntar para que a regra existe. Saber qual lente alguém está usando ajuda a entender por que duas pessoas de boa-fé chegam a conclusões opostas a partir dos mesmos fatos. Veja <a href="valores-e-decisoes.html">valores e decisões</a>, e, mais adiante, as <a href="teorias-da-justica.html">teorias da justiça</a>, que levam essas lentes à pergunta sobre como dividir o que é de todos.</p>
<h2>Os subtipos que mudam tudo</h2>
<table><thead><tr><th>Família</th><th>Variações</th><th>A diferença</th></tr></thead><tbody>
<tr><td>Consequencialismo</td><td>Utilitarismo, prioritarismo, maximin, igualitarismo, suficientismo</td><td>Somar o bem de todos? Priorizar quem está pior? Garantir um mínimo?</td></tr>
<tr><td>Consequencialismo</td><td>Simétrico, prioridade ao sofrimento, negativo</td><td>Quanto pesa evitar sofrimento comparado a gerar prazer</td></tr>
<tr><td>Deontologia</td><td>Religiosa, absolutista, moderada, de direitos</td><td>De onde vêm as regras, e se cedem diante de uma catástrofe</td></tr>
<tr><td>Caráter</td><td>Ética das virtudes, ética do cuidado</td><td>Traços admiráveis ou relações de cuidado</td></tr>
<tr><td>Outras</td><td>Egoísmo ético, relativismo, ceticismo</td><td>Interesse próprio, cultura, ou dúvida sobre haver resposta</td></tr>
</tbody></table>
<h2>Quem entra na conta? O círculo moral</h2>
<p>Toda teoria precisa dizer quem conta moralmente, e a resposta mudou ao longo da história. Durante séculos, escravizados, mulheres, estrangeiros e pessoas de outra religião ficaram fora do círculo de quem “importa”. O filósofo Peter Singer chama de <strong>expansão do círculo moral</strong> esse movimento de incluir quem antes era ignorado.</p>
<p>O que empurra o círculo para fora é um princípio simples, a <strong>universalidade</strong>: casos iguais devem ser tratados de forma igual, a menos que exista uma diferença relevante. A cor da pele, o sexo ou o lugar de nascimento não mudam a capacidade de sofrer, de pensar ou de querer, e por isso não serviam como razão para excluir ninguém. Quase todo avanço moral foi a descoberta de que uma diferença tratada como importante não era.</p>
<p>Isso permite falar em <strong>progresso</strong>: a abolição e o voto feminino não foram só mudanças de costume, e sim correções de uma incoerência. A pergunta que fica aberta, e que os níveis seguintes discutem, é se o círculo terminou de crescer, e quem mais poderia entrar nele. Veja <a href="testar-visao-moral.html">como testar sua visão moral</a> e <a href="progresso-moral-e-politico.html">progresso moral e político</a>.</p>
<div class="cta"><a class="btn" href="https://ethicstest.biblioverse.org/" target="_blank" rel="noopener">Faça o Teste de Visão Moral</a><a class="btn alt" href="https://ethicstest.biblioverse.org/map.html" target="_blank" rel="noopener">Veja o mapa das teorias</a></div>
''', fontes=[('Teste de Visão Moral: mapa', 'https://ethicstest.biblioverse.org/map.html'), ('Ética normativa (Wikipédia)', 'https://pt.wikipedia.org/wiki/%C3%89tica_normativa'), VINDING]),

dict(slug='esquerda-e-direita', titulo='Esquerda e direita', resumo='De onde vêm os termos, os valores comuns a cada lado e por que o rótulo ajuda, mas não basta.', corpo='''
<p class="abre">Os termos nasceram na Revolução Francesa de 1789: na assembleia, quem defendia o rei sentava à direita e quem queria mudanças, à esquerda. O assento virou rótulo, e o rótulo ficou.</p>
<p>Para o italiano Norberto Bobbio, a diferença mais duradoura é a atitude diante da <strong>igualdade</strong>: a esquerda tende a ver as desigualdades como problema a corrigir; a direita tende a vê-las como naturais, inevitáveis ou até úteis. O mesmo autor separa outro eixo: <strong>liberdade × autoridade</strong>. Por isso existem esquerda autoritária e esquerda libertária, direita autoritária e direita liberal.</p>
<table><thead><tr><th>Valores comuns a quem é considerado de esquerda</th><th>Valores comuns a quem é considerado de direita</th></tr></thead><tbody>
<tr><td>Igualdade e redução de desigualdades</td><td>Mérito e responsabilidade individual</td></tr>
<tr><td>Estado ativo em saúde, educação e renda</td><td>Livre mercado, menos impostos e menos Estado na economia</td></tr>
<tr><td>Direitos de minorias e mudança social</td><td>Tradição, família e continuidade</td></tr>
<tr><td>Direitos trabalhistas e sindicatos</td><td>Liberdade de contratar e empreender</td></tr>
<tr><td>Segurança ligada à prevenção e às causas sociais</td><td>Segurança ligada à ordem e à punição</td></tr>
</tbody></table>
<p class="legenda">São tendências, não regras. Há muita gente que mistura as duas colunas, e os dois lados têm correntes internas que brigam entre si.</p>
<h2>O espectro e seus eixos</h2>
<div class="espectro" aria-label="Espectro político"><span>Extrema-esquerda</span><span>Esquerda</span><span>Centro-esquerda</span><span>Centro</span><span>Centro-direita</span><span>Direita</span><span>Extrema-direita</span></div>
<!--MAPA-ED-->
<p>Uma linha só simplifica demais. Testes como o de Coordenadas Políticas usam dois eixos: um econômico (esquerda-direita) e um social (comunitário-liberal). Jean Laponce mostrou que a oposição entre esquerda e direita funciona quase como uma topografia mental, ligada a símbolos como sagrado e profano. Milton Rokeach propôs que a posição política acompanha o peso dado à liberdade e à igualdade. Pablo Stefanoni mostra como a “rebeldia” mudou de lado nas redes.</p>
<div class="nota"><strong>Rótulo é ponto de partida:</strong> “sou de direita” ou “sou de esquerda” diz pouco sobre o que alguém pensa de um tema específico. Pergunte sobre o tema.</div>
<div class="cta"><a class="btn" href="https://www.idrlabs.com/pt/coordenadas-politicas/teste.php" target="_blank" rel="noopener">Faça o Teste de Coordenadas Políticas</a></div>
''', fontes=[('Direita e Esquerda', 'https://pt.wikipedia.org/wiki/Norberto_Bobbio'), ('The Nature of Human Values', 'https://en.wikipedia.org/wiki/Milton_Rokeach'), ('Left and Right', 'https://www.google.com/search?tbm=bks&q=Jean+Laponce+Left+and+Right+The+Topography+of+Political+Perceptions'), ('A rebeldia tornou-se de direita?', 'https://www.google.com/search?tbm=bks&q=A+rebeldia+tornou-se+de+direita')]),

dict(slug='palavras-em-disputa', titulo='Palavras em disputa: liberdade e conservar', resumo='Esquerda e direita usam as mesmas palavras e querem dizer coisas diferentes.', corpo='''
<p class="abre">Muita discussão política é feita com a mesma palavra em dois sentidos. Antes de concordar ou discordar, pergunte: o que você quer dizer com isso?</p>
<h2>Liberdade</h2>
<table><thead><tr><th>Para a direita, em geral</th><th>Para a esquerda, em geral</th></tr></thead><tbody>
<tr><td><strong>Liberdade negativa:</strong> ninguém, sobretudo o Estado, deve interferir na sua vida, nos seus negócios, na sua propriedade.</td><td><strong>Liberdade positiva:</strong> ter condições reais de escolher. Quem passa fome não é livre, ainda que nada o proíba.</td></tr>
</tbody></table>
<p>A distinção é do filósofo Isaiah Berlin. Os dois usos têm força e têm risco: o primeiro pode ignorar quem não tem nada, o segundo pode justificar um Estado que decide tudo por você.</p>
<p>Uma terceira camada: a liberdade precisa estar minimamente ligada à ausência de sofrimento e a um bom nível de bem-estar. O filósofo Alasdair Cochrane é útil aqui. Ele argumenta que a liberdade tem valor principalmente porque serve ao bem-estar de quem a vive. O que importa de modo mais básico é o interesse em não sofrer e em viver bem. Uma “liberdade” que produz sofrimento em massa merece, no mínimo, ser questionada.</p>
<h2>Conservar</h2>
<table><thead><tr><th>Para a direita, em geral</th><th>Para a esquerda, em geral</th></tr></thead><tbody>
<tr><td>Conservar a família, a religião, as instituições e os costumes que passaram pelo teste do tempo.</td><td>Conservar a natureza, os direitos conquistados, a CLT, o SUS, os povos tradicionais.</td></tr>
</tbody></table>
<p>Ou seja, os dois lados conservam alguma coisa e os dois querem mudar outras. <strong>Conservar algo não é bom em si</strong>, assim como mudar não é bom em si. A escravidão também era tradição. A pergunta útil é: isso que queremos conservar ou mudar reduz sofrimento e melhora a vida de quem?</p>
<h2>Outras palavras para desconfiar</h2>
<ul>
<li><strong>Justiça:</strong> dar a cada um o que mereceu, ou o que precisa?</li>
<li><strong>Democracia:</strong> vontade da maioria, ou maioria com limites e direitos?</li>
<li><strong>Povo:</strong> todos, ou só quem concorda comigo?</li>
<li><strong>Liberal:</strong> no Brasil, costuma significar pró-mercado; nos EUA, progressista. Veja <a href="esquerda-e-direita-pelo-mundo.html">esquerda e direita pelo mundo</a>.</li>
<li><strong>Patriota, família, ordem, igualdade:</strong> quem está incluído, e quem fica de fora?</li>
<li><strong>Coletivista e individualista:</strong> viraram xingamentos dos dois lados. Veja <a href="coletivismo-e-individualismo.html">coletivismo e individualismo</a>.</li>
</ul>
''', fontes=[('Dois conceitos de liberdade', 'https://pt.wikipedia.org/wiki/Isaiah_Berlin'), ('Animal Rights Without Liberation', 'https://cup.columbia.edu/book/animal-rights-without-liberation/9780231151832'), ('Vídeo indicado: Reel sobre liberdade e conservar', 'https://www.instagram.com/reels/DOvxsydgNeV/'), ('Post indicado no Instagram', 'https://www.instagram.com/p/DTk-B15Dn0V')]),

dict(slug='democracia', titulo='Democracia, sem enrolação', resumo='Mais do que votar: direitos, imprensa livre, tribunais e troca pacífica de poder.', corpo='''
<p class="abre">Democracia é o regime em que o poder vem dos cidadãos, que podem trocar seus governantes sem violência. Mas eleição sozinha não basta: ditaduras também fazem eleições.</p>
<h2>O que precisa existir junto</h2>
<ul><li>Eleições livres, com oposição de verdade e voto secreto.</li><li>Direitos garantidos, mesmo contra a vontade da maioria.</li><li>Imprensa livre e liberdade de expressão.</li><li>Justiça independente.</li><li>Poderes que se fiscalizam.</li><li>Quem perde aceita o resultado.</li></ul>
<h2>Formatos</h2>
<table><thead><tr><th>Tipo</th><th>Como funciona</th></tr></thead><tbody>
<tr><td>Representativa</td><td>Elegemos quem decide. É o principal modelo no Brasil.</td></tr>
<tr><td>Direta</td><td>Os cidadãos decidem diretamente. No Brasil: plebiscito, referendo e lei de iniciativa popular.</td></tr>
<tr><td>Participativa</td><td>Conselhos, audiências e orçamento participativo somam-se aos eleitos.</td></tr>
</tbody></table>
<h2>Por que ela costuma dar resultados melhores</h2>
<p>Não é só uma questão de princípio. O economista Amartya Sen, Nobel de 1998, observou que nenhuma grande fome aconteceu em um país com eleições e imprensa livre: quando o governo pode ser cobrado e a notícia circula, ele é forçado a agir. O mesmo mecanismo vale para epidemias, desastres e corrupção. Ditaduras escondem os próprios erros, porque ninguém pode denunciá-los, e por isso os repetem. A democracia não garante bons governos. Garante que os ruins possam ser trocados sem sangue, e que os erros apareçam a tempo de serem corrigidos.</p>
<h2>Quem vota no Brasil</h2>
<table><thead><tr><th>Quem</th><th>Voto</th></tr></thead><tbody>
<tr><td>De 18 a 70 anos</td><td>Obrigatório. Quem não vota nem justifica paga uma multa pequena e fica com pendências, como não poder tirar passaporte</td></tr>
<tr><td>16 e 17 anos, mais de 70 anos e analfabetos</td><td>Facultativo</td></tr>
<tr><td>Estrangeiros e conscritos no serviço militar</td><td>Não votam</td></tr>
</tbody></table>
<p>O voto é direto, secreto e tem o mesmo peso para todos. O eleitorado passou de 155 milhões de pessoas em 2022, e as eleições acontecem a cada dois anos, alternando as gerais (presidente, governador, Congresso e assembleias) e as municipais. Se o voto obrigatório é bom ou ruim é uma pergunta em aberto: veja o <a href="debates/voto-obrigatorio.html">debate</a>.</p>
<h2>Como democracias morrem hoje</h2>
<p>Steven Levitsky e Daniel Ziblatt mostram que, hoje, o risco costuma vir de dentro: líderes eleitos que atacam juízes, imprensa e regras do jogo aos poucos, sempre dizendo defender a democracia. Os sinais são rejeitar resultados, tratar adversários como inimigos, tolerar violência e limitar liberdades civis.</p>
<div class="nota">A democracia tem muitos defeitos, e criticá-la para melhorá-la é saudável. O perigo está em <a href="perigo-de-questionar-a-democracia.html">abandoná-la</a> sem nada melhor no lugar.</div>
''', fontes=[('Como as democracias morrem', 'https://pt.wikipedia.org/wiki/How_Democracies_Die'), ('Constituição Federal, art. 14', 'https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm'), ('Desenvolvimento como liberdade (Amartya Sen)', 'https://pt.wikipedia.org/wiki/Amartya_Sen'), ('TSE: estatísticas do eleitorado', 'https://www.tse.jus.br/eleicoes/estatisticas')]),

dict(slug='como-votar-bem', titulo='Como votar da melhor forma', resumo='Um roteiro simples: conheça a história, leia as propostas, cheque os números, pense além de você.', corpo='''
<p class="abre">Votar bem dá trabalho, mas não é complicado. Quatro passos resolvem a maior parte.</p>
<ol class="roteiro">
<li><strong>Conheça a história de quem pede seu voto.</strong> O que fez nos cargos anteriores? Como votou? Responde a processos? Veja no <a href="https://divulgacandcontas.tse.jus.br/" target="_blank" rel="noopener">DivulgaCandContas do TSE</a>.</li>
<li><strong>Leia as propostas.</strong> O plano de governo está registrado no TSE. Olhe economia, saúde, segurança, liberdades, diversidade e meio ambiente. Veja também o partido e as alianças, porque ninguém governa sozinho.</li>
<li><strong>Verifique se o que dizem é verdade.</strong> Políticos inflam números. Use as <a href="checagem-de-fatos.html">agências de checagem</a>.</li>
<li><strong>Pense além de você.</strong> Quem tem capacidade real de ajudar mais gente, inclusive quem está em pior situação? Não vote só por interesse pessoal ou por raiva de alguém.</li>
</ol>
<h2>Não esqueça o resto da cédula</h2>
<p>Deputados, senadores, governadores, prefeitos e vereadores decidem muita coisa do seu dia a dia. Veja <a href="cargos.html">o que cada cargo faz</a>. E anote em quem votou para poder cobrar.</p>
<h2>Como a conta funciona</h2>
<ul>
<li><strong>Eleição majoritária</strong> (presidente, governador, senador, prefeito): vence quem tem mais votos. Para presidente, governador e prefeito de cidade com mais de 200 mil eleitores, há segundo turno entre os dois primeiros se ninguém passar da metade dos votos válidos. Senador não tem segundo turno.</li>
<li><strong>Eleição proporcional</strong> (deputados e vereadores): as vagas são divididas conforme os votos do partido ou da federação. Seu voto ajuda o partido, por isso pode eleger outra pessoa da lista.</li>
<li><strong>Branco e nulo</strong> não entram nos votos válidos. Não “vão para o primeiro colocado” nem anulam a eleição.</li>
</ul>
<h2>Depois da eleição</h2>
<p>Acompanhe, cobre e critique. Não idolatre ninguém. Discuta ideias sem baixar o nível.</p>
''', fontes=[('Tudo que você precisa saber para votar', 'https://julismo.wordpress.com/2018/08/16/tudo-que-voce-precisa-saber-para-votar-da-melhor-forma-possivel/'), ('TSE', 'https://www.tse.jus.br/'), ('Politize!', 'https://www.politize.com.br/')]),

dict(slug='checagem-de-fatos', titulo='Fake news e checagem de fatos', resumo='Mentira viraliza porque mexe com a emoção. Como se defender em dois minutos.', corpo='''
<p class="abre">Desinformação é conteúdo falso ou enganoso que circula como se fosse verdade. Costuma ser feita para provocar raiva ou medo, porque emoção forte faz a gente compartilhar sem pensar.</p>
<p>O estudo <em>Anatomia da desinformação eleitoral</em>, da Lupa, mostra que a mentira hoje depende menos do conteúdo totalmente falso e mais da manipulação, da distorção e do que é tirado de contexto. Só 34% das falas de políticos checadas eram totalmente verdadeiras, e a esquerda e a direita aparecem entre os checados.</p>
<h2>O teste de dois minutos</h2>
<ol class="roteiro"><li><strong>Respire.</strong> Se te deu muita raiva ou muita alegria, redobre o cuidado.</li><li><strong>Veja a fonte.</strong> Quem publicou? É um veículo com endereço, autor e correção de erros?</li><li><strong>Procure em outro lugar.</strong> Se fosse grave e verdade, outros veículos estariam falando.</li><li><strong>Confira data e contexto.</strong> Vídeo antigo, corte de fala e legenda inventada são truques comuns.</li><li><strong>Consulte quem checa.</strong> Veja a lista abaixo.</li></ol>
<h2>Casos clássicos no Brasil</h2>
<p>Alguns boatos marcaram eleições e viraram exemplos de como a desinformação funciona: emoção forte, um detalhe verdadeiro deformado e uma rede de distribuição pronta. Todos foram checados e desmentidos, e todos continuaram circulando.</p>
<table><thead><tr><th>O boato</th><th>O que era de fato</th></tr></thead><tbody>
<tr><td><strong>“Kit gay” nas escolas</strong> (2018)</td><td>Material de combate à homofobia do programa Escola sem Homofobia, de 2011, nunca distribuído: o governo Dilma o cancelou antes. Na campanha de 2018, foi apresentado como livro de Fernando Haddad para ensinar sexo a crianças, com um livro que não fazia parte do material. O TSE mandou remover as peças e a checagem concluiu que o “kit” não existiu</td></tr>
<tr><td><strong>“Mamadeira de piroca”</strong> (2018)</td><td>Boato de que o PT distribuiria em creches mamadeiras com bico em formato de pênis. Não havia nenhum programa, produto ou documento: a imagem era de um item de brincadeira de despedida de solteira. Viralizou no WhatsApp e foi desmentido por todas as agências</td></tr>
<tr><td><strong>Fraude nas urnas</strong> (2018 a 2022)</td><td>Vídeos de urnas “se autocompletando” eram falsos ou editados; os testes públicos de segurança, as auditorias e as checagens não encontraram fraude. O TSE tornou Bolsonaro inelegível em 2023 por ataques ao sistema sem provas, e o boato foi um dos combustíveis do 8 de janeiro</td></tr>
<tr><td><strong>Cloroquina cura a covid</strong> (2020)</td><td>Estudos pequenos e falhos foram usados como prova; os ensaios grandes mostraram que o remédio não funciona contra a doença e pode fazer mal. O boato foi promovido por autoridades, e não só por anônimos</td></tr>
<tr><td><strong>Lula vai fechar igrejas</strong> (2022)</td><td>Montagens e cortes de fala sugeriam perseguição religiosa. Nenhuma proposta existia; as checagens desmentiram, e o tema dominou grupos evangélicos na reta final</td></tr>
<tr><td><strong>Bolsonaro e o canibalismo</strong> (2022)</td><td>Uma fala real, sobre uma viagem a uma aldeia, foi cortada e usada em vídeo do PT para sugerir que ele cometeria canibalismo. O TSE mandou tirar do ar por descontextualização</td></tr>
<tr><td><strong>“Taxação do Pix”</strong> (2025)</td><td>Uma norma da Receita sobre monitoramento de transações foi lida como imposto novo. Não havia imposto; a confusão derrubou a norma e mostrou que um boato pode mudar uma política em dias</td></tr>
</tbody></table>
<p class="legenda">Os casos vêm de campos diferentes de propósito. Veja o <a href="ranking-da-mentira.html">Ranking da mentira</a> para quem mais teve frases checadas como falsas, e a lição sobre <a href="perigo-dos-grupos-de-mensagem.html">grupos de mensagem</a>, por onde a maioria desses boatos circulou.</p>
<h2>Agências de checagem</h2>
<ul class="links">
<li><a href="https://www.agencialupa.org/" target="_blank" rel="noopener">Agência Lupa</a></li><li><a href="https://www.aosfatos.org/" target="_blank" rel="noopener">Aos Fatos</a></li><li><a href="https://projetocomprova.com.br/" target="_blank" rel="noopener">Projeto Comprova</a></li><li><a href="https://g1.globo.com/fato-ou-fake/" target="_blank" rel="noopener">Fato ou Fake (g1)</a></li><li><a href="https://factcheck.afp.com/" target="_blank" rel="noopener">AFP Checamos</a></li><li><a href="https://www.reuters.com/fact-check/" target="_blank" rel="noopener">Reuters Fact Check</a></li><li><a href="https://www.boatos.org/" target="_blank" rel="noopener">Boatos.org</a></li><li><a href="https://www.e-farsas.com/" target="_blank" rel="noopener">E-farsas</a></li><li><a href="https://toolbox.google.com/factcheck/explorer" target="_blank" rel="noopener">Google Fact Check Explorer</a></li>
</ul>
<p>Agências também erram e também são criticadas. A diferença é que mostram as fontes, publicam o método e corrigem em público. Isso é o que permite conferir.</p>
<div class="cta"><a class="btn" href="ranking-da-mentira.html">Ver o Ranking da mentira</a><a class="btn alt" href="acompanhar.html">Onde acompanhar política</a></div>
''', fontes=[('Anatomia da desinformação eleitoral (2026)', 'https://uploads.agencialupa.org/2026/07/RELATORIO-ANATOMIA-DA-DESINFORMACAO-ELEITORAL_LUPA-FINAL.pdf'), ('Biblioteca Antigolpes: checagem', 'https://biblioverse.org/antiscam/#verificar-antes-de-confiar--checagem-de-fatos-e-boatos'), ('Biblioteca de Dados: jornalismo e checagem', 'https://biblioverse.org/data/#jornalismo-de-dados-e-checagem')]),

dict(slug='sem-binarismo', titulo='Sair do nós contra eles', resumo='Política não é torcida. Quem trata assim perde a chance de aprender e de resolver problemas.', corpo='''
<p class="abre">O debate na internet costuma funcionar como jogo de torcidas: meu time acerta sempre, o outro erra sempre. São embates, não debates. A meta vira vencer, não entender.</p>
<p>Vinding resume o mecanismo: nossa política é muito movida pela vontade de ver o nosso time ganhar e de mostrar lealdade a ele, e não por boas políticas.</p>
<h2>Como isso atrapalha</h2>
<ul><li><strong>Boas ideias morrem pela origem.</strong> “Veio do outro lado, então é ruim.”</li><li><strong>Pacotes inteiros.</strong> Você adota tudo que seu lado defende, sem pensar tema a tema.</li><li><strong>Erros dos nossos ficam impunes.</strong> A lealdade vira licença.</li><li><strong>Quem ganha é quem lucra com a raiva.</strong></li></ul>
<h2>Pontos em comum existem</h2>
<p>A maioria das pessoas concorda que crianças não devem passar fome, que ninguém deve morrer esperando atendimento e que sofrimento extremo precisa ser evitado. Começar por aí não acaba com as divergências, mas muda o tom e abre soluções em que todos ganham.</p>
<h2>Como conversar melhor</h2>
<ol class="roteiro"><li>Explique a posição do outro de um jeito que ele aceitaria.</li><li>Separe <a href="valores-e-decisoes.html">valores de fatos</a>.</li><li>Diga o que faria você mudar de ideia.</li><li>Critique ideias, não pessoas.</li><li>Admita quando o outro lado tem razão em algo.</li></ol>
<p>Para aprofundar, veja <a href="perigo-do-tribalismo.html">o perigo do tribalismo e dos pacotes de ideias</a>.</p>
<div class="nota">Evitar o binarismo não é ficar em cima do muro. A neutralidade total não existe e tomar posição é legítimo. O problema é tratar a própria posição como time.</div>
''', fontes=[('Binarismo político', 'https://julismo.wordpress.com/2016/03/09/binarismo-politico/'), VINDING]),
]
