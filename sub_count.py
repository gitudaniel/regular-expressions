import re

"""count in sub()

Count limits the number of substitutions performed.
In the example below since count=1 only the first of the
two substitutions is made.
"""

bold = re.compile(r'\*{2}(.*?)\*{2}', re.UNICODE)

text = 'Make this **bold**.   This **too**.'

print 'Text:', text
print 'Bold:', bold.sub(r'<b>\1</b>', text, count=1)
