# Question Link : https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3451/
# level : Easy
# Solution is right below :-

class Solution(object):
    def wordPattern(self, pattern, strg):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        tokens = strg.split(' ')
        if len(tokens)!=len(pattern):
            return False
        maper = dict()
        for i in range(len(pattern)):
            if pattern[i] in maper:
                if maper[pattern[i]] != tokens[i]:
                    return False
            else:
                maper[pattern[i]] = tokens[i]
        token_set = set(maper.values())
        return len(maper.values()) == len(token_set)
        
print("is patterns matched :",Solution().wordPattern('abba',['dog','cat','cat','dog']))
