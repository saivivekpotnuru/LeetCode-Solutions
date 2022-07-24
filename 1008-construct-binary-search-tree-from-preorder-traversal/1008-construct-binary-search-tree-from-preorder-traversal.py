# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        stack=[]
        N=len(preorder)
        root = TreeNode(preorder[0])
        
        stack.append(root)
        
        for i in range(1,N):
            #if this value is less than current node, add left 
            if preorder[i]<stack[-1].val:
                stack[-1].left=TreeNode(preorder[i])
                stack.append(stack[-1].left)
            else:
                while stack and preorder[i]>stack[-1].val:
                    last=stack.pop()
                last.right=TreeNode(preorder[i])
                stack.append(last.right)
        return root