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
# 1 1 0 예시
# 1: direction = 3(북쪽을 바라 보고,왼쪽 방향), turn_time =1
# 2: direction = 2(북,아래 뱡향), 2 1, tutn_time=2
# 3: direction = 1(북,오른쪽 뱡향), 1 2, tutn_time=2
#   if 문 들어감 -> d[1][2] = 1, x=1,y=2 count=2,turn_time=0
# 4: direction = 0,(동, 윗부터) 0,2. turn_time=1
# 5: direction = 3,(동,왼쪽) 1,1 이미갔기때문에  turn_time=2
# 6: direction = 2,(동,아래 ) 2, 2 d[2][2]=1,
#    x=2,y=2, count=3, turn_time=0
# 7 :direction =1 (남,오른쪽) 2,3 turn_time=1
# 8: direction=0 (남,위) 1,2 turn_time=2
# 9: direction=3 (남,왼쪽) 2,1 turn_time=3
#10 : d=2 (남,아래)3,2 turn_time=4=> 1,2
#11:
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