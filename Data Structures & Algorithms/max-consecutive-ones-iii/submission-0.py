class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        max_l=0
        

        for i in range(len(nums)):
            z_cnt=0
            for j in range(i,len(nums)):
                if nums[j]==0:
                    z_cnt+=1
                if z_cnt>k:
                    break   
                max_l=max(max_l,j-i+1)

            
        return max_l
        