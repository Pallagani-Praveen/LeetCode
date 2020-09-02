# Question Link : https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3445/
# Level : hard
# Solution is right below :-


class Solution(object):
    maxtime = -1
    def buildTime(self,A):
        h,i,j,k = A
        hour = h*10+i
        minute = j*10+k
        if hour<24 and minute<60:
            self.maxtime = max(self.maxtime,hour*60+minute)
    
    def permutate(self,A,start):
        if start==len(A):
            self.buildTime(A)
            return
        for ind in range(start,len(A)):
            self.swap(A,ind,start)
            self.permutate(A,start+1)
            self.swap(A,ind,start)
    
    def swap(self,A,i,j):
        if i!=j:
            A[i],A[j] = A[j],A[i]
    
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        self.permutate(A,0)
        if self.maxtime == -1:
            return ''
        return '{:02d}:{:02d}'.format(self.maxtime//60,self.maxtime%60)
        
print('Max Time :',Solution().largestTimeFromDigits([1,2,3,4]))
