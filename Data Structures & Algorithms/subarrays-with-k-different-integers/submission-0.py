class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ans=0
        for l in range(len(nums)):
            mapp={}
            for r in range(l,len(nums)):
                mapp[nums[r]]=mapp.get(nums[r],0)+1

                if len(mapp)>k:
                    break

                if len(mapp)==k:
                    ans+=1
        return ans            
                
        