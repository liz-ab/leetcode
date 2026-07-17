class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        for i in range(k):
            res=nums.pop()
            nums.insert(0,res)
        