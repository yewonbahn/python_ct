import sys
m,n,h=map(int,sys.stdin.readline().split())
array=arr = [0 for _ in range(n*h)]
for i in range(n*h):
    array[i]=list(map(int,sys.stdin.readline().split()))

dx=[0,0,1,-1,n,-n]
dy=[1,-1,0,0,0,0]
visited2=[[False]*m for i in range(n*h)]
def tomato(x,y):
    num=0
    visited[x][y] = True
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if int(x/n)*n<=nx<int(x/n)*n+n and 0<=ny<m:
            #익지않은 토마토가 있다면
            print((x/n-1)*n,(x/n-1)*n+n)
            if array[nx][ny]==0:
                visited[nx][ny]=True
                array[nx][ny]=1
                num+=1
    for i in range(4,6):
        print(i)
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n*h and 0<=ny<m:
            if array[nx][ny]==0:
                visited[nx][ny]=True
                array[nx][ny]=1
                num+=1
    return num

cnt=0

def check():
    total=0
    for i in range(n*h):
        for j in range(m):
            if array[i][j]!=0:
                total+=1

    return total
def print_array():
    for i in array:
        print(i)

answer=n*m*h
check2=1
real=check()

while True:

    if real==answer:
        print(cnt)
        break

    check2=0
    num2=0
    visited = [[False] * m for i in range(n * h)]
    cnt+=1

    for i in range(n*h):
        for j in range(m):
            if array[i][j]==1 and not visited[i][j] and not visited2[i][j]:
                check2+=1
                visited2[i][j]=True
                value2=tomato(i,j)
                num2+=value2
    real+=num2


    if num2==0:
        print(-1)
        break
