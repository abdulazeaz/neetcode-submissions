# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
           return None
        
        if list1 == None or list2 == None:
            return list1 if list1 != None else list2
        
        prev, head = None, None
        c1, c2 = list1, list2

        while c1 or c2:
            if not c1:
                prev.next = c2
                prev = c2
                c2 = c2.next
                continue
            
            if not c2:
                prev.next = c1
                prev = c1
                c1 = c1.next
                continue

            if c1.val <= c2.val:
                if prev:
                    prev.next = c1
                else:
                    head = c1
                
                prev = c1
                c1 = c1.next
            else:
                if prev:
                    prev.next = c2
                else:
                    head = c2
                
                prev = c2
                c2 = c2.next
        
        return head
        
                
       