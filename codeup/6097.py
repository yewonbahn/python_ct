h,w=map(int,input().split())
n=int(input())
array=[]
new_array=[[0]*w for i in range(h)]
print(new_array)
for i in range(n):
    array.append(list(map(int,input().split())))
dx=[0,1]
dy=[1,0]
di=1
for li in array:
    x,y=li[2]-1,li[3]-1
    if li[1]==0:
        di=0
    else:
        di=1
    for j in range(li[0]):
        print(x,y)
        new_array[x][y]=1
        x += dx[di]
        y += dy[di]
for i in new_array:
    print(*i)
