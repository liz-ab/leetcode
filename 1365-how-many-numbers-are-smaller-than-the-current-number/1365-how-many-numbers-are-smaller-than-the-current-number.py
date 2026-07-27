class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        pos={}
        ans=[]
        s_nums=sorted(nums)
        for i in range(len(s_nums)):
            if s_nums[i] not in pos:
                pos[s_nums[i]]=i
        for num in nums:
            ans.append(pos[num])
        return ans