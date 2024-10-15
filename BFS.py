# graph:dict = {
#     "5":["3","7"],
#     "3":["2","4"],
#     "7":["8"],
#     "2":[],
#     "4":["8"],
#     "8":[]
# }

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
# # drive code
# print('Following is the Breadth-First Search')
# bfs(visited,graph,'5')

from collections import deque

# BFS from given source s
def bfs(adj, s):
    # create a queue for bfs
    q = deque()

    # initially mark all the vertices as not visited
    # when we push a vertex into the q, we mark it as 
    # visited
    visited = [False] * len(adj)

    # mark the source node as visited and enqueue it
    visited[s] = True
    q.append(s)

    # iterate over the queue
    while q:
        # dequeue a vertex from queue and print it
        curr = q.popleft()
        print(curr, end=" ")

        # get all adjacent vertices of the dequeued
        # vertex. If an adjacent has not been visited,
        # mark it visited and enqueue it
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

# function to add an edge to the graph
def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

# example usage
if __name__ == "__main__":
    # number of vertices in the graph
    V = 5

    # adjacency list representation of the graph
    adj = [[] for _ in range(V)]

    # add edges to the graph
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)
    add_edge(adj, 2, 4)

    # perform BFS traversal starting from vertex 0
    print('BFS starting from 0: ')
    bfs(adj, 0)

