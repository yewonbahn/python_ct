n,m,k=map(int,input().split()) #n 격자 m플레이어수 k 라운드수
lst=[]
players=[]
player_postion=[[-1]*n for i in range(n)]
for i in range(n):
    lst.append(list(map(list,input().split())))
for i in range(m):
    player=list(map(int,input().split()))
    players.append([player[0]-1,player[1]-1,player[2],player[3],0,0])
    player_postion[player[0]-1][player[1]-1]=i

dx=[-1,0,1,0]
dy=[0,1,0,-1]
print(player_postion)

def loser_move(loser,player):
    x, y, d, s, gun, point = player[0], player[1], player[2], player[3], player[4], player[5]
    # print("진애 스펙",player)
    print(player_postion)
    #이동하자
    if gun!=0:
        lst[x][y].append(str(gun))
    player[4]=0

    while True:
        nx=x+dx[d%4]
        ny=y+dy[d%4]

        if 0<=nx<n and 0<=ny<n:
            if player_postion[nx][ny]==--1:  # 플레이어가 있으면
                continue

            # print("진애 일로 이동",nx,ny)
            #
            # print("진애 번호",player_num)
            player_postion[nx][ny]=loser
            player[0]=nx
            player[1]=ny

            #총이 있다면, 가장 공격력 높은 총 획득하고 자기 총 반납
            if len(lst[nx][ny]) == 1:
                if int(lst[nx][ny][0]) == 0:
                    # print("총없음")
                    break
                else:  # 총이 있다면
                    # print("총있음")

                    best = get_gun(gun, nx, ny)
                    if best!=False:
                        player[4] = best


            break
        else:
            d+=1
            player[2]=d%4


def get_gun(gun,nx,ny):
    best=gun
    best_i=0
    check=False
    # print(lst)
    # print("플레이어 총",gun)
    # print("총바꾸는 위치",nx,ny)
    for i in range(len(lst[nx][ny])):
        if best<int(lst[nx][ny][i]):
            best=int(lst[nx][ny][i])
            best_i=i
            check=True
    if check==True:
        lst[nx][ny].pop(best_i)
        # print("여기서 지금 lst", lst)
        # print(lst[nx][ny])

        if len(lst[nx][ny])==0:
            lst[nx][ny].append('0')
        print("최종",lst)
        return best
    return False
for turn in range(k):
    for player in players:
        # print(player)
        x,y,d,s,gun,point=player[0],player[1],player[2],player[3],player[4],player[5]
        # print(player_postion)
        player_num= player_postion[x][y]
        # print(player_num,"플레이어 이동시작")
        loser=0
        winner=0
        loser_check=False
        while True:
            nx = x + dx[d%4]
            ny = y + dy[d%4]
            if 0<=nx<n and 0<=ny<n:
                # print(nx,ny,"로 이동")
                player[0] = nx
                player[1] = ny
                # print(player_postion)
                # print(player_postion[nx][ny])

                if player_postion[nx][ny]!=-1:  #플레이어가 있으면
                    # print("플레이어있음")
                    loser_check=True
                    me=s+gun
                    enemy=players[player_postion[nx][ny]][3]+players[player_postion[nx][ny]][4]
                    #싸우자
                    if me>enemy:

                        player[5]+=(me-enemy)
                        loser=player_postion[nx][ny]
                        winner=player_num
                    if enemy>me:
                        players[player_postion[nx][ny]][5]+=(enemy-me)
                        loser=player_postion[x][y]
                        winner = player_postion[nx][ny]
                    else:
                        if s>players[player_postion[nx][ny]][3]:
                            player[5]+=abs(enemy - me)
                            loser = player_postion[nx][ny]
                            winner = player_num
                        else:
                            players[player_postion[nx][ny]][5]+=abs(enemy - me)
                            loser = player_postion[x][y]
                            winner = player_postion[nx][ny]
                else:
                    # print("플레이어없어")
                    player_postion[nx][ny] = player_num
                    player_postion[x][y] = -1
                    if len(lst[nx][ny])==1:
                        if int(lst[nx][ny][0])==0:
                            break
                        else: #총이 있다면
                            # print("총있어")
                            best=get_gun(gun,nx,ny)
                            if best!=False:

                                player[4]=best
                                print(players)
                                print("총현황")
                                print(lst)
                if loser_check==True:


                    #
                    # print(loser,"진애이동시작")
                    loser_move(loser,players[loser])
                    player_postion[x][y] = winner
                    player_postion[x][y] = -1
                    # print("진애이동후")
                    # print(players)
                    # print("총현")
                    # print(lst)
                    best = get_gun(gun, nx, ny)
                    if best!=False:
                        player[4] = best


                break
            else:
                # print("방향바꿈")
                d+=2
                player[2]=d%4


    print(turn,":",players)
print("result")
print(players)