#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"
def main():
	mystr = sys.argv[1]
	#print mystr
	counter = len(mystr)/2
	#print "counter:%s"%counter
	longest = 0
	for i in range(1,counter):
		for j in range (0,len(mystr)-i):
			ptr = 1
			while(ptr<len(mystr)-i):
				if (mystr[j:j+i] == mystr[j+ptr:j+i+ptr]) and (i > 1) and (mystr[j:j+1] != mystr[j+1:j+2]):
					longest = i
				ptr += 1
	print "Length of Longest Substring Without Repeating Character:%s" % longest
if __name__ == '__main__':
    main()