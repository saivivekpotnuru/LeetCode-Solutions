# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        if not postorder or not inorder:
            return None
        value=postorder[-1]
        root=TreeNode(value)
        indx=inorder.index(value)
        root.left=self.buildTree(inorder[:indx],postorder[:indx])
        root.right=self.buildTree(inorder[indx+1:],postorder[indx:-1])
        return root