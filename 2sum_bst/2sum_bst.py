# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        t_set = set()
        
        # 闭包+递归
        def find(c_node):
            if not c_node:
                return False
            if (k - c_node.val) in t_set:
                return True
            else:
                t_set.add(c_node.val)
            # 这个or是算法的关键和精髓
            return find(c_node.right) or find(c_node.left)
        
        return find(root)
                    
                
        
        
        
