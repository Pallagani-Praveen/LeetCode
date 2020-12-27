# Question Link : https://leetcode.com/problems/jump-game-iv/
# See hints 1,2
# Level : Hard
# Algo : BFS

class Solution(object):
    
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        graph = {}
        n = len(arr)
        #  bfs graph helper      
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]
                
        currs = [0]
        visited = {0}
        steps = 0
        
        while currs:
            _next = []
            
            for node in currs:
                if node == n-1:
                    return steps
                
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        _next.append(child)
                
                graph[arr[node]] = []
                
                for child in [node-1,node+1]:
                    if 0<= child < n and child not in visited:
                        visited.add(child)
                        _next.append(child)
                
            steps += 1
            currs = _next
        return -1
