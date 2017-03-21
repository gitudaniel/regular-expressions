from patterns_updated import test_patterns

test_patterns('abbaaabbbbaaaaa',
              [r'a((a*)(b*))', # 'a' followed by 0-n 'a' and 0-n 'b'
               ])
