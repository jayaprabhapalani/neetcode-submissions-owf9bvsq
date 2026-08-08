class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        cnt=0
        prd=1
        left=0

        for right in range(len(nums)):
            prd*=nums[right]

            #shrink the left if it when the prd is greater than k
            while prd>=k:
                prd//=nums[left]
                left+=1

            cnt+=right-left+1
        return cnt         
