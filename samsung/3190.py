n=int(input())
k=int(input())

board=[[0]*n for i in range(n)]
snake_check=[[0]*n for i in range(n)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
size=1
time=0
lst=[]
for i in range(k):
    a,b=map(int,input().split())
    board[a-1][b-1]=1
l=int(input())
snake={}

for i in range(l):
    a,b=input().split()
    snake[int(a)]=b
x,y=0,0
xt,yt=0,0
dir=0


while True:
    lst.append([x,y])
    if time in snake:
        if snake[time]=="D":
            dir+=1
        if snake[time] == "L":
            dir-=1
        dir=dir%4


    x+=dx[dir]
    y+=dy[dir]

    time += 1
    if  x<0 or y<0 or x>n-1 or y>n-1:
        break
    if snake_check[x][y] == 1:
        break

    if board[x][y]==1:
        board[x][y]=0
        size+=1
    else:
        a,b=lst.pop(0)
        snake_check[a][b]=0

    snake_check[x][y] = 1

print(time)



















