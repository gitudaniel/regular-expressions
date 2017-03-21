import re

"""Self-referencing Expression

In this example we're matching only addresses composed of the first and last
name. We do this by referencing back to those previously matched groups by id
number i.e. '\num'.
This only works because the program requires that a first and last
name be listed before a match be made. 
The names listed must also be the ones used in the email. 
Otherwise no match will be made.
"""

address = re.compile(
    r'''

    # The regular name
    (\w+)              # first name -> group 1 (\1)
    \s+                # group 2 -> \2
    (([\w.]+)\s+)?     # optional middle name or initial -> (\3)
    (\w+)              # last name -> \4

    \s+

    <

    # The address: first_name.last_name@domain.tld
    (?P<email>
      \1                # first name
      \.                # format should be first.last name
      \4                # last name
      @
      ([\w\d.]+\.)+     # domain name prefix
      (com|org|edu)     # limit the allowed top-level domains
    )

    >
    ''',
    re.UNICODE | re.VERBOSE | re.IGNORECASE)

candidates = [
    u'First Last <first.last@example.com>',
    u'Different Name <first.last@example.com>',
    u'First Middle Last <first.last@example.com>',
    u'First M. Last <first.last@example.com>',
    ]

for candidate in candidates:
    print
    print 'Candidate:', candidate
    match = address.search(candidate)
    if match:
        print '  Match name :', match.group(1), match.group(3), match.group(4)
        print '  Match email:', match.group(5)
    else:
        print '  No match'
