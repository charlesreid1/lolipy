"""Generate dialogue between astronauts and Mission Control.

Demonstrates DialogueAssembler with the Apollo 11 transcript corpus.
"""
from lolipy import corpora
from lolipy.queneau import DialogueAssembler

transcript = corpora.words.literature.nonfiction.apollo_11['transcript']
assembler = DialogueAssembler.loadlist(transcript)

last_speaker = None
for i in range(20):
    speaker, tokens = assembler.assemble(last_speaker)
    last_speaker = speaker
    print(f"{speaker}: {' '.join(x for x, y in tokens)}")
