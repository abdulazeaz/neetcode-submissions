# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()

        def are_all_none(lists: List[Optional[ListNode]]) -> bool:
            for node in lists:
                if node:
                    return False
            
            return True
        
        def argmin(lists: List[Optional]) -> ListNode:
            key, val = 0, 1001
            for k, node in enumerate(lists):
                if node and node.val < val:
                    val = node.val
                    key = k
            
            return key

        while not are_all_none(lists):
            key = argmin(lists)
            curr.next = lists[key]
            curr = curr.next
            lists[key] = lists[key].next
        
        return dummy.next

            