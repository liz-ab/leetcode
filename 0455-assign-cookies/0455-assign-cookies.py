class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        l,r,c=0,0,0
        while(l<=len(g)-1 and r<=len(s)-1):
            if(g[l]<=s[r]):
                c+=1
                r+=1
                l+=1
            else:
                r+=1
        return c

        