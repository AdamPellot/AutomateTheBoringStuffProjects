#! python3
# regexVersionOfStrip.py - Takes a string and does the same thing as the strip
#                string method.
# Adam Pellot

import re


# Strips a string using arguments passed by user.
def strip(args, string):
    if args == '':  # If no args are passed strip white space.
        stripRegex = re.compile(r'(^\s+)|(\s+$)')
        print(stripRegex.sub('', string))
    else:
        stripRegex = re.compile(r'(^{}+)|({}+$)'.format(args, args))
        print(stripRegex.sub('', string))


print('Please enter a string to be stripped')
string = input()

print('Please enter the arguments for strip')
args = input()

strip(args, string)
