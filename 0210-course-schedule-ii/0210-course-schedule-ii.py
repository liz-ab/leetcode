class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph={i:[] for i in range(numCourses)}
        indegree=[0]*numCourses
        for cor,pre in prerequisites:
            graph[pre].append(cor)
            indegree[cor]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        order=[]
        while(q):
            node=q.popleft()
            order.append(node)
            for neigh in graph[node]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    q.append(neigh)
        return order if len(order)==numCourses else []

