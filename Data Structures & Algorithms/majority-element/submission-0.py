class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=Counter(nums)
        for key , val in maj.items():
            if val>=len(nums)//2:
                return key
        