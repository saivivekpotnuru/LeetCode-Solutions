# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        flag=True
        
        res=[]
        q=[root]
        while q:
            level=[]
            for i in range(len(q)):
                node=q.pop(0)
                if flag:
                    level.append(node.val)
                else:
                    level.insert(0,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            flag = not flag
            res.append(level)
        return res

            