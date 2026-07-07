class Solution(object):
    def sortColors(self, nums):
        i,mid=0,0
        j=len(nums)-1
        while(mid<=j):
            if(nums[mid]==0):
                nums[mid],nums[i]=nums[i],nums[mid]
                i=i+1
                mid=mid+1
            elif(nums[mid]==1):
                mid=mid+1
            else:
                nums[mid],nums[j]=nums[j],nums[mid]
                j-=1
        return nums
        