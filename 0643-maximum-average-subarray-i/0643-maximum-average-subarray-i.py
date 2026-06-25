class Solution(object):
    def findMaxAverage(self, nums, k):
        cur_sum = sum(nums[:k])
        max_sum = cur_sum

        for i in range(k, len(nums)):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]
            max_sum = max(max_sum, cur_sum)

        return max_sum / float(k)