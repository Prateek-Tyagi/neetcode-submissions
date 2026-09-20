class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        best = 0
        for price in prices[1:]:
            profit_today = price - cheapest
            best = max(best, profit_today)
            cheapest = min(cheapest, price)

        return best
            





        