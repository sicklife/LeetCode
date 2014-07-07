#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

def divide_two_integers(a, b):
	a = int(a)
	b = int(b)
	if a == 0:
		return 0
	sign = 1 if (a > 0 and b > 0) or (a < 0 and b < 0) else -1
	a = abs(a)
	b = abs(b)

	res = 0
	while(a>=b):
		k = 0; tmp_b = b
		while a >= tmp_b:
			res += 1 << k
			a -= tmp_b
			tmp_b <<=1
			k += 1

	return sign * res

def main():

	first_int = sys.argv[1]
	second_int = sys.argv[2]

	result = divide_two_integers(first_int,second_int)
	print result

if __name__ == '__main__':
    main()
