class Solution(object):
    def canPlaceFlowers(self, f, n):
        if(n==0):
            return True 
        if(len(f)==1):
            return (f[0]==0 and n==1)
        if(f[0]==0 and f[1]==0):
            f[0]=1
            n-=1
        for i in range(1,len(f)-1):
            if(f[i]==0 and f[i+1]==0 and f[i-1]==0):
                f[i]=1
                n-=1
        if(f[len(f)-2]==0 and f[len(f)-1]==0):
            f[len(f)-1]=1
            n-=1
        print(f)
        return n<=0

        