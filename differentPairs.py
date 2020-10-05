# Question Link : https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3482/
# Level : Easy
# Solution is right below :-

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maper = collections.Counter(nums)
        nums = set(nums)
        count = 0
        if k==0:
            for num in nums:
                if maper[num]>1:
                    count += 1
            return count
        else:
            for num in nums:
                if num+k in nums:
                    count += 1
            return count
        
print('diff-pair count :',Solution().findPairs([1,2,4,4,3,3,0,9,2,3],3))
