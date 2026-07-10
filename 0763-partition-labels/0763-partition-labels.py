class Solution(object):
    def partitionLabels(self, s):
        last={s[i]:i for i in range(len(s))}
        start=0
        end=0
        res=[]
        for i,ch in enumerate(s):
            end=max(end,last[ch])
            if(i==end):
                res.append(end-start+1)
                start=i+1
        return res

        
        