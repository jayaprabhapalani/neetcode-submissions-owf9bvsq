class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # two steps to solve this problem
        # first calculating all the valid subarrays which till atMost(K)
        # then exact cnt at K exact(K)=atMost(K)-atMost(K-1)
        def atMost(k:int)->int:
            cnt=0
            l=0
            mapp={}
            for r in range(len(nums)):
                mapp[nums[r]]=mapp.get(nums[r],0)+1

                #shrink window until it has at most k distinct element
                while l<=r and len(mapp)>k:
                    mapp[nums[l]]-=1
                    if mapp[nums[l]]==0:
                        del mapp[nums[l]]
                    l+=1
                
                #no of valid subarrays ending at r is the window lenght
                cnt+=r-l+1

            return cnt

        return atMost(k)-atMost(k-1)   


                
        