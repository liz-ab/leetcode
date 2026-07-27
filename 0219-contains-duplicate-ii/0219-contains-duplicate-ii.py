class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        map=defaultdict(list)
        for i,num in enumerate(nums):
            if num in map:
                for val in map[num]:
                    if abs(val-i)<=k:
                        return True
            map[num].append(i)
        return False
       
        