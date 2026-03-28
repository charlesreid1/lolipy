"""Create symmetrical Unicode mosaic patterns.

Demonstrates MirroredMosaicGibberish for generating tweet-sized
Unicode art.
"""
from olipy.mosaic import MirroredMosaicGibberish

mosaic = MirroredMosaicGibberish()

for i in range(3):
    print(mosaic.tweet())
    print()
