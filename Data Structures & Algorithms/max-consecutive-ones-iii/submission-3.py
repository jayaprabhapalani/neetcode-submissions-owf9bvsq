class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        if len(nums)==0:
            return 0
        max_l=0
        left=0
        z_cnt=0
        
        for right in range(len(nums)): 
            if nums[right]==0:
                    z_cnt+=1

            # shrinking the left pointer until it reaches the 
            #appropriate ptr to start the calculation again
            #so we can reduce the cost
            while(z_cnt>k):
                if(nums[left]==0):
                    z_cnt-=1
                left+=1

            max_l=max(max_l,right-left+1)
        
        return max_l
        