# Question Link : https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3473/
# Level : Easy
# Solution is right below :-

class Solution(object):
    def findPoisonedDuration(self, times, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not times:
            return 0
        tt = 0
        for i in range(len(times)-1):
            if times[i+1]<=times[i]+duration:
                tt += times[i+1]-times[i]
            else:
                tt += duration
        tt += duration
        return tt
        
print('total time :',Solution().findPoisonedDuration([1,2], 2))
