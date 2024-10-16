from collections import deque
maze = [ 
        [0, 1, 0, 0, 0], 
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0], 
        [0, 0, 0, 1, 0]
       ]
def bfs(maze):
    r,c = len(maze),len(maze[0])
    s = (0,0)
    g = (r-1,c-1)
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    queue = deque([s])
    visited = set([s])
    dis = {s : 0}

    while queue:
        cur = queue.popleft()

        if cur == g:
            return dis[cur]
        
        for d in direction:
            n_r , n_c = cur[0] + d[0], cur[1] + d[1]

            if 0 <= n_r < r and 0 <= n_c < c and maze[n_r][n_c] == 0:
                n_node = (n_r, n_c)

                visited.add(n_node)
                queue.append(n_node)
    return -1

if __name__ == "__main__":
    r = 5
    c = 5
    result =bfs(maze)
    print(result)