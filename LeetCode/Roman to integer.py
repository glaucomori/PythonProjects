class Solution:
    def __init__(self) -> None:
        pass

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = s
        integer = []
        result = 0
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000

        roman = roman[::-1]

        for i in range(len(roman)):
            if roman[i] == 'I':
                integer.append(1)
            elif roman[i] == 'V':
                integer.append(5)
            elif roman[i] == 'X':
                integer.append(10)
            elif roman[i] == 'L':
                integer.append(50)
            elif roman[i] == 'C':
                integer.append(100)
            elif roman[i] == 'D':
                integer.append(500)
            elif roman[i] == 'M':
                integer.append(1000)

        for i in range(len(integer)):
            if i == 0:
                result = integer[0]
            elif integer[i] < integer[i-1]:
                result -= integer[i]
            else:
                result += integer[i]

        return result