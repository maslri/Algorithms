from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            # Update the minimum price if we find a lower price
            if price < min_price:
                min_price = price
            else:
                # Calculate the profit and update max_profit
                max_profit = max(max_profit, price - min_price)
        return max_profit

prices = [3,2,6,5,0,3]
a = Solution()
print(a.maxProfit(prices))