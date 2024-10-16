maze = [
  [0, 1, 0, 0, 0],
  [0, 1, 0, 1, 0],
  [0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0]
]

visited = set()

def dfs(visited, maze, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in maze[node]:
            dfs(visited, maze, neighbour)

dfs(visited,maze,0)

# def dfs(visited, maze):
#     if maze not in visited:
#         print(maze)
#         visited.add(maze)
#         for neighbour in maze:
#             dfs(visited, maze, neighbour)


# dfs(visited,maze,0)

