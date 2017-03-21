from patterns import test_patterns

"""This section covers anchoring.

Anchoring specifies the relative location in the input text where the pattern should appear.
"""

test_patterns('This is some text -- with punctuation.',
              [ r'^\w+',     # word at start of string
                r'\A\w+',    # word at start of string
                r'\w+\S*$',  # word at end of string, with optional punctuation
                r'\w+\S*\Z', # word at end of string, with optional punctuation
                r'\w*t\w*',  # word containing 't'
                r'\bt\w+',   # 't' at start of word
                r'\w+t\b',   # 't' at end of word
                r'\Bt\B',    # 't', not start or end of word
                ])
