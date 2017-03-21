import re

""" You can restrict the search range where only a subset of the full input should be searched.

If the pattern must appear at the front of the input, using match() instead of search() will anchor the search without having to explicitly include an anchor in the search pattern.

The example below shows a comparison of match and search.
"""

text = 'This is some text -- with punctuation.'
pattern = 'is'

print 'Text   :', text
print 'Pattern:', pattern

m = re.match(pattern, text)
print 'Match  :', m # is doesn't appear at the start of text. match() doesn't find it
s = re.search(pattern, text)
print 'Search :', s # is appears twice in the text so search() finds it. 'Th"is"' & 'is'
