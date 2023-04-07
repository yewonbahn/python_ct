from collections import deque

n=int(input())
size=2
board=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]

for i in range(n):
    board.append(list(map(int,input().split())))


for i in range(n):
    for j in range(n):
        if board[i][j]==9:
            board[i][j] = 0
            x,y=i,j


def bfs(i,j,size):
    q=deque()
    q.append((i,j))
    dist = [[-1] * n for i in range(n)]
    dist[i][j]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and board[nx][ny]<=size and dist[nx][ny]==-1:

                dist[nx][ny]=dist[x][y]+1
                q.append((nx,ny))
    print(dist)
    return dist


def shark_move(size,dist):
    min_value=1e9
    for i in range(n):
        for j in range(n):
            if 0<board[i][j]<size and dist[i][j]!=-1:
                if min_value>dist[i][j]:
                    min_value=dist[i][j]
                    bx,by=i,j
    if min_value==1e9:
        return False
    return bx,by,dist[bx][by]




time=0
ate=0
while True:
    dist=bfs(x,y,size)
    v=shark_move(size, dist)
    print(v)
    if v==False:
        break
    board[v[0]][v[1]]=0
    ate+=1
    time+=v[2]
    x,y=v[0],v[1]
    if ate==size:
        size+=1
        ate=0

print(time)