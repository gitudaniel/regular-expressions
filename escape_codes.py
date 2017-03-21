from patterns import test_patterns

test_patterns('This is a prime #1 example!',
              [ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # sequence of alphanumeric characters. NOTE Alphanumeric = alphabet + numerals
                r'\W+', # sequence of non-alphanumeric characters
                ])
