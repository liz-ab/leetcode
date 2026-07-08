class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack=[]
        di={}
        for i in reversed(nums2):
            while stack and i>stack[-1]:
                stack.pop()
            if stack:
                di[i]=stack[-1]
            else:
                di[i]=-1
            stack.append(i)
        res=[]
        for i in nums1:
            res.append(di[i])
        return res
        
            
        