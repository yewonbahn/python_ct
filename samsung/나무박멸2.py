import copy
n,m,k,c=map(int,input().split())
lst=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]

effet=[[0]*n for i in range(n)]
answer=0
reset_total=[]
for i in range(n):
    lst.append(list(map(int,input().split())))

year=1
while True:
    print(year,"년")
    curr=[]
    reset=[]
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
    new_tree=[]
    for i in lst:
        print(i)
    print("인접완")
    for i,j in curr:
        if lst[i][j]>0:
            # 나무 있음
            growth_trees=[]
            growth_possi=0
            for z in range(4):
                nx=i+dx[z]
                ny=j+dy[z]
                if 0<=nx<n and 0<=ny<n and [nx,ny] not in curr:
                        if lst[nx][ny]==0 or [nx,ny] in new_tree and effet[nx][ny]==0:
                            growth_possi+=1
                            growth_trees.append([nx,ny])
                            new_tree.append([nx,ny])
            for z in growth_trees:
                lst[z[0]][z[1]]=lst[z[0]][z[1]]+(lst[i][j]//growth_possi)
    for i in lst:
        print(i)
    print("번식")
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
                        if 0>nx or nx>=n or ny<0 or ny>=n or lst[nx][ny]==-2 or lst[nx][ny]==-1 or lst[nx][ny]==0:
                            break
                        else:
                            total_die_tree[nx][ny]+=lst[i][j]

    max_x,max_y=0,0
    max_tree=0
    #가장 많이 박멸되는 나무 위치 찾기
    for i in range(n):
        for j in range(n):
            if max_tree<total_die_tree[i][j]:
                max_tree=total_die_tree[i][j]
                max_x,max_y=i,j
    print(max_tree,max_x,max_y)

    answer+=max_tree
    recur=[]

    print("제초전 c일때 효과풀자")
    for i in effet:
        print(i)
    reset.append([max_x, max_y])

    for i in range(n):
        for j in range(n):
            if effet[i][j]>0:
                if effet[i][j] == c:
                    print(i,j,"효과풀ㅔ")
                    lst[i][j]=0
                    effet[i][j]=0
                else:
                    effet[i][j]+=1
    print("효과풀")
    for i in lst:
        print(i)
    lst[max_x][max_y] = -2
    for z in range(4):
        for size in range(1, k + 1):
            nx = max_x + (dx2[z] * size)
            ny = max_y + (dy2[z] * size)
            print(nx,ny)
            if 0 > nx or nx >= n or ny < 0 or ny >= n or lst[nx][ny]==0 or lst[nx][ny]==-1:
                break
            else:
                if lst[nx][ny] == -2:
                    effet[nx][ny] -= 1
                    break
                print("됨")
                print(lst[nx][ny])
                if effet[nx][ny]!=0:
                    print("효과연장",nx,ny)
                    effet[nx][ny]-=1
                else:
                    print("새롭게추가",nx,ny)
                    effet[nx][ny]= 1
                lst[nx][ny] = -2

    for i in lst:
        print(i)
    print("제초완 ")
    reset_total.append(reset)
    if year==m:
        break
    year+=1
for i in effet:
    print(i)
print(reset_total)
print(answer)