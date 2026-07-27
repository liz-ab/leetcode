class Solution(object):
    def findNumbers(self, nums):
        ans=0
        for num in nums:
            c=0
            while(num>0):
                c+=1
                num//=10
            if c%2==0:
                ans+=1
        return ans
        