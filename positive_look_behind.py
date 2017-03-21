import re

"""Positive look behind (?<=pattern)

This is a script to find twitter handles using a positive look behind assertion.
In this example we know what sections of the text are twitter handles because they are preceeded by an @.
Refer to:
http://stackoverflow.com/questions/2973436/regex-lookahead-lookbehind-and-atomic-groups
https://www.reddit.com/r/explainlikeimfive/comments/x7x8t/eli5_negative_and_positive_lookaheadlookbehinds/
"""

twitter = re.compile(
    '''
    # A twitter handle: @username
    (?<=@)
    ([\w\d_]+)      # username
    ''',
    re.UNICODE | re.VERBOSE)

text = '''This text includes two Twitter handles.
One for @ThePSF, and one for the author, @doughellmann,
'''

print text
for match in twitter.findall(text):
    print 'Handle:', match
