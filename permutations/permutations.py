#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
# Reference: http://chaoren.is-programmer.com/posts/42943.html
__author__ = ['Yue']
__version__ = "0.0.1"

def permutations(num):
	l = len(num)
	if l == 0: return []
	if l == 1: return [num]
	result = []
	for i in xrange(l):
		for j in permutations(num[0:i] + num[i+1:]):
			result.append([num[i]] + j)
	return result
def main():
	inputlist = list()

	for i in range(0, 3):
		inputlist.append(random.randint(0,10))

	print inputlist

	result = permutations(inputlist)
	print "Permutations of given list:"
	print result
	
if __name__ == '__main__':
    main()
