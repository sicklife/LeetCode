#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def removeNthFromEnd(head, n):
    	i = 0
    	j = 0
    	first_ptr = head
    	second_ptr = head
    	while (j<n):
    		if second_ptr.next:
    			second_ptr = second_ptr.next
    			j += 1

    	if j == n - 1:
    		head = head.next
    		return head

    	else:
	    	while second_ptr.next:
	    		first_ptr = first_ptr.next
	    		second_ptr = second_ptr.next

	    	first_ptr.next = first_ptr.next.next

	    	return head

def main():
	newnode = ListNode(2)
	head_node = newnode

	for i in range(0,10):
		temp = ListNode(random.randint(1,10))
		newnode.next = temp
		newnode = temp
		
	phead = head_node
	while phead:
		sys.stdout.write("%s," % phead.val)
		phead = phead.next
	print ""
	sol = removeNthFromEnd(head_node,1)
	while sol:
		sys.stdout.write("%s," % sol.val)
		sol = sol.next
	print ""
if __name__ == '__main__':
    main()
