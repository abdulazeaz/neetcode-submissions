# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def visit(self, node: TreeNode) -> None:
        self.nodes.append(node.val)
    
    def traverse(self, node: Optional[TreeNode]):
        if node:
            self.traverse(node.left)
            self.visit(node)
            self.traverse(node.right)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nodes = []
        self.traverse(root)
        
        return self.nodes[k-1]
            