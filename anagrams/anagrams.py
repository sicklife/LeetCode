#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
# Reference: http://jelices.blogspot.com/2014/05/leetcode-python-combination-sum-ii.html
__author__ = ['Yue']
__version__ = "0.0.1"

def anagrams(strs):
	newdict = dict()
	for word in strs:
		sortedword = ''.join(sorted(word))
		newdict[sortedword] = [word] if sortedword not in newdict else newdict[sortedword] + [word]
	res = []
	for item in newdict:
		if len(newdict[item]) >= 2:
			res += newdict[item]
	return res

def main():
	inputlist = ['zzzz','abc','bac','cab','ccab','cbca']
	result = anagrams(inputlist)
	print "Result:"
	print result
	
if __name__ == '__main__':
    main()
