# Question Link : https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3447/
# Level : Easy
# Solution is right below :-

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range((n//2)):
            re = s[:i+1]
            tn = len(re)
            if n%tn==0:
                qut = n//tn
                if s==re*qut:
                    return True
        return False 

print('is Repeated SubString :',Solution().repeatedSubstringPattern('abcabcabc'))
