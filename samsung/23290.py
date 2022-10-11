#마법사 상어와 복제
m,s=map(int,input().split())

fishes=[]
for i in range(m):
    x,y,di=map(int,input().split())
    fishes.append([x-1,y-1,di-1])
print(fishes)
sx,sy= map(int,input().split())
sx-=1
sy-=1
print(fishes)
#←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]


def shar_move(sx,sy,shark_move):
    #상화좌우 이동
    outfish=0
    print(shark_move)
    if(shark_move==3):
        return
    for i in range(m):
        fx,fy=fishes[i][0],fishes[i][1]
        if (x,y)==(fx,fy):
            print("냠")
            outfish+=1
            break

    for i in [2,6,0,4]:

        print(i,"번째")
        nx=sx+dx[i]
        ny=sy+dy[i]

        if nx<0 or nx>=m or ny<0 or ny>=m:
            return
        else:
            sx,sy=nx,ny
            print('nx,ny', nx, ny)
            print()
            shar_move(sx,sy,shark_move+1)
            shark_move=0

def fish_1move():
    #모든 물고기 이동시켜야함
    for i in range(m):

        x,y=fishes[i][0],fishes[i][1]
        print(x,y)
        di=fishes[i][2]
        cnt=0
        while True:
            if(cnt==9):
                nx,ny=0,0
                break
            nx=x+ dx[di]
            ny=y+ dy[di]
            if nx<0 or nx>=m or ny<0 or ny>=m or (sx,sy)==(nx,ny):
                di=8-(di+1)%8
                cnt+=1
            else:
                break
        print(nx,ny,di)
        fishes[i][0], fishes[i][1]=nx,ny
        fishes[i][2]=di

#물고기 이동
fish_1move()
print(fishes)
#상어 이동
shar_move(sx,sy,0)

print(outfish)