# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        
        def dfs(root: Optional[TreeNode]) -> None:
            nonlocal res
            if not root:
                res.append("N")
                return
            
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Split by ',', then convert to python ds
        raw = list(data.split(','))

        def to_val_or_none(value: str) -> Optional[int]:
            if value == 'N':
                return None
            return int(value)
        
        nodes = map(to_val_or_none, raw)
        
        from collections import deque
        nodes = deque(list(nodes))

        def dfs() -> Optional[TreeNode]:
            if not nodes:
                return None
            
            val = nodes.popleft()
            if val is None:
                return None
            
            root = TreeNode()
            root.val = val
            root.left = dfs()
            root.right = dfs()

            return root
        
        return dfs()

            


