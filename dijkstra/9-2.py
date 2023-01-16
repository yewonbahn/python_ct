import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드 갯수, 간선 개수 입력
n,m=map(int,input().split())
start=int(input())
graph=[[] for i in range(n+1)]
distance = [INF] *(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
print("graph",graph)
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0 # 시작 노드로 가기위한 최단 경로 0 설정 큐삽입
    while q:
        print(q)
        dist,now= heapq.heappop(q)
        if distance[now]<dist:
            print(distance[now],dist)
            continue
        #현재 노드와 연결된 다른 인접 노드 화긴
        print(graph[now])
        for i in graph[now]:

            cost=dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)
for i in range(1,n+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])





