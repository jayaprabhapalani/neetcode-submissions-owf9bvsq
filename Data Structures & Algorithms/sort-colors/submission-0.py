class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt_zero,cnt_one,cnt_two=0,0,0
        # calculate the count of each val and store in a counter
        for i in nums:
            if i ==0:
                cnt_zero+=1
            elif i==1:
                  cnt_one+=1
            else:
               cnt_two+=1
        #use the counter with while loop to do inplace modification
        i=0 #pointer starts with 0th idx
        while (cnt_zero>0):
            nums[i]=0
            i+=1
            cnt_zero-=1
        while (cnt_one>0):
            nums[i]=1
            i+=1
            cnt_one-=1
        while (cnt_two>0):
            nums[i]=2
            i+=1
            cnt_two-=1
                   

        