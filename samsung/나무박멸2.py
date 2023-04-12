import copy
n,m,k,c=map(int,input().split())
lst=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]

answer=0
effect=[[0]*n for i in range(n)]
reset_total=[]
for i in range(n):
    lst.append(list(map(int,input().split())))

year=1
while True:
    print(year,"년")
    reset=[]
    curr=[]
    for i in range(n):
        for j in range(n):
            if lst[i][j]>0:
                curr.append([i,j])
                # 나무 있음
                cnt=0
                for z in range(4):
                    nx=i+dx[z]
                    ny=j+dy[z]
                    if 0<=nx<n and 0<=ny<n and lst[nx][ny]>=1 :
                        cnt+=1
                lst[i][j]+=cnt
    print("증가")
    new_tree=[]
    for i in lst:
        print(i)
    for i,j in curr:
        if lst[i][j]>0:
            # 나무 있음
            growth_trees=[]
            growth_possi=0
            print(i,j)
            for z in range(4):
                nx=i+dx[z]
                ny=j+dy[z]
                if 0<=nx<n and 0<=ny<n and [nx,ny] not in curr:
                        if lst[nx][ny]==0 or [nx,ny] in new_tree:
                            growth_possi+=1
                            growth_trees.append([nx,ny])
                            new_tree.append([nx,ny])
            print(growth_possi)
            for z in growth_trees:
                lst[z[0]][z[1]]=lst[z[0]][z[1]]+(lst[i][j]//growth_possi)
    print("번식")
    for i in lst:
        print(i)
    #각각의 칸에 제초제 뿌려졌을시 가장 많이 박멸되는나무
    dx2=[-1,-1,1,1]
    dy2=[-1,1,-1,1]

    total_die_tree=copy.deepcopy(lst)

    for i in range(n):
        for j in range(n):
            if lst[i][j]>0: #나무있으면
                # total_die_tree[i][j]+=lst[i][j]
                for z in range(4):
                    for size in range(1,k+1):
                        nx=i+(dx2[z]*size)
                        ny=j+(dy2[z]*size)
                        if 0 > nx or nx >= n or ny < 0 or ny >= n or lst[nx][ny] == 0 or lst[nx][ny] == -1:
                            break
                        else:

                            total_die_tree[nx][ny]+=lst[i][j]
    for i in total_die_tree:
        print(i)
    max_x,max_y=0,0
    max_tree=0

    print(max_tree,max_x,max_y)
    #가장 많이 박멸되는 나무 위치 찾기
    for i in range(n):
        for j in range(n):
            if max_tree<total_die_tree[i][j]:
                max_tree=total_die_tree[i][j]
                max_x,max_y=i,j
    recur=[]
    print(max_tree, max_x, max_y)
    answer+=max_tree
    print("**efeetct")
    for i in effect:
        print(i)
    for i in range(n):
        for j in range(n):
            if effect[i][j]>0:
                if effect[i][j]==c:
                    print(i,j,"효과품")
                    recur.append([i,j])
                    effect[i][j]=0
                    lst[i][j]=0
                else:
                    effect[i][j]+=1


    reset.append([max_x, max_y])
    reset_total.append(reset)
    lst[max_x][max_y] = -2
    for z in range(4):
        for size in range(1, k + 1):
            nx = max_x + (dx2[z] * size)
            ny = max_y + (dy2[z] * size)
            if 0 > nx or nx >= n or ny < 0 or ny >= n  or lst[nx][ny] == -1:

                break

            else:
                if lst[nx][ny]==0 and [nx,ny] not in recur:
                    break
                if lst[nx][ny] == -2 :
                    if effect[nx][ny] == 0:
                        effect[nx][ny] = 1
                    elif effect[nx][ny] > 0:
                        effect[nx][ny] -= 1
                    lst[nx][ny] = -2
                    break

                if effect[nx][ny]==0:
                    effect[nx][ny]=1
                elif effect[nx][ny]>0:
                    effect[nx][ny] -= 1

                lst[nx][ny] = -2

    print("제초뿌리기")
    for i in lst:
        print(i)

    if year==m:
        break
    year+=1


print(answer)