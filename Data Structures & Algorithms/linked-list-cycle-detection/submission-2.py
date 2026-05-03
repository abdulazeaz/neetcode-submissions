# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast slow pointers
        dummy = ListNode()
        dummy.next = head

        fast = dummy.next.next if dummy.next else None
        slow = dummy.next

        while fast != None:
            if slow == fast:
                return True
            
            fast = fast.next.next if fast.next else None
            slow = slow.next
        
        return False
