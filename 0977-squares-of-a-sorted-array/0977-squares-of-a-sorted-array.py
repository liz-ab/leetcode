class Solution(object):
    def sortedSquares(self, nums):
        res=[0]*len(nums)
        i=0
        j=len(nums)-1
        for k in range(len(nums)-1,-1,-1):
            if(abs(nums[i])>abs(nums[j])):
                res[k]=nums[i]*nums[i]
                i+=1
            else:
                res[k]=nums[j]*nums[j]
                j-=1
        return res
        