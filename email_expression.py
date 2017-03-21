import re

"""Verbose mode expressions

These allow you to add comments and extra whitespace to be able to keep track of why each element is needed and how exactly the parts of the expression interact.
"""

address = re.compile('[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)', re.UNICODE)

candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valid@example.foo',
    ]

for candidate in candidates:
    print
    print 'Candidate:', candidate
    match = address.search(candidate)
    if match:
        print '  Matches'
    else:
        print ' No match'
