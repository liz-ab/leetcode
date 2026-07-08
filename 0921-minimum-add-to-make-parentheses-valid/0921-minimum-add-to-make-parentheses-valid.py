class Solution(object):
    def minAddToMakeValid(self, s):
        stack=[]
        if(len(s)==0):
            return 0
        c=0
        cTo={')':'(',']':'[','}':'{'}
        for chr in s:
            if chr in cTo:
                if stack and stack[-1]==cTo[chr]:
                    stack.pop()
                else:
                    c+=1
            else:
                stack.append(chr)
        s=len(stack)+c
        return s



        