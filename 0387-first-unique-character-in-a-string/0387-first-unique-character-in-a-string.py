class Solution(object):
    def firstUniqChar(self, s):
       k=Counter(s)
       for i in range(len(s)):
         if k[s[i]]==1:
             return i
       return -1