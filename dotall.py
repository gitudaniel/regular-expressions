import re

"""DOTALL flag

Normally the dot(.) character matches everything in the input text except a newline character. The flag allows dot to match newlines as well.
"""

text = 'This is some text -- with punctuation.\nAnd a second line.'
pattern = r'.+'
no_newlines = re.compile(pattern)
dotall = re.compile(pattern, re.DOTALL)

print 'Text        :', repr(text)
print 'Pattern     :', pattern
print 'No newlines :', no_newlines.findall(text)
print 'Dotall      :', dotall.findall(text)
