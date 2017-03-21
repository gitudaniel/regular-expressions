import re

"""Negative Look Behind (?<!pattern)

The expression must use a fixed length pattern. A negative look behind only
returns a match if it is not preceeded by pattern. Pattern here means whatever
we're looking for.
Refer to:
http://stackoverflow.com/questions/2973436/regex-lookahead-lookbehind-and-atomic-groups
https://www.reddit.com/r/explainlikeimfive/comments/x7x8t/eli5_negative_and_positive_lookaheadlookbehinds/
"""

address = re.compile(
    '''
    ^

    # An address: username@domain.tld

    [\w\d.+-]+      #username

    # Ignore noreply addresses
    (?<!noreply)

    @
    ([\w\d.]+\.)+   # domain name prefix
    (com|org|edu)   # limit the allowed top-level domains

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
