"""Ilustrações geométricas do site, feitas só de círculos e retângulos com gradiente."""
DEFS = '''<defs>
<linearGradient id="gC" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f7b267"/><stop offset="1" stop-color="#ef5d7a"/></linearGradient>
<linearGradient id="gV" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f4d06f"/><stop offset="1" stop-color="#3fb98a"/></linearGradient>
<linearGradient id="gA" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6fb1ec"/><stop offset="1" stop-color="#7a5be0"/></linearGradient>
<linearGradient id="gL" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f6c3a0"/><stop offset="1" stop-color="#ea8a9c"/></linearGradient>
</defs>'''
def q(x, y, r, c, f):
    """Quarto de círculo com o centro em (x, y). c: ne, no, se, so."""
    a, b = {'ne': (1, -1), 'no': (-1, -1), 'se': (1, 1), 'so': (-1, 1)}[c]
    return f'<path d="M{x} {y}L{x + a * r} {y}A{r} {r} 0 0 {1 if a * b > 0 else 0} {x} {y + b * r}Z" fill="url(#{f})"/>'
def r(x, y, w, h, f, rx=0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="url(#{f})"/>'
def c(x, y, s, f):
    return f'<circle cx="{x}" cy="{y}" r="{s}" fill="url(#{f})"/>'
def meio(x, y, s, f, cima=True):
    d = 1 if cima else 0
    return f'<path d="M{x - s} {y}A{s} {s} 0 0 {d} {x + s} {y}Z" fill="url(#{f})"/>'
def hero():
    # Congresso Nacional: câmara (tigela), torres, senado (cúpula) e plataforma
    p = [DEFS, r(278, 40, 36, 300, 'gA', 3), r(326, 40, 36, 300, 'gA', 3), r(278, 150, 84, 15, 'gL', 2)]
    p += [meio(140, 228, 112, 'gC', cima=False), meio(500, 340, 100, 'gV', cima=True)]
    p += [r(20, 340, 600, 24, 'gA', 4), r(70, 364, 500, 16, 'gL', 3)]
    return f'<svg class="arte" viewBox="10 25 620 365" role="img" aria-label="Ilustração geométrica do Congresso Nacional">{"".join(p)}</svg>'

def _ic(body, gid=''):
    return f'<svg class="ico" viewBox="0 0 64 64" aria-hidden="true"><use href="#defs-arte"/>{body}</svg>'
ICONES = {
 'cargo': lambda: c(32, 18, 10, 'gC') + q(32, 54, 24, 'no', 'gA') + q(32, 54, 24, 'ne', 'gV'),
 'valor': lambda: r(8, 26, 48, 6, 'gA', 2) + r(29, 12, 6, 42, 'gA', 2) + meio(16, 34, 11, 'gC', cima=False) + meio(48, 34, 11, 'gV', cima=False),
 'compara': lambda: r(8, 14, 21, 40, 'gC', 4) + r(35, 8, 21, 46, 'gV', 4),
 'votos': lambda: r(8, 30, 11, 24, 'gC', 2) + r(26, 18, 11, 36, 'gA', 2) + r(44, 8, 11, 46, 'gV', 2),
 'arvore': lambda: c(32, 13, 8, 'gA') + c(14, 48, 8, 'gC') + c(50, 48, 8, 'gV') + r(30, 20, 4, 16, 'gA') + r(14, 34, 36, 4, 'gA') + r(12, 36, 4, 6, 'gC') + r(48, 36, 4, 6, 'gV'),
 'troca': lambda: q(30, 30, 22, 'no', 'gC') + q(34, 34, 22, 'se', 'gA'),
 'ficha': lambda: r(12, 6, 40, 52, 'gL', 5) + r(19, 18, 26, 4, 'gA') + r(19, 28, 26, 4, 'gA') + r(19, 38, 16, 4, 'gA'),
 'cadeira': lambda: ''.join(c(14 + 12 * (i % 4), 16 + 12 * (i // 4), 5, ['gC', 'gA', 'gV'][i % 3]) for i in range(12)),
 'livro': lambda: r(9, 10, 21, 44, 'gC', 3) + r(34, 10, 21, 44, 'gV', 3),
 'urna': lambda: r(10, 26, 44, 30, 'gC', 4) + r(23, 8, 18, 24, 'gV', 2) + r(20, 32, 24, 3, 'gL'),
}
def icone(n):
    return f'<svg class="ico" viewBox="0 0 64 64" aria-hidden="true">{DEFS.replace("gC", "gC" + n).replace("gV", "gV" + n).replace("gA", "gA" + n).replace("gL", "gL" + n)}{ICONES[n]().replace("#gC", "#gC" + n).replace("#gV", "#gV" + n).replace("#gA", "#gA" + n).replace("#gL", "#gL" + n)}</svg>'
LOGO = '<svg viewBox="0 0 40 40" width="34" height="34" aria-hidden="true"><defs><linearGradient id="lgA" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#ef5d7a"/><stop offset="1" stop-color="#f7b267"/></linearGradient><linearGradient id="lgB" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#3fb98a"/><stop offset="1" stop-color="#f4d06f"/></linearGradient><linearGradient id="lgC" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#7a5be0"/><stop offset="1" stop-color="#6fb1ec"/></linearGradient></defs><rect x="5" y="23" width="8" height="13" rx="2" fill="url(#lgB)"/><rect x="16" y="14" width="8" height="22" rx="2" fill="url(#lgA)"/><rect x="27" y="5" width="8" height="31" rx="2" fill="url(#lgC)"/></svg>'
