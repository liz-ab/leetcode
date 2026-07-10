class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        act=sorted(intervals,key=lambda x:x[1])
        pre_end=act[0][1]
        task=0
        for i in range(1,len(intervals)):
            if(act[i][0]>=pre_end):
                pre_end=act[i][1]
            else:
                task+=1
        return task
        