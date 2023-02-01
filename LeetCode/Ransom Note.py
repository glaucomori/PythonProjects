class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        item = list(magazine)
        check = True
        for i in ransomNote:
            if i in item:
                    item.remove(i)
            else:
                check = False
                break

        return check

item1 = 'test'
item2 = 'text'
print(Solution.canConstruct(item1, item1, item2))