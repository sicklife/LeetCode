#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

#reference: http://codesays.com/2014/solution-to-implement-strstr-by-leetcode/
#KMP
def strStr(haystack, needle):
	# Hanlde two special cases.
	if needle == "":        return haystack
	if haystack == "":      return None

	lenHaystack = len(haystack)
	lenNeedle = len(needle)
	begin = 0

	# Compare each substring as long as their length
	# is >= the length of needle
	while lenHaystack - begin >= lenNeedle:
		for index in xrange(lenNeedle):
			if haystack[begin+index] != needle[index]:
				# Find a different char
				break
		else:
			# Completely the same
			return haystack[begin:]
		
		begin += 1

	return None

def main():
	hs = sys.argv[0]
	needle = sys.argv[1]

	result = strStr(hs,needle)
	print result
	
if __name__ == '__main__':
    main()
