from patterns import test_patterns

test_patterns('This is some text -- with punctuation.',
              [ '[^-. ]+', # finds sequences without -, ., or space
                ])
