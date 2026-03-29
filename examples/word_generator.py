"""Generate common-looking and obscure-looking English words.

Demonstrates WordAssembler for generating new words from a dictionary.
"""
from lolipy import corpora
from lolipy.queneau import WordAssembler

words = corpora.words.english_words['words']
corpus = WordAssembler(words)

print("Words that look like they could be real:")
for i in range(10):
    print(f"  {corpus.assemble_word()}")
