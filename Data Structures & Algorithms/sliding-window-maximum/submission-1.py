class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res=[]
        for l in range(len(nums)-k+1):
            mapp={}
            max_val=float('-inf')
            for r in range(l,l+k):
                max_val=max(max_val,nums[r])

            res.append(max_val)
        return res

        