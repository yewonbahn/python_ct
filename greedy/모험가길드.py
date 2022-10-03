a = int(input())

team=list(map(int,input().split()))

team.sort()

cnt=0 # 총그룹수
mb = 0 #현재 그룹에 포함된 모헙가 수

for i in team:
    mb+=1
    if mb >= i:
        cnt+=1
        mb = 0
print(cnt)