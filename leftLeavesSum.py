# Question Link : https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3435/
# Level : Medium
# Solution is right below :

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    leftSum = 0
    def helper(self,root,flag):
        if root:
            if flag and root.left==None and root.right==None:
                self.leftSum += root.val
            else:
                self.helper(root.left,True)
                self.helper(root.right,False)
            
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            self.helper(root.left,True)
            self.helper(root.right,False)
            return self.leftSum
        else:
            return 0
