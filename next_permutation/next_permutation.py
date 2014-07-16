#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

# Reference: http://chaoren.is-programmer.com/posts/43985.html
# 1. From right to left, find the first digit (PartitionNumber) which violates the increase trend.
# 2. From right to left, find the first digit which is larger than PartitionNumber, call it ChangeNumber.
# 3. Swap PartitionNumber and ChangeNumber.
# 4. Reverse all the digit on the right of partition index.

# @param num, a list of integer
# @return a list of integer
def next_permutation(num):
	lenNum = len(num)
	# find the first number (PartitionNumber) which violates the increase trend
	partitionIndex = -1
	for i in reversed(xrange(lenNum - 1)):
	    if num[i] < num[i + 1]:
	        partitionIndex = i
	        break
	if partitionIndex != -1:
	    for i in reversed(xrange(lenNum)):
	        if num[i] > num[partitionIndex]:
	            num[i], num[partitionIndex] = num[partitionIndex], num[i]
	            break
	# reverse all numbers behind PartitionIndex
	i = partitionIndex + 1
	j = lenNum - 1
	while i < j:
	    num[i], num[j] = num[j], num[i]
	    i += 1
	    j -= 1
	return num

def main():

	inputlist = list()

	for i in range(0, 5):
		inputlist.append(random.randint(0,10))

	print inputlist

	sortedlist = sorted(inputlist)
	print sortedlist

	result = next_permutation(sortedlist)
	# or 
	# result = next_permutation(inputlist)
	print "Next permutation is:"
	print result
	
if __name__ == '__main__':
    main()
