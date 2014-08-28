#!/usr/bin/python
import cPickle, string, getopt, sys, random, time, re, pprint
# Reference: http://jelices.blogspot.com/2014/05/leetcode-python-combination-sum-ii.html
__author__ = ['Yue']
__version__ = "0.0.1"

def jumpgame(mylist):
	len_list = len(mylist)
	myposition = 0
	for i in xrange(len_list):
		if i <= myposition:
			myposition = max(myposition, i+mylist[i])
			if myposition >= len_list -1: return True
	return False

def main():
	inputlist_1 = [2,3,1,1,4]
	inputlist_2 = [3,2,1,0,4]
	inputlist_3 = [2,0]
	result = jumpgame(inputlist_1)
	print inputlist_1
	print "Result:%s" % result
	result = jumpgame(inputlist_2)
	print inputlist_2
	print "Result:%s" % result
	result = jumpgame(inputlist_3)
	print inputlist_3
	print "Result:%s" % result
	
if __name__ == '__main__':
    main()