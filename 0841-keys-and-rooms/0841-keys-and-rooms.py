class Solution(object):
    def canVisitAllRooms(self, rooms):
        graph=[[] for _ in range(len(rooms))]
        for i in range(len(rooms)):
            for num in rooms[i]:
                graph[i].append(num)
        stack=[0]
        visited=[False]*len(rooms)
        while stack:
            cur=stack.pop()
            if not visited[cur]:
                visited[cur]=True
                for neigh in graph[cur]:
                    if not visited[neigh]:
                        stack.append(neigh)
        if False in visited:
            return False
        else:
            return True
        