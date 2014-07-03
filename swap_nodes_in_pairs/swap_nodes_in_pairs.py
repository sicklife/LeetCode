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

def swap_nodes_in_pairs(head):
	dummyNode = ListNode(0) # add a dummy node to avoid special case
	dummyNode.next = head
	head = dummyNode
	prev = head
	curr = prev.next
	if curr == None: return
	succ = curr.next
	while curr and succ:
		curr.next = succ.next
		succ.next = curr
		prev.next = succ
		if curr.next:
			prev = curr
			curr = prev.next
			succ = curr.next
		else:
			break
	return head.next # note that we added a dummy node

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
	sol = swap_nodes_in_pairs(head_node)
	while sol:
		sys.stdout.write("%s," % sol.val)
		sol = sol.next
	print ""
if __name__ == '__main__':
    main()
