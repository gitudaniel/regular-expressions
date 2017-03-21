import re

"""Negative look ahead (?!pattern)

This assertion says that at this position the following regex does not match.
Example: Take a directory file drupal-6.14, the assertion drupal-6.14/(?!sites)
means that drupal-6.14 cannot be followed by sites. So when searching for 
directories you cannot get a match like drupal-6.14/sites. But you will get all
the other directories under drupat-6.14.
Refer to:
http://stackoverflow.com/questions/1749437/regular-expression-negative-lookahead
http://stackoverflow.com/questions/2973436/regex-lookahead-lookbehind-and-atomic-groups
https://www.reddit.com/r/explainlikeimfive/comments/x7x8t/eli5_negative_and_positive_lookaheadlookbehinds/
"""

address = re.compile(
    '''
    ^

    # An address: username@domain.tld

    # Ignore noreply addresses
    (?!noreply@.*$)

    [\w\d.+-]+     # username
    @
    ([\w\d.]+\.)+  # domain name prefix
    (com|org|edu)  # limit the allowed top-level domains

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
