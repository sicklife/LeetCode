#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"
# Reference: http://www.programcreek.com/2012/12/leetcode-string-to-integer-atoi/
def string_to_int(mystr):
	print mystr
	if len(mystr) == 0:
		return 0
	mystr = mystr.strip()

	fg = '+'
	i = 0
	if mystr[0]=='-':
		fg = '-'
		i += 1
	elif mystr[0] == '+':
		i += 1

	result = 0.0

	while (i < len(mystr) and\
		mystr[i] >= '0' and mystr[i] <= '9'):
		result = result * 10.0 + float(int(mystr[i]) - int('0'))
		i += 1

	if fg == '-':
		result = -result

	return int(result)

def main():
	mystr = sys.argv[1]
	result = string_to_int(mystr)		
	print result
if __name__ == '__main__':
    main()

