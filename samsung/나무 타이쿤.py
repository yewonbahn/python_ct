n,m=map(int,input().split())
leaves=[]
lst=[]
for i in range(n):
    leaves.append(list(map(int,input().split())))
for i in range(m):
    lst.append(list(map(int,input().split())))

#→ ↗ ↑ ↖ ← ↙ ↓ ↘

dx=[0,-1,-1,-1,0,1,1,1]
dy=[1,1,0,-1,-1,-1,0,1]

# ↗  ↖  ↙  ↘
dx2=[-1,-1,1,1]
dy2=[1,-1,-1,1]
new_nutrients=[]
year=0


def total_leaves():
    sum = 0
    for i in range(n):
        for j in range(n):
                sum+=leaves[i][j]
    print(sum)

nutrients=[[n-2,0],[n-2,1],[n-1,0],[n-1,1]]

def fun(nutrients):
    global year
    year += 1
    print(leaves)
    print("year",year)
    print("nutrients", nutrients)

    if year>m:
        print("year 다됨")
        return

    nuvalue=[]

    #이동 후, 높이 1만큼 증가 시킴
    dir=lst[year-1][0]
    move=lst[year-1][1]
    print("dir,move",dir,move)
    dir=dir-1
    for i in range(len(nutrients)):


        if(nutrients[i][0] + move * dx[dir]<0 or nutrients[i][1] + move * dy[dir]<0 or nutrients[i][0] + move * dx[dir]>=n or nutrients[i][1] + move * dy[dir]>=n):

            continue

        nutrients[i] = nutrients[i][0] + move * dx[dir], nutrients[i][1] + move * dy[dir]
        nuvalue.append([nutrients[i][0],nutrients[i][1]])
    for i in range(len(nuvalue)):
        leaves[nuvalue[i][0]][nuvalue[i][1]] = leaves[nuvalue[i][0]][nuvalue[i][1]] + 1

    if not nuvalue:
        print("이동불가")
        fun(nutrients)
    print("nuvalue",nuvalue)
    print("leave", leaves)
    for i in range(len(nuvalue)):
        cnt=0
        x_index=nuvalue[i][0]
        y_index=nuvalue[i][1]

        for j in range(4):
            nx = x_index + dx2[j]
            ny = y_index + dy2[j]
            print()
            if(ny>=n or nx>=n or ny<0 or nx<0 or leaves[nx][ny]<1):
                continue
            else:
                print(nx, ny)
                print(leaves[nx][ny])
                cnt+=1
        print("cnt",cnt)
        leaves[x_index][y_index]+=cnt
        print(leaves[x_index][y_index])
    new_nutrients=[]
    print("leaves")
    print(leaves)
    for i in range(n):
        for j in range(n):
            if leaves[i][j]>=2 and (i,j) not in nutrients:
                leaves[i][j]-=2
                new_nutrients.append([i,j])
    fun(new_nutrients)


fun(nutrients)
print(leaves)
total_leaves()