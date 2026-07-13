class Solution(object):
    def canVisitAllRooms(self, rooms):
        stack=[0]
        visited=[False]*len(rooms)
        while stack:
            cur=stack.pop()
            if not visited[cur]:
                visited[cur]=True
                for neigh in rooms[cur]:
                    if not visited[neigh]:
                        stack.append(neigh)
        if False in visited:
            return False
        else:
            return True
        