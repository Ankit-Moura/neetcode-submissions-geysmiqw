class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        profit = 0
        for i in range(len(prices)):
            
            profit = max(prices[i]-mn, profit)
            mn = min(prices[i], mn)

        
        return profit