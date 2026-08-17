class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums) # from this we can total sum that will give as a adv of r-l summation so we can just dereive the formula
        #left_sum+right_sum+num=total
        #right_sum=total-left_sum-num
        # for pivot left_sum == right_sum
        # so the formula changes to
        #left_sum=total-left_sum-num
        left_sum=0
        for i,num in enumerate(nums):
            if left_sum==total-left_sum-num:
                return i
            left_sum+=num
        return -1


        
        