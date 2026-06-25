class Solution(object):
    def findMaxAverage(self, nums, k):
        n=len(nums)
        cur_sum=0
        for i in range(k):
            cur_sum+=nums[i]
        maxAvg=cur_sum/float(k)
        for i in range(k,n):
            cur_sum+=nums[i]
            cur_sum-=nums[i-k]
            avg=cur_sum/float(k)
            maxAvg=max(maxAvg,avg)
        return maxAvg