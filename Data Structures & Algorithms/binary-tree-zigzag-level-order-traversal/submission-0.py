# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q=deque([root])
        res=[]
        rev=False

        while q:
            level_size=len(q)
            cur_lvl=[]
            for _ in range(level_size):
                node=q.popleft()
                cur_lvl.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if rev:
                cur_lvl.reverse()
            res.append(cur_lvl)            
            rev=not rev
            
        return res    
                

        
        