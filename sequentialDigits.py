# Question Link : https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3465/
# Level : Hard
# Solution is right below :-
class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        ls,hs = str(low),str(high)
        n = len(hs)-len(ls)+1
        l = len(ls)
        nums = '123456789'
        res = []
        
        for i in range(n):
            for j in range(9-l+1):
                num = int(nums[j:j+l])
                if num>=low and num<=high: 
                    res.append(num)  
            l+=1
        return res
        
print('Sequence :',Solution().sequentialDigits(1000,3000))
