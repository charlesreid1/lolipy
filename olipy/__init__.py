__version__ = "2.0.0"

from olipy.gibberish import Gibberish, Corruptor
from olipy.queneau import Assembler, WordAssembler, DialogueAssembler
from olipy.markov import MarkovGenerator
from olipy.typewriter import Typewriter
from olipy.letterforms import alternate_spelling
from olipy.ebooks import EbooksQuotes
from olipy.randomness import WanderingMonsterTable, Gradient


def __getattr__(name):
    if name == "ia":
        from olipy import ia
        return ia
    if name == "corpora":
        from olipy import corpora
        return corpora
    raise AttributeError(f"module 'olipy' has no attribute {name!r}")
