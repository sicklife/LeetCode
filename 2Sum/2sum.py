#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

#Reference: http://chaoren.is-programmer.com/posts/42597.html

# 多年之后，再看这个，感慨万千
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        t_dict = {target-nums[i]: i for i in range(len(nums))}
         # print t_dict

        for i in range(len(nums)):
            if t_dict.get(nums[i]) and i != t_dict.get(nums[i]):
                return [i, t_dict[nums[i]]]

def two_sum(mylist, target):
	#mylist = sorted(mylist)
	d = dict()
	n = len(mylist)
	for i in xrange(n):
		d[mylist[i]] = [i+1] if mylist[i] not in d else d[mylist[i]]+[i+1]
	
	for i in mylist:
		if target - i in d:
			if i == target - i and len(d[i]) == 2:
				return (d[i][0], d[i][1])
			else:
				return (d[i][0], d[target - i][0]) if d[i][0] < d[target - i][0] else (d[target - i][0], d[i][0])

def main():
	inputlist = list()
	for i in range(0,20):
		inputlist.append(random.randint(-20,20))
	target = 10
	result = two_sum(inputlist, target)	
	print "inputlist:%s" % inputlist
	print "target:%s" % target
	print "Indices of two numbers:"	
	print result
if __name__ == '__main__':
    main()

