import re

patterns = [ 'this', 'that' ]

text = 'Does this text match the pattern?'

for pattern in patterns:
    """ This picks an item from the list patterns and then the text in it 
    entirety.

    The %s is a python string formatting syntax borrowed from C's sprintf.
    The first %s matches to an item in pattern and the second %s matches to
    the text.
    The % (pattern, text) shows that the %s relates to the tuples after the %
    The -> is just a pointer to the response we get after running. (the if 
    block)
    """

    print 'Looking for "%s" in "%s" ->' % (pattern, text),

    if re.search(pattern, text):
        print 'found a match!'
    else:
        print 'no match'
