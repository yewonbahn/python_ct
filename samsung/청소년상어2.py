import copy

# 4 X 4 크기 격자에 존재하는 각 물고기의 번호(없으면 -1)와 방향 값을 담는 테이블
array = [[None] * 4 for _ in range(4)]
ate = 0
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        array[i][j] = [data[j * 2], data[j * 2 + 1] - 1]

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
sx, sy = 0, 0
ate += array[sx][sy][0]


def turn_left(di):
    di = (di + 1) % 8
    return di


def find_index(array,f):
    for i in range(4):
        for j in range(4):
            if (array[i][j][0] == f):
                return i, j
    return None


def move_fishes(array,sx,sy):
    for i in range(1, 17):
        print(i,'번째 이동')
        value = find_index(i)
        if value == None:
            continue
        x,y=value[0],value[1]
        di = array[x][y][1]
        for j in range(8):
            nx = x + dx[di]
            ny = y + dy[di]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or (sx,sy)==(nx,ny):
                di = turn_left(di)
            else:
                array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                break

def print_array():
    for i in range(4):
        print(array[i])
def move_all_fishes(array, now_x, now_y):
    # 1번부터 16번까지의 물고기를 차례대로 (낮은 번호부터) 확인
    print(array)
    for i in range(1, 17):
        # 해당 물고기의 위치를 찾기
        position = find_index(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]
            # 해당 물고기의 방향을 왼쪽으로 계속 회전시키며 이동이 가능한지 확인
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                # 해당 방향으로 이동이 가능하다면 이동 시키기
                if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                direction = turn_left(direction)
# 물고기 이동 하기
# 상어가 머금
def position(array,sx,sy):

    lst=[]
    di=array[sx][sy][1]

    for i in range(4):
        sx+=dx[di]
        sy+=dy[di]
        if 0<=sx<4 and 0<=sy<4:
            if array[sx][sy][0] != -1:
                lst.append((sx, sy))
                continue

    return lst

result=0
def dfs(array,sx,sy,total):
    # array = copy.deepcopy(array)  # 리스트를 통째로 복사
    # print("전",total)
    # print_array()
    # total += array[sx][sy][0]  # 현재 위치의 물고기 먹기
    # print("후",total)
    # array[sx][sy][0] = 0  # 물고기를 먹었으므로 번호 값을 -1로 변환
    # global result
    #
    #
    # move_fishes(array, sx,sy)  # 전체 물고기 이동 시키기
    #
    # print("이동후",array)
    # # 이제 다시 상어가 이동할 차례이므로, 이동 가능한 위치 찾기
    # positions=position(array,sx,sy)
    # print(positions)
    #
    # if len(positions) == 0:
    #     result = max(result, total)  # 최댓값 저장
    #
    #     return result
    # print("total",total)
    #     # 모든 이동할 수 있는 위치로 재귀적으로 수행
    # for next_x, next_y in positions:
    #     print("next_x,next_y",next_x,next_y)
    #     dfs(array, next_x, next_y, total)
    #     print("마지막,",array)
    #
    # print("반복", now_x, now_y, total)
    global result
    array = copy.deepcopy(array)  # 리스트를 통째로 복사

    total += array[sx][sy][0]  # 현재 위치의 물고기 먹기
    array[sx][sy][0] = -1  # 물고기를 먹었으므로 번호 값을 -1로 변환

    move_all_fishes(array, sx, sy)  # 전체 물고기 이동 시키기

    # 이제 다시 상어가 이동할 차례이므로, 이동 가능한 위치 찾기
    positions = position(array, sx, sy)
    # 이동할 수 있는 위치가 하나도 없다면 종료
    if len(positions) == 0:
        print("dfs 종료 후 total", total)
        result = max(result, total)  # 최댓값 저장
        return
        # 모든 이동할 수 있는 위치로 재귀적으로 수행
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)
dfs(array,sx,sy,0)

print(result)