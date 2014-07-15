#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

def search_in_rotated_sorted_array(A, target):
	l = 0; r = len(A) - 1
	while l <= r:
		m = (l + r) //2
		if A[m] == target:
			return m
		if A[m] >= A[l]:
			if A[l] <= target and target <= A[m]:
				r = m - 1
			else:
				l = m + 1
		else:
			if A[m] >= target or target >= A[l]:
				r = m - 1
			else:
				l = m + 1
	return -1

def main():
	inputlist = list()

	for i in range(0, 20):
		inputlist.append(random.randint(0,10))

	print inputlist

	sortedlist = sorted(inputlist)
	print sortedlist
	print sortedlist[5:]+sortedlist[0:5]
	target = 4
	result = search_in_rotated_sorted_array(sortedlist[5:]+sortedlist[0:5], target)
	print "target is :%s" % target
	print "Index of target in rotated sorted array:"
	print result
	
if __name__ == '__main__':
    main()
