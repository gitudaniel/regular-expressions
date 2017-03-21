from patterns import test_patterns

test_patterns('abbaaabbbbaaaaa',
              ['a.',    # a followed by any one character
               'b.',    # b followed by any one character
               'a.*b',  # a followed by anything, ending in b
               'a.*?b', # a followed by anything, ending in b non-greedy
               ])
