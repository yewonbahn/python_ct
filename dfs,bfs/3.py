#음료수 얼려먹기
def dfs(data,a,b,visited):
    visited[a][b]=True
    if visited[a][b]==0 and


data=[]
n,m=map(int,input().split())
for i in range(n):
    data.append(list(map(int,input())))

print(data)

visited = n* [[False] * m ]
print(visited)

def dfs(data,0,0,visited):
