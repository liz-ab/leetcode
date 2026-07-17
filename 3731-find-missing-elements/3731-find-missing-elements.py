class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l=min(nums)
        r=max(nums)
        nums=set(nums)
        ans=[]
        for i in range(l,r+1,1):
            if i not in nums:
                ans.append(i)
        return ans
