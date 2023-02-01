class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        a = 1
        while True:
            if len(nums) > a:
                if nums[a] in nums[:a]:
                    nums.pop(a)
                else:
                    a += 1
            else:
                break
        return len(nums)