import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드 갯수, 간선 개수 입력
n,m,c=map(int,input().split())

graph=[[] for i in range(n+1)]
distance = [INF] *(n+1)

for _ in range(m):
    a,b,d=map(int,input().split())
    graph[a].append((b,d))

def dijkstra(c):
    cnt = 0  # 도시 초갯수
    q=[]
    heapq.heappush(q,(0,c))
    distance[c]=0 # 시작 노드로 가기위한 최단 경로 0 설정 큐삽입
    while q:
        dist,now= heapq.heappop(q)
        if distance[now]<dist:
            print("이미 처리된적이 있는 노드")
            print(distance[now],dist)
            continue
        #현재 노드와 연결된 다른 인접 노드 화긴

        for i in graph[now]:
            cost=dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                cnt+=1
                heapq.heappush(q,(cost,i[0]))
    return cnt
cnt=dijkstra(c)
print(cnt,distance[c+1])






