# Question Name : Pseudo-Palindromic Paths in a Binary Tree
# Question Link : https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/573/week-5-december-29th-december-31st/3585/
# Level : Easy
# Logic : Recursion

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    count = 0
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = []
        if root:
            nodes.append(root.val)
            if root.left == None and root.right == None:
                if self.checkPalin(nodes):
                    self.count +=1 
            if root.left != None:
                self.rover(root.left,nodes[:])
            if root.right != None:
                self.rover(root.right,nodes[:])
        return self.count
    
    def rover(self,root,nodes):
        if root:
            nodes.append(root.val)
            if root.left == None and root.right == None:
                if self.checkPalin(nodes):
                    self.count +=1 
            if root.left != None:
                self.rover(root.left,nodes[:])
            if root.right != None:
                self.rover(root.right,nodes[:])
                
    def checkPalin(self,nodes):
        freaks = collections.Counter(nodes)
        count = 0
        for num in freaks:
            if freaks[num]%2!=0:
                count += 1
        return True if count <= 1 else False
