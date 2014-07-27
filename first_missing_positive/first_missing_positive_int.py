#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
# Reference: http://codesays.com/2014/solution-to-first-missing-positive-by-leetcode/
__author__ = ['Yue']
__version__ = "0.0.1"

def first_missing_positive_int(A):
	 # Place number i in the place A[i-1]
	index = 0
	while index < len(A):
		if index + 1 == A[index]:
			index += 1
		# Nowhere to swap
		elif A[index] <= 0:
			index += 1
		# Nowhere to swap
		elif A[index] > len(A):
			index += 1
		# No effect to swap
		elif A[index] == A[A[index]-1]:
			index += 1
		else:
			swapI, swapJ = index, A[index]-1
			A[swapI], A[swapJ] = A[swapJ], A[swapI]

	# Try to find the first i, such that i + 1 != A[i]
	for index in xrange(len(A)):
		if index + 1 != A[index]:   return index + 1

	# If all positive integers appears, the first missing
	# one would be the next integer
	return len(A) + 1


def main():
	inputlist = list()

	for i in range(0, 20):
		inputlist.append(random.randint(0,10))

	print inputlist
	result = first_missing_positive_int(inputlist)
	print "First Missing Positive Integer is:"
	print result
	
if __name__ == '__main__':
    main()
