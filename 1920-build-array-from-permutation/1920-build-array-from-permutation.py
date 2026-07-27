class Solution(object):
    def buildArray(self, nums):
        ans=[0]*len(nums)
        for i in range (len(nums)):
            x=nums[i]
            ans[i]=nums[x]
        return ans