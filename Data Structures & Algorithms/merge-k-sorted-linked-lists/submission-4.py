# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        
        def argmin(lists: List[Optional]) -> int:
            key, val = -1, 1001
            for k, node in enumerate(lists):
                if not node:
                    continue
                
                if node.val < val:
                    val = node.val
                    key = k
            
            return key
        
        while argmin(lists) >= 0:
            key = argmin(lists)
            curr.next = lists[key]
            curr = curr.next
            lists[key] = lists[key].next
        
        return dummy.next

            