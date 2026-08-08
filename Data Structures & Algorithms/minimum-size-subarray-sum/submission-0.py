class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        min_l=float('inf')
        s=0

        for right in range(len(nums)):
            s+=nums[right]

            while s>=target:
                min_l=min(min_l,right-left+1)
                s-=nums[left]
                left+=1

        return min_l if min_l!=float('inf') else 0
        