import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=high
        while(low<=high):
            m=low+(high-low)//2
            if self.is_valid(piles,h,m):
                ans=m
                high=m-1  
            else:
                low=m+1
        return ans
    def is_valid(self,piles,h,m): #returns the hr for the speed
        hr=0
        for pile in piles:
            hr+=math.ceil(pile/m)
        if hr<=h:
            return hr


        