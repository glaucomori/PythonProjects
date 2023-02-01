class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        mark = None

        if ch in word:
            for i in range(len(word)):
                if word[i] == ch:
                    mark = i
                    break
                else:
                    pass
            word1 = word[:mark+1]
            word1 = word1[::-1]
            word2 = word[mark+1:]
            word = word1 + word2
        return word