# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = second = ListNode()
        dummy.next = first = head




        N = 0
        while first:
            first = first.next
            N += 1
        
        i = 0
        while i < N - n:
            second = second.next
            i += 1
        
        # Delete next
        tmp = second.next
        second.next = tmp.next

        return dummy.next

