#!usr/bin/python
import cPickle, string, numpy, getopt, sys, random, time, re, pprint
__author__ = ['Yue']
__version__ = "0.0.1"

"""
cons   = lambda el, lst: (el, lst)
mklist = lambda *args: reduce(lambda lst, el: cons(el, lst), reversed(args), None)
car = lambda lst: lst[0] if lst else lst
cdr = lambda lst: lst[1] if lst else lst
nth = lambda n, lst: nth(n-1, cdr(lst)) if n > 0 else car(lst)
length  = lambda lst, count=0: length(cdr(lst), count+1) if lst else count
begin   = lambda *args: args[-1]
display = lambda lst: begin(w("%s " % car(lst)), display(cdr(lst))) if lst else w("nil\n")
"""

class Node: 
    def __init__(self, v=None): 
        self._value = v 
        self._next = None
    def setnext(self, v):
        self._next = v
    def getnext(self):
        return self._next
    def __str__(self): 
        return str(self._value)
    def __int__(self):
        return int(self._value)
class LinkedList:
    def __init__(self, mylist):
        self._length = len(mylist)
        if(len(mylist) == 1):
            self._head = Node(mylist[0])
        else:
            self._head = Node(mylist[0])
            nextNode = Node(mylist[1])
            self._head.setnext(nextNode)
            curNode = nextNode
            for i in range(2, len(mylist)):
                postNode = Node(mylist[i])
                curNode.setnext(postNode)
                curNode = postNode
            curNode.setnext(None)
    def gethead(self):
        return self._head
    def getLen(self):
        return self._length
    def printlist(self):
        if self._head != None:
            curnode = self._head
            while(curnode!=None):
                if curnode.getnext() == None:
                    sys.stdout.write(str(curnode))
                else:
                    sys.stdout.write(str(curnode)+"->")
                curnode = curnode.getnext()
def linkedlist_plus(list1, list2):
    if (list1.getLen()!= list2.getLen()):
        print "Length doesn't match!"
    else:
        result = list()
        curnode1 = list1.gethead()
        curnode2 = list2.gethead()
        carry = (int(curnode1) + int(curnode2))/10
        remain = (int(curnode1) + int(curnode2))%10
        result.append(remain)
        while(curnode1.getnext() != None):
            postnode1 = curnode1.getnext()
            postnode2 = curnode2.getnext()
            cur_carry = (int(postnode1) + int(postnode2))/10
            cur_remain = (int(postnode1) + int(postnode2))%10 + carry
            cur_carry = cur_carry + cur_remain/10
            cur_remain = cur_remain % 10
            carry = cur_carry
            curnode1 = postnode1
            curnode2 = postnode2
            result.append(cur_remain)
        if carry!=0:
            result.append(carry)
        return LinkedList(result)
def main():
        list1 = [2,4,3,6]
        list2 = [5,6,6,2]
        llst1 = LinkedList(list1)
        llst2 = LinkedList(list2)
        llst1.printlist()
        print "\n+"
        llst2.printlist()
        print "\n="
        result = linkedlist_plus(llst1,llst2)
        result.printlist()
        print ""
if __name__ == '__main__':
    main()

