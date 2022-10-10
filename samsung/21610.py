n, m = map(int, input().split())
leaves = []
lst = []
for i in range(n):
    leaves.append(list(map(int, input().split())))
for i in range(m):
    lst.append(list(map(int, input().split())))

# → ↗ ↑ ↖ ← ↙ ↓ ↘

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# ↗  ↖  ↙  ↘
dx2 = [-1, -1, 1, 1]
dy2 = [1, -1, -1, 1]
new_nutrients = []
year = 0


def total_leaves():
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += leaves[i][j]
    print(sum)


nutrients = [[n - 2, 0], [n - 2, 1], [n - 1, 0], [n - 1, 1]]


def fun(nutrients, year):
    print("year",year)
    nuvalue = []
    is_cloud = [[False] * n for _ in range(n)]
    # 이동 후, 높이 1만큼 증가 시킴
    dir = lst[year - 1][0]
    move = lst[year - 1][1]
    dir = dir - 1
    for i in range(len(nutrients)):
        a = nutrients[i][0] + move * dx[dir]
        b = nutrients[i][1] + move * dy[dir]
        nutrients[i] = a%n,b%n
        nuvalue.append([nutrients[i][0], nutrients[i][1]])
        is_cloud[nutrients[i][0]][nutrients[i][1]]=True
        leaves[nuvalue[i][0]][nuvalue[i][1]] = leaves[nuvalue[i][0]][nuvalue[i][1]] + 1

    for i in range(len(nuvalue)):

        cnt = 0
        x_index = nuvalue[i][0]
        y_index = nuvalue[i][1]
        for j in range(4):
            nx = x_index + dx2[j]
            ny = y_index + dy2[j]

            if (ny >= n or nx >= n or ny < 0 or nx < 0 or leaves[nx][ny] < 1):
                continue
            else:
                cnt += 1
        leaves[x_index][y_index] += cnt
    new_nutrients = []
    print(is_cloud)
    for i in range(n):
        for j in range(n):

            if not is_cloud[i][j] and leaves[i][j]>=2:
                leaves[i][j] -= 2
                new_nutrients.append([i, j])

    if year == m:
        total_leaves()
        exit()
    else:
        fun(new_nutrients, year + 1)


fun(nutrients, 1)
total_leaves()

print("time :", time.time() - start)  #