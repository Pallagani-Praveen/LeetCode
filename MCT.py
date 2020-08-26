# Question Link : https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3436/
# Level : Hard
# Solution right below :-

class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        def dp(day):
            if day>days[-1]:
                return 0
            if memo[day]:
                return memo[day]
            if(day in days):
                ans = min(dp(day+1)+costs[0],dp(day+7)+costs[1],dp(day+30)+costs[2])
            else:
                ans = dp(day+1)
            memo[day] = ans 
            return ans
            
        memo = [False]*(days[-1]+1)
        return dp(1)
        
print('Min Cost :',Solution().mincostTickets([1,4,6,7,8,20],[2,7,15]))
