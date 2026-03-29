"""Generate Shakespearean sonnets using Queneau assembly.

Demonstrates Assembler for recombining lines from Shakespeare's sonnets
into new poems.
"""
from lolipy import corpora
from lolipy.queneau import Assembler

sonnets = corpora.words.literature.shakespeare_sonnets['sonnets']
corpus = Assembler.loadlist(sonnets, tokens_in='lines')

for i in range(3):
    print("\n".join(line for line, source in corpus.assemble('0.l')))
    print()
