# Question Link : https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3594/
# Level : Medium
# Solution Right Below :-

class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        i = len(arr)-1
        while i>=0 and (arr[i]-1)-(i)-k>=0:
            i-=1
        tn = k-(arr[i]-1-i)
        return arr[i]+tn
