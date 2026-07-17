class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x=defaultdict(int)
        for num in nums:
            x[num]+=1
        for num,freq in x.items():
            if freq==1:
                return num
        