class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            if(i == len(prices)-1):
                return profit
            current_price = prices[i]
            max_price_except_current = max(prices[i+1:])  
            probable_profit = max_price_except_current - current_price
            if (probable_profit > profit):
                profit = probable_profit
        return profit
