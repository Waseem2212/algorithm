# Problem: Maze Solving with BFS, DFS, and UCS
from collections import deque

def bfs(adj, s):
    q = deque()
    visited = [False] * len(adj)
    visited[s] = True
    q.append(s)
    while q:
        curr = q.popleft()
        print(curr, end=" ")
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
def add_edge(adj, u, v,x,y,z):
    adj[u].append(v)
    adj[v].append(u)
    adj[x].append(y)
    adj[y].append(x)
    adj[z].append(y)
    adj[u].append(z)

if __name__ == "__main__":

    V = 20
    adj = [[] for _ in range(V)]

    add_edge(adj, 0, 1, 0, 0, 0)
    add_edge(adj, 0, 1, 0, 1, 0)
    add_edge(adj, 0, 0, 0, 1, 0)
    add_edge(adj, 0, 1, 0, 0, 0)
    add_edge(adj, 0, 1, 0, 0, 0)

    bfs(adj, 0)

# graph:list = [
#     [0, 1, 0, 0, 0],
#     [0, 1, 0, 1, 0],
#     [0, 0, 0, 1, 0],
#     [0, 1, 0, 0, 0],
#     [0, 1, 0, 0, 0]
# ]

# visited = []
# queue = []

# def bfs(visited,graph,node):
#     visited.append(node)
#     queue.append(node)

#     while queue:
#         m = queue.pop(0)
#         print(f"{m}", end=" ")

#         for neighbour in graph[m]:
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 queue.append(neighbour)
# bfs(visited,graph,0)






