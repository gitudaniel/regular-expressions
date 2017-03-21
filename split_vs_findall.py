import re

"""re.split() re.findall()

This compares how using findall and using split will change how
the the solution is written.
For re.findall() an extension is needed that says a paragraph ends with
two or more newlines, or the end of the input.
re.split() handles the boundary condition automatically.
For re.split, r'\n{2,}' means that two or more newline characters mark
a separator point between paragraphs in the input string.
"""

text = 'Paragraph one\non two lines.\n\nParagraph two.\n\n\nParagraph three.'

print 'With findall:'
for num, para in enumerate(re.findall(r'(.+?)(\n{2,}|$)', text, flags=re.DOTALL)):
    print num, repr(para)
    print

print
print 'With split:'
for num, para in enumerate(re.split(r'\n{2,}', text)):
    print num, repr(para)
    print
