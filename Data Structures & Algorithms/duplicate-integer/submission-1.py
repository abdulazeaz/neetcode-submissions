class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def hasDuplicate(self, nums: List[int]) -> bool:
        mem = set()

        for num in nums:
            if num in mem:
                return True
            mem.add(num)
        
        return False
