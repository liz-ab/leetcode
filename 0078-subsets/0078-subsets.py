class Solution(object):
    def subsets(self, nums):
        subset=[]
        res=[]
        def dfs(i):
            if i>=len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res

        