class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cur=0
        ma=0
        for i in nums:
            if(i==1):
                cur+=1
            else: 
                cur=0
            ma=max(ma,cur)
        return ma
                        
        