import re

"""Splitting strings using regex

This is used where str.split() would fail. For example many plain 
text markup languages define paragraph separators as two or more 
newline (\n) characters. str.split() fails on the or more part.
"""

text = 'Paragraph one\non two lines.\n\nParagraph two. \n\n\nParagraph three.'

for num, para in enumerate(re.findall(r'(.+?)\n{2,}', text, flags=re.DOTALL)):
    print num, repr(para)
    print
