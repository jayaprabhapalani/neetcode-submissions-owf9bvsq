class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        cnt=0
        for i in range(len(nums)):
            prd=1
            for j in range(i,len(nums)):
                prd*=nums[j]

                if prd<k:
                    cnt+=1

                else:
                    break
        return cnt                


             

           

    