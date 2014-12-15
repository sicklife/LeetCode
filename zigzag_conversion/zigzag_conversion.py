#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint

__author__ = ['Yue']
__version__ = "0.0.1"

def zigzag_conversion(mystr, nrows):
	print mystr

	if nrows <= 1:
		return mystr

	if len(mystr) == 0:
		return ""

	result = ""
	size = 2 * nrows - 2
	for i in range(0, nrows):
		j = i
		while(j < len(mystr)):
			result += mystr[j]
			if i != 0 and i != nrows - 1 and\
				j + size-2*i < len(mystr):
				result += mystr[j+size-2*i]
			j += size

	return str(result)
	

def zigzag(mystr, n):
    a = [[] for i in range(int(n)) ]	#创建一个list，包含n个空list，
    strlist = list(mystr) #将原始字符串变为一个list
    i = 0 #计数器
    counter = -1 #变向器
    while strlist != []:
        a[i].append(strlist.pop(0)) #用pop()函数将原始字符串内的字母，填入相应的list内
        if i % (int(n)-1) == 0: 
            counter += 1 #到头后，变向。
        i += (-1) ** counter #计数器，决定下一次填入的list
    for j in a:
        for i in j:
            print(i, end='')

if __name__ == '__main__':
    zigzag('aaaabbbbccccdddd', 4)

	
def main():
	mystr = sys.argv[1]
	n = int(sys.argv[2])
	result = zigzag_conversion(mystr,n)		
	print result
if __name__ == '__main__':
    main()
