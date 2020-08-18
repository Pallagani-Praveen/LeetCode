# Question Link :- https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3427/
# Level : Easy
# Solution is right below -

class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [ 0 for i in range(num_people) ]
        candie = 1
        ind = 0
        while candies > 0:
            if ind>=num_people:
                ind = 0
            if candie < candies:
                res[ind] += candie
                candies -= candie
                candie += 1
            else:
                res[ind] += candies
                candies = 0
            ind += 1
        return res
        
print('result :',Solution().distributeCandies(10,3))
        
