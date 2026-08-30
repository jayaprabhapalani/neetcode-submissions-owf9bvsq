class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        ans=low
        while(low<=high):
            m=low+(high-low)//2
            if self.valid_capacity(weights,days,m):
                ans=m
                high=m-1
            else:
                low=m+1
        return ans
    
    def valid_capacity(self,weights,days,m):
        total=0
        cnt=1 # day calculator
        for w in weights:
            if total+w> m:
                cnt+=1
                total=w
            else:
                total+=w
        return cnt<=days # it is valid if the cnt of days is less than or equal to the given days
                

        