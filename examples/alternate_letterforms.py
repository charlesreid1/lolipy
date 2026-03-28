"""Replace letters with visually similar Unicode characters.

Demonstrates the alternate_spelling function from olipy.letterforms.
"""
from olipy.letterforms import alternate_spelling

phrases = [
    "I love alternate letterforms.",
    "Hello, world!",
    "The quick brown fox jumps over the lazy dog.",
]

for phrase in phrases:
    print(f"Original:  {phrase}")
    print(f"Alternate: {alternate_spelling(phrase)}")
    print()
