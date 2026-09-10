# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidIntervalBST(self, root: Optional[TreeNode], interval: tuple[int, int]) -> bool:
        if not root:
            return True

        lower, upper = interval

        if not (lower < root.val < upper):
            return False
        
        return self.isValidIntervalBST(root.left, interval=(lower, root.val)) and \
            self.isValidIntervalBST(root.right, interval=(root.val, upper))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        upper = math.inf
        lower = -math.inf

        return self.isValidIntervalBST(root, interval=(lower, upper))