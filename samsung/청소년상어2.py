import copy
array=[[None]*4 for _ in range(4)]
for i in range(4):
    data=list(map(int,input().split()))
    for j in range(4):
        array[i][j]=[data[j*2],data[j*2+1]-1]
#↑, ↖, ←, ↙, ↓, ↘, →, ↗
result = 0  # 최종 결과
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]
def turn_left(direction):
    return (direction+1)%8

def find_index(array,index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0]==index:
                return i,j

def move_all_fishes(array,now_x,now_y):
    for i in range(1,17):
        value=find_index(array,i)
        if value != None:

            x,y=value[0],value[1]
            di=array[x][y][1]
            print("x,y,di",x,y,di)
            for j in range(8):
                nx=x+dx[di]
                ny=y+dy[di]
                print("nx,ny",nx,ny)
                if 0<=nx<4 and 0<=ny<4 and (x,y)!=(now_x,now_y) and array[nx][ny][0]!=-1:
                    array[x][y][1] = di
                    array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                    break
                di=turn_left(di)

def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    # 현재의 방향으로 쭉 이동하기
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        # 범위를 벗어나지 않는지 확인하며
        if 0 <= now_x and now_x < 4 and 0 <= now_y and now_y < 4:
            # 물고기가 존재하는 경우
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    print(positions)
    return positions


def dfs(array,now_x,now_y,total):
    global result
    array=copy.deepcopy(array)
    total += array[now_x][now_y][0]  # 현재 위치의 물고기 먹기
    array[now_x][now_y][0]=-1
    print(array)
    move_all_fishes(array,now_x,now_y)

    positions=get_possible_positions(array,now_x,now_y)

    if len(positions) == 0:
        print("dfs 종료 후 total",total)
        result = max(result, total)  # 최댓값 저장
        return
        # 모든 이동할 수 있는 위치로 재귀적으로 수행
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)


dfs(array,0,0,0)
print(array)
print(result)