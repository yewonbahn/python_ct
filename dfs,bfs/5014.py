from collections import deque
f,s,g,u,d=list(map(int,input().split()))
#1->10
dx=[u,-d]
visited=[0]*(f+1)
q=deque()
q.append((s,0))
check=False
visited[s]=True
if s!=g:
    while q:
        if check == True:
            break
        x,y=q.popleft()
        for i in range(2):
            nx=x+dx[i]
            if 1<=nx<=f and not visited[nx]:
                if nx==g:
                    check = True
                    print(y+1)
                    break
                visited[nx]=True
                q.append((nx,y+1))
    if check==False:
        print("use the stairs")

else:
    print(0)
