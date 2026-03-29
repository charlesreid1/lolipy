"""Weighted random selection and gradients.

Demonstrates WanderingMonsterTable (D&D-style weighted random selection)
and Gradient (transitioning between character sets).
"""
import string
from lolipy.randomness import WanderingMonsterTable, Gradient

# WanderingMonsterTable: weighted random selection
monsters = WanderingMonsterTable(
    common=["Giant rat", "Alligator"],
    uncommon=["Orc", "Hobgoblin"],
    rare=["Mind flayer", "Neo-otyugh"],
    very_rare=["Flumph", "Ygorl, Lord of Entropy"],
)

print("Wandering monster encounters:")
for i in range(10):
    print(f"  {monsters.choice()}")

print()

# Gradient: weighted transition between two sets
print("Gradient from lowercase to uppercase:")
print("".join(Gradient.gradient(string.ascii_lowercase, string.ascii_uppercase, 50)))
print()

print("Rainbow gradient:")
print("".join(Gradient.rainbow_gradient(string.ascii_lowercase, string.ascii_uppercase, 50)))
