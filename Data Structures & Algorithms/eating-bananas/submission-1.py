import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        high=max(piles)
        for i in range(l,high+1):
            hr=0
            for pile in piles:
                hr+=math.ceil(pile/i)
            if hr<=h:
                return i

        