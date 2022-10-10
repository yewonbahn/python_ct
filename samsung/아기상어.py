#아기상어 bfs
from collections import deque

INF=1e9 #무한으로 10억 설정
n=int(input())

array=[]
for i in range(n):
    array.append(list(map(int,input().split())))

now_size=2
now_x,now_y=0,0

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x,now_y=i,j
            array[now_x][now_y]=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]

#모든 위치까지의 최단거리만 계산 하는 BFS

def bfs():
    dist=[[-1] * n for _ in range(n)]
    q=deque([(now_x,now_y)])

    dist[now_x][now_y]=0
    while q:
        x,y=q.popleft()
        for i in range(4):

            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if dist[nx][ny] == -1 and array[nx][ny]<=now_size:
                    dist[nx][ny]=dist[x][y]+1

                    q.append((nx,ny))
    return dist
#최단 거리 테이블 -> 먹을 물고기 찾는 함수
def find(dist):
    x,y=0,0
    min_dist=INF
    for i in range(n):
        for j in range(n):
            #도달이 가능하면서 먹을 수 있는 물고기 일때
            if dist[i][j]!=-1 and 1 <= array[i][j] and array[i][j]<now_size:
                if dist[i][j] < min_dist:
                    x,y=i,j
                    min_dist=dist[i][j]
    if min_dist==INF: # 먹을 수 있는 물고기 없는 경우
        return None
    else:
        return  x,y,min_dist # 먹을 물고기의 위치와 최단거리

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
