from queue import PriorityQueue
 # filling adjacency matrix with empty arrays
vertices = 14
graph = [[] for i in range(vertices)]

# function for adding edges to graph
def add_edge(x,y, cost):
    graph[x].append((y,cost))
    graph[y].append((x,cost))

# function for implementing bet ferst search
# gives output path having the lowest cost
def best_first_search(source, target, vertices):
    visited = [0] * vertices
    pq = PriorityQueue()
    pq.put((0, source))
    print('path: ')

    while not pq.empty():
        u = pq.get()[1]
        # deplaying the path having the lowet cost
        print(u, end=" ")
        if u == target:
            break

        for v, c in graph[u]:
            if not visited[v]:
                visited[v] = True
                pq.put((c,v))

    print()
 
if __name__ == "__main__":
    # add_edge(0, 1, 1)
    # add_edge(0, 2, 8)
    # add_edge(1, 2, 12)
    # add_edge(1, 4, 13)
    # add_edge(2, 3, 6)
    # add_edge(4, 3, 3)

    add_edge(0, 1, 1)
    add_edge(1, 0, 1)
    add_edge(1, 0, 0)
    add_edge(1, 1, 0)

    source = 0
    target = 2
    best_first_search(source, target, vertices)

# import heapq
# import math
# class Node:
#     def __init__(self, x, y, cost):
#         self.x = x
#         self.y = y
#         self.cost = cost
#     def __lt__(self, other):
#         return self.cost < other.cost
# def euclidean_distance(x1, y1, x2, y2):
#     return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
# def greedy_best_first_search(grid, start, goal):
#     rows = len(grid)
#     cols = len(grid[0])
#     pq = []
#     heapq.heappush(pq, Node(start[0], start[1], 0))
#     visited = set()
#     visited.add((start[0], start[1]))
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     while pq:
#         current = heapq.heappop(pq)
#         if (current.x, current.y) == goal:
#             print(f"Goal reached at ({current.x}, {current.y})")
#             return
#         for d in directions:
#             new_x, new_y = current.x + d[0], current.y + d[1]
#             if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 0 and (new_x, new_y) not in visited:
#                 cost = euclidean_distance(new_x, new_y, goal[0], goal[1])
#                 heapq.heappush(pq, Node(new_x, new_y, cost))
#                 visited.add((new_x, new_y))
#     print("Goal not reachable")

# # Example grid
# # grid = [
# #     [0, 1, 1, 1],
# #     [1, 0, 1, 1],
# #     [1, 0, 0, 1],
# #     [1, 1, 0, 0]

# # ]
# grid = [
#     [0, 1, 1],
#     [0, 2, 8],
#     [1, 2, 12],
#     [1, 4, 13],
#     [2, 3, 6],
#     [4, 3, 3]

# ]

# start = (0, 0)
# goal = (3, 3)
# greedy_best_first_search(grid, start, goal)