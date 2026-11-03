"""Seção "Como funciona e como se proteger" de cada viés: reúne os quatro lotes por categoria. Chave: slug; valor: parágrafos separados por quebra de linha."""
from vieses_fundo_a import FA
from vieses_fundo_b import FB
from vieses_fundo_c import FC
from vieses_fundo_d import FD
F = {**FA, **FB, **FC, **FD}
assert len(F) == len(FA) + len(FB) + len(FC) + len(FD), 'slug repetido entre os lotes'
