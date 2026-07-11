class Solution(object):
    def change(self, amount, coins):
        dp=[0]* (amount+1)
        dp[0]=1
        for coin in coins:
            for am in range(coin,amount+1):
                dp[am]+=dp[am-coin]
        return dp[amount]
        
        