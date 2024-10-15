# graph = {
#   '5' : ['3','7'],
#   '3' : ['2', '4'],
#   '7' : ['8'],
#   '2' : [],
#   '4' : ['8'],
#   '8' : []
# }

# visited = set()

# def dfs(visited, graph, node):
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)


# # drive code
# print('Following is the Dept_first Search')
# dfs(visited,graph,'5')

# graph = {'0': set(['1', '2']),
#          '1': set(['0', '3', '4']),
#          '2': set(['0']),
#          '3': set(['1']),
#          '4': set(['2', '3'])}

# visited = set()

# def dfs(visited,graph,node):
#     if node not in visited:
#         print(node)
#         visited.add(node)

#         for neighbour in graph[node]:
#             dfs(visited,graph,neighbour)
# dfs(visited,graph,'0')


# graph = {
#     'A':['B','C'],
#     'B':['D','E'],
#     'C':['F'],
#     'D':[],
#     'E':['F'],
#     'F':[]
# }
# visited = set() # set to keep track of visited nodes.

# def dfs(visited, graph, node):
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         for neighbour in graph[node]:
#             # print("Neighbour is now " + neighbour)
#             dfs(visited, graph, neighbour)
# # driver code
# dfs(visited, graph, 'A')