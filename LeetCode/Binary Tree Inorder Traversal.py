# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            if len(stack) == 0:
                break
            
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res