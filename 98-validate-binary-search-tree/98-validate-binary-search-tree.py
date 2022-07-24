# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        
    #for every node i use a low range and high range
    
        def isvalid(node,left,right):
            
            #if i  reach end of the tree i should return true
            if not node:
                return True
            
            #at every node the val should be greater than right and lower than left
            if not(node.val<right and node.val>left):
                return False
            
            #now we check left subtree and right sub tree
            #for left subtree my left val is -inf and right should be root.val and similarly for right
            return (isvalid(node.left,left,node.val) and isvalid(node.right,node.val,right))
        
        #at first the first and last elements will be -inf and inf
        return isvalid(root,float("-inf"),float("inf"))