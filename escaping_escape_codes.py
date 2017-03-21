from patterns import test_patterns

test_patterns(r'\d+ \D+ \s+ \S+ \w+ \W+',
              [ r'\\d\+',
                r'\\D\+',
                r'\\s\+',
                r'\\S\+',
                r'\\w\+',
                r'\\W\+',
                ])
