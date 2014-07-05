#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

# @return a list of strings, [s1,s2] 
def letter_combinations_of_phone_number(digits):
	teldict = dict()
	teldict[0] = [' ']
	teldict[2] = ['a','b','c']
	teldict[3] = ['d','e','f']
	teldict[4] = ['g','h','i']
	teldict[5] = ['j','k','l']
	teldict[6] = ['m','n','o']
	teldict[7] = ['p','q','r','s']
	teldict[8] = ['t','u','v']
	teldict[9] = ['w','x','y','z']

	result = list()
	if len(digits) == 0:
		return [""]
	
	temp = [i for i in teldict[int(digits[0])]]
    # Recursion case. Append the recursion result to each string for current digit.
	for tail in letter_combinations_of_phone_number(digits[1:]):
		result.extend([i+tail for i in temp])
	'''
	for i in xrange(len(digits)):
		dset = teldict[digits[i]]
		for j in xrange(len(dset)):
			others_set = list()
			if i < len(digits) - 1:
				for k in range(i+1, len(digits)):
					kth_set = teldict[digits[k]]
					for m in xrange(len(kth_set)):
						result.append(dset[j]+kth_set[m])
			else:
				result.append(dset[j])
	'''
	return result



	
def main():
	inputlist = list()
	inputlist.append(2)
	inputlist.append(2)
	#inputlist.append(9)
	result = letter_combinations_of_phone_number(inputlist)
	print "All combinations:"
	print result
	
if __name__ == '__main__':
    main()
