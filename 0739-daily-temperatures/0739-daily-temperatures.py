class Solution(object):
    def dailyTemperatures(self, temperatures):
        ans=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[i]>=stack[-1][1]:
             stack.pop()
            if stack:
             ans[i]=stack[-1][0]-i
            stack.append([i,temperatures[i]])
        return ans
