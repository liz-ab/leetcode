class Solution(object):
    def sortVowels(self, s):
        s=list(s)
        vow=[]
        for i in range(len(s)):
            if(s[i] in "aeiouAEIOU"):
                vow.append(s[i])
        vow.sort()
        for i in range(len(s)):
            if(s[i] in "aeiouAEIOU"):
                s[i]=vow.pop(0)
        s="".join(s)
        return s    