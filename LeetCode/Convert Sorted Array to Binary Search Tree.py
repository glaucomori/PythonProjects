# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        i = len(nums)//2
        root = TreeNode(val = nums[i])
        root.left = self.sortedArrayToBST(nums[0:i])
        root.right = self.sortedArrayToBST(nums[i+1:])
        return root