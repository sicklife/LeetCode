#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

def remove_duplicates_from_sorted_array(A):
	if not A: 
		return 0
	first = 0
	for second in xrange(len(A)):
	    if A[second] == A[first]:
	        continue
	    else:
	        first += 1
	        A[first] = A[second]
	return first + 1

def main():
	inputlist = list()

	for i in range(0, 20):
		inputlist.append(random.randint(0,10))

	print inputlist

	sortedlist = sorted(inputlist)
	print sortedlist

	result = remove_duplicates_from_sorted_array(sortedlist)
	print "length new array after removing duplicates:"
	print result
	
if __name__ == '__main__':
    main()
