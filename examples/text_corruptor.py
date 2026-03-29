"""Corrupt text by adding diacritical marks.

Demonstrates the Corruptor class from lolipy.gibberish.
"""
from lolipy.gibberish import Corruptor

text = "All work and no play makes Jack a dull boy."

print("Original:", text)
print()

for level in range(10):
    print(f"Level {level}: {Corruptor(level).corrupt(text)}")
