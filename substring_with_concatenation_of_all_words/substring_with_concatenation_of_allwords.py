#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
#Reference: http://codesays.com/2014/solution-to-substring-with-concatenation-of-all-words-by-leetcode/

__author__ = ['Yue']
__version__ = "0.0.1"

def find_str(S, L):
	result = []
	# Count the occurrence of each word in L
	occurrence = {}
	totalCount = len(L)
	for element in L:
	    occurrence[element] = occurrence.get(element,0) + 1

	# The frequency of words in current window
	curentOccurrence = {k:0 for k in occurrence.keys()}
	# The length of words in L
	subLen = len(L[0])

	# Travel the S in a Caterpillar method: S[offset:] with step of subLen
	# S[0::subLen] + S[1::subLen] + ... + S[sublen-1::subLen] = all possibility
	for offset in xrange(subLen):
	    currentCount = 0        # Overall occurrence of words in L in current window
	    # The frequency of words in current window is initially set to be zero
	    for k in curentOccurrence:
	        curentOccurrence[k] = 0
	        
	    BeginIndex = offset     # Begin position of current window
	    EndIndex = offset       # End position of current window
	    
	    # Not enough letters to form a qualified string
	    if BeginIndex >= len(S) - subLen * len(L) + 1:      break
	    
	    # As long as there are enough letters to form a qualified string, and the EndIndex
	    # can be moved forwards, we continue our search.
	    while BeginIndex < len(S) - subLen * len(L) + 1 and EndIndex < len(S) - subLen + 1:
	        # Try to move the EndIndex forward
	        while EndIndex < len(S) - subLen + 1:
	            if S[EndIndex:EndIndex + subLen] in occurrence:
	                # Current word appears in L
	                curentOccurrence[S[EndIndex:EndIndex + subLen]] += 1
	                currentCount += 1

	                if curentOccurrence[S[EndIndex:EndIndex + subLen]] > occurrence[S[EndIndex:EndIndex + subLen]]:
	                    # Current word appears too many times. It is impossible for current window to be a
	                    # qualified string.
	                    
	                    # Skip the words in current window, which are before current word's earliest occurrence.
	                    while S[BeginIndex:BeginIndex + subLen] != S[EndIndex:EndIndex + subLen]:
	                        curentOccurrence[S[BeginIndex:BeginIndex + subLen]] -= 1
	                        currentCount -= 1
	                        BeginIndex += subLen
	                        
	                    # Skip current word's earliest occurrence.
	                    curentOccurrence[S[BeginIndex:BeginIndex + subLen]] -= 1
	                    currentCount -= 1
	                    BeginIndex += subLen
	                    EndIndex += subLen
	                    continue
	            else:
	                # Current word does not appear in L. We need to skip it and begin a new search.
	                BeginIndex = EndIndex + subLen
	                EndIndex = BeginIndex
	                currentCount = 0
	                for k in curentOccurrence:
	                    curentOccurrence[k] = 0
	                continue

	            EndIndex += subLen              # Move the EndIndex forward
	            
	            if currentCount == totalCount:
	                # Current window contains a qualified string
	                result.append(BeginIndex)
	                
	                # Move the BeginIndex forward to continue the next search.
	                currentCount -= 1
	                curentOccurrence[S[BeginIndex:BeginIndex+subLen]] -= 1
	                BeginIndex += subLen
	                
	return result

def main():
	s = "barfoothefoobarman"
	l = ["bar", "foo"]
	result = find_str(s, l)
	print "Position of Concatenations of Substrings are:"
	print result
	
if __name__ == '__main__':
    main()
