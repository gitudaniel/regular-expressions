# _*_ coding: utf-8 _*_
import re
import codecs
import sys

"""Unicode 

Regular expression processing assumes that the pattern and input text are both ASCII. Those assumptions mean that the pattern \w+ will match the word "French" but not “Français”, since the ç is not part of the ASCII character set.
To enable unicode matching for python 2 add the UNICODE flag when compiling the pattern.
NOTE: Python 3 uses unicode for all strings by default, so the flag is unnecessary
"""

# Set standard output encoding to UTF-8.
sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)

text = u'Français złoty Österreich'
pattern = ur'\w+'
ascii_pattern = re.compile(pattern)
unicode_pattern = re.compile(pattern, re.UNICODE)

print 'Text     :', text
print 'Pattern  :', pattern
print 'ASCII    :', u', '.join(ascii_pattern.findall(text))
print 'Unicode  :', u', '.join(unicode_pattern.findall(text))

