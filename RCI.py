# Question : https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3483/
# Level : Easy
# Solution right below :-

class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        intervals.sort(key=lambda x:(x[0],-x[1]))
        res = [intervals[0]]
        for i,j in intervals[1:]:
            if j > res[-1][1]:
                res.append([i,j])
        return len(res)
        
print("Solution :",[[3,10],[4,10],[5,11]])
