# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        #this is my base case
        if root==None or root==p or root==q:
            return root
        #now i have to check both left and right
        
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        
        #result checking
        if left==None:
            return right
        elif right==None:
            return left
        else:
            return root
        
        