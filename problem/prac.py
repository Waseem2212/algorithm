maze = [
  [0, 1, 0, 0, 0],
  [0, 1, 0, 1, 0],
  [0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0]
]
visited = []
queue = []
for i in maze[0][0]:
    visited.append(i)
    queue.append(i)

print(visited)
print(queue)



# def bfs(visited,maze):
#     visited.append(maze[0])
#     queue.append(maze[0])

#     while queue:
#         m = queue.pop(0)
#         print(m, end=" ")

#         for i in maze:
#             if i not in visited:
#                 visited.append(i)
#                 queue.append(i)
    
# bfs(visited,maze)