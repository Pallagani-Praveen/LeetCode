# Question Link : https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3417/
# Level : Medium 
# Solution is right below:-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    path = 0
    def pathSum(self, root, sumval):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None:
            return 0
        self.helper(root,sumval)
        self.pathSum(root.left,sumval)
        self.pathSum(root.right,sumval)
        return self.path
    
    def helper(self,node,sumval):
        if node!=None and node.val == sumval:
            self.path += 1
        if node != None:
            sumval -= node.val
            self.helper(node.left,sumval)
            self.helper(node.right,sumval)
 #  print('Solution : ',Solution().pathSum('passTheHeadNode','SumVal'))
