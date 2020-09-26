# Question Link : https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3472/
# Level : Medium
# Solution is right below :-

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        customCompare = lambda a,b: cmp(b+a,a+b)
        nums = map(str,nums)
        nums = sorted(nums,cmp=customCompare)
        res = "".join(nums)
        return res if res[0]!='0' else '0'
        
print('Max Number :',Solution().largestNumber([3,30,34,5,9]))
