# Question Link : https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3419/
# Level : Easy Math
# Solttion is right below:-

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        vals = []
        
        for i,c in enumerate(s[::-1]):
            val = (ord(c)-ord('A')+1)*(26**i)
            vals.append(val)
        return sum(vals)
        
        # onliner : return sum([ (ord(c)-ord('A')+1)*(26**i) for i,c in enumerate(s[::-1]) ]) 
       

print('col number :',Solution().titleToNumber('AAA'))
