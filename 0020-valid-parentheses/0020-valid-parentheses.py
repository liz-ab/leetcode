class Solution(object):
    def isValid(self, s):
        stack=[]
        cTo={'}':'{',')':'(',']':'['}
        for c in s:
            if c in cTo:
                if stack and stack[-1]==cTo[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        
        