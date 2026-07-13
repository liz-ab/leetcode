class Solution(object):
    def floodFill(self, image, sr, sc, color):
        source=image[sr][sc]
        if source==color:
            return image
        row=len(image)
        col=len(image[0])
        def dfs(r,c):
            if r<0 or c<0 or r>row-1 or c>col-1 or image[r][c]!=source:
                return
            image[r][c]=color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        dfs(sr,sc)
        return image
        