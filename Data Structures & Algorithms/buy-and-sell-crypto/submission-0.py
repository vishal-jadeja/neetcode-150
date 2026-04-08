class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        minPrice = prices[0]
        for price in prices:
            profit = price - minPrice
            maxPro = max(maxPro, profit)
            minPrice = min(minPrice, price)
        return maxPro