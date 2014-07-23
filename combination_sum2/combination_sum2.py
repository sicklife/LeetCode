#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
# Reference: http://jelices.blogspot.com/2014/05/leetcode-python-combination-sum-ii.html
__author__ = ['Yue']
__version__ = "0.0.1"

def combination_sum2(candidates, target):
	candidates.sort()
	solution =[]
	combination_helper(candidates, target, 0, 0, [], solution)
	return solution
    
def combination_helper(candidates, target, index, sum, tempList, solution):
	if sum == target:
		solution.append(list(tempList))
		return
	for i in range(index, len(candidates)):
		if (i==index or candidates[i-1]!=candidates[i]) and sum+candidates[i]<=target:
		    tempList.append(candidates[i])
		    combination_helper(candidates, target, i+1, sum+candidates[i], tempList, solution) 
		    tempList.pop()

def main():
	inputlist = list()

	for i in range(0, 20):
		inputlist.append(random.randint(0,10))

	print inputlist

	target = 4
	result = combination_sum2(inputlist, target)
	print "Result:"
	print result
	
if __name__ == '__main__':
    main()
