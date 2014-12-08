#!/usr/bin/python
import sys
import cProfile



i = 100000

def stradd(i):
  string = ""
  for _ in range(i):
    string += "+"

def strlist(i):
  string = ""
  appendlist = []
  for _ in range(i):
    appendlist.append("+")
  string.join(appendlist)

print "\n\nadding strings"
addprofile = cProfile.run('stradd(i)')

print "\n\nusing a list"
listprofile = cProfile.run('strlist(i)')
