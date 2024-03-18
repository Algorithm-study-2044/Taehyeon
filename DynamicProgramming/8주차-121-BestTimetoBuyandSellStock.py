class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0
        for right in range(1, len(prices)):
            if prices[right-1] < prices[left]:
                left = right-1
            temp_profit = prices[right] - prices[left]
            profit = max(profit, temp_profit)
        return profit