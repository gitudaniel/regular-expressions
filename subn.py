import re

"""subn()

It returns both the modified string and the count of substitutions made.
"""

bold = re.compile(r'\*{2}(.*?)\*{2}', re.UNICODE)

text = 'Make this **bold**.  This **too**.'

print 'Text:', text
print 'Bold:', bold.subn(r'<b>\1</b>', text)
