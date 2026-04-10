class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        has_duplicates=False
        for i in nums:
            if i in seen:
                has_duplicates=True
                break
            seen.add(i)  
        return has_duplicates       
         