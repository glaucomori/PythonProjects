# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res = []
        while head is not None:
            res.append(str(head.val)) 
            head = head.next
        return res == res[::-1]        
