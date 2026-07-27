class Solution(object):
    def intersection(self, nums1, nums2):
        ans=[]
        s=set(nums1)
        for num in nums2:
            if num in s and num not in ans:
                ans.append(num)
        return ans
        