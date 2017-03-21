from patterns import test_patterns

test_patterns('This is some text -- with punctuation.',
              [ '[a-z]+',      # sequences of lower case letters
                '[A-Z]+',      # sequences of upper case letters
                '[a-zA-Z]+',   # sequences of lower or upper case letters
                '[A-Z][a-z]+', # one uppercase letter followed by lowercase letters
                ])
