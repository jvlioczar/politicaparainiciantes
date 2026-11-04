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
})();
