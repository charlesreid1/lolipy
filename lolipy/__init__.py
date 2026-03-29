__version__ = "2.0.0"

from lolipy.gibberish import Gibberish, Corruptor
from lolipy.queneau import Assembler, WordAssembler, DialogueAssembler
from lolipy.markov import MarkovGenerator
from lolipy.typewriter import Typewriter
from lolipy.letterforms import alternate_spelling
from lolipy.ebooks import EbooksQuotes
from lolipy.randomness import WanderingMonsterTable, Gradient


def __getattr__(name):
    if name == "ia":
        from lolipy import ia
        return ia
    if name == "corpora":
        from lolipy import corpora
        return corpora
    raise AttributeError(f"module 'lolipy' has no attribute {name!r}")
