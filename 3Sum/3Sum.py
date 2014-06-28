#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

#Reference: http://leetcode.com/2010/04/finding-all-unique-triplets-that-sums.html

def triple_sum(mylist):
	print mylist
	mylist = sorted(mylist)
	#print mylist
	result = list()
	n = len(mylist)

	for i in range(0, n):
		j = i + 1
		k = n - 1
		while (j < k):
			two_sum = mylist[i]+mylist[j]
			if two_sum + mylist[k] < 0:
				j += 1
			elif two_sum + mylist[k] > 0:
				k -= 1
			else:
				temp = list()
				temp.append(mylist[i])
				temp.append(mylist[j])
				temp.append(mylist[k])
				result.append(temp)
				j += 1
				k -= 1

	return result

def main():
	inputlist = list()
	for i in range(0,20):
		inputlist.append(random.randint(-20,20))
	result = triple_sum(inputlist)	
	print "Unique triples:"	
	for triple in result:
		print triple
if __name__ == '__main__':
    main()

