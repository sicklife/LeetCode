__Author__ = ["Zhao"]
__Version__ = "0.0.1"
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 0 是一个占位符
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                # cur可以理解为一个游标
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            # 将cur指向其子节点
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
        
