#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

def longest_valid_parentheses(A):
	stack = []

	# The leftmost ")" is useless
	for item in A.lstrip(")"):
		if item == "(":
			stack.append(item)
		else:
			if stack[-1] == "(":
				stack.pop()
				stack.append(2)
			elif len(stack) > 1 and stack[-2] == "(":
				temp = stack.pop()
				stack.pop()
				stack.append(temp+2)
			else:
				stack.append(")")
				continue
			while len(stack) > 1 and type(stack[-2]) == int:
				temp = stack.pop()
				temp += stack.pop()
				stack.append(temp)
	stack = [item for item in stack if type(item) == int]
	return 0 if len(stack)==0 else max(stack)

def main():
	inputstr = sys.argv[1]
	result = longest_valid_parentheses(inputstr)
	print "Longest Valid Parentheses is:"
	print result
	
if __name__ == '__main__':
    main()
