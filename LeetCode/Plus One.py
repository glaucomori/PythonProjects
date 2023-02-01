class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        digits[0] += 1
        for i in range(len(digits)):
            if digits[i] == 10:
                digits[i] = 0
                if i == (len(digits)) - 1:
                    digits.append(1)
                else:
                    digits[i+1] = digits[i+1] + 1
            else:
                break
        digits = digits[::-1]
        return digits