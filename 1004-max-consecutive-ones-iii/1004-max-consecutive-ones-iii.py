class Solution(object):
    def longestOnes(self, nums, k):
        start=0
        ma=0
        zero_count=0
        for end in range(len(nums)):
            if(nums[end]==0):
                zero_count+=1
            while(zero_count>k):
                if(nums[start]==0):
                    zero_count-=1
                start+=1
            ma=max(ma,end-start+1)
        return ma
            