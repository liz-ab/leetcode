class Solution:
    def countPrimes(self, n: int) -> int:
        if(n<=1):
            return 0
        dp=[1]*n
        count=0
        dp[0]=dp[1]=0
        for i in range(2,n):
            if dp[i]==1:
                count+=1
                for j in range(i+i,n,i):
                    dp[j]=0
        return count
