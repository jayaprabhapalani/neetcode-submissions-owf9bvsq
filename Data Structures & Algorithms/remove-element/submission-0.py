class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p=[]
        for i in nums:
            if i!=val:
                p.append(i)
        return p    


        