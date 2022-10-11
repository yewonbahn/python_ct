from collections import deque
n= int(input())
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))
dx=[1,0,0,-1]
dy=[0,-1,1,0]

#현재 상어 위치
now_x,now_y=0,0
now_size=2

for i in range(n):
    for j in range(n):
        if array[i][j]==9:
            now_x,now_y=i,j
            array[i][j]=0

def bfs():
    q=deque([(now_x,now_y)])
    dist=[[-1]*n for _ in range(n)]
    dist[now_x][now_y]=0

    while q:
        nx,ny=q.popleft()
        print(nx,ny)
        for i in range(4):
            newx=nx+dx[i]
            newy=ny+dy[i]
            if 0<=newx<n and 0<=newy<n:
                if dist[newx][newy]==-1 and now_size>=array[newx][newy]:
                    q.append((newx,newy))
                    dist[newx][newy]=dist[nx][ny]+1
    print(dist)
    return dist
def find(dist):
    x, y = 0, 0
    min_dist = 1e9
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < now_size:
                if dist[i][j] < min_dist:
                    min_dist=dist[i][j]
                    x,y=i,j
    if min_dist==1e9:
        return None

    print(x,y,min_dist)
    return x,y,min_dist
result=0 #최종답안
ate=0 #현재 크기에서 먹은 양
while True:
    #먹을 수 있는 물고기 위치 찾기
    value = find(bfs())
    if value==None:
        print(result)
        break
    else:
        #현재위치 갱신 및 이동거리 변경
        now_x,now_y=value[0],value[1]
        result+=value[2]

        array[now_x][now_y]=0
        ate+=1
        if ate>= now_size:
            now_size+=1
            ate=0
