#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

#Reference: http://leetcode.com/2011/11/longest-palindromic-substring-part-i.html

def main():
	mystr = sys.argv[1]
	print mystr
	reverse_mystr = mystr[::-1]

	print reverse_mystr
	longest = 0
	# longest common substring of reverse string and original string DOESN'T work
	n = len(mystr)
	longest_begin = 0
	max_len = 1
	table = list()
	for i in range(0,1000):
		temp = list()
		for j in range(0,1000):
			temp.append(-1)
		table.append(temp)
	for i in range(0,1000):
		table[i][i] = 1
	
	for i in range(0,n-1):
		if(mystr[i]==mystr[i+1]):
			table[i][i+1] = 1
			longest_begin = i
			max_len = 2

	for l in range(3, n+1):
		for i in range(0, n - l + 1):
			j = i + l -1
			if (mystr[i]==mystr[j] and table[i+1][j-1]==1):
				table[i][j] = 1
				longest_begin = i
				max_len = l

	print "Length of Longest Palindromic Substring:%s, which is:%s" 
		% (max_len, mystr[longest_begin:longest_begin+max_len])
if __name__ == '__main__':
    main()

