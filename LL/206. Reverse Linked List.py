# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        prevPtr = None
        nextPtr = None

        while temp != None:
            nextPtr = temp.next
            temp.next = prevPtr
            prevPtr = temp
            temp = nextPtr
        head = prevPtr

        return head
        
