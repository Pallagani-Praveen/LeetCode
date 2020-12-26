# Question Link : https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3581/

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0] * n
        if s[0] != '0':
            dp[0] = 1
            
            for i in range(1,n):
                if s[i]!='0':
                    dp[i] += dp[i-1]
                if s[i-1]=='1' or (s[i-1]=='2' and int(s[i])<7):
                    if i-2>0:
                        dp[i] += dp[i-2]
                    else:
                        dp[i]+=1
        return dp[-1]
