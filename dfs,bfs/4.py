from collections import deque

n,m = map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
#상하좌우

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    print("psuh", x, y)
    #큐가 빌때까지 반복
    while queue:
        x,y= queue.popleft()
        print("pop",x,y)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny <0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
                print("psuh",nx,ny)
        print(graph)
    return graph[n-1][m-1]
print(graph)
print(bfs(0,0))
print(graph)