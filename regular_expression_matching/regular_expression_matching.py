#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

#Reference: http://leetcode.com/2011/11/longest-palindromic-substring-part-i.html

def isMatch(mystr, regular):
	print mystr
	print regular

	if ('.' not in regular) and ('*' not in regular):
		if mystr != regular:
			return False
		else:
			return True

	else:
		if (len(regular) == 0 or len(mystr) == 0):
			return False
		if len(regular) == 1 or regular[1] != '*':
			if len(mystr) < 1 or (regular[0] != '.' and mystr[0]!=regular[0]):
				return False
			return isMatch(mystr[1:],regular[1:]) 
		else:
			length = len(mystr)
			i = -1
			while(i < length and (i < 0 or regular[0] == '.' or regular[0] == mystr[i])):
				if isMatch(mystr[i+1:],regular[2:]):
					return True
				i += 1
			return False

def main():
	mystr = sys.argv[1]
	regular = sys.argv[2]
	result = isMatch(mystr, regular)		
	if result is False:
		print "false"
	else:
		print "true"
if __name__ == '__main__':
    main()

