from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sort = all(earlier >= later for earlier, later in zip(prices, prices[1:]))
        if sort or not prices:
            return 0
        length = len(prices)
        price = 0
        for i in range(0, length - 1):
            if prices[i] < prices[i + 1]:
                price = price + prices[i + 1] - prices[i]
        return price
