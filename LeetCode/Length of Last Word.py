class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        string = s.rstrip()
        string = string.split(' ')
        string = string[::-1]
        return (len(string[0]))