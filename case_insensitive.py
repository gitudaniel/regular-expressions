import re

"""This embeds case-insensitive matching inside the expression string itself.
Options should always come at the beginning of the expression because they control the way the entire expression is evaluated.
"""

text = 'This is some text -- with punctuation.'
pattern = r'(?i)\bT\w+'
regex = re.compile(pattern)

print 'Text      :', text
print 'Pattern   :', pattern
print 'Matches   :', regex.findall(text)
