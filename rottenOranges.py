# Question Link : https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3418/
# Level : medium
# Solution is right below:-

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rotten,fresh = [],0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    rotten.append((i,j))
                elif grid[i][j]==1:
                    fresh += 1
        time,dirs = 0,[[1,0],[0,1],[-1,0],[0,-1]]
        
        while len(rotten)!=0 and fresh>0:
            time += 1
            size = len(rotten)
            while size > 0:
                size -= 1
                ind = rotten.pop(0)
                for x,y in dirs:
                    xx,yy = ind[0]+x,ind[1]+y
                    if xx<0 or xx>=len(grid) or yy <0 or yy>=len(grid[0]) or grid[xx][yy]==0 or grid[xx][yy]==2:
                        continue
                    grid[xx][yy] = 2
                    rotten.append((xx,yy))
                    fresh -= 1
        return time if fresh==0 else -1

print('No of minutes :',Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))

