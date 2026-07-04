class Solution(object):
    def generateMatrix(self, n):
        top,left=0,0
        bottom,right=n-1,n-1
        num=1
        res=[[0]*n for _ in range(n)]
        while(left<=right and top<=bottom):
            for i in range(left,right+1):
                res[left][i]=num
                num=num+1
            top+=1
            for i in range(top,bottom+1):
                res[i][right]=num
                num=num+1
            right-=1
            for i in range(right,left-1,-1):
                res[bottom][i]=num
                num=num+1
            bottom-=1
            for i in range(bottom,top-1,-1):
                res[i][left]=num
                num=num+1
            left+=1
        return res[:n*n]

        