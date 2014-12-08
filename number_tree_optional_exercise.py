#!/usr/bin/python
# Prints a christmas tree on the terminal made up of ascending and descending integers
# 2014 datamungeblog.com
import sys
import random

size = int(sys.argv[1]) # first argument is an integer which is the height of the tree
probability_green = .7 # how much of the tree will be green vs a random ornament

class colors: # colors
    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'
ornaments = [colors.purple, colors.blue, colors.yellow, colors.red, '']
def decorate(s):
  if random.random() > probability_green:
    color = random.choice(ornaments)
    return color + str(s) + colors.end
  else:
    return colors.green + str(s) + colors.end
for i in range(1,size+1):
  line = ""
  for s in range(i, size): # this will loop over each digit left
    for c in range(0,len(str(s))): # prepend a space for each character of each digit
      line += " "
  for j in range(1,i+1):
    line += decorate(j)
  for j in range(i-1,0,-1):
    line += decorate(j)
  print line
trunk_length = 3 #TODO: if this wasn't a joke I'd make this an argument
for i in range(0, trunk_length):
  line = ""
  for s in range(1, size): # this will loop over each digit left
    for c in range(0,len(str(s))): # prepend a space for each character of each digit
      line += " "
  print line + "00"
