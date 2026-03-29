"""Generate aesthetically pleasing Unicode gibberish.

Demonstrates the Gibberish class for creating tweet-length strings
of interesting Unicode characters.
"""
from lolipy.gibberish import Gibberish

for i in range(5):
    print(Gibberish.random().tweet())
    print()
