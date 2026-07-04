class Solution(object):
    def spiralOrder(self, matrix):
        res=[]
        top,left=0,0
        right=len(matrix[0])-1
        bottom=len(matrix)-1
        while(left<=right and top<=bottom):
            for i in range(left,right+1):
                res.append(matrix[left][i])
            top+=1
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1
            for i in range(right,left-1,-1):
                res.append(matrix[bottom][i])
            bottom-=1
            for i in range(bottom,top-1,-1):
                res.append(matrix[i][left])
            left+=1
        return res[:(len(matrix)*len(matrix[0]))]
            

       
        