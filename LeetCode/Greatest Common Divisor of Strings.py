class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        smallest = str1 if len(str1) < len(str2) else str2
        temp = ""
        final = ""
        for char in smallest:
            temp += char
            if len(str1) % len(temp) != 0 or len(str2) % len(temp) != 0 or ''.join(str1.split(temp)) != '' or ''.join(str2.split(temp)) != '':
                continue
            else:
                final = temp
        return final        
