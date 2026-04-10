class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        def is_valid(speed):
            time=0
            for pile in piles:
                time+=math.ceil(pile/speed)  
            return time<=h 
        while l<r:
            m=(l+r)//2
            if is_valid(m):
                r=m
            else:
                l=m+1
        return l
          



        