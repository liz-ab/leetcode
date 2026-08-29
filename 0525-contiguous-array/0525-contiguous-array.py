class Solution(object):
    def findMaxLength(self, nums):
        prefix={0:-1}
        maxL=0
        s=0
        for i in range(len(nums)):
            if nums[i]==0:
                s-=1
            else:
                s+=1
            if s in prefix:
                length=i-prefix[s]
                maxL=max(length,maxL)
            else:
                prefix[s]=i
        return maxL
            

        