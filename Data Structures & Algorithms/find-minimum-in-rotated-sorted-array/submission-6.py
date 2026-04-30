class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        m = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                m = min(m, nums[l])
                break

            mid = (r + l) // 2
            m = min(m, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return m