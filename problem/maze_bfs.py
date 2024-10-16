from collections import deque

visit = []
queue = []
def bfs(r,c,grid):
    if grid[0][0] == 1 or grid[r-1][c-1] == 1:
        return -1
    
    q = deque()
    q.append((0,0))

    dx = [-1,0,1,0,1]
    dy = [0,1,0,-1,0]


    dis = [[-1 for _ in range(c)] for _ in range(r)]
    dis[0][0] = 0 

    while queue:
        p = q.popleft()
        for i in range(5):
            x = p[0] + dx[i]
            y = p[1] + dy[i]

            if 0 <= x < r and 0 <= y  < c and dis[x][y] == -1:
                if grid[x][y] == 0 or grid[x][y] ==2:
                    dis[x][y] = dis[p[0]][p[1]] + 1
                    q.append((x,y))

    return dis[r -1][c-1]

if __name__ == "__main__":
        r = 5
        c = 5
        grid =  [ [0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0] ]
        
        result =bfs(r,c,grid)
        print(result)


