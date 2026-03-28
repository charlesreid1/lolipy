"""Extract pithy quotes from a text in the style of @horse_ebooks.

Demonstrates EbooksQuotes and ProjectGutenbergText for sampling
interesting passages from a text.
"""
from olipy import corpora
from olipy.ebooks import EbooksQuotes
from olipy.gutenberg import ProjectGutenbergText

# Load a public domain text
data = corpora.words.literature.nonfiction.literary_shrines
text = ProjectGutenbergText(data['text'])

ebooks = EbooksQuotes(["London", "literary"])

count = 0
for para in text.paragraphs:
    for quote in ebooks.quotes_in(para):
        print(quote)
        count += 1
        if count >= 20:
            break
    if count >= 20:
        break

print(f"\n({count} quotes extracted)")
