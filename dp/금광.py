t=int(input())
n,m=map(int,input().split())
array=[]
str=input().split()
print(str)
for i in range(len(str)):
    if i%m==0:
        array.append(list(map(int,str[i:i+m])))
#오른쪽 위, 오른쪽, 오른쪽 아래
dx=[-1,0,1]
dy=[1,1,1]
result=0
def dfs(x,y,total):
    result=0
    for j in range(3):
        nx=x+dx[j]
        ny=y+dy[j]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        total+=array[nx][ny]
        print(nx, ny,"에 가고",array[nx][ny],"값을 더해")
        dfs(nx,ny,total)
        result=max(total,result)
        print("total",total)
        total=0

#스타트를 행의 0부터
for  i in range(n):
    total=0
    x,y=i,0
    total+=array[x][y]
    dfs(x,y,0)


print(array)
print(result)