# Question Link : https://leetcode.com/problems/boats-to-save-people/
# Level : Medium
# Solution is right below :


class Solution(object):
    def numRescueBoats(self, people, max_weight):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        
        i,j=0,len(people)-1
        boat_count = 0
        while i<=j:
            boat_count += 1
            if people[i]+people[j]<=max_weight:
                i+=1
            j-=1
        return boat_count
