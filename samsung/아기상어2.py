from collections import deque
n=int(input())
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))
sx,sy=0,0
size=2
for i in range(n):
    for j in range(n):
        if array[i][j]==9:
            sx,sy=i,j

dx=[-1,1,0,0]
dy=[0,0,-1,1]

array[sx][sy]=0
def bfs():
    dist= [[-1]*n for _ in range(n)]

    queue=deque()
    queue.append((sx,sy))
    print(sx,sy)
    dist[sx][sy]=0
    while(queue):
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and size>=array[nx][ny]:
                if dist[nx][ny]==-1:
                    dist[nx][ny]=dist[x][y]+1

                    queue.append((nx,ny))
    print(dist)
    return dist

def find(dist):
    x, y = 0, 0
    min_dist = 1e9
    for i in range(n):
        for j in range(n):
            # 도달이 가능하면서 먹을 수 있는 물고기 일때
            if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == 1e9:  # 먹을 수 있는 물고기 없는 경우
        return None
    else:
        print(x, y, min_dist)
        return x, y, min_dist  # 먹을 물고기의 위치와 최단거리
answer=0
ate=0
while True:
    print("sx,sy",sx,sy)
    dist=bfs()
    value=find(dist)
    if value == None:
        break
    print("h",value[2])
    sx,sy=value[0],value[1]
    array[sx][sy]=0
    print(value)
    answer+=value[2]
    ate+=1
    if(ate==size):
        size+=1
        ate=0

print(answer)
