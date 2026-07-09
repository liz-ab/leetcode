class Solution(object):
    def findTheWinner(self, n, k):
     st=0
     end=k-1
     num=list(range(1,n+1))
     while(len(num)>1):
        del num[end]
        n-=1
        if(len(num)==1):
            break
        else:
           st=(end)%n
           end=(st+(k-1))%n
     return num[0]
        