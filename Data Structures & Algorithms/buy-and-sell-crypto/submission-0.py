class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1

        pmax = 0
        while r < len(prices):
            p_l = prices[r] - prices[l]
            if p_l > pmax:
                pmax = p_l
            else:
                l = r if prices[r] < prices[l] else l
            r += 1
        
        return pmax
            

