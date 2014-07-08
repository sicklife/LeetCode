#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

def search_for_a_range(A, target):
	if not A: 
		return [-1,1]
	n = len(A)

	begin = -1; end = -1
	# Find the first occurrence of target in A
	last = len(A) - 1
	first = 0
	while first <= last:
		mid = (first + last) // 2
		if A[mid] > target:
			last = mid - 1
		elif A[mid] < target:
			first = mid + 1
		else:
			last = mid - 1
			begin = mid
	        
	# Target is not found in the array A
	if begin == -1:         return [-1, -1]

	# Find the last occurrence of target in A
	last = len(A) - 1
	first = 0
	while first <= last:
		mid = (first + last) // 2
		if A[mid] > target:
			last = mid - 1
		elif A[mid] < target:
			first = mid + 1
		else:
			first = mid + 1
			end = mid  

	return [begin, end]

def main():
	inputlist = list()

	for i in range(0, 20):
		inputlist.append(random.randint(0,10))

	print inputlist

	sortedlist = sorted(inputlist)
	print sortedlist

	target = random.randint(0,10)
	print "target is %s" % target
	result = search_for_a_range(sortedlist, target)
	print "Range of the target in the given sorted list is:"
	print result
	
if __name__ == '__main__':
    main()
