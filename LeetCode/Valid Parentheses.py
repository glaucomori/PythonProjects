class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '()' in s or '[]'in s or '{}' in s:
            s = s.replace('()','').replace('[]','').replace('{}','')
        return True if len(s) ==0 else False        


#1
s = "()"
output = True
print(Solution.isValid(0, s))
print(output)
print()

# 2
s = "()[]{}"
output = True
print(Solution.isValid(0, s))
print(output)
print()

# 3
s = "(]"
output = False
print(Solution.isValid(0, s))
print(output)
print()

# 4
s = "{[]}"
output = True
print(Solution.isValid(0, s))
print(output)
print()