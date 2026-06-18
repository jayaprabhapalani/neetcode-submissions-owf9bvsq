# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q=deque([root])
        res=[]
        while q:
            cur_len=len(q)
            for _ in range(cur_len):
                node=q.popleft()
                if _ ==cur_len-1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)    
                if node.right:
                    q.append(node.right)  
        return res 

        