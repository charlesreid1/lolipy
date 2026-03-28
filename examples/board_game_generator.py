"""Generate fictional board game names and descriptions.

Demonstrates complex Queneau assembly using Assembler, WordAssembler,
and CompositeAssembler together.
"""
import re
import textwrap
from olipy import corpora
from olipy.queneau import Assembler, WordAssembler, CompositeAssembler

corpus = Assembler.loadlist(
    corpora.games.bgg_board_games['board_games'], tokens_in='description'
)

no_punctuation_at_end = re.compile("[a-zA-Z0-9]$")
whitespace = re.compile(r"\s+")

for i in range(3):
    sentences = []
    names = []
    genres = []
    mechanics = []
    for line, source in corpus.assemble("0.l"):
        if no_punctuation_at_end.search(line):
            line += "."
        sentences.append(line)
        names.append(source['name'])
        genres.append([genre for id, genre in source.get('boardgamecategory', [])])
        mechanics.append([mechanic for id, mechanic in source.get('boardgamemechanic', [])])

    # Make assemblers for single- and multi-word names.
    single_word_assembler = WordAssembler()
    multi_word_assembler = Assembler()
    name_assembler = CompositeAssembler([single_word_assembler, multi_word_assembler])
    for name in names:
        words = whitespace.split(name)
        if len(words) == 1:
            single_word_assembler.add(name)
        else:
            multi_word_assembler.add(words)

    assembler, choice = name_assembler.assemble()
    if assembler == single_word_assembler:
        separator = ''
    else:
        separator = ' '
    print(separator.join([x for x, source in choice]))

    for name, l in (('Genres', genres), ('Mechanics', mechanics)):
        assembler = Assembler()
        for lst in l:
            assembler.add(lst)
        choices = [choice for choice, source in assembler.assemble()]
        print(f"{name}: {', '.join(choices)}")

    for s in textwrap.wrap(" ".join(sentences)):
        print(s)
    print("-" * 60)
