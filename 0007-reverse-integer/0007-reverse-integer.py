class Solution:
    def reverse(self, x: int) -> int:
        neg=x<0
        if neg:
            x=x*-1
        res=int(str(x)[::-1])
        if neg:
            res=-res
        if res>=-2**31 and res<=(2**31)-1:
            return res
        else:
            return 0