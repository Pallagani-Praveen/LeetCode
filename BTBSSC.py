# Question Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# Level : hard
# Solution is right below :-


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        maxProfit = defaultdict(lambda: 0)
        bestEntry = -prices[0] #max(-prices[j] + maxProfit[j-2] )
        for i in range(1, len(prices)):
            maxProfit[i] = maxProfit[i-1]
            maxProfit[i] = max(maxProfit[i], prices[i]+bestEntry)
            bestEntry =max(bestEntry, -prices[i]+maxProfit[i-2])        
        return maxProfit[len(prices)-1]
 
 print('Max Profit :',Solution().maxProfit([1,2,3,0,2]))
