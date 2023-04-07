EMPTY = (-1, -1, -1, -1, -1, -1)
n, m, k = map(int, input().split())  # n 격자 m플레이어수 k 라운드수
lst =  [
    [[] for _ in range(n)]
    for _ in range(n)
]

players = []
player_postion = [[-1] * n for i in range(n)]
for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(n):
        # 총이 놓여 있는 칸입니다.
        if nums[j] != 0:
            lst[i][j].append(nums[j])

for i in range(m):
    x, y, d, s = tuple(map(int, input().split()))
    players.append((i, x - 1, y - 1, d, s, 0))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
points = [0] * m

def move(p, pos):
    num, x, y, d, s, a = p
    nx, ny = pos

    # 가장 좋은 총으로 갱신해줍니다.
    lst[nx][ny].append(a)
    lst[nx][ny].sort(reverse=True)
    a = lst[nx][ny][0]
    lst[nx][ny].pop(0)

    p = (num, nx, ny, d, s, a)
    update(p)


# (x, y)가 격자를 벗어나는지 확인합니다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def find_player(pos):
    for i in range(m):
        _, x, y, _, _, _ = players[i]
        if pos == (x, y):
            return players[i]

    return EMPTY
def update(p):
    num, _, _, _, _, _ = p

    # Player의 위치를 찾아
    # 값을 갱신해줍니다.
    for i in range(m):
        num_i, _, _, _, _, _ = players[i]

        if num_i == num:
            players[i] = p
            break


# def loser_move(loser, player):
#     x, y, d, s, gun, point = player[0], player[1], player[2], player[3], player[4], player[5]
#     # 이동하자
#     if gun != 0:
#         if len(lst[x][y]) == 1:
#             if lst[x][y] == ['0']:
#                 lst[x][y] = [str(gun)]
#         else:
#             lst[x][y].append(str(gun))
#     player[4] = 0
#     player_check = False
#     while True:
#         nx = x + dx[d % 4]
#         ny = y + dy[d % 4]
#
#         if 0 <= nx < n and 0 <= ny < n:
#             if player_postion[nx][ny] != -1:  # 플레이어가 있으면 방향전환
#
#                 d += 1
#                 player[2] = d % 4
#                 continue
#             else:
#                 player_postion[nx][ny] = loser
#
#                 player[0] = nx
#                 player[1] = ny
#
#                 # 총이 있다면, 가장 공격력 높은 총 획득하고 자기 총 반납
#                 if len(lst[nx][ny]) == 1:
#                     if lst[nx][ny] == ['0']:
#
#                         break
#                     else:  # 총이 있다면
#                         best = get_gun(gun, nx, ny)
#                         if best != False:
#                             player[4] = best
#
#                 break
#         else:
#             d += 1
#             player[2] = d % 4


def get_gun(gun, nx, ny):
    best = gun
    best_i = 0
    check = False
    for i in range(len(lst[nx][ny])):
        if best < int(lst[nx][ny][i]):
            best = int(lst[nx][ny][i])
            best_i = i
            check = True
    if check == True:
        lst[nx][ny].pop(best_i)
        lst[nx][ny].append(str(gun))

        return best
    return False


def loser_move(p):
    num, x, y, d, s, a = p

    # 먼저 현재 위치에 총을 내려놓게 됩니다.
    lst[x][y].append(a)

    # 빈 공간을 찾아 이동하게 됩니다.
    # 현재 방향에서 시작하여
    # 90'씩 시계방향으로
    # 회전하다가
    # 비어있는 최초의 곳으로 이동합니다.
    for i in range(4):
        ndir = (d + i) % 4
        nx, ny = x + dx[ndir], y + dy[ndir]
        if in_range(nx, ny)  and find_player((nx, ny)) == EMPTY:
            p = (num, x, y, ndir, s, 0)
            move(p, (nx, ny))
            break


# p2과 p2가 pos에서 만나 결투를 진행합니다.
def duel(p1, p2, pos):
    num1, _, _, d1, s1, a1 = p1
    num2, _, _, d2, s2, a2 = p2

    # (초기 능력치 + 총의 공격력, 초기 능력치) 순으로 우선순위를 매겨 비교합니다.

    # p1이 이긴 경우
    if (s1 + a1, s1) > (s2 + a2, s2):
        # p1은 포인트를 얻게 됩니다.
        points[num1] += (s1 + a1) - (s2 + a2)
        # p2는 진 사람의 움직임을 진행합니다.
        loser_move(p2)
        # 이후 p1은 이긴 사람의 움직임을 진행합니다.
        move(p1, pos)
    # p2가 이긴 경우
    else:
        # p2는 포인트를 얻게 됩니다.
        points[num2] += (s2 + a2) - (s1 + a1)
        # p1은 진 사람의 움직임을 진행합니다.
        loser_move(p1)
        # 이후 p2는 이긴 사람의 움직임을 진행합니다.
        move(p2, pos)


for turn in range(k):
    for i in range(m):
        num, x, y, d, s, gun = players[i]
        player_num = player_postion[x][y]
        loser = 0
        winner = 0
        loser_check = False
        while True:
            nx = x + dx[d % 4]
            ny = y + dy[d % 4]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                next_player = find_player((nx, ny)) # 해당 위치에 있는 전 플레이어 정보 어더옴
                curr_player= (num, nx, ny, d, s, gun)
                update(curr_player)
                if next_player == EMPTY:  # 플레이어가 없으면
                    move(curr_player, (nx, ny))
                else:
                    duel(curr_player, next_player, (nx, ny))
                break

            else:
                d += 2



for point in points:
    print(point, end=" ")