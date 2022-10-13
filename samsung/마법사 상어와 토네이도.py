n = int(input())
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))
x=n//2
y=n//2

left=[[-1,1,0.01],[1,1,0.01],[-1,0,0.07],[1,0,0.07],[-2,0,0.02],
          [2,0,0.02],[-2,0,0.02],[-1,-1,0.1],[1,-1,0.1],[0,-2,0.05]]

#좌 하 우 상

dx=[[0,-1],[1,0],[0,1],[-1,0]]

left = [[1, 1, 0.01], [-1, 1, 0.01], [1, 0, 0.07], [-1, 0, 0.07], [1, -1, 0.1],
        [-1, -1, 0.1], [2, 0, 0.02], [-2, 0, 0.02], [0, -2, 0.05]]
right = [[x, -y, z] for x, y, z in left]
down = [[-y, x, z] for x, y, z in left]
up = [[y, x, z] for x, y, z in left]
di= {0: left, 1: down, 2: right, 3: up}

def cloud_move(mx,my,direction,k):
    #모래 있는지 확인
    if array[mx][my]==0:
        return
    sand=array[mx][my]
    array[mx][my]=0
    total=0
    ans=0

    for i in range(len(direction)):

        nx,ny=mx+direction[i][0],my+direction[i][1]

        if(0<=nx<n and 0 <=ny<n):
            array[nx][ny]+=int(sand*direction[i][2])
            total += int(sand * direction[i][2])
        else:
            ans+=int(sand * direction[i][2])
            total+=int(sand * direction[i][2])
    if sand-total>0:
        mx=mx+dx[k][0]
        my=my+dx[k][1]
        if(0<=mx<n and 0 <=my<n):

            array[mx][my]+=sand-total
        else:
            ans=ans+sand-total
    return ans

total=0
#토네이도부터 생각하기
# 1 1 2 2 3 3
time=0
for i in range(n*2-1):
    direction=di[i%4]
    if(i%2==0):
        time+=1
    for j in range(time):
        print(direction)
        # 토네이도 한칸 이동
        x, y = x + dx[i%4][0], y + dx[i%4][1]
        if x<0 or x>=n or y<0 or y>=n:
            continue

        s=i%4
        ans=cloud_move(x,y,direction,s)
        if ans:
            total+=ans

print(total)
