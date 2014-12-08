#!/usr/bin/python
import re
import sys
question = """
Write a script that prompts the user for their phone number, x. Then carry out the following steps:
 

1. Compute x minus the sum of the digits of x. Call this result y. (hint: to find the sum of the digits of x, check to see what x//10 and x%10 give you)

2. Compute the sum of the digits of y, and store the result back in y.

3. Repeat step 2 until y has just one digit, then display it.
 

What answer do you get?
"""
def sum_digits(i):
  sum_of_digits = 0;
  s = str(i)
  for char in s:
    if re.match('\d', char):
      sum_of_digits += int(char)
  return sum_of_digits


#raw_num = "570-205-3283"
raw_num = sys.argv[1]

x = ""
for char in raw_num:
  if re.match('\d', char):
    x += char
x = int(x)

y = x - sum_digits(x)
print "x is:", x
print "sum of digits of x is: ", sum_digits(x)

while len(str(y)) > 1:
  y = sum_digits(y)

print y


