class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum>9*num:
            return ""
        res=""
        for i in range(num):
            digit=min(9,sum)
            res=res+str(digit)
            sum-=digit
        return res

        