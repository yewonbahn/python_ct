import sys
import time
start = time.time()  # 시작 시간 저장
array=[]
for each in range(10):
    array.append(list(map(int, sys.stdin.readline().split())))
dx=[0,1]
dy=[1,0]
sx,sy=1,1
array[sx][sy]=9
di=0
nx,ny=0,0
while True:
    if sx < 0 or sy >= 9 or sx < 0 or sy >= 9:
        break
    if sx == 8 and sy == 8:
        array[sx][sy]=9
        break
    nx=sx+dx[di]
    ny=sy+dy[di]
    print(nx,ny)

    if array[nx][ny]==0 :
        array[nx][ny] = 9
        sx=nx
        sy=ny
        di=0
        continue
    if array[nx][ny]==2 :
        array[nx][ny] = 9
        break


    di=1


for i in array:
    print(" ".join(map(str,i)))

