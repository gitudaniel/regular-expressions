import re

"""Named Group Substitution

The example below shows how to use named groups in the substitution.
"""

bold = re.compile(r'\*{2}(?P<bold_text>.*?)\*{2}', re.UNICODE)

text = 'Make this  **bold**. This **too**.'

print 'Text:', text
print 'Bold:', bold.sub(r'<b>\g<bold_text></b>', text)

# The \g<name> syntax in this case \g<bold_text> eliminates any
# ambiguity between group numbers and surrounding literal digits
# it works with numbered references
# omission makes no difference in current example though
