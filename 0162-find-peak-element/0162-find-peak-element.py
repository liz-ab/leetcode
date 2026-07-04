class Solution(object):
    def findPeakElement(self, nums):
       if len(nums)==1:
        return 0
       if len(nums)==2:
        if(nums[0]>nums[1]):
            return 0
        else:
            return 1
       l,r=0,1
       while(r<len(nums)-1):
        if(nums[r]>nums[l] and nums[r]>nums[r+1]):
            return r
        else:
            l+=1
            r+=1
       if(nums[r]>nums[l]):
        return r
       return 0 

        