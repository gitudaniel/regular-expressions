from patterns_updated import test_patterns

"""| is used to indicate that one pattern or another should match."""

test_patterns('abbaaabbbbaaaaa',
              [r'a((a+)|(b+))', # 'a' followed by a sequence of 'a' or a sequence of 'b'
               r'a((a|b)+)',    # 'a' followed by a sequence of 'a' or 'b'
               ])
