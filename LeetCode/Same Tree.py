# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None and q is not None:
            return False
        elif q is None and p is not None:
            return False
        else:
            if p.val != q.val:
                return False
        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)
        if not l or not r:
            return False
        else:
            return True