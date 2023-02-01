class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = -1
        for i in range(len(nums)):
            if target > nums[i]:
                pass
            else:
                res = i
                break
        if res == -1:
            return len(nums)
        else:
            return res