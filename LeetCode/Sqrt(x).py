class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        sqrt = 1
        while True:
            if (sqrt * sqrt) > x:
                result = sqrt - 1
                break
            else:
                sqrt += 1
        return result