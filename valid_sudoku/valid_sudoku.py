#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"
#Reference: http://codesays.com/2014/solution-to-valid-sudoku-by-leetcode/
def valid_sudoku(board):
	char2int = {".":0, "1":1, "2":2, "3":4, "4":8, "5":16, "6":32, "7":64, "8":128, "9":256}
	board = [[char2int[item] for item in line] for line in board]
	# Check each row
	for i in xrange(9):
		sum  = 0
		for value in board[i]:
			if sum & value != 0:                
				return False
			sum = sum | value
	        
	# Check each column
	for i in xrange(9):
		sum = 0
		for row in xrange(9):
			if sum & board[row][i] != 0:
				return False
			sum = sum | board[row][i]

	# Check each block
	for iBlock in xrange(3):
		for jBlock in xrange(3):
			sum = 0
			for i in xrange(3):
				for j in xrange(3):
					if sum & board[iBlock*3+i][jBlock*3+j] != 0:
						return False
					sum = sum | board[iBlock*3+i][jBlock*3+j]

	return True



def main():
	input_2d_array=[".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
	print input_2d_array
	result = valid_sudoku(input_2d_array)
	if result is False:
		print "NOT VALID"
	else:
		print "VALID"
	
if __name__ == '__main__':
    main()