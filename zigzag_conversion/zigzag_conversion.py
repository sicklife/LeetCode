#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint

__author__ = ['Yue']
__version__ = "0.0.1"

def zigzag_conversion(mystr, nrows):
	print mystr

	if nrows <= 1:
		return mystr

	if len(mystr) == 0:
		return ""

	result = ""
	size = 2 * nrows - 2
	for i in range(0, nrows):
		j = i
		while(j < len(mystr)):
			result += mystr[j]
			if i != 0 and i != nrows - 1 and\
				j + size-2*i < len(mystr):
				result += mystr[j+size-2*i]
			j += size

	return str(result)
		
def main():
	mystr = sys.argv[1]
	n = int(sys.argv[2])
	result = zigzag_conversion(mystr,n)		
	print result
if __name__ == '__main__':
    main()