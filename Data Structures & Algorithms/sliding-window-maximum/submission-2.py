from collections import deque
from typing import List
class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q=deque() # to store the indicies
        res=[]

        for i in range(len(nums)):
            # remove elements smaller than the curr one
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            #append the current element index    
            q.append(i)

            #remove the index which are not part of the curr window
            if q[0]<=i-k:
                q.popleft()
            
            #add max of that window to the res (max is always at 0 the index)once the first window is complete
            if i>=k-1:
                res.append(nums[q[0]])
        return res    
            


        
             

        