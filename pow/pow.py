#!/usr/bin/python
import cPickle, string, getopt, sys, random, time, re, pprint
# Reference: http://jelices.blogspot.com/2014/05/leetcode-python-combination-sum-ii.html
__author__ = ['Yue']
__version__ = "0.0.1"

def pow(x, n):
	return x**n

def pow_recursive(x, n):
	if n == 0:	return 1
	elif n < 0:	return 1.0 / pow_recursive(x, -n)
	elif n ==1 : return x
	else:
		if n % 2 == 0: return pow_recursive(x*x, n//2)
		else: return pow_recursive(x*x, n//2) * x

def pow_iterative(x, n):
	if n == 0: return 1
	if n < 0: div = True; n = -n
	else: div = False

	stack = []
	while n!=1 and n != -1:
		if n % 2 ==0: stack.append(1)
		else: stack.append(x)
		n //= 2

	result = x
	while len(stack)!=0:
		result = result * result * stack.pop()
	if div: return 1.0 / result
	else: return result


def main():
	x = int(sys.argv[1])
	n = int(sys.argv[2])
	#x = 2; n = 5
	#result = pow(x, n)
	#result = pow_recursive(x, n)
	result = pow_iterative(x, n)
	print "Result:"
	print result
	
if __name__ == '__main__':
    main()
