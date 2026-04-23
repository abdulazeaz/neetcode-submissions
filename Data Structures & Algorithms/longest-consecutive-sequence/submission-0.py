class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # unique = set()
        
        # for num in nums:
        #     unique.add(num)
        
        # max_seq = 0
        # cur_len = 1
        # unique = list(unique)

        # print(unique)

        # for i in range(1, len(unique)):
        #     if (unique[i] - unique[i-1]) == 1:
        #         cur_len += 1
        #     else:
        #         cur_len = 1

        #     max_seq = max(max_seq, cur_len)

        
        # return max_seq
        longest = 0
        for num in nums:
            length = 1
            cur = num

            while cur + 1 in nums:
                cur += 1
                length += 1
            
            longest = max(longest, length)
        
        return longest

        