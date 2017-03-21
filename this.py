import re

patterns = ['this','that']
text = 'Does this text match that pattern?'

for pattern in patterns:
    match = re.search(pattern, text)

    s = match.start()
    e = match.end()

    print 'Found "%s" in "%s" from %d to %d ("%s")' % \
        (match.re.pattern, match.string, s, e, text[s:e])
