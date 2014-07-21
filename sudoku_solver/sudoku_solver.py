import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

def sudoku_solver(board):
	def isValid(x,y):
		tmp = board[x][y]; board[x][y] = 'D'
		for i in range(9):
			if board[i][y]==tmp: return False
		for i in range(9):
			if board[x][i]==tmp: return False
		for i in range(3):
			for j in range(3):
				if board[(x/3)*3+i][(y/3)*3+j]==tmp: return False
		board[x][y] = tmp
		return True
	def dfs(board):
		for i in range(9):
			for j in range(9):
				if board[i][j]=='.':
					for k in '123456789':
						board[i][j] = k
						if isValid(i,j) and dfs(board):
							return True
						board[i][j] = '.'
					return False
		return True
	dfs(board)
def print_2d(arr):
	for i in xrange(len(arr)):
		if (i % 3) == 0:
			print "----------------------"
		for j in xrange(len(arr[i])):
			if (j % 3) == 0:
				sys.stdout.write("|")
			sys.stdout.write(arr[i][j]+" ")
		sys.stdout.write('|\n')
	print "----------------------"
def main():
	input_2d_array = [[".","8","7","6","5","4","3","2","1"],
						["2",".",".",".",".",".",".",".","."],
						["3",".",".",".",".",".",".",".","."],
						["4",".",".",".",".",".",".",".","."],
						["5",".",".",".",".",".",".",".","."],
						["6",".",".",".",".",".",".",".","."],
						["7",".",".",".",".",".",".",".","."],
						["8",".",".",".",".",".",".",".","."],
						[".",".",".",".",".",".",".",".","."]]
	print_2d(input_2d_array)
	sudoku_solver(input_2d_array)
	print "Solver:"
	print_2d(input_2d_array)
	
if __name__ == '__main__':
    main()
