class Solution(object):
    def validPath(self, n, edges, source, destination):
        gr=[[] for _ in range(n)]
        for i in range(len(edges)):
            gr[edges[i][0]].append(edges[i][1])
            gr[edges[i][1]].append(edges[i][0])
        stack=[source]
        visited=[False]*n
        while stack:
            cur=stack.pop()
            if not visited[cur]:
                visited[cur]=True
                if(cur==destination):
                    return True
                for neigh in gr[cur]:
                    if not visited[neigh]:
                        stack.append(neigh)
        return False