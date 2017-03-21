import re

"""The groups() method of the Match object.

This is used to access the substrings matched by the individual groups within a pattern.
"""

text = 'This is some text -- with punctuation.'

print text
print # This print statement provides an empty line between outputs. Maybe for readability

for pattern in [ r'^(\w+)',       #word at start of string
                 r'(\w+)\S*$',    # word at end of string with optional punctuation
                 r'(\bt\w+)\W+(\w+)', # word starting with 't' then another word
                 r'(\w+t)\b',        # word ending with 't'
                 ]:
    regex = re.compile(pattern)
    match = regex.search(text)
    print 'Matching "%s"' % pattern
    print '  ', match.groups()
    print
