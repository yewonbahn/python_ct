import sys
from collections import deque
n,m=map(int,input().split())
array=[]
for i in range(n):
    array.append(list(map(int, list(input()))))

dx=[-1,1,0,0]
dy=[0,0,1,-1]
visited=[[False]*m for i in range(n)]
x,y=0,0
q=deque()
cnt=0
q.append((x,y))
while (x,y)!=(n-1,m-1):

    x,y=q.popleft()

    if not visited[x][y]:
        visited[x][y] = True
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m or array[nx][ny]==0:
                cnt-=1
                continue
            else:
                array[nx][ny]=array[x][y]+1
                q.append((nx,ny))

print(array[-1][-1])