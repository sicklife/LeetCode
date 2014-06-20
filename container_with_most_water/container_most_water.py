#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint,argparse
__author__ = ['Yue']
__version__ = "0.0.1"
def main():
	# number of elements in the array
    n = 10
    intlist = list()
    # randomly generate integer elements for the array
    for i in range(0,n):
    	intlist.append(random.randint(1,100))

    maxarea = 0
    max_i = 0
    max_j = 0
    i = 0
    j = n - 1
    # iterate all possible solution to find the maximum area of rectangle min(ai, aj) * abs(j - i)
    for i in range(0,n):
    	for j in range(i+1,n):
    while (i < j):
    	area = 0
   	if (intlist[i] < intlist[j]):
    		area = intlist[i] * abs(j-i)
    	else:
    		area = intlist[j] * abs(j-i)
    		j -= 1
    	
    	if area > maxarea:
    		max_i = i
    		max_j = j
    		maxarea = area
    print "a[1] to a[n] is "+ str(intlist)
    print "Maximum water in the container: %s, from a[%s] to a[%s]" %(maxarea, max_i, max_j)

if __name__ == '__main__':
    main()
