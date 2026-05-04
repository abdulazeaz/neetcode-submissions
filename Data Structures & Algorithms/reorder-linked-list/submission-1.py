# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None

        # Reverse
        while second:
            old = second
            second = second.next
            old.next = prev
            prev = old
        
        first, second = head, prev

        # Merge
        while second:
            f_next = first.next
            s_next = second.next
            first.next = second
            second.next = f_next
            first, second = f_next, s_next
        
        
        




        





        