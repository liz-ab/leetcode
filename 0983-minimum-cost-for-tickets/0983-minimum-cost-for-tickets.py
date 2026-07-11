class Solution(object):
    def mincostTickets(self, days, costs):
        travel=set(days)
        last=days[-1]
        dp=[0]*(last+1)
        for i in range(1,last+1):
            if i not in travel:
                dp[i]=dp[i-1]
            else:
                cost1=dp[i-1]+costs[0]
                cost2=dp[max(0,i-7)]+costs[1]
                cost3=dp[max(0,i-30)]+costs[2]
                dp[i]=min(cost1,cost2,cost3)
        return dp[last]
            
        