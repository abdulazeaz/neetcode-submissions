# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def formTree(self, left: int, right: int) -> TreeNode:
        if left >= right:
            return None
        
        root_val = self.preorder.pop()
        index = self.indexes[root_val]
        root = TreeNode()
        root.val = root_val
        root.left = self.formTree(left, index)
        root.right = self.formTree(index+1, right)
        return root
    

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        # index
        self.indexes = {}
        n = len(inorder)
        for i in range(n):
            current = inorder[i]
            self.indexes[current] = i
        
        self.preorder = list(reversed(preorder))
        l, r = 0, n
        return self.formTree(l, r)
    