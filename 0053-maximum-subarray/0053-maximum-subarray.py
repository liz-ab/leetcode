class Solution(object):
    def maxSubArray(self, nums):
        if(len(nums)==1):
            return nums[0]
        if(len(nums)==2):
            return max(sum(nums),max(nums))
        cur=0
        ma=0
        for i in nums:
            cur+=i
            ma=max(cur,ma)
            if cur<0:
                cur=0
        if(ma>0):
            return ma
        else:
            return max(nums)

       
        