"""Generate fictional dinosaur names.

Demonstrates WordAssembler for creating new words from existing words
by recombining their phonetic structure.
"""
from olipy import corpora
from olipy.queneau import WordAssembler

dinosaurs = corpora.animals.dinosaurs['dinosaurs']
assembler = WordAssembler(dinosaurs)

print("Newly discovered dinosaur species:")
for i in range(10):
    dino = assembler.assemble_word()
    if dino[0] in 'AEIOU':
        dino = "an " + dino
    else:
        dino = "a " + dino
    print(f"  - {dino}")
