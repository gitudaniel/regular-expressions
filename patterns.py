import re

def test_patterns(text, patterns=[]):
    """Given source text and a list of patterns, look for matches
    for each pattern within the text and print them to stdout.
    """

    # Show the character positions and input text
    print 
    print ''.join(str(i/10 or ' ') for i in range(len(text)))
    # range(len(text)) prints a list of the positions of each individual letter in text
    # str(i/10) gives the remainder of the division of each of the positions by 10
    # if the division is less than one it prints out an empty space instead of 0

    print ''.join(str(i%10) for i in range(len(text))) 
    # This gives the remainder of each of the positions divided by 10

    print text # This prints the text in question

    # Look for each pattern in the text and print the results
    for pattern in patterns:
        print
        print 'Matching "%s"' % pattern
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            print ' %2d : %d = "%s"' % \
                (s, e-1, text[s:e])
    return

if __name__ == '__main__':
    test_patterns('abbaaabbbbaaaaa', ['ab','ba'])
