#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

# 这个其实就是之前判断合法性的逆操作
def generate_parentheses(n):
	n = int(n)
	result = list()
	stack = ""
	if n != 0:
		helper(result, stack, n, n)
	return result

def helper(result, stack, leftnum, rightnum):
	if rightnum < leftnum:
		return
	if leftnum == 0 and rightnum==0:
		result.append(stack)

	if leftnum > 0:
		helper(result, stack+'(', leftnum-1, rightnum)

	if rightnum > 0:
		helper(result, stack+')', leftnum, rightnum-1)

def main():
	n = sys.argv[1]
	result = generate_parentheses(n)
	print "All solutions with %s parentheses:" % n
	print result
	
if __name__ == '__main__':
    main()
