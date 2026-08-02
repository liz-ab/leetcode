class Solution(object):
    def subarraySum(self, nums, k):
        count={0:1}
        cursum=0
        ans=0
        for i in nums:
            cursum+=i
            if cursum-k in count:
                ans+=count[cursum-k]
            count[cursum]=1+count.get(cursum,0)
        return ans


        