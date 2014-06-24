#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

def main():
	mystr = sys.argv[1]
	print mystr
	myint = int(mystr)
	print myint
	#I= 1;V = 5;X = 10;L = 50;C = 100;D = 500;M = 1000;
	temp = myint
	while (temp > 0):
		if temp >= 1000:
			first_divider = temp / 1000
			if first_divider < 5:
				while first_divider > 0:
					sys.stdout.write("M")
					first_divider -= 1
			temp = temp % 1000
		elif temp / 900 > 0:
			sys.stdout.write("CM")	
			temp = temp % 900	
		elif temp >= 500:
			sys.stdout.write("D")
			temp = temp % 500
		elif temp / 400 > 0:
			sys.stdout.write("CD")
			temp = temp % 400
		elif temp >= 100:
			first_divider = temp / 100
			if first_divider < 5:
				while first_divider > 0:
					sys.stdout.write("C")
					first_divider -= 1
			temp = temp % 100
		elif temp / 90 > 0:
			sys.stdout.write("XC")
			temp = temp % 90
		elif temp >= 50:
			sys.stdout.write("L")
			temp = temp % 50
		elif temp / 40 > 0:
			sys.stdout.write("XL")
			temp = temp % 40
		elif temp >= 10:
			first_divider = temp / 10
			if first_divider < 5:
				while first_divider > 0:
					sys.stdout.write("X")
					first_divider -= 1
			temp = temp % 10
		elif temp == 9:
			sys.stdout.write("IX")
			temp = 0
		elif temp >= 5:
			sys.stdout.write("V")
			temp = temp % 5
		elif temp == 4:
			sys.stdout.write("IV")
			temp = 0
		else:
			while temp > 0:
				sys.stdout.write("I")
				temp -= 1
	print ""
if __name__ == '__main__':
    main()


