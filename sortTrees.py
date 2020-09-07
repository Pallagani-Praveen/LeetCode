# Question Link : https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3449/
# Level : Easy
# Solution is right below :-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    
    def inorder(self,node,num,tree):
        if node:
            self.inorder(node.left,num,tree)
            tree.append(node.val)
            self.inorder(node.right,num,tree)
            
    def merge(self,l1,l2):
        i=j=0
        m,n = len(l1),len(l2)
        res = []
        while i<m and j<n:
            if l1[i]<=l2[j]:
                res.append(l1[i])
                i+=1
            else:
                res.append(l2[j])
                j+=1
        while i<m:
            res.append(l1[i])
            i+=1
        while j<n:
            res.append(l2[j])
            j+=1
        return res
            
        
            
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        tree1 , tree2 = [],[]
        self.inorder(root1,1,tree1)
        self.inorder(root2,2,tree2)
        return self.merge(tree1,tree2)
