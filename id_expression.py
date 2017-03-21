import re

"""(?(id)yes-expression|no-expression)

This lets you choose a different pattern based on whether or not a
previous group matched.
"id" is the group name or number
"yes-expression" is the pattern to use if the group matched
"no-expression" is the pattern to use otherwise.
In this particular example the names and the email do not have to match
a different email from the name given can be used.

If the name group matches, then the look ahead assertion requires both 
angle brackets and sets up the brackets group. i.e. (?P<brackets>(?=(<.*>$)))

(?=(<.*>$)) This means that it is supposed to look for an opening bracket (<) something inside the bracket (.*) and a closing bracket at the end (>$)

(.*) can be any string or symbol
$ means it is at the end of a string or a line.

If name is not matched the assertion requires the rest of the text not
have angle brackets around it.
If the brackets group is set, the actual pattern matching code consumes
the brackets in the input using literal patterns (?P<brackets>(?=(<.*>$))),
otherwise it consumes any blank space (?=([^<].*[^>]$)).
"""

address = re.compile(
    '''
    ^

    # A name is made up of letters, and may include "." for title,
    # abbreviations and middle initials.
    (?P<name>
       ([\w.]+\s+)*[\w.]+
     )?
    \s*

    # Email addresses are wrapped in angle brackets, but we only want
    # the brackets if we found a name.
    (?(name)
      # remainder wrapped in angle brackets because we have a name
      (?P<brackets>(?=(<.*>$)))
      |
      # remainder does not include angle brackets without a name
      (?=([^<].*[^>]$))
     )

    # Only look for a bracket if our look ahead assertion found both
    # of them.
    (?(brackets)<|\s*) # look for an < or a whitespace (\s) appearing
                       #  zero or more times (*)

    # The address itself: username@domain.tld
    (?P<email>
      [\w\d.+-]+       # username
      @
      ([\w\d.]+\.)+    # domain name prefix
      (com|org|edu)    # limit the allowed top-level domains
     )

    # Only look for a bracket if our look ahead assertion found both
    # of them.
    (?(brackets)>|\s*) # look for a > or a whitespace (\s) appearing
                       # zero or more times (*)

    $
    ''',
    re.UNICODE | re.VERBOSE)

candidates = [
    u'First Last <first.last@example.com>',
    u'No Brackets first.last@example.com',
    u'Open Bracket <first.last@example.com',
    u'Close Bracket first.last@example.com',
    u'no.brackets@example.com',
    ]

for candidate in candidates:
    print
    print 'Candidate:', candidate
    match = address.search(candidate)
    if match:
        print '  Match name :', match.groupdict()['name']
        print '  Match email:', match.groupdict()['email']
    else:
        print '  No match'

