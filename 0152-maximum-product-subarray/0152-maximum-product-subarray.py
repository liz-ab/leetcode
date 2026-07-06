class Solution(object):
    def maxProduct(self, nums):
        if len(nums)==1:
            return nums[0]
        min_max=nums[0]
        max_max=nums[0]
        res=nums[0]
        for i in range (1,len(nums)):
            cur=nums[i]
            if(cur<0):
                min_max,max_max=max_max,min_max
            min_max=min(cur,cur*min_max)
            max_max=max(cur,cur*max_max)
            res=max(res,max_max)
        return res