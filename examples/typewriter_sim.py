"""Simulate typing on the Adler Universal 39 typewriter from The Shining.

Demonstrates the Typewriter class for introducing realistic typos.
"""
from olipy.typewriter import Typewriter

text = "All work and no play makes Jack a dull boy."

print("Original:")
print(f"  {text}")
print()

print("Typed with increasing error rates:")
for error_rate in [1, 2, 3, 5, 8]:
    typewriter = Typewriter(error_rate, 0.5)
    print(f"  (rate={error_rate}) {typewriter.type(text)}")
