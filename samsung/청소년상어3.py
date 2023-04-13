import copy
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]
fishes=[[0]* 4 for i in range(4)]


answer=[]
result=0

for i in range(4):
    input_data=list(map(int,input().split()))
    for j in range(4):
        fishes[i][j]=[input_data[j*2],input_data[j*2+1]-1]

def fish_move(fishes,index,sx,sy):
    check=False
    cnt=0
    for i in range(4):
        for j in range(4):
            if fishes[i][j][0]==index:
                while True:
                    if cnt>=9:
                        check = True
                        break
                    cnt+=1
                    nx=i+dx[fishes[i][j][1]%8]
                    ny=j+dy[fishes[i][j][1]%8]
                    if( nx==sx and ny==sy):
                        fishes[i][j][1] += 1
                        continue
                    if 0<=nx<4 and 0<=ny<4:

                        fishes[i][j][0],fishes[nx][ny][0]=fishes[nx][ny][0],fishes[i][j][0]
                        fishes[i][j][1],fishes[nx][ny][1]=fishes[nx][ny][1],fishes[i][j][1]
                        check=True
                        break
                    else:
                        fishes[i][j][1]+=1
                if check==True:
                    break
        if check==True:
            break




def move_all_fishes(fishes,sx,sy):
    for i in range(1,17):
        fish_move(fishes,i,sx,sy)


def check_possible_eat(fishes,x,y,dir):
    shark_move_list=[]
    nx=x
    ny=y
    for i in range(4):
        nx+=dx[dir%8]
        ny+=dy[dir%8]
        if 0<=nx<4 and 0<=ny<4:
            if fishes[nx][ny][0] != -1:
                shark_move_list.append([nx,ny])
    return shark_move_list

def dfs(fishes,x,y,total):
    global result
    array=copy.deepcopy(fishes)
    shark_dir = array[x][y][1]
    total+=array[x][y][0]
    array[x][y][0] = -1
    move_all_fishes(array,x,y)
    shark_lst=check_possible_eat(array,x,y,shark_dir)
    if len(shark_lst) == 0:
        answer.append(total)
        return
    for lst in shark_lst:
        dfs(array,lst[0],lst[1],total)

dfs(fishes,0,0,0)
print(max(answer))