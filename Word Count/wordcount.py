#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
nonalpha = ['\"', ')', '(', '.', ',']

def hF(filename):
  f = open(filename, "r")
  l = f.read().lower().replace(':',' ').replace(';',' ').replace(',',' ').replace('.',' ').replace('?',' ').split()

  di = {}
  for each in l:

    while(each and each[0] in nonalpha):
      each = each[1:]
    while(each and each[-1] in nonalpha):
      each = each[:-1]

    if each == '':
      continue

    if each in di:
      di[each]+=1
    else:
      di[each]=1
  return di

def print_words(filename):
  d = hF(filename)

  for key in sorted(d.keys()):
    print key, d[key]

  return

def get_value(tuple):
  return tuple[1]

def print_top(filename):
  d = hF(filename)
  d = sorted(d.items(), key=get_value)

  for i in range(40):
    if i <= len(d):
      print d[-i-1][0] + ' ' + str(d[-i-1][1])


def print_noncommon(filename, printed = True):
  d = hF(filename)
  d = sorted(d.items(), key=get_value)

  common = ['a','the', 'i', 'not', 'in', 'is', 'are', 'to', 'of']
  out = []

  for i in range(len(d)):
    if d[-i-1][0] not in common:
      out.append( str(d[-i-1][1]) +'\t'+ d[-i-1][0] )
      #print out[-1]
  if printed:
    for each in out:
      print each
  else:
    return out

def print_topnon(filename):
  d = hF(filename)
  d = sorted(d.items(), key=get_value)

  common = ['a','the', 'i', 'not', 'in', 'is', 'are', 'to', 'of']
  out = []

  for i in range(len(d)):
    if d[-i-1][0] not in common and d[-i-1][1] > 1:
      print str(d[-i-1][1]) +'\t'+ d[-i-1][0]

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount | --noncommon | --topnon} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  elif option == '--noncommon':
    print_noncommon(filename)
  elif option == '--topnon':
    print_topnon(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
