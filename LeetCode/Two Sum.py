class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i, j]

nums = [2,4,11,3]
target = 6
# Output: [0,1]
print(Solution.twoSum(0, nums, target))
print('resultado deveria ser [0,1]\n')

nums = [2,7,11,15]
target = 9
# Output: [0,1]
print(Solution.twoSum(0, nums, target))
print('resultado deveria ser [0,1]\n')

nums = [3,2,4]
target = 6
# Output: [1,2]
print(Solution.twoSum(0, nums, target))
print('resultado deveria ser [1,2]\n')

nums = [3,3]
target = 6
# Output: [0,1]
print(Solution.twoSum(0, nums, target))
print('resultado deveria ser [0,1]\n')