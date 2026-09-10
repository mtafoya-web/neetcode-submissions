class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < buy:
                buy = price
            else:
                buy = min(buy, price)
            diff = price - buy
            max_profit = max(max_profit, diff)

        return max_profit 