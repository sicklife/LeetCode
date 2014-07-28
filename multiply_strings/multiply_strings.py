#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
# Reference: http://codesays.com/2014/solution-to-multiply-strings-by-leetcode/
__author__ = ['Yue']
__version__ = "0.0.1"

def multiply_strings(num1, num2):
	if num1 == "0" or num2 == "0":      return "0"

	result = [0] * (len(num1) + len(num2))
	num1 = [int(i) for i in num1]
	num2 = [int(i) for i in num2]

	for index1 in xrange(len(num1)):
		multiplier = num1[index1]
		temp = [i*multiplier for i in num2]         # Multiply
		temp.extend([0] * (len(num1) - index1 - 1)) # Shift

		# Add to the final result
		for resIndex in xrange(1, len(temp) + 1):
			result[-resIndex] += temp[-resIndex]

	for resIndex in xrange(len(result)-1, 0, -1):
		result[resIndex-1] += result[resIndex] // 10
		result[resIndex] %= 10

	# Convert the final result into string
	result = "".join([str(i) for i in result]).lstrip("0")

	return result
def main():

	result = multiply_strings("32","34")
	print "Result of multiplication:"
	print result
	
if __name__ == '__main__':
    main()
