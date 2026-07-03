class Solution(object):
    def isPowerOfTwo(self, n):
        m,i=0,0
        while m<=n:
            m=2**i
            if(n==m):
                return True 
            i+=1
        return False

        