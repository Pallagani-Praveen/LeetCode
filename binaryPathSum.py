# Question Link : https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3453/
# Level : Easy
# Solution is right below :-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def getPathSum(self,root,val,bs):
        
        if root and not root.left and not root.right:
            bs += str(root.val)
            val[0] += int(bs,2)
        elif root:
            bs += str(root.val)
            self.getPathSum(root.left,val,bs)
            self.getPathSum(root.right,val,bs)
            
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        val = [0]
        self.getPathSum(root,val,'')
        return val[0]
