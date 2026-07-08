class Solution(object):
    def makeGood(self, s):
        stack=[]
        for chr in s:
            if not stack:
                stack.append(chr)
            elif abs(ord(chr)- ord(stack[-1]))==32:
                stack.pop()
            else:
                stack.append(chr)
        return "".join(stack)
        