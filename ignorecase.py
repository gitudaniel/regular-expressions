import re

"""Changes the way the matching engine processes an expression using option
flags.

The example below shows a situation where we can change how case sensitive
the engine is.
"""

text = 'This is some text -- with punctuation.'
pattern = r'\bT\w+'
with_case = re.compile(pattern)
without_case = re.compile(pattern, re.IGNORECASE)

print 'Text          :', text
print 'Pattern       :', pattern
print 'Case-sensitive:', with_case.findall(text)
print 'Case-insensitive:', without_case.findall(text)
