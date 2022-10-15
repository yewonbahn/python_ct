n,m=map(int,input().split())
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))
blizards=[]
for i in range(m):
    d,h=map(int,input().split())
    blizards.append([d,h])


sx=int((n+1)/2-1)
sy=int((n+1)/2-1)

#방향  ↑, ↓, ←, →
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#방향  <- 아래 -> 위
dx=[0,1,0,-1]
dy=[-1,0,1,0]
lst=[]

def print_array():
    for i in array:
        print(i)
def move():
    print("이동전")
    print_array()
    time = 0
    nx2,ny2=sx,sy
    for i in range(n*2-1):
        if(i%2==0):
            time+=1
        for j in range(time):

            nx2=nx2+dx[i%4]
            ny2=ny2+dy[i%4]
            if(array[nx2][ny2]==0):
                continue
            lst.append(array[nx2][ny2])



def bomb(lst):
    total=0
    stack2=[]
    stack=[]
    for i in lst:
        if len(stack2) >= 4 and i!=stack2[-1]:
            total+=stack2[-1]*len(stack2)
            for j in range(len(stack2)):
                stack.pop()
            stack2 = []
        stack.append(i)

        if (len(stack2)==0):
            stack2.append(i)
            continue

        if i==stack2[-1]:
            stack2.append(i)
        else:
            for k in range(len(stack2)):
                stack2.pop()
            stack2.append(i)
    return stack,total
def change(lst):
    stack2=[]
    stack=[]
    for i in lst:

        if(len(stack)==0):
            stack.append(i)
            continue
        if(len(stack2)==0):
            stack2.append(i)

        if(stack2[-1]==i):
            stack2.append(i)
            stack.append(i)
        else:

            a=len(stack2)
            b=stack2[-1]
            for j in range(len(stack2)):
                stack.pop()

            stack.append(a)
            stack.append(b)
            stack.append(i)
            stack2=[]
            stack2.append(i)


    stack.append(lst[-1])
    return stack


def move2(lst):
    array=[[0]*n for _ in range(n)]
    time = 0
    nx2,ny2=sx,sy
    cnt=0
    for i in range(n*2-1):

        if(i%2==0):
            time+=1
        for j in range(time):
            if (len(lst) <= cnt):
                break

            nx2=nx2+dx[i%4]
            ny2=ny2+dy[i%4]

            array[nx2][ny2]=lst[cnt]

            cnt+=1

    return array




answer=0
for i in range(m):
    print(i,"번째")
    print_array()
    real_total = 0

    dir=blizards[i][0]-1
    length=blizards[i][1]
    print(dir,length)
    # 구슬 파괴
    nx,ny=sx,sy
    for j in range(length):
        nx=nx+dx[dir]
        ny=ny+dy[dir]
        array[nx][ny]=0
    #구슬 이동
    move()
    #구슬 폭파

    while True:
        value=bomb(lst)
        new_list=value[0]
        real_total+=value[1]
        lst=new_list
        if(lst==new_list):

            value=bomb(lst)
            real_total+=value[1]
            lst=value[0]
            break
    answer+=real_total
    #구슬 변화단계
    new_list2=change(lst)
    array=move2(new_list2)
print(answer)
