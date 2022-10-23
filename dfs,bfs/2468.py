from collections import deque
n=int(input())
array=[[0]*n for _ in range(n)]
h=0
for i in range(n):
    new=list(map(int,input().split()))
    h=max(max(new),h)
    array[i]=new
print('h',h)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
visited=[[0]*n for _ in range(n)]
def bfs(x,y):

    visited[x][y] = 1
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and check[nx][ny]==0:
                if not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny]=1
    return visited
def print_check():
    for i in check:
        print(i)
#1~100 부터 잠겨진다고 생각
check=[[0]*n for _ in range(n)]
answer=0
for i in range(0,h+1):
    visited = [[0] * n for _ in range(n)]
    cnt=0
    for j in range(n):
        for k in range(n):
            if array[j][k]<=i:
                check[j][k]=1
    print_check()
    #안전 영역 구하기
    for j in range(n):
        for k in range(n):
            if check[j][k]==0 and not visited[j][k]:
                visited
                bfs(j,k)
                visited[j][k]=1
                cnt+=1

    print(cnt)
    answer=max(answer,cnt)
if answer==0:
    print(1)
else:
    print(answer)