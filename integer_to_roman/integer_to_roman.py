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
	
	result = ""
	while (temp > 0):
		if temp >= 1000:
			first_divider = temp / 1000
			if first_divider < 5:
				while first_divider > 0:
					result += "M"
					first_divider -= 1
			temp = temp % 1000
		elif temp / 900 > 0:
			result += "CM"	
			temp = temp % 900	
		elif temp >= 500:
			result += "D"
			temp = temp % 500
		elif temp / 400 > 0:
			result += "CD")\
			temp = temp % 400
		elif temp >= 100:
			first_divider = temp / 100
			if first_divider < 5:
				while first_divider > 0:
					result += "C"
					first_divider -= 1
			temp = temp % 100
		elif temp / 90 > 0:
			result += "XC"
			temp = temp % 90
		elif temp >= 50:
			result += "L"
			temp = temp % 50
		elif temp / 40 > 0:
			result += "XL"
			temp = temp % 40
		elif temp >= 10:
			first_divider = temp / 10
			if first_divider < 5:
				while first_divider > 0:
					result += "X"
					first_divider -= 1
			temp = temp % 10
		elif temp == 9:
			result += "IX"
			temp = 0
		elif temp >= 5:
			result += "V"
			temp = temp % 5
		elif temp == 4:
			result += "IV"
			temp = 0
		else:
			while temp > 0:
				result += "I"
				temp -= 1
	print ""
if __name__ == '__main__':
    main()


