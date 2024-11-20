# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # result = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         diff = prices[i] - prices[j]
        #         if diff < result:
        #             result = diff
        # return -result

        price = prices[0]
        result = 0
        for i in range(1, len(prices)):
            # the profit will be higher if the new price is lower than what it was previously
            if prices[i] < price:
                price = prices[i]
            # update the profit if it's greater than what it was before
            elif prices[i] - price > result:
                result = prices[i] - price
        return result


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 5
