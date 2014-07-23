#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

def combination_sum(candidates, target):
	result = []
        
	# We add a 0 at the head of candidates. If the length of
	# of original answer is M, the answer here will be length
	# of "limit", with original answer M and additional 
	# (limit - M) 0s.
	candidates.append(0)
	candidates.sort()

	# The maximum number of items in one answer set
	limit = target // candidates[1]
	if limit == 0:          return []
	if limit == 1:
		if target in candidates:    return [[target]]
		else:                       return []

	# The pointers used for n-sum. The time complexity is O(M^(n-1))
	pointers = [0] * limit
	pointers[-1] = len(candidates) - 1

	while pointers[0] < len(candidates):
		preSum = sum([candidates[i] for i in pointers[:-2]])
		if preSum + candidates[pointers[-2]] + candidates[pointers[-2]] > target:
			# All combinations in this round are too big
			pass
		elif preSum + candidates[pointers[-1]] + candidates[pointers[-1]] < target:
			# All combinations in this round are too small
			pass
		else:
			while pointers[-2] <= pointers[-1]:
				temp = preSum + candidates[pointers[-2]] + candidates[pointers[-1]]
				moveAhead, moveBack = False, False

				if temp > target:
					moveBack = True
				elif temp < target:
					moveAhead = True
				else:
					# Found a qualified combination
					result.append([candidates[i] for i in pointers if candidates[i] != 0])
					moveAhead, moveBack = True, True
				if moveBack:
					pointers[-1] -= 1
					while pointers[-2] <= pointers[-1] and \
							candidates[pointers[-1]] == candidates[pointers[-1]+1]:
						pointers[-1] -= 1
				if moveAhead:
				    pointers[-2] += 1
				    while pointers[-2] <= pointers[-1] and \
				    		candidates[pointers[-2]] == candidates[pointers[-2]-1]:
						pointers[-2] += 1

		# Adjust the pointers for the next round n-sum trying
		pointerIndex = limit - 3
		while pointerIndex >= 0:
		    pointers[pointerIndex] += 1
		    while pointers[pointerIndex] < len(candidates) and \
		          candidates[pointers[pointerIndex]] == candidates[pointers[pointerIndex]-1]:
		        pointers[pointerIndex] += 1
		    
		    if pointers[pointerIndex] == len(candidates):     pointerIndex -= 1
		    else:                                             break
		else:                                                 break

		for i in xrange(pointerIndex+1, limit-1):     pointers[i] = pointers[pointerIndex]
		pointers[-1] = len(candidates) - 1

	return result

def main():
	inputlist = list()

	for i in range(0, 20):
		inputlist.append(random.randint(0,10))

	print inputlist

	target = 5
	result = combination_sum(inputlist, target)
	print "Result:"
	print result
	
if __name__ == '__main__':
    main()
