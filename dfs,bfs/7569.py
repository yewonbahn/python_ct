import sys
from collections import deque
m,n,h=map(int,sys.stdin.readline().split())
array=arr = [0 for _ in range(n*h)]
for i in range(n*h):
    array[i]=list(map(int,sys.stdin.readline().split()))

dx=[0,0,1,-1,n,-n]
dy=[1,-1,0,0,0,0]
visited=[[False]*m for i in range(n*h)]

q=deque()

for i in range(n * h):
    for j in range(m):
        if array[i][j] == 1 :
            q.append((i,j,0))
real=n*m*h
cnt=0
answer=0

while q:
    x,y,z=q.popleft()

    num = 0
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if int(x / n) * n <= nx < int(x / n) * n + n and 0 <= ny < m and array[nx][ny] == 0:
            # 익지않은 토마토가 있다면

            if array[nx][ny] == 0:
                visited[nx][ny] = True
                array[nx][ny] = 1
                q.append((nx,ny,z+1))
                answer = z + 1
    for i in range(4, 6):

        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n * h and 0 <= ny < m:
            if array[nx][ny] == 0:
                visited[nx][ny] = True
                array[nx][ny] = 1
                q.append((nx, ny,z+1))
                answer=z+1

for i in range(n * h):
    for j in range(m):
        if array[i][j] == 1 or array[i][j]==-1 :
            cnt+=1
if real==cnt:
    print(answer)
else:
    print(-1)
