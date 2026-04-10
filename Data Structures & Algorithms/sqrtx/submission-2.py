class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x

        l=0
        r=x
        while l<r:
            m=(l+r)//2
            sq=m*m
            if sq<=x:
                l=m+1
            else:
                r=m
        return l-1            


        