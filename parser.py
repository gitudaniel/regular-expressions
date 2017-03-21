from patterns import test_patterns

"""Dissecting matches with groups.

Adding groups to a pattern lets you isolate parts of the matching text, expanding those capabilities to create a parser. Groups are defined by enclosing patterns in double parentheses.
"""

# in this code the hyphen (-) is meant to give a range of values where n can be an infinite number.
test_patterns('abbaaabbbbaaaaa',
              [ 'a(ab)',   # a followed by literal 'ab'
                'a(a*b*)', # a followed by 0-n 'a' and 0-n 'b'
                'a(a+b*)', # a followed by 1-n 'a' and 1-n 'b'
                'a(ab)*',  # a followed by 0-n 'ab'
                'a(ab)+',  # a followed by 1-n 'ab'
                ])
