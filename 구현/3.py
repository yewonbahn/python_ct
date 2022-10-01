a,b = map(int,input().split())
d=[[0]*b for _ in range(a)]

x,y,direction = map(int,input().split())
d[x][y] = 1

lst=[]  # 전체 맵 정보를 입력받기
for i in range(a):
    lst.append(list(map(int,input().split())))


dx=[-1,0,1,0]
dy=[0,1,0,-1]

def turn_left():
    global direction
    direction -=1
    if direction == -1:
        direction = 3
count =1
turn_time=0
while True:
    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction]
    if d[nx][ny]==0 and lst[nx][ny]==0:
        d[nx][ny] = 1
        x=nx
        y=ny
        count+=1
        turn_time=0
        continue
    else:
        turn_time +=1
    if turn_time==4: #네방향 모두 갈 수 없는 경우
        nx = x- dx[direction]
        ny = y - dy[direction]
        if lst[nx][ny] ==0:
            x= nx
            y= ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time=0




print(count)