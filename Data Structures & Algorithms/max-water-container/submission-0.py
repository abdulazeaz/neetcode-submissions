class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_total = 0
        left, right = 0, len(heights) - 1

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            vol =  height * width
            
            max_total = max(max_total, vol)
            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
        
        return max_total