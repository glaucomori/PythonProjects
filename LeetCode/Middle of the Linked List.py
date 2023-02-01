# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        init_list = []

        while head is not None:
            init_list.append(str(head.val)) 
            head = head.next

        range_lista = len(init_list)

        init = (range_lista // 2) + 1
        final_list = init_list[:init]

        return final_list