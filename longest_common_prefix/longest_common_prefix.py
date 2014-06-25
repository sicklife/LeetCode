#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

def main():
    mystrs = list()
    mystrs.append("ababc")
    mystrs.append("abcbca")
    mystrs.append("acaba")
    #mystrs.append("ab")
    print mystrs

    shortest_len = 5000
    for i in range(0, len(mystrs)):
        if len(mystrs[i]) < shortest_len:
            shortest_len = len(mystrs[i])

    #print "shortest length:%s" % shortest_len
    longest = 0
    i = 0
    while(i < shortest_len):
        counter = 0
        for j in range(1, len(mystrs)):
            if mystrs[j][i] != mystrs[j-1][i]:
                break
            counter += 1
        if counter < len(mystrs) - 1:
            break
        else:
            i += 1
            
    longest = i
    #print longest

    print "Longest Common Prefix is %s" % mystrs[0][0:longest]
if __name__ == '__main__':
    main()