#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

def remove_element(A, value):
	if len(A) == 0:
		return 0
	while value in A:
		A.remove(value)
	return len(A)    	

def main():
	inputlist = list()

	for i in range(0, 20):
		inputlist.append(random.randint(0,10))

	print inputlist
	value = 2
	length = remove_element(inputlist, value)
	print "new length after removing element %s: %s" % (value, length)
	
if __name__ == '__main__':
    main()
