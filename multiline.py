import re

"""MULTILINE flag

This controls how the pattern matching code processes anchoring
instructions for text containing newline characters.
With multiline mode on, the anchor rules for ^ and $ apply at
the beginning and end of each line in addition to the entire string.
"""

text = 'This is some text -- with punctuation.\nAnd a second line.'
pattern = r'(^\w+)|(\w+\S*$)'
single_line = re.compile(pattern)
multiline = re.compile(pattern, re.MULTILINE)

print 'Text         :', repr(text)
print 'Pattern      :', pattern
print 'Single Line  :', single_line.findall(text)
print 'Multiline    :', multiline.findall(text)
