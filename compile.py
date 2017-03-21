import re

"""The compile() function.

The compile function convrets an expression string into a RegexObject. Compile the expressions your program uses frequently for efficiency.
"""

# Pre-compile the patterns
regexes = [ re.compile(p) for p in [ 'this', 'that', ]]

text = 'Does this text match the pattern?'

for regex in regexes:
    print 'Looking for "%s" in "%s" ->' % (regex.pattern, text),

    if regex.search(text):
        print 'found a match!'
    else:
        print 'no match'
