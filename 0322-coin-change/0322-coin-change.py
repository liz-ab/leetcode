class Solution(object):
    def coinChange(self, coins, amount):
        dp=[amount+1]* (amount+1)
        dp[0]=0
        for am in range(1,amount+1):
            for coin in coins:
                if(am>=coin):
                    dp[am]=min(dp[am],dp[am-coin]+1)
        return dp[amount] if dp[amount]!=amount+1 else -1

        