from collections import deque
N,K=map(int,input().split())

q=deque()
q.append((N,0))
value=max(N,K)
dx=[1,-1]
array=[0]*(value*2+1)
visited=[False]*(value*2+1)
cnt=0
while True:

    x,y=q.popleft()
    if x==K:
        print(y)
        break

    for i in range(3):
        if i==2:
            nx=x*2
        else:
            nx=x+dx[i]

        if nx>=(value*2+1) or nx<0:
            continue
        if not visited[nx] :

            visited[nx]=True
            q.append((nx,y+1))
            array.append(nx)
