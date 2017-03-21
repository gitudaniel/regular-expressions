import re

text = 'This is some text -- with punctuation.'

print text
print

for pattern in [ r'^(?P<first_word>\w+)', # word at the beginning of a string
                 r'(?P<last_word>\w+)\S*$', # word at the end of a string with optional punctuation
                 r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)', # a word starting with t and the word after it
                 r'(?P<ends_with_t>\w+t)\b', # word ending with t
                 ]:
    regex = re.compile(pattern)
    match = regex.search(text)
    print 'Matching "%s"' % pattern
    print '  ', match.groups()
    print '  ', match.groupdict()
    print

# groupdict() retreives the dictionary mapping of groupnames to substrings from the match
