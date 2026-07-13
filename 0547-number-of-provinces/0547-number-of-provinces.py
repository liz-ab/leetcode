class Solution(object):
    def findCircleNum(self, isConnected):
        p=0
        visited=[False]*len(isConnected)
        n=len(isConnected)
        def dfs(city):
            visited[city]=True 
            for i in range(n):
                if isConnected[city][i]==1 and not visited[i]:
                    dfs(i)
        for i in range(n):
            if not visited[i]:
                p+=1
                dfs(i)
        return p
            

            
         
        