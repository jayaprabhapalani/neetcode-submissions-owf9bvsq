class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        ans=0
        l=0
        mapp={}
        for r in range(n):
            mapp[fruits[r]]=mapp.get(fruits[r],0)+1

            while l<=r and len(mapp)>2:
                mapp[fruits[l]]-=1
                # remove that fruit when the cnt is 0
                if mapp[fruits[l]]==0:
                    del mapp[fruits[l]]
                
                l+=1

            ans=max(ans,r-l+1)
        return ans    
            
                       
        