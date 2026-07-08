class Solution(object):
    def calPoints(self, operations):
        stack=[]
        for i in operations:
            if i=='C':
                stack.pop()
            elif i=='+':
                s=stack[-1]+stack[-2]
                stack.append(s)
            elif i=='D':
                dub=stack[-1] * 2
                stack.append(dub)
            else:
                stack.append(int(i))
        return sum(stack)
        
        
        

        