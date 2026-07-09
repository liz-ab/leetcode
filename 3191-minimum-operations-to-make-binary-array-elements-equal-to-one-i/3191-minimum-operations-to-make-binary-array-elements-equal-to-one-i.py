class Solution(object):
    def minOperations(self, nums):
        l=0
        k=2
        c=0
        while(k<len(nums)):
            if(nums[l]==0):
                l=l+1
                nums[l]=abs(1-nums[l])
                nums[k]=abs(1-nums[k])
                k=k+1
                c+=1
            else:
                l+=1
                k+=1
        while(l<len(nums)):
            if(nums[l]==1):
                l+=1
            else:
                return -1
        return c
            


