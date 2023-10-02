class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mins = prices[0]
        maxs = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < maxs:
                res += (maxs - mins)
                mins = prices[i]
                maxs = mins
            else:
                maxs = prices[i]
        return res + maxs - mins