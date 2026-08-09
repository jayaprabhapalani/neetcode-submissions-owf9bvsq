class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        ans=0
        for l in range(n):
            cnt=0
            mapp={}
            for r in range(l,n):
                mapp[fruits[r]]=mapp.get(fruits[r],0)+1

                if len(mapp)>2:
                    break

                cnt+=1
            ans=max(ans,cnt)
        return ans            
        