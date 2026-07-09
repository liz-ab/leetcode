class Solution(object):
    def frequencySort(self, s):
        res=Counter(s)
        res=sorted(res.items(),key=lambda x:x[1],reverse=True)
        final=""
        for i,j in res:
            final=final + (i*j)
        return final
