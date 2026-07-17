class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        target=1
        nums=set(nums)
        while target in nums:
            target+=1
        return target