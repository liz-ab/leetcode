class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if(sum(gas)<sum(cost)):
            return -1
        start,cur=0,0
        for i in range(len(gas)):
            cur=cur+gas[i]-cost[i]
            if(cur<0):
                cur=0
                start=i+1
        return start 

        