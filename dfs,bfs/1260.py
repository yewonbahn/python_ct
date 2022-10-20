from collections import deque
N,M,V=map(int,input().split())
array=[]

new=[]
for i in range(M):
    array.append(list(map(int,input().split())))
for i in array:
    i.sort()

array.sort()
def dfs(array,V,visited):
    visited[V]=True
    print(V,end=" ")
    for i in range(len(array)):
        if V == array[i][0]:
            if not visited[array[i][1]]:
                dfs(array,array[i][1],visited)
        if V == array[i][1]:
            if not visited[array[i][0]]:
                dfs(array,array[i][0],visited)


visited = [False] * (N+1)

def bfs(V,visited):
    queue=deque()
    queue.append(V)

    while queue:
        v=queue.popleft()
        if not visited[v]:
            print(v,end=" ")
        visited[v] = True

        for i in range(len(array)):
            if v == array[i][0]:
                if not visited[array[i][1]]:
                    queue.append(array[i][1])
                    continue
            if v == array[i][1]:
                if not visited[array[i][0]]:
                    queue.append(array[i][0])



dfs(array,V,visited)
visited = [False] * (N+1)
print("")
bfs(V,visited)