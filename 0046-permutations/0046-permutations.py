class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        check={num:False for num in nums}
        def backtrack(current,check):
            if(len(current)==len(nums)):
                res.append(current.copy())
                return
            for i in nums:
                if check[i]:
                    continue
                check[i]=True
                current.append(i)
                backtrack(current,check)
                current.pop()
                check[i]=False
        backtrack([],check)
        return res