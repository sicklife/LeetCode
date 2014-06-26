#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

def main():
    mystr = sys.argv[1]
    myint = int(mystr)
    isPalindrome = True

    if myint < 0:
        print "Input integer is not Positive!"
    divider = 1
    while (myint / divider >= 10):
        divider *= 10
    while (myint != 0):
        l = myint / divider
        r = myint % 10
        if l != r:
            isPalindrome = False
        myint = (myint % divider) / 10
        divider /= 100

    if isPalindrome == False:
        print "Input number is not Palindrome"
    else:
        print "Palindrome"
if __name__ == '__main__':
    main()