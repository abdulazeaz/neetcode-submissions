# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = left = ListNode()
        dummy.next = right = head

        # initialize right
        i = 0
        while i < n and right:
            right = right.next
            i += 1
        
        while right:
            left = left.next
            right = right.next
        
        # delete
        tmp = left.next
        left.next = tmp.next

        return dummy.next
        



