# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def helper(left, right):
            if not left and not right:
                return True
            
            if left and right:
                return left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left)
            
            return False
        
        return helper(root.left, root.right)