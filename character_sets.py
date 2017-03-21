from patterns import test_patterns

test_patterns('abbaaabbbbaaaaa',
              [ '[ab]', # either a or b
                'a[ab]+', # a followed by one or more a or b
                'a[ab]+?', # a followed by one or more a or b, not greedy. It takes the shortest valid set and then moves on. If we have aaab we will have responses aa and ab since we're looking for a followed by a or b.
                ])
