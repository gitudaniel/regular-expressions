import re

"""If you're using groupings to find parts of the string but you don't need all of the parts matched by groups, you can ask for the match of only a single group with group()
"""

text = 'This is some text -- with punctuation.'

# word starting with 't' then another word
regex = re.compile(r'(\bt\w+)\W+(\w+)')
print 'Pattern              :', regex.pattern

match = regex.search(text)
print 'Entire match          :', match.group(0)
print 'Word starting with "t":', match.group(1)
print 'Word after "t" word   :', match.group(2)
