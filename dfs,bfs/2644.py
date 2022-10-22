from collections import deque
n=int(input())
a,b=map(int,input().split())
m=int(input())
array=[]
for i in range(m):
    array.append(list(map(int,input().split())))
q=deque()
if a<b:
    a,b=b,a
set=False
q.append((b))
cnt=0
visited=[False]*(n+1)
lst=[0]*(n+1)
while q:
    if set==True:
        break
    print(q)
    x=q.popleft()
    if not visited[x]:
        cnt+=1
        for i in range(m):
            if array[i][1]==x and not visited[array[i][0]]:
                visited[x]=True
                if (array[i][0] == a):
                    set=True
                lst[array[i][0]] = lst[x] + 1
                q.append(array[i][0])
                continue
            if array[i][0]==x and not visited[array[i][1]]:
                visited[x]=True
                if (array[i][1] == a):
                    set=True
                lst[array[i][1]]=lst[x]+1
                q.append(array[i][1])
if lst[a]!=0:
    print(lst[a])
else:
    print(-1)