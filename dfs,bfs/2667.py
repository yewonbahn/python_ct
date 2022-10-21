from collections import deque
n=int(input())
array=[]
for i in range(n):
    array.append(list(map(int, list(input()))))
dx=[1,-1,0,0]
dy=[0,0,1,-1]

visited=[[False]*(n+1) for _ in range(n+1)]

def bfs(x,y):
    cnt=1

    q = deque()
    q.append((x, y))
    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if array[nx][ny]==0:
                continue
            if visited[nx][ny]==True:
                continue
            q.append((nx,ny))
            visited[nx][ny]=True
            cnt+=1
    if cnt==1:
        return 1
    else:
        return cnt-1
total=0
lst=[]
for i in range(n):
    for j in range(n):
        # 방문하지 않거나, 1인 값에서 bfs
        if visited[i][j]==False and array[i][j]==1:

            value= bfs(i,j)
            if value!=0:
                total+=1
                lst.append(value)
print(total)
lst.sort()
for i in lst:
    print(i)