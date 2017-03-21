from patterns_updated import test_patterns

test_patterns('abbaaabbbbaaaaa',
              [r'a((a+)|(b+))',    # capturing form
               r'a((a+)|(?:b+))',# non-capturing form
               ])
