class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        def reverse(start,stop):
            while start<stop:
                nums[start],nums[stop]=nums[stop],nums[start]
                start+=1
                stop-= 1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
               
        