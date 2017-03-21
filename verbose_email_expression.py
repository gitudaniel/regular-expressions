import re

"""This is the verbose format of the email_expression.py file."""

address = re.compile(
    '''
    [\w\d.+-]+     # username
    @
    ([\w\d.]+\.)+  # domain name prefix
    (com|org|edu)  # we should support more top-level domains
    ''',
    re.UNICODE | re.VERBOSE)

# [\w\d.+-]+ the username can contain words or digits or a dot for abbreviations and titles and it must appear at least once
# ([\w\d.]+\.)+ the domain name prefix must contain either words or digits or any other symbols and must be followed by a dot(.) & must appear at least once
# (com|org|edu) it must contain one of the listed options to be valid

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
        print '  No matches'
