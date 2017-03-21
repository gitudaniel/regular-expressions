import re

"""Using parentheses

Enclosing the expression in parentheses to define a group causes split
to work more like str.partition.
It returns each paragraph, as well as the sequence of newlines
separating them.
"""

text = 'Paragraph one\non two lines.\n\nParagraph two.\n\n\nParagraph three.'

print
print 'With split:'
for num, para in enumerate(re.split(r'(\n{2,})', text)):
    print num, repr(para)
    print
