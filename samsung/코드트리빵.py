from collections import deque
n,m=map(int,input().split())
lst=[]
peoples=[[0]*n for _ in range(n)]
people_pos=[[-1,-1]]*m
peple_dir=[0]*m
base_camp_check=[[-1]*n for _ in range(n)]
perfect=[0]*m
members=[]
dx=[-1,0,0,1]
dy=[0,-1,1,0]
t=1


for i in range(n):
    lst.append(list(map(int,input().split())))
for i in range(m):
    x, y = map(int, input().split())
    members.append([i+1,x-1,y-1])


def go_to_best_store(t):
    visited=[[0]*n for _ in range(n)]
    lst2 = [[0] * n for _ in range(n)]

    d_lst = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]


    check = False
    q=deque()
    q.append((0,people_pos[t][0],people_pos[t][1],[]))
    visited[people_pos[t][0]][people_pos[t][1]]=1
    possible=[]
    print("플레이어 위치", [people_pos[t][0], people_pos[t][1]])
    print("목표편의점",[members[t][1],members[t][2]])
    print(base_camp_check)
    while q:
        c,x,y,d=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and base_camp_check[nx][ny]==-1:
                if [nx,ny]==[members[t][1],members[t][2]]:
                    possible.append([c+1,nx,ny,d+[i]])
                visited[nx][ny]=1
                lst2[nx][ny]=c
                q.append((c+1,nx,ny,d+[i]))
    possible.sort(key = lambda x:(x[0],x[1],x[2]))
    d=possible[0][3][0]
    movex=people_pos[t][0]+dx[d]
    movey =people_pos[t][1] + dy[d]
    people_pos[t]=[movex,movey]
    if people_pos[t] == [members[t][1], members[t][2]]:
        perfect[t] = 1
        base_camp_check[members[t][1]][members[t][2]] = 1
    return people_pos[t]

#3번행동부터
def check_people(t):
    if people_pos[t]==[-1,-1]:
        return False
    return True

def close_basecamp(t):
    visited=[[0]*n for _ in range(n)]
    lst2 = [[0] * n for _ in range(n)]
    check = False
    q=deque()
    q.append((members[t][1],members[t][2],1,[]))
    visited[members[t][1]][members[t][2]]=1
    possible=[]
    while q:
        x,y,c,d=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and base_camp_check[nx][ny]==-1:
                if lst[nx][ny]!=0 :

                    possible.append([c,nx,ny])

                visited[nx][ny]=1
                d.append(i)
                lst2[nx][ny]=c
                q.append((nx,ny,c+1,d))

    possible.sort(key = lambda x:(x[0],x[1],x[2]))
    people_pos[t] = [possible[0][1], possible[0][2]]
    base_camp_check[possible[0][1]][possible[0][2]]=1

    return lst2,possible[0][1], possible[0][2]


while True:
    print(t,"분 ")
    for i in range(m):
        # print(i+1,"번 사람 시작")
        if perfect[i]==1:
            # print("얜 도착임")
            continue
        if t-1>=i:

            if t-1==i:
                print("격자에없음")
                newlst,bx,by=close_basecamp(i)
                print(bx,by,"에있는 베이스캠프로감")
            else:
                check_people(i)
                print("격자에있음")
                go_to_best_store(i)
                print("이동완",people_pos)
              #      #편의점 방향으로 이동동
    print("플레이어방향",peple_dir)
    print("플레이어위치",people_pos)
    print(perfect)
    cnt=0
    for i in range(m):
        if perfect[i]==1:
            cnt+=1
    if cnt==m:
        print(t)
        break
    t+=1

