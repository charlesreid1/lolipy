"""Generate names and IAU citations for fictional minor planets.

Demonstrates Queneau assembly on sentences combined with WordAssembler
for generating new names.
"""
import textwrap
from olipy import corpora
from olipy.queneau import Assembler, WordAssembler

asteroids = corpora.science.minor_planet_details["minor_planets"]
corpus = Assembler.loadlist(asteroids, tokens_in='citation')

for i in range(5):
    sentences = []
    names = []
    for sentence, source in corpus.assemble("f.l", min_length=3):
        sentences.append(sentence)
        names.append(source['name'])

    name_assembler = WordAssembler(names)
    name = name_assembler.assemble_word()
    print(name)
    for s in textwrap.wrap(" ".join(sentences)):
        print(s)
    print()
