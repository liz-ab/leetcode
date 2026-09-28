class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums)%2:
            return False
        dp=set()
        target=sum(nums)//2
        dp.add(0)
        for i in range(len(nums)-1,-1,-1):
            nextDP=set()
            for n in dp:
                nextDP.add(n)
                nextDP.add(n+nums[i])
            dp=nextDP
        return True if target in dp else False