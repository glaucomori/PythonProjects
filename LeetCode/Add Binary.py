class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1]
        b = b[::-1]
        resulta = 0
        resultb = 0
        for i in range(len(a)):
            resulta += int(a[i]) * 2**i
        for i in range(len(b)):
            resultb += int(b[i]) * 2**i
        result = resulta + resultb
        result = bin(result)
        return result[2:]