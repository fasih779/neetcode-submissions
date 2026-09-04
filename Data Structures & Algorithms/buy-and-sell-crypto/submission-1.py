class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        for i in range(len(prices) - 1, -1, -1):
            sell = prices[i]
            buy = min(prices[:i]) if i > 0 else sell
            profit = max(profit, sell - buy)

        return max(0, profit)