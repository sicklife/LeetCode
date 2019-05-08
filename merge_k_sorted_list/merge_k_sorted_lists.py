#!/usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint, heapq
__author__ = ['Yue']
__version__ = "0.0.1"


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @param a list of ListNode
# @return a ListNode
def merge_k_sorted_lists(lists):
    heap = []
    for node in lists:
        if node != None: heap.append((node.val, node))
    heapq.heapify(heap)
    head = ListNode(0); curr = head
    while heap:
        pop = heapq.heappop(heap)
        curr.next = ListNode(pop[0])
        curr = curr.next
        if pop[1].next: heapq.heappush(heap, (pop[1].next.val, pop[1].next))
    return head.next

# 暴力方法
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


def main():
    headnodes = list()

    for i in range(0, 20):
        hnode = ListNode(random.randint(0,50))
        temp = hnode
        for j in range(0,9):
            temp.next = ListNode(random.randint(0,50))
            temp = temp.next
        headnodes.append(hnode)
    for i in range (0, len(headnodes)):
        tmp = headnodes[i]
        tmplist = list()
        while tmp:
            tmplist.append(tmp.val)
            tmp = tmp.next
        print tmplist
    result = merge_k_sorted_lists(headnodes)
    print "First node of merged sorted list is:"
    print result.val
    
if __name__ == '__main__':
    main()
