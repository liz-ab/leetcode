class Solution(object):
    def subsets(self, nums):
        ret=[[]]
        for n in nums:
            ret+=[r+[n] for r in ret]
        return ret
        