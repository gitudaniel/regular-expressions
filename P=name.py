import re

"""(?P=name)

Python's expression parser includes an extension that uses (?P=name) to
refer to the value of a named group matched earlier in the expression.
"""

address = re.compile(
    '''

    # The regular name
    (?P<first_name>\w+)
    \s+
    (?P<middle_name>([\w.]+)\s+)?       # optional middle name or initial
    (?P<last_name>\w+)

    \s+

    <

    # The address: first_name.last_name@domain.tld
    (?P<email>
      (?P=first_name)
      \.
      (?P=middle_name
      \.
      (?P=last_name)
      @
      ([\w\d.]+\.)+    # domain name prefix
      (com|org|edu)    # limit the allowed top-level domains
    )

    >
    ''',
    re.UNICODE | re.VERBOSE | re.IGNORECASE)

candidates = [
    u'First Last <first.last@example.com>',
    u'Different Name <first.last@example.com>',
    u'First Middle Last <first.last@example.com>',
    u'First M. Last <first.m.last@example.com>',
    ]

for candidate in candidates:
    print
    print 'Candidate:', candidate
    match = address.search(candidate)
    if match:
        print '  Match name :', match.groupdict()['first_name'], \
        match.groupdict()['last_name']
        print '  Match email:', match.groupdict()['email']
    else:
        print '  No match'
