class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        
        for i in range(low,high+1):
            total=0
            cnt=1 # day calculator
            for w in weights:
                if total+w> i:
                    cnt+=1
                    total=w
                else:
                    total+=w
            if cnt>days:
                cnt=0
            else:
                return i

        