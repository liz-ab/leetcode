class Solution(object):
    def removeDuplicates(self, nums):
        j=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[j]:
                nums[i],nums[j+1]=nums[j+1],nums[i]
                j+=1
        return j+1

        