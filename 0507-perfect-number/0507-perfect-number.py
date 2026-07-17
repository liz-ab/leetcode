class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=5:
            return False
        sum=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                sum+=i
                if(num//i != i):
                    sum+=num//i
        return sum==num