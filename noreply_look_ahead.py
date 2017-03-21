import re

"""Negative look ahead

This says that the pattern does not match the text following the current point.
"""

address = re.compile(
    '''
    ^

    # An address: username@domain.tld

    # Ignore noreply addresses
    (?!noreply@.*$)

    [\w\d.+-]+      # username
    @
    ([\w\d.]+\.)+   # domain name prefix
    (com|org|edu)   # limit the allowed top-level domain

    $
    ''',
    re.UNICODE | re.VERBOSE)

candidates = [
    u'first.last@example.com',
    u'noreply@example.com',
    ]

for candidate in candidates:
    print
    print 'Candidate:', candidate
    match = address.search(candidate)
    if match:
        print '  Match:', candidate[match.start():match.end()]
    else:
        print '  No match'
