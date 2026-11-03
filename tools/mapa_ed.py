"""Mapa esquerda e direita. x: -100 esquerda, 100 direita. y: -100 reforma gradual, 100 ruptura. São posições aproximadas e editoriais."""
ED = {
 'marxismo-leninismo': (-88, 92), 'maoismo': (-75, 84), 'extrema-esquerda': (-90, 76), 'trotskismo': (-72, 68), 'comunismo': (-92, 60), 'anarcocomunismo': (-70, 52), 'marxismo': (-88, 44), 'anarcossindicalismo': (-66, 36), 'anarquismo': (-86, 28),
 'mutualismo': (-55, 18), 'ecossocialismo': (-58, 6), 'teologia-da-libertacao': (-60, -6), 'socialismo-democratico': (-65, -18), 'feminismo': (-50, -30), 'progressismo': (-62, -40), 'lulismo': (-44, -50), 'trabalhismo': (-66, -56), 'desenvolvimentismo': (-45, -64), 'social-democracia': (-50, -74),
 'ambientalismo': (-35, -20), 'sencientismo': (-30, -6), 'senciocracia': (-22, 8), 'cosmopolitismo': (-28, -42), 'social-liberalismo': (-18, -70), 'comunitarismo': (-6, -60), 'centrismo': (0, -88), 'petismo-e-antipetismo': (-8, -28),
 'totalitarismo': (-6, 96), 'autoritarismo': (0, 80), 'populismo': (-4, 40), 'nacionalismo': (20, 30),
 'nazismo': (92, 97), 'fascismo': (78, 90), 'extrema-direita': (94, 83), 'militarismo-autoritario': (72, 76), 'integralismo': (92, 69), 'direita-radical': (74, 62), 'ultranacionalismo': (94, 55), 'teocracia': (76, 48), 'reacionarismo': (94, 41), 'ultraconservadorismo': (74, 34), 'bolsonarismo': (92, 27), 'anarcocapitalismo': (70, 20), 'monarquismo': (92, 13), 'tradicionalismo': (72, 6), 'libertarianismo': (92, -2), 'neoconservadorismo': (72, -12), 'conservadorismo': (70, -30), 'liberal-conservadorismo': (88, -38), 'neoliberalismo': (66, -48), 'liberalismo-classico': (52, -58), 'democracia-crista': (40, -68),
}

def espalhar(gap=3.6):
    """Dá a cada corrente uma linha própria, para os rótulos não se sobreporem, com o mínimo de deslocamento."""
    ordem = sorted(ED, key=lambda s: -ED[s][1]); ys = [ED[s][1] for s in ordem]
    for i in range(1, len(ys)): ys[i] = min(ys[i], ys[i - 1] - gap)
    if ys[-1] < -98: ys[-1] = -98
    for i in range(len(ys) - 2, -1, -1): ys[i] = max(ys[i], ys[i + 1] + gap)
    for s, y in zip(ordem, ys): ED[s] = (ED[s][0], round(y, 1))
espalhar()
