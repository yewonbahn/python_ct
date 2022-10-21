from collections import deque
n=int(input())
b=int(input())
array=[]
for i in range(b):
    array.append(list(map(int,input().split())))

visited=[False]* (n+1)
x=1
q=deque()
q.append(x)
cnt=0
while q:
    nx=q.popleft()
    if not visited[nx]:
        for i in range(b):
            if nx == array[i][0]:
                visited[array[i][0]]=True
                q.append(array[i][1])
                continue
            if nx == array[i][1]:
                visited[array[i][1]]=True
                q.append(array[i][0])

for i in visited:
    if i ==True:
        cnt+=1
print(cnt-1)

