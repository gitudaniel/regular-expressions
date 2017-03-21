import re

"""Positive look ahead (?=pattern)

This is useful where you want to match a part of a pattern only if some 
other part should  match pattern.
Refer to:
http://stackoverflow.com/questions/1749437/regular-expression-negative-lookahead
http://stackoverflow.com/questions/2973436/regex-lookahead-lookbehind-and-atomic-groups
https://www.reddit.com/r/explainlikeimfive/comments/x7x8t/eli5_negative_and_positive_lookaheadlookbehinds/

"""

address = re.compile(
    '''
    # A name is made up of letters, and may include "." for title
    # abbreviations and middle initials.
    ((?P<name>
       ([\w.,]+\s+)*[\w.,]+
      )
      \s+
    ) # name is no longer optional

    # LOOKAHEAD
    # Email addresses are wrapped in angle brackets, but we only want
    # the brackets if they are both there, or neither are.
    (?= (<.*>$)     # remainder wrapped in angle brackets
        |
        ([^<].*[^>]$) # remainder *not* wrapped in angle brackets
      )

    <? # optional opening angle bracket

    # The address itself: username@domain.tld
    (?P<email>
      [\w\d.+-]+       # username
      @
      ([\w\d.]+\.)+    # domain name prefix
      (com|org|edu)    # limit the allowed top-level domains
    )

    >? # optional closing angle bracket
    ''',
    re.UNICODE | re.VERBOSE)

candidates = [
    u'First Last <first.last@example.com>',
    u'No Brackets first.last@example.com',
    u'Open Bracket <first.last@example.com',
    u'Close Bracket first.last@example.com>',
    ]

for candidate in candidates:
    print
    print 'Candidates:', candidate
    match = address.search(candidate)
    if match:
        print ' Match name :', match.groupdict()['name']
        print ' Match email:', match.groupdict()['email']
    else:
        print ' No match'
