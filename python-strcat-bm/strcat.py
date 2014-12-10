#!/usr/bin/python
import sys
import cProfile
import time
import memory_profiler

i = 10000000
tladd = open("timelog-add.csv",'w')
tllst = open("timelog-lst.csv",'w')
j = 0

def timefunc(f):
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print f.__name__, 'took', end - start, 'time'
        if f.__name__ == 'stradd':
          tladd.write(str(j) + "," + str(end-start) + "\n")
        elif f.__name__ == 'strlist':
          tllst.write(str(j) + "," + str(end-start) + "\n")
        return result
    return f_timer

@timefunc
@profile
def stradd(i):
  string = ""
  for _ in xrange(i):
    string += "+"
  print "string length ", len(string)

@timefunc
def strlist(i):
  string = ""
  appendlist = []
  for _ in xrange(i):
    appendlist.append("-")
  string = string.join(appendlist)
  print "string length ", len(string)

print "using a list"
for k in range(0,i,i//100):
  j = k
  strlist(j)

print "adding strings"
for k in range(0,i,i//100):
  j = k
  stradd(j)
