// Interações do site: busca, menu, progresso, testes, filtros e ferramentas.
(function () {
  var base = document.body.dataset.base || '';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
  var norm = function (s) { return String(s).normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase(); };
  /* busca: o nome vem antes da descrição (0 nome igual, 1 começa, 2 palavra, 3 trecho, 4 só no resto) */
  var pontua = function (titulo, t) {
    var n = norm(titulo).trim();
    if (n === t) return 0;
    if (n.indexOf(t) === 0) return 1;
    if (n.split(/[^a-z0-9]+/).some(function (w) { return w.indexOf(t) === 0; })) return 2;
    return n.indexOf(t) >= 0 ? 3 : 4;
  };
  var ordena = function (raiz, cards, t) {
    t = t.trim();
    cards.forEach(function (c, i) { if (!c._casa) { c._casa = c.parentNode; c._pos = i; } });
    cards.forEach(function (c) { if (c.parentNode !== c._casa) c._casa.appendChild(c); });
    cards.slice().sort(function (a, b) { return a._pos - b._pos; }).forEach(function (c) { c._casa.appendChild(c); });
    var rb = raiz._rb;
    if (rb) rb.hidden = true;
    if (!t) return;
    var vis = cards.filter(function (c) { return !c.hidden; }).map(function (c) { var h = c.querySelector('h3'); return { c: c, p: pontua(h ? h.textContent : c.textContent, t) }; });
    vis.sort(function (a, b) { return a.p - b.p || a.c._pos - b.c._pos; });
    var unica = cards.every(function (c) { return c._casa === cards[0]._casa; });
    if (unica) { vis.forEach(function (x) { x.c._casa.appendChild(x.c); }); return; }
    if (!rb) { rb = raiz._rb = document.createElement('div'); rb.className = 'grade res-busca'; raiz.insertBefore(rb, raiz.firstChild); }
    rb.hidden = false;
    vis.forEach(function (x) { rb.appendChild(x.c); });
  };
  var el = function (t, a, tx) { var e = document.createElement(t); if (a) Object.keys(a).forEach(function (k) { e.setAttribute(k, a[k]); }); if (tx != null) e.textContent = tx; return e; };
  var ler = function (k, d) { try { return JSON.parse(localStorage.getItem(k)) || d; } catch (x) { return d; } };
  var grava = function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (x) {} };

  /* menu */
  var hamb = $('.hamb'), menu = $('.menu');
  if (hamb) hamb.addEventListener('click', function () { menu.classList.toggle('aberto'); hamb.setAttribute('aria-expanded', menu.classList.contains('aberto')); });
  var drops = $$('.drop');
  function fechaMenus(fora) { drops.forEach(function (d) { if (d !== fora) { $('.mega', d).hidden = true; $('button', d).setAttribute('aria-expanded', 'false'); } }); }
  drops.forEach(function (d) {
    var b = $('button', d), m = $('.mega', d);
    b.addEventListener('click', function (e) { e.stopPropagation(); fechaMenus(d); m.hidden = !m.hidden; b.setAttribute('aria-expanded', !m.hidden); });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.drop')) fechaMenus();
    if (hamb && menu.classList.contains('aberto') && !e.target.closest('.topo')) { menu.classList.remove('aberto'); hamb.setAttribute('aria-expanded', 'false'); }
  });

  /* busca */
  var ov = $('#busca'), q = $('#q'), res = $('#res'), dados = null;
  function abre() { ov.hidden = false; q.value = ''; res.textContent = ''; q.focus(); if (!dados) fetch(base + 'assets/busca.json').then(function (r) { return r.json(); }).then(function (j) { dados = j; }); }
  function fecha() { ov.hidden = true; }
  $$('.bbusca').forEach(function (b) { b.addEventListener('click', abre); });
  document.addEventListener('keydown', function (e) {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); abre(); }
    if (e.key === 'Escape') { fecha(); fechaMenus(); }
  });
  if (ov) {
    ov.addEventListener('click', function (e) { if (e.target === ov) fecha(); });
    q.addEventListener('input', function () {
      var t = norm(q.value.trim()); res.textContent = '';
      if (t.length < 2 || !dados) return;
      var a = dados.filter(function (d) { return norm(d.t + ' ' + d.d).indexOf(t) >= 0; }).map(function (d, i) { return { d: d, p: pontua(d.t, t), i: i }; }).sort(function (x, y) { return x.p - y.p || x.i - y.i; }).slice(0, 9).map(function (x) { return x.d; });
      if (!a.length) res.appendChild(el('p', null, 'Nada encontrado.'));
      a.forEach(function (d) { var l = el('a', { href: base + d.u }, d.t); l.appendChild(el('small', null, d.d)); res.appendChild(l); });
    });
    q.addEventListener('keydown', function (e) { if (e.key === 'Enter') { var a = $('a', res); if (a) location.href = a.href; } });
  }

  /* progresso das lições */
  var lidas = ler('ppi-lidas', []);
  var marca = $('.marcar');
  function pinta() {
    $$('[data-licao]').forEach(function (c) { c.classList.toggle('lido', lidas.indexOf(c.dataset.licao) >= 0); });
    $$('[data-ponto]').forEach(function (c) { c.classList.toggle('lida', lidas.indexOf(c.dataset.ponto) >= 0); });
    $$('[data-prog]').forEach(function (p) {
      var ids = p.dataset.prog.split(','), n = ids.filter(function (i) { return lidas.indexOf(i) >= 0; }).length;
      $('i', p).style.width = (n / ids.length * 100) + '%';
      var t = $('[data-prog-t="' + p.id + '"]'); if (t) t.textContent = n + ' de ' + ids.length + ' lições lidas';
    });
  }
  if (marca) {
    var id = marca.dataset.id, est = function () { var on = lidas.indexOf(id) >= 0; marca.setAttribute('aria-pressed', on); marca.textContent = on ? '✓ Lição lida' : 'Marcar como lida'; };
    marca.addEventListener('click', function () { var i = lidas.indexOf(id); if (i >= 0) lidas.splice(i, 1); else lidas.push(id); grava('ppi-lidas', lidas); est(); pinta(); });
    est();
  }
  pinta();

  /* setas do teclado entre as lições */
  if ($('.indice')) document.addEventListener('keydown', function (e) {
    if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
    if (e.ctrlKey || e.metaKey || e.altKey || e.shiftKey) return;
    if (e.target.closest('input,textarea,select,[contenteditable],.tabela')) return;
    var a = $(e.key === 'ArrowLeft' ? '.indice-seta[rel=prev]' : '.indice-seta[rel=next]');
    if (a) location.href = a.href;
  });

  /* sumário */
  var toc = $('.toc');
  if (toc) {
    $$('.leitura h2').forEach(function (h, i) { if (h.closest('.fontes')) return; h.id = h.id || 's' + i; var li = el('li'); li.appendChild(el('a', { href: '#' + h.id }, h.textContent)); toc.appendChild(li); });
    if (!toc.children.length) toc.closest('.caixa').hidden = true;
  }

  /* pergunta com alternativas */
  function pergunta(raiz, texto, ops, certo, expl, depois) {
    raiz.textContent = '';
    raiz.appendChild(el('p', { class: 'q' }, texto));
    var box = el('div', { class: 'ops' }), fb = el('p', { class: 'fb', role: 'status' });
    ops.forEach(function (o, i) {
      var b = el('button', { type: 'button' }, o);
      b.addEventListener('click', function () {
        $$('button', box).forEach(function (x, j) { x.disabled = true; if (j === certo) x.classList.add('certo'); });
        var ok = i === certo; if (!ok) b.classList.add('errado');
        fb.textContent = (ok ? 'Isso! ' : 'Quase. ') + expl;
        if (depois) depois(ok);
      });
      box.appendChild(b);
    });
    raiz.appendChild(box); raiz.appendChild(fb);
  }
  /* placar da página de revisão: conta respondidas e acertos */
  var placar = $('#placar-rev'), respondidas = 0, acertos = 0;
  function somaPlacar(ok) {
    respondidas++; if (ok) acertos++;
    placar.textContent = 'Placar: ' + acertos + ' acerto' + (acertos === 1 ? '' : 's') + ' em ' + respondidas + ' respondida' + (respondidas === 1 ? '' : 's') + ', de ' + placar.dataset.total + ' perguntas.' + (respondidas >= +placar.dataset.total ? (acertos === respondidas ? ' Tudo certo!' : ' Volte às lições das perguntas que errou.') : '');
  }
  $$('[data-quiz]').forEach(function (z) { var d = JSON.parse(z.dataset.quiz); pergunta($('.alvo', z), d[0], d[1], d[2], d[3], placar ? somaPlacar : null); });
  function jogo(raiz, itens, opsDe, certoDe, textoDe, explDe) {
    var i = 0, pts = 0, alvo = $('.alvo', raiz), plc = $('.placar', raiz), bar = $('.barra-prog i', raiz), prox = $('.prox-q', raiz);
    function mostra() {
      plc.firstChild.textContent = 'Pergunta ' + (i + 1) + ' de ' + itens.length; plc.lastChild.textContent = pts + ' acertos';
      bar.style.width = (i / itens.length * 100) + '%'; prox.hidden = true;
      var it = itens[i], ops = opsDe(it);
      pergunta(alvo, textoDe(it), ops, ops.indexOf(certoDe(it)), explDe(it), function (ok) { if (ok) pts++; plc.lastChild.textContent = pts + ' acertos'; prox.hidden = false; prox.textContent = i + 1 < itens.length ? 'Próxima' : 'Ver resultado'; });
    }
    prox.addEventListener('click', function () {
      i++;
      if (i < itens.length) return mostra();
      bar.style.width = '100%'; prox.hidden = true; alvo.textContent = '';
      alvo.appendChild(el('p', { class: 'q' }, 'Você acertou ' + pts + ' de ' + itens.length + '.'));
      var de = el('button', { class: 'btn', type: 'button' }, 'Jogar de novo'); de.addEventListener('click', function () { i = 0; pts = 0; mostra(); }); alvo.appendChild(de);
    });
    mostra();
  }
  var dj = $('#dados-jogo');
  if (dj) {
    var J = JSON.parse(dj.textContent);
    if (J.tipo === 'cargos') { var nomes = ['Vereador', 'Prefeito', 'Deputado estadual', 'Governador', 'Deputado federal', 'Senador', 'Presidente']; jogo($('#jogo'), J.itens, function () { return nomes; }, function (x) { return x[1]; }, function (x) { return x[0] + '. Quem é o responsável principal?'; }, function (x) { return x[2]; }); }
    if (J.tipo === 'truques') jogo($('#jogo'), J.itens, function () { return J.ops; }, function (x) { return x[1]; }, function (x) { return x[0]; }, function (x) { return x[2]; });
    if (J.tipo === 'frases') jogo($('#jogo'), J.itens, function () { return ['Fato', 'Valor']; }, function (x) { return x[1]; }, function (x) { return '“' + x[0] + '”'; }, function (x) { return x[2]; });
  }

  /* catálogo */
  var cat = $('#catalogo');
  if (cat) {
    var cs = $$('.cartao', cat), busca = $('#fq'), cont = $('#contagem'), f = { tema: '', nivel: '' }, u = new URLSearchParams(location.search);
    f.tema = u.get('tema') || ''; f.nivel = u.get('nivel') || '';
    var aplicaC = function () {
      var t = norm(busca.value), n = 0;
      cs.forEach(function (c) { var ok = (!f.tema || c.dataset.temas.split(' ').indexOf(f.tema) >= 0) && (!f.nivel || c.dataset.nivel === f.nivel) && norm(c.textContent).indexOf(t) >= 0; c.hidden = !ok; if (ok) n++; });
      ordena(cat, cs, t);
      cont.textContent = n + (n === 1 ? ' item' : ' itens');
      $$('.filtros button').forEach(function (b) { b.setAttribute('aria-pressed', f[b.dataset.k] === b.dataset.v); });
    };
    busca.addEventListener('input', aplicaC);
    $$('.filtros button').forEach(function (b) { b.addEventListener('click', function () { f[b.dataset.k] = b.dataset.v; aplicaC(); }); });
    aplicaC();
  }

  /* partidos */
  var lista = $('#partidos');
  if (lista) {
    var cards = [].slice.call(lista.children), fq = $('#fq'), atual = '';
    var aplica = function () { var t = norm(fq.value); cards.forEach(function (c) { c.hidden = !((!atual || c.dataset.e === atual) && norm(c.textContent).indexOf(t) >= 0); }); ordena(lista, cards, t); };
    fq.addEventListener('input', aplica);
    $$('.filtros button').forEach(function (b) { b.addEventListener('click', function () { atual = b.dataset.e; $$('.filtros button').forEach(function (o) { o.setAttribute('aria-pressed', o === b); }); aplica(); }); });
  }

  /* figuras */
  var figs = $('#figuras');
  if (figs) {
    var fc = $$('.fig', figs), gs = $$('.grupo-fig', figs), fb = $('#fq'), ctg = $('#contagem'), ff = { cat: '', tipo: '', deb: '', reg: '' };
    var aplicaF = function () {
      var t = norm(fb.value), n = 0;
      fc.forEach(function (c) { var ok = (!ff.cat || c.dataset.cat === ff.cat) && (!ff.tipo || c.dataset.tipo === ff.tipo) && (!ff.deb || c.dataset.deb === ff.deb) && (!ff.reg || c.dataset.reg === ff.reg) && norm(c.textContent).indexOf(t) >= 0; c.hidden = !ok; if (ok) n++; });
      ordena(figs, fc, t);
      gs.forEach(function (g) { g.hidden = !$$('.fig', g).some(function (c) { return !c.hidden; }); });
      ctg.textContent = n + (n === 1 ? ' figura' : ' figuras');
    };
    fb.addEventListener('input', aplicaF);
    $$('.filtros button').forEach(function (b) { b.addEventListener('click', function () { ff[b.dataset.k] = b.dataset.v; $$('.filtros button[data-k="' + b.dataset.k + '"]').forEach(function (o) { o.setAttribute('aria-pressed', o === b); }); aplicaF(); }); });
    aplicaF();
  }

  /* sites: nacionais e internacionais */
  var famb = $('#famb');
  if (famb) {
    $$('button', famb).forEach(function (b) { b.addEventListener('click', function () {
      $$('button', famb).forEach(function (o) { o.setAttribute('aria-pressed', o === b); });
      $$('.ambito').forEach(function (x) { x.hidden = !!b.dataset.a && x.dataset.amb !== b.dataset.a; });
      $$('.grupo-s').forEach(function (g) { g.hidden = !$$('.ambito', g).some(function (x) { return !x.hidden; }); });
    }); });
  }

  /* vertentes */
  var vz = $('#vertentes');
  if (vz) {
    var vc = $$('.vert', vz), vg = $$('.grupo-v', vz), vq = $('#vq'), vf = '';
    var aplicaV = function () { var t = norm(vq.value); vc.forEach(function (c) { c.hidden = !((!vf || c.dataset.f === vf) && norm(c.textContent).indexOf(t) >= 0); }); ordena(vz, vc, t); vg.forEach(function (g) { g.hidden = !$$('.vert', g).some(function (c) { return !c.hidden; }); }); };
    vq.addEventListener('input', aplicaV);
    $$('#vfam button').forEach(function (b) { b.addEventListener('click', function () { vf = b.dataset.f; $$('#vfam button').forEach(function (o) { o.setAttribute('aria-pressed', o === b); }); aplicaV(); }); });
    var VD = JSON.parse($('#dados-vert').textContent), vs = [$('#va'), $('#vb'), $('#vc')], ini = ['liberalismo-classico', 'social-democracia', 'marxismo'];
    var compV = function () {
      var ps = vs.map(function (s) { return VD.filter(function (x) { return x.s === s.value; })[0]; }), tb = $('#vcomp'); tb.textContent = '';
      var h = el('thead'), tr = el('tr'); tr.appendChild(el('th')); ps.forEach(function (p) { var th = el('th'); th.appendChild(el('a', { href: 'vertentes/' + p.s + '.html' }, p.n)); tr.appendChild(th); }); h.appendChild(tr); tb.appendChild(h);
      var bd = el('tbody');
      [['Estado', 'e'], ['Economia', 'm'], ['Liberdades', 'd'], ['Igualdade', 'q'], ['Pontos fortes ou apelo', 'forte'], ['Contradições', 'contra'], ['Referências', 'p'], ['Críticas', 'c']].forEach(function (c) { var l = el('tr'); l.appendChild(el('td', null, c[0])); ps.forEach(function (p) { var v = p[c[1]]; l.appendChild(el('td', null, Array.isArray(v) ? v.join(' ') : v)); }); bd.appendChild(l); });
      tb.appendChild(bd);
    };
    vs.forEach(function (s, i) { VD.forEach(function (x) { s.appendChild(el('option', { value: x.s }, x.n)); }); s.value = ini[i]; s.addEventListener('change', compV); });
    compV();
  }

  /* vieses */
  var vbz = $('#vieses');
  if (vbz) {
    var vbs = $$('.vies', vbz), vbg = $$('.grupo-vies', vbz), vbq = $('#vbq'), vbc = '', vbn = $('#vbc');
    var aplicaB = function () { var t = norm(vbq.value), n = 0; vbs.forEach(function (c) { var ok = (!vbc || c.dataset.c === vbc) && norm(c.textContent).indexOf(t) >= 0; c.hidden = !ok; if (ok) n++; }); ordena(vbz, vbs, t); vbg.forEach(function (g) { g.hidden = !$$('.vies', g).some(function (c) { return !c.hidden; }); }); vbn.textContent = n + (n === 1 ? ' viés' : ' vieses'); };
    vbq.addEventListener('input', aplicaB);
    $$('#vbf button').forEach(function (b) { b.addEventListener('click', function () { vbc = b.dataset.c; $$('#vbf button').forEach(function (o) { o.setAttribute('aria-pressed', o === b); }); aplicaB(); }); });
    aplicaB();
  }

  /* como votaram e comparador */
  function trilho(v) {
    var s = v.s || 0, n = v.n || 0, o = v.o || 0, t = s + n + o, d = el('span', { class: 'vtrilho' });
    if (t) [['vs', s], ['vn', n], ['vo', o]].forEach(function (x) { if (x[1]) { var i = el('i', { class: x[0] }); i.style.width = (x[1] / t * 100) + '%'; d.appendChild(i); } });
    return d;
  }
  var dv = $('#dados-votos');
  if (dv) {
    var V = JSON.parse(dv.textContent), sel = $('#vot'), lb = $('#lista-votos'), de = $('#vot-desc');
    if (sel) {
      V.votos.forEach(function (v, i) { sel.appendChild(el('option', { value: i }, v.rot + ' (' + v.ano + ')')); });
      var mostraV = function () {
        var v = V.votos[sel.value]; lb.textContent = '';
        var tt = v.tot; de.textContent = v.desc + ' Total na Câmara: ' + (tt.s || 0) + ' a favor, ' + (tt.n || 0) + ' contra. Votação de ' + v.data + '.';
        var ps = Object.keys(v.p).map(function (k) { return [k, v.p[k]]; }).sort(function (a, b) { var f = function (x) { var t = (x.s || 0) + (x.n || 0); return t ? (x.s || 0) / t : 0; }; return f(b[1]) - f(a[1]); });
        ps.forEach(function (x) { var l = el('div', { class: 'vbar' }), id = V.ids[x[0]]; l.appendChild(id ? el('a', { href: base + 'partidos/' + id + '.html' }, x[0]) : el('span', null, x[0])); l.appendChild(trilho(x[1])); l.appendChild(el('span', null, (x[1].s || 0) + ' × ' + (x[1].n || 0))); lb.appendChild(l); });
      };
      sel.addEventListener('change', mostraV); mostraV();
    }
    var a = $('#pa'), b = $('#pb'), cc = $('#pc');
    if (a) {
      var U = new URLSearchParams(location.search), sels = [a, b, cc], def = [U.get('a') || 'pt', U.get('b') || 'pl', U.get('c') || ''];
      sels.forEach(function (s, i) { if (i === 2) s.appendChild(el('option', { value: '' }, 'Nenhum')); V.partidos.forEach(function (p) { s.appendChild(el('option', { value: p.id }, p.s)); }); s.value = def[i]; s.addEventListener('change', comp); });
      function comp() {
        var ps = sels.map(function (s) { return V.partidos.filter(function (p) { return p.id === s.value; })[0]; }).filter(Boolean), tb = $('#comp');
        tb.textContent = '';
        var cab = el('tr'); cab.appendChild(el('th')); ps.forEach(function (p) { var th = el('th'); th.appendChild(el('a', { href: base + 'partidos/' + p.id + '.html' }, p.s)); cab.appendChild(th); }); var th = el('thead'); th.appendChild(cab); tb.appendChild(th);
        var body = el('tbody');
        [['Espectro', 'esp'], ['Número', 'num'], ['Fundação', 'ano'], ['Presidente', 'pres'], ['Federação', 'fed'], ['Valores', 'val'], ['Como mudou', 'ali']].forEach(function (c) { var tr = el('tr'); tr.appendChild(el('td', null, c[0])); ps.forEach(function (p) { tr.appendChild(el('td', null, p[c[1]] || '—')); }); body.appendChild(tr); });
        V.votos.forEach(function (v) { var tr = el('tr'); tr.appendChild(el('td', null, v.rot + ' (' + v.ano + ')')); ps.forEach(function (p) { var cod = p.vot.filter(function (k) { return v.p[k]; })[0], x = cod && v.p[cod], td = el('td'); if (x) { td.appendChild(trilho(x)); td.appendChild(el('small', null, (x.s || 0) + ' a favor, ' + (x.n || 0) + ' contra')); } else td.textContent = 'Sem bancada'; tr.appendChild(td); }); body.appendChild(tr); });
        tb.appendChild(body);
      }
      comp();
    }
  }

  /* teste de troca */
  var tr = $('#troca');
  if (tr) {
    var C = JSON.parse($('#dados-troca').textContent), ct = 0, r1 = null;
    var cena = $('.cena', tr), ops = $('.ops', tr), msg = $('.fb', tr), prox2 = $('.prox-q', tr);
    function etapa(lado) {
      var c = C[ct]; cena.textContent = c[0].replace('{a}', lado === 0 ? 'Um político que você admira' : 'Um político que você rejeita');
      ops.textContent = ''; msg.textContent = ''; prox2.hidden = true;
      [c[1], c[2]].forEach(function (o, i) {
        var b = el('button', { type: 'button' }, o);
        b.addEventListener('click', function () {
          if (lado === 0) { r1 = i; etapa(1); return; }
          msg.textContent = r1 === i ? 'Você julgou os dois do mesmo jeito. Boa coerência: é isso que o teste procura.' : 'Você julgou o mesmo ato de duas formas. É assim que o raciocínio motivado funciona, e acontece com todo mundo.';
          $$('button', ops).forEach(function (x) { x.disabled = true; }); prox2.hidden = false;
        });
        ops.appendChild(b);
      });
    }
    prox2.addEventListener('click', function () { ct = (ct + 1) % C.length; etapa(0); });
    etapa(0);
  }

  /* ficha */
  var fi = $('#ficha');
  if (fi) {
    var nm = $('#ficha-nome'), key = function () { return 'ppi-ficha-' + norm(nm.value || 'geral'); }, cx = $$('input[type=checkbox]', fi), pr = $('#ficha-prog');
    var conta = function () { var n = cx.filter(function (c) { return c.checked; }).length; $('i', pr).style.width = (n / cx.length * 100) + '%'; $('#ficha-t').textContent = n + ' de ' + cx.length + ' itens'; };
    var carrega = function () { var d = ler(key(), []); cx.forEach(function (c, i) { c.checked = d.indexOf(i) >= 0; }); conta(); };
    cx.forEach(function () {}); cx.forEach(function (c) { c.addEventListener('change', function () { grava(key(), cx.map(function (x, i) { return x.checked ? i : -1; }).filter(function (i) { return i >= 0; })); conta(); }); });
    nm.addEventListener('change', carrega); carrega();
    $('#ficha-limpa').addEventListener('click', function () { cx.forEach(function (c) { c.checked = false; }); grava(key(), []); conta(); });
  }

  /* simulador de cadeiras */
  var sim = $('#sim');
  if (sim) {
    var ins = $$('input[data-p]', sim), cad = $('#cad'), out = $('#sim-res');
    var calc = function () {
      var vagas = Math.max(1, +cad.value || 1), vs = ins.map(function (i) { return Math.max(0, +i.value || 0); }), tot = vs.reduce(function (a, b) { return a + b; }, 0);
      out.textContent = ''; if (!tot) return;
      var qe = Math.round(tot / vagas), ass = vs.map(function (v) { return Math.floor(v / qe); }), usados = ass.reduce(function (a, b) { return a + b; }, 0);
      while (usados < vagas) { var m = -1, mi = 0; vs.forEach(function (v, i) { var r = v / (ass[i] + 1); if (r > m) { m = r; mi = i; } }); ass[mi]++; usados++; }
      out.appendChild(el('p', null, 'Quociente eleitoral: ' + tot.toLocaleString('pt-BR') + ' votos ÷ ' + vagas + ' vagas = ' + qe.toLocaleString('pt-BR') + ' votos por cadeira.'));
      var cam = el('div', { class: 'camara', 'aria-hidden': 'true' }); ass.forEach(function (a, i) { for (var j = 0; j < a; j++) cam.appendChild(el('i', { class: 'cor' + i })); }); out.appendChild(cam);
      ass.forEach(function (a, i) { var p = el('p', { style: 'margin:.2em 0' }); p.appendChild(el('strong', null, ins[i].dataset.p + ': ')); p.appendChild(document.createTextNode(a + (a === 1 ? ' cadeira' : ' cadeiras') + ' (' + (vs[i] / tot * 100).toFixed(1).replace('.', ',') + '% dos votos)')); out.appendChild(p); });
    };
    ins.concat([cad]).forEach(function (i) { i.addEventListener('input', calc); }); calc();
  }

  /* voto preferencial */
  var pref = $('#pref');
  if (pref) {
    var G = JSON.parse($('#dados-pref').textContent), pi = $$('input', pref), s2 = $('#pref-res');
    var run = function () {
      var bl = G.map(function (g, i) { return { ordem: g.ordem, n: Math.max(0, +pi[i].value || 0) }; }), cand = ['Ana', 'Bruno', 'Clara'], tot = bl.reduce(function (a, b) { return a + b.n; }, 0);
      var pri = {}; cand.forEach(function (c) { pri[c] = 0; }); bl.forEach(function (b) { pri[b.ordem[0]] += b.n; });
      var ordem = cand.slice().sort(function (a, b) { return pri[b] - pri[a]; }), simples = ordem[0];
      var fica = ordem.slice(0, 2), rod = {}; fica.forEach(function (c) { rod[c] = 0; }); bl.forEach(function (b) { for (var i = 0; i < 3; i++) if (fica.indexOf(b.ordem[i]) >= 0) { rod[b.ordem[i]] += b.n; break; } });
      var venc = rod[fica[0]] >= rod[fica[1]] ? fica[0] : fica[1];
      s2.textContent = '';
      s2.appendChild(el('p', null, 'Com maioria simples, vence ' + simples + ' com ' + pri[simples] + ' de ' + tot + ' votos (' + cand.map(function (c) { return c + ': ' + pri[c]; }).join(', ') + ').'));
      s2.appendChild(el('p', null, 'Com voto preferencial, quem ficou em último (' + ordem[2] + ') sai da disputa, seus votos migram, e vence ' + venc + ' (' + fica.map(function (c) { return c + ': ' + rod[c]; }).join(', ') + ').'));
      s2.appendChild(el('p', { class: 'q' }, simples === venc ? 'Aqui, as duas regras dão o mesmo vencedor.' : 'A regra mudou o vencedor, com os mesmos eleitores.'));
    };
    pi.forEach(function (i) { i.addEventListener('input', run); }); run();
  }

  /* data das marcações (revisão espaçada) */
  if (marca) marca.addEventListener('click', function () { var tt = ler('ppi-lidas-t', {}); var id = marca.dataset.id; if (lidas.indexOf(id) >= 0) tt[id] = Date.now(); else delete tt[id]; grava('ppi-lidas-t', tt); });
  var rev = $('.revisao-esp');
  if (rev) {
    var tt2 = ler('ppi-lidas-t', {}), todas = $$('.cartao[data-licao]').filter(function (c) { return !c.closest('.revisao-esp'); });
    var lidasAqui = todas.filter(function (c) { return lidas.indexOf(c.dataset.licao) >= 0; });
    if (lidasAqui.length >= 3) {
      lidasAqui.sort(function (a, b) { return (tt2[a.dataset.licao] || 0) - (tt2[b.dataset.licao] || 0); });
      var rg = $('#rev-grade'); lidasAqui.slice(0, 3).forEach(function (c) { rg.appendChild(c.cloneNode(true)); });
      rev.hidden = false;
    }
  }

  /* teste do nível: dez perguntas sorteadas */
  var dtn = $('#dados-teste');
  if (dtn && $('#jogo')) {
    var TN = JSON.parse(dtn.textContent), its = TN.itens.slice().sort(function () { return Math.random() - .5; }).slice(0, TN.n);
    jogo($('#jogo'), its, function (x) { return x[1]; }, function (x) { return x[1][x[2]]; }, function (x) { return x[0]; }, function (x) { return x[3]; });
  }

  /* listas com filtro por grupo e busca (debates) */
  var lst = $('#lista');
  if (lst) {
    var lc = $$('.item', lst), lg = $$('.grupo-l', lst), lq = $('#fq'), lcnt = $('#contagem'), lf = {};
    var aplicaL = function () {
      var t = norm(lq ? lq.value : ''), n = 0;
      lc.forEach(function (c) { var ok = Object.keys(lf).every(function (k) { return !lf[k] || c.dataset[k] === lf[k]; }) && norm(c.textContent).indexOf(t) >= 0; c.hidden = !ok; if (ok) n++; });
      lg.forEach(function (g) { g.hidden = !$$('.item', g).some(function (c) { return !c.hidden; }); });
      if (lcnt) lcnt.textContent = n + (n === 1 ? ' item' : ' itens');
    };
    if (lq) lq.addEventListener('input', aplicaL);
    $$('.filtros button[data-k]').forEach(function (b) { b.addEventListener('click', function () { lf[b.dataset.k] = b.dataset.v; $$('.filtros button[data-k="' + b.dataset.k + '"]').forEach(function (o) { o.setAttribute('aria-pressed', o === b); }); aplicaL(); }); });
    aplicaL();
  }

  /* posição antes e depois, nos debates */
  var posB = $$('.posicao');
  if (posB.length) {
    var PP = ler('ppi-pos', {});
    posB.forEach(function (b) {
      var s = b.dataset.deb, dep = b.classList.contains('depois'), fb = $('.fb', b), bts = $$('button', b), k = dep ? 1 : 0;
      var pinta2 = function () { var cur = PP[s] || [null, null]; bts.forEach(function (x) { x.setAttribute('aria-pressed', String(x.dataset.v === cur[k])); }); };
      bts.forEach(function (x) {
        x.addEventListener('click', function () {
          var cur = PP[s] || [null, null]; cur[k] = x.dataset.v; PP[s] = cur; grava('ppi-pos', PP); pinta2();
          if (!dep) { fb.textContent = 'Registrado. Leia os dois lados e responda de novo no fim da página.'; return; }
          var a = cur[0];
          if (a === null) fb.textContent = 'Você não registrou a posição antes de ler. Da próxima vez, tente: comparar o antes e o depois é o exercício.';
          else if (a === x.dataset.v) fb.textContent = x.dataset.v === 'ns' ? 'Você continua sem posição. Pode ser que o debate esteja em aberto, ou que falte informação. Anote o que faria você decidir.' : 'Você manteve a posição. Pergunte-se: qual foi o melhor argumento do outro lado, e por que ele não bastou?';
          else fb.textContent = 'Você mudou de posição depois de ler. É o que a lição sobre mudar de ideia pede quando o argumento convence; vale checar se mudou por razão ou por cansaço.';
        });
      });
      pinta2();
      if (dep) { var c0 = (PP[s] || [null])[0]; if (c0 !== null) { var r = bts.filter(function (x) { return x.dataset.v === c0; })[0]; if (r) fb.textContent = 'Antes de ler, você pendia para: ' + r.textContent + '.'; } }
    });
  }

  /* minha posição política */
  var mpd = $('#dados-mp');
  if (mpd) {
    var MP = JSON.parse(mpd.textContent), sel = {}, salvo = ler('ppi-minha', {});
    var opc = function (id, lista, vazio) { var s = $('#' + id); s.appendChild(el('option', { value: '' }, vazio)); lista.forEach(function (o) { s.appendChild(el('option', { value: o[0] }, o[1])); }); if (salvo[id] && lista.some(function (o) { return o[0] === salvo[id]; })) s.value = salvo[id]; sel[id] = s; };
    opc('mp-econ', [['-90', 'Abolir a propriedade privada dos meios de produção'], ['-60', 'Muito Estado: planejar setores e redistribuir muito'], ['-30', 'Mais Estado: regular e redistribuir'], ['0', 'Equilíbrio: depende do setor'], ['30', 'Mais mercado: menos impostos e regras'], ['60', 'Muito mercado: Estado mínimo'], ['90', 'Nenhum Estado na economia: só contratos privados']], 'Economia');
    opc('mp-cost', [['-95', 'Ultraprogressista: libertação total, novas formas de família e de gênero, libertação animal'], ['-60', 'Progressista: ampliar direitos e liberdades'], ['-30', 'Moderadamente progressista'], ['0', 'Moderado: mudar com cautela'], ['30', 'Moderadamente conservador'], ['60', 'Conservador: preservar tradições e instituições'], ['95', 'Ultraconservador: impor pela lei uma moral tradicional, muitas vezes religiosa']], 'Costumes');
    opc('mp-lib', [['-80', 'O Estado não deve interferir na vida pessoal'], ['-40', 'Interferir pouco, só para evitar dano a outros'], ['0', 'Equilíbrio entre liberdade e ordem'], ['40', 'Ordem acima da liberdade, quando há conflito'], ['80', 'Autoridade forte: o Estado deve orientar a vida das pessoas']], 'Liberdade e autoridade');
    opc('mp-met', [['conservar', 'Conservar o que existe'], ['gradual', 'Reformar aos poucos, dentro das regras'], ['rapida', 'Reformas grandes e rápidas, dentro das regras'], ['ruptura', 'Ruptura: refazer o sistema do zero'], ['passado-recente', 'Voltar a como o país era há algumas décadas'], ['passado-antigo', 'Restaurar uma ordem antiga: monarquia, religião oficial, hierarquias tradicionais']], 'Rumo da mudança');
    opc('mp-dem', [['liberal', 'Democracia representativa com limites fortes'], ['direta', 'Mais democracia direta e participação'], ['epist', 'Mais peso a quem tem conhecimento'], ['forte', 'Um governo forte, com menos freios, resolve melhor'], ['sem-estado', 'Sem governo central: comunidades auto-organizadas']], 'Democracia');
    opc('mp-circ', [['familia', 'Minha família, minha comunidade e meu povo'], ['pais', 'Os cidadãos do meu país'], ['humanos', 'Todos os humanos, inclusive estrangeiros e futuros'], ['sencientes', 'Todos os que podem sofrer, inclusive animais'], ['vida', 'Toda a vida e os ecossistemas']], 'Quem conta');
    var saida = $('#mp-saida');
    var V = function (s) { return MP.vert.filter(function (t) { return t.s === s; })[0]; };
    var link = function (p, s, txt) { var t = V(s); return t ? el('a', { href: base + 'vertentes/' + s + '.html' }, txt || t.n) : null; };
    var licao = function (s, txt) { return el('a', { href: base + s + '.html' }, txt); };
    var bloco = function (partes) { var p = el('p'); partes.forEach(function (x) { if (x) p.appendChild(typeof x === 'string' ? document.createTextNode(x) : x); }); return p; };
    var lista = function (rotulo, slugs) { var ps = [rotulo]; slugs.filter(V).forEach(function (s, i) { if (i) ps.push(', '); ps.push(link(null, s)); }); ps.push('.'); return ps; };
    var monta = function () {
      var v = {}; Object.keys(sel).forEach(function (k) { v[k] = sel[k].value; }); grava('ppi-minha', v); saida.textContent = '';
      if (!Object.keys(v).some(function (k) { return v[k]; })) { saida.appendChild(el('p', { class: 'nota' }, 'Escolha as opções acima. O resultado aparece aqui e fica salvo no seu navegador.')); return; }
      var nota = el('div', { class: 'nota' });
      var econ = +v['mp-econ'] || 0, cost = +v['mp-cost'] || 0, lib = v['mp-lib'] === '' ? 0 : +v['mp-lib'];
      var ajM = { conservar: 0, gradual: -5, rapida: 0, ruptura: 15, 'passado-recente': 10, 'passado-antigo': 25 }[v['mp-met']] || 0;
      var ajD = { liberal: -10, direta: -15, epist: 10, forte: 35, 'sem-estado': -40 }[v['mp-dem']] || 0;
      var x = Math.max(-100, Math.min(100, .75 * econ + .25 * cost)), y = Math.max(-100, Math.min(100, lib + ajM + ajD));
      var perto = MP.vert.map(function (t) { return { t: t, d: Math.hypot(t.x - x, t.y - y) }; }).sort(function (a, b) { return a.d - b.d; }).slice(0, 3);
      var ps = ['No mapa das vertentes (economia na horizontal, liberdade e autoridade na vertical), sua posição fica mais perto de: '];
      perto.forEach(function (q, i) { if (i) ps.push(', '); ps.push(link(null, q.t.s)); }); ps.push('. O mapa é aproximado: ele mede eixos, não todas as suas ideias.');
      nota.appendChild(bloco(ps));
      /* extremos de costumes */
      if (v['mp-cost'] === '-95') {
        nota.appendChild(bloco(['No extremo progressista estão propostas como reconhecer em lei o poliamor e outras formas de família, retirar o gênero dos documentos, descriminalizar drogas e trabalho sexual e acabar com a exploração de animais. Esta última é o centro do sencientismo, para o qual todo ser que sente conta, de qualquer espécie: veja ', link(null, 'senciocracia'), ' e a lição sobre ', licao('politica-baseada-na-senciencia', 'política baseada na senciência'), '. A lição sobre ', licao('critica-ao-identitarismo', 'a crítica ao identitarismo'), ' mostra o que esse campo acerta e onde é criticado.']));
        nota.appendChild(bloco(lista('Vertentes desse campo: ', ['senciocracia', 'progressismo', 'feminismo', 'anarquismo'])));
      }
      if (v['mp-cost'] === '95') {
        nota.appendChild(bloco(['No extremo conservador estão propostas como proibir o aborto em qualquer caso, rever o casamento entre pessoas do mesmo sexo, tornar obrigatório o ensino religioso e dar à moral religiosa força de lei. A lição sobre ', licao('perigo-do-ultraconservadorismo', 'o perigo do ultraconservadorismo'), ' separa o que vale preservar do que impede corrigir injustiças, e a sobre ', licao('religiao-e-estado', 'religião e Estado'), ' discute o limite da laicidade.']));
        nota.appendChild(bloco(lista('Vertentes desse campo: ', ['ultraconservadorismo', 'tradicionalismo', 'teocracia'])));
      }
      /* voltar ao passado */
      if (v['mp-met'] === 'passado-recente' || v['mp-met'] === 'passado-antigo') {
        nota.appendChild(bloco(['Querer voltar a uma época passada, desfazendo mudanças, é a marca do reacionarismo, diferente do conservadorismo, que quer preservar o presente e mudar devagar. ', v['mp-met'] === 'passado-antigo' ? 'Restaurar uma ordem antiga, com monarquia, religião oficial ou hierarquias tradicionais, é a versão mais radical. ' : 'Voltar algumas décadas costuma vir com a ideia de uma era de ouro de ordem e respeito. ', 'A lição sobre ', licao('perigo-do-reacionarismo', 'o perigo do reacionarismo'), ' pergunta para quem aquela época era boa.']));
        nota.appendChild(bloco(lista('Vertentes desse campo: ', v['mp-met'] === 'passado-antigo' ? ['reacionarismo', 'monarquismo', 'tradicionalismo', 'integralismo'] : ['reacionarismo', 'tradicionalismo', 'conservadorismo'])));
        if (cost < 0) nota.appendChild(bloco(['Você combinou costumes progressistas com voltar ao passado, uma combinação rara. Talvez queira restaurar algo específico, como direitos trabalhistas ou um Estado maior na economia; o rótulo de reacionário cabe mal a isso.']));
      }
      if (v['mp-met'] === 'ruptura') nota.appendChild(bloco(['Você escolheu refazer o sistema. A lição sobre ', licao('perigo-das-revolucoes', 'o perigo das revoluções'), ' lista as perguntas a fazer antes: que limites o novo poder terá, e quem poderá tirá-lo se der errado?']));
      if (v['mp-met'] === 'conservar' && cost <= 0) nota.appendChild(bloco(['Conservar o que existe com costumes moderados ou progressistas é uma posição de cautela, que o ', link(null, 'centrismo'), ' e parte do ', link(null, 'conservadorismo'), ' compartilham.']));
      /* democracia e autoridade */
      var td = { liberal: 'Sobre a democracia, você fica com a representativa de limites fortes: tribunais, imprensa e oposição como freios ao vencedor.', direta: 'Você quer mais participação direta; a lição sobre democracia direta e epistocracia mostra o que isso ganha e arrisca.', epist: 'Você daria mais peso a quem sabe mais; a objeção principal é que quem define o saber captura o poder.', forte: 'Você aceitaria um governo forte com menos freios; a lição sobre o perigo de questionar a democracia e a história das ditaduras na América do Sul são o contraponto a ler.', 'sem-estado': 'Você dispensaria o governo central, como os anarquistas de esquerda e os anarcocapitalistas de direita, que discordam sobre quase tudo menos isso.' };
      if (v['mp-dem']) nota.appendChild(bloco([td[v['mp-dem']]]));
      if (v['mp-dem'] === 'sem-estado') nota.appendChild(bloco(lista('Vertentes desse campo: ', econ > 0 ? ['anarcocapitalismo', 'libertarianismo'] : ['anarquismo', 'anarcocomunismo', 'mutualismo'])));
      if (v['mp-dem'] === 'forte' || lib >= 80) nota.appendChild(bloco(lista('Vertentes que defenderam governo forte: ', econ < 0 ? ['autoritarismo', 'marxismo-leninismo', 'populismo'] : ['autoritarismo', 'militarismo-autoritario', 'nacionalismo'])));
      /* quem conta */
      var tc = { familia: 'Sobre quem conta, você começa pelos seus. Deveres especiais com família e comunidade são legítimos; a lição sobre o perigo do tribalismo mostra quando eles viram desprezo pelos de fora.', pais: 'Sobre quem conta, você para nos cidadãos do seu país: as lições sobre culpar o estrangeiro e sobre imparcialidade testam essa fronteira.', humanos: 'Sobre quem conta, você inclui todos os humanos: a lição sobre sencientismo pergunta se a fronteira da espécie é tão diferente das outras.', sencientes: 'Sobre quem conta, você inclui todos os que sofrem: a lição sobre política baseada na senciência mostra o que isso muda em leis e orçamentos.', vida: 'Sobre quem conta, você inclui toda a vida e os ecossistemas. A crítica sencientista pergunta se um ecossistema conta por si ou pelos seres que sentem nele.' };
      if (v['mp-circ']) { nota.appendChild(bloco([tc[v['mp-circ']]])); if (v['mp-circ'] === 'sencientes') nota.appendChild(bloco(lista('Vertente ligada: ', ['senciocracia']))); if (v['mp-circ'] === 'vida') nota.appendChild(bloco(lista('Vertentes ligadas: ', ['ambientalismo', 'ecossocialismo']))); }
      saida.appendChild(nota);
      var temas = []; if (v['mp-econ']) temas.push('Economia e Estado'); if (v['mp-cost']) temas.push('Direitos e costumes'); if (v['mp-circ'] === 'sencientes' || v['mp-circ'] === 'vida') temas.push('Ambiente e animais'); if (v['mp-dem'] || v['mp-lib']) temas.push('Instituições');
      var ds = []; temas.forEach(function (t) { (MP.deb[t] || []).slice(0, 2).forEach(function (d) { ds.push(d); }); });
      if (ds.length) { var h = el('p', null, 'Debates que testam essa posição: '); ds.forEach(function (d, i) { if (i) h.appendChild(document.createTextNode(', ')); h.appendChild(el('a', { href: base + 'debates/' + d[0] + '.html' }, d[1])); }); h.appendChild(document.createTextNode('.')); saida.appendChild(h); }
    };
    Object.keys(sel).forEach(function (k) { sel[k].addEventListener('change', monta); }); monta();
  }

  /* glossário: toque abre a definição */
  function posGl(g) { var r = g.getBoundingClientRect(), vw = document.documentElement.clientWidth, w = Math.min(320, vw - 32); g.style.setProperty('--gl-w', w + 'px'); g.style.setProperty('--gl-x', Math.min(0, vw - 16 - r.left - w) + 'px'); }
  function fechaGl() { $$('.gl.ativo').forEach(function (o) { o.classList.remove('ativo'); o.blur(); }); }
  $$('.gl').forEach(function (g) {
    g.addEventListener('mouseenter', function () { posGl(g); });
    g.addEventListener('focus', function () { posGl(g); });
    g.addEventListener('click', function (ev) { ev.stopPropagation(); posGl(g); var on = g.classList.contains('ativo'); fechaGl(); if (!on) g.classList.add('ativo'); });
  });
  document.addEventListener('click', fechaGl);
  var posTodos = function () { $$('.gl').forEach(posGl); };
  posTodos(); window.addEventListener('resize', posTodos);
  document.addEventListener('keydown', function (ev) { if (ev.key === 'Escape') fechaGl(); });
})();

/* home: mede a altura das barras acima da capa para que ela ocupe a primeira tela (CSS usa --topo-capa) */
(function () {
  var c = document.querySelector('.capa'); if (!c) return;
  function mede() { document.documentElement.style.setProperty('--topo-capa', Math.round(c.getBoundingClientRect().top + window.scrollY) + 'px'); }
  mede(); window.addEventListener('load', mede); window.addEventListener('resize', mede);
})();

/* barra da página: ouvir (voz em pt-BR), como citar e imprimir ou PDF, adaptado do Questão de Ética */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
  var acoes = $('.acoes-cap'), raiz = $('.leitura');
  if (!acoes || !raiz) return;
  var dlg = null;
  function modal(titulo, html) {
    if (!dlg) {
      dlg = document.createElement('dialog'); dlg.className = 'janela';
      dlg.innerHTML = '<div class="jan-cab"><h2></h2><button type="button" class="jan-x" aria-label="Fechar">×</button></div><div class="jan-corpo"></div>';
      document.body.appendChild(dlg);
      $('.jan-x', dlg).addEventListener('click', function () { dlg.close(); });
      dlg.addEventListener('click', function (ev) { if (ev.target === dlg) dlg.close(); });
    }
    $('h2', dlg).textContent = titulo; $('.jan-corpo', dlg).innerHTML = html;
    if (dlg.showModal) dlg.showModal(); else dlg.setAttribute('open', '');
    return $('.jan-corpo', dlg);
  }
  function copiar(txt, btn) {
    var ok = function () { if (btn) { var o = btn.textContent; btn.textContent = 'Copiado ✓'; setTimeout(function () { btn.textContent = o; }, 1600); } };
    if (navigator.clipboard) navigator.clipboard.writeText(txt).then(ok, function () {});
    else { var t = document.createElement('textarea'); t.value = txt; document.body.appendChild(t); t.select(); try { document.execCommand('copy'); ok(); } catch (x) {} t.parentNode.removeChild(t); }
  }

  /* ----- imprimir: abre as gavetas fechadas antes de imprimir e as devolve depois ----- */
  window.addEventListener('beforeprint', function () { $$('details', raiz).forEach(function (d) { d.dataset.antes = d.open ? '1' : ''; d.open = true; }); });
  window.addEventListener('afterprint', function () { $$('details', raiz).forEach(function (d) { d.open = d.dataset.antes === '1'; }); });
  $('[data-acao="imprimir"]', acoes).addEventListener('click', function () { window.print(); });

  /* ----- como citar ----- */
  var MES = ['jan.', 'fev.', 'mar.', 'abr.', 'maio', 'jun.', 'jul.', 'ago.', 'set.', 'out.', 'nov.', 'dez.'];
  $('[data-acao="citar"]', acoes).addEventListener('click', function () {
    var d = new Date(), hoje = d.getDate() + ' ' + MES[d.getMonth()] + ' ' + d.getFullYear();
    var abnt = (acoes.dataset.abnt || '').replace('{ACESSO}', hoje), apa = acoes.dataset.apa || '';
    var limpo = function (h) { var t = document.createElement('div'); t.innerHTML = h; return t.textContent; };
    var c = modal('Como citar esta página', '<p class="fino">Referência da página, com o link e a data de acesso de hoje. Confira as normas exigidas pela sua instituição.</p>' +
      '<div class="cit-bloco"><p class="cit-ti">ABNT</p><p class="cit-txt">' + abnt + '</p><button type="button" class="btn alt" data-c="abnt">Copiar ABNT</button></div>' +
      '<div class="cit-bloco"><p class="cit-ti">APA</p><p class="cit-txt">' + apa + '</p><button type="button" class="btn alt" data-c="apa">Copiar APA</button></div>');
    $('[data-c="abnt"]', c).addEventListener('click', function () { copiar(limpo(abnt), this); });
    $('[data-c="apa"]', c).addEventListener('click', function () { copiar(limpo(apa), this); });
  });

  /* ----- ouvir ----- */
  var bOuvir = $('[data-acao="ouvir"]', acoes);
  if (!('speechSynthesis' in window)) { bOuvir.hidden = true; return; }
  var synth = window.speechSynthesis, fila = [], pos = 0, tocando = false, vel = 1, atual = null;
  var bParar = document.createElement('button'); bParar.type = 'button'; bParar.innerHTML = '<span aria-hidden="true">■</span> Parar'; bParar.hidden = true;
  var bVel = document.createElement('button'); bVel.type = 'button'; bVel.textContent = '1×'; bVel.title = 'Velocidade da leitura'; bVel.hidden = true;
  bOuvir.after(bParar, bVel);
  /* escolhe uma voz em português do Brasil; as vozes chegam depois do carregamento em vários navegadores */
  var vozPt = null;
  var escolheVoz = function () {
    var vs = synth.getVoices(); if (!vs.length) return;
    var nota = function (v) {
      var l = (v.lang || '').replace('_', '-').toLowerCase(), n = (v.name || '').toLowerCase();
      if (l !== 'pt-br' && !/portugu[eê]s.*brasil|brazil/.test(n)) return l.indexOf('pt') === 0 ? 1 : 0;
      return 10 + (/natural|online|neural/.test(n) ? 4 : 0) + (/google/.test(n) ? 3 : 0) + (/microsoft/.test(n) ? 2 : 0) + (v.localService ? 0 : 1);
    };
    var melhor = vs.map(function (v) { return [nota(v), v]; }).filter(function (x) { return x[0] > 0; }).sort(function (a, b) { return b[0] - a[0]; })[0];
    vozPt = melhor ? melhor[1] : null;
  };
  escolheVoz();
  if ('onvoiceschanged' in synth) synth.addEventListener('voiceschanged', escolheVoz);
  var voz = function () { if (!vozPt) escolheVoz(); return vozPt; };
  /* o que é lido: o texto da coluna de leitura, sem quizzes, fontes, índices, enquetes, botões e tabelas */
  var PULA = '.quiz, .fontes, .pager, .nota.cruzada, .marcar, .toc, .toc-caixa, .posicao, .links-d, .legenda, table, button, nav';
  var monta = function () {
    fila = [];
    $$('h2, h3, h4, p, li, blockquote, dt, dd', raiz).forEach(function (b) {
      if (b.closest(PULA)) return;
      if (b.tagName === 'LI' && b.querySelector('p, li')) return; /* evita ler duas vezes */
      var c = b.cloneNode(true); $$('sup, button', c).forEach(function (s) { s.parentNode.removeChild(s); });
      var t = c.textContent.replace(/\s+/g, ' ').trim(); if (!t) return;
      (t.match(/[^.!?;]+[.!?;]*\s*/g) || [t]).reduce(function (acc, f) {
        if (acc.length && (acc[acc.length - 1] + f).length < 220) acc[acc.length - 1] += f; else acc.push(f);
        return acc;
      }, []).forEach(function (pedaco) { fila.push([b, pedaco]); });
    });
  };
  var marca = function (b) {
    if (atual) atual.classList.remove('lendo');
    atual = b; if (!b) return; b.classList.add('lendo');
    var r = b.getBoundingClientRect(); if (r.top < 80 || r.bottom > innerHeight) b.scrollIntoView({ block: 'center', behavior: 'smooth' });
  };
  var fala = function () {
    if (pos >= fila.length) { para(); return; }
    var it = fila[pos], u = new SpeechSynthesisUtterance(it[1]);
    var v = voz(); if (v) { u.voice = v; u.lang = v.lang; } else u.lang = 'pt-BR'; u.rate = vel;
    u.onend = function () { if (!tocando) return; pos++; fala(); };
    marca(it[0]); synth.speak(u);
  };
  var estado = function () {
    bOuvir.setAttribute('aria-pressed', String(tocando));
    bOuvir.innerHTML = tocando ? '<span aria-hidden="true">❚❚</span> Pausar' : '<span aria-hidden="true">▶</span> ' + (pos > 0 ? 'Continuar' : 'Ouvir');
    bParar.hidden = bVel.hidden = !(tocando || pos > 0);
  };
  var para = function () { tocando = false; synth.cancel(); pos = 0; marca(null); estado(); };
  bOuvir.addEventListener('click', function () {
    if (!tocando && !voz() && !bOuvir.dataset.avisou) {
      bOuvir.dataset.avisou = '1';
      modal('Voz em português não encontrada', '<p>Seu navegador ou sistema não tem uma voz em português do Brasil instalada, então a leitura pode sair com sotaque de outra língua.</p><p class="fino">No Windows: Configurações → Hora e idioma → Fala → Adicionar vozes → Português (Brasil). No Android e no iPhone, a voz em português costuma vir nas configurações de acessibilidade ou de texto para fala. O Chrome e o Edge já trazem vozes em português na maioria dos computadores.</p>');
    }
    if (tocando) { tocando = false; synth.cancel(); estado(); return; }
    if (!fila.length) monta();
    tocando = true; estado(); fala();
  });
  bParar.addEventListener('click', para);
  bVel.addEventListener('click', function () {
    var vs = [1, 1.25, 1.5, 0.85]; vel = vs[(vs.indexOf(vel) + 1) % vs.length]; bVel.textContent = String(vel).replace('.', ',') + '×';
    if (tocando) { synth.cancel(); setTimeout(fala, 60); }
  });
  window.addEventListener('pagehide', function () { synth.cancel(); });
})();
