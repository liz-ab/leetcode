class Solution(object):
    def findTheWinner(self, n, k):
     win=0
     for i in range(2,n+1):
        win=(win+k)%i
     return win+1