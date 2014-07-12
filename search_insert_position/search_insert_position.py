#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

def search_insert_position(A, target):
	# Binary search
	if len(A) == 0:
		return 0
	start = 0; end = len(A)-1
	insertion = -1
	while start <= end:
		mid = (start + end) // 2
		if A[mid] > target:
			end = mid - 1
			if end < start:
				insertion = end + 1 
		elif A[mid] < target:
			start = mid + 1
			if start > end:
				insertion = start
				break
		else:
			end = mid - 1
			insertion = mid
	
	if insertion != -1:
		return insertion
	else:
		return 0
def main():
	inputlist = list()

	for i in range(0, 20):
		inputlist.append(random.randint(0,10))

	print inputlist

	sortedlist = sorted(inputlist)
	print sortedlist

	target = int(sys.argv[1])
	result = search_insert_position(sortedlist, target)
	print "Position target %s will be inserted is:" % target
	print result
	
if __name__ == '__main__':
    main()
