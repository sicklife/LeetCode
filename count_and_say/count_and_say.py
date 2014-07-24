#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
# Reference: http://codesays.com/2014/solution-to-count-and-say-by-leetcode/
__author__ = ['Yue']
__version__ = "0.0.1"
# Start from 1, count numbers in the last line
# 1
# 11
# 21
# 1211
# 111221
# 312211
# 13112211 
def count_and_say(n):
	result = "1"    # The result for n == 1
	for _ in xrange(n-1):
		temp = ""   # The result for next round

		current = result[0]
		currentCount = 1

		for item in result[1:]:
			if item == current:
				# Same value as previous
				currentCount += 1
			else:
				# Meet with a new value, store the result of
				# previous value
				temp += str(currentCount) + current

				#Reset these two variables
				current = item
				currentCount = 1

		# Store the result for the last unique value
		temp += str(currentCount) + current
		result = temp

	return result

def main():

	n = 10
	result = count_and_say(n)
	print "nth sequence:"
	print result
	
if __name__ == '__main__':
    main()
