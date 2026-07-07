class Solution(object):
    def mySqrt(self, x):
        if(x<2):
            return x
        low,high=1,x//2
        while(low<=high):
            mid=low+(high-low)//2
            if mid*mid>x:
                high=mid-1
            else:
                low=mid+1
        return high
        
        