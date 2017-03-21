import re

"""sub()

The re module also supports modifying text using regular expressions.
sub() replaces all occurences of a pattern with another string.
"""

bold = re.compile(r'\*{2}(.*?)\*{2}', re.UNICODE)

text = 'Make this **bold**.  This **too**.'

print 'Text:', text
print 'Bold:', bold.sub(r'<b>\1</b>', text)
