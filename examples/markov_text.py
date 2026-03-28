"""Generate text using a Markov chain.

Demonstrates MarkovGenerator for assembling sequences of words
from training text.
"""
from olipy import corpora
from olipy.markov import MarkovGenerator

text = corpora.words.literature.nonfiction.literary_shrines['text']

generator = MarkovGenerator(order=1, max=100)
generator.add(text)

for i in range(3):
    print(" ".join(generator.assemble()))
    print()
