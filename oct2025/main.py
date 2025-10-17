from collections import deque

# inputs 
n, m = map(int, input().split())
a, b, c, d = map(int, input().split())
s = int(input())

# init maze via nested list 
maze = []
for _ in range(n):
    maze.append(input())
   
# pre define poss. moves  
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  
# bfs algorithm -- got from google   
def bfs(x, y):
    dists = [[-1] * m for _ in range(n)]
    queue = deque([(x, y)])
    dists[x][y] = 0
    
    while queue:
        row, col = queue.popleft()
        d = dists[row][col]
        
        for hori, vert in moves:
            t_row = row + hori; t_col = col + vert 
            if (0 <= t_row < n 
            and 0 <= t_col < m 
            and maze[t_row][t_col] == '*' 
            and dists[t_row][t_col] == -1):
                dists[t_row][t_col] = d + 1
                queue.append((t_row, t_col))

    return dists 
    
# subtract to use 0-based indexing 
d1 = bfs(a-1, b-1)
d2 = bfs(c-1, d-1)

meet = False
# brute force n check if they can meet at any position within time limit
for i in range(n):
    for j in range(m):
        if d1[i][j] != -1 and d2[i][j] != 1:
            if max(d1[i][j], d2[i][j]) <= s:
                meet = True; break 
    if meet:
        break
    
print('good job' if meet else 'cooked')                
