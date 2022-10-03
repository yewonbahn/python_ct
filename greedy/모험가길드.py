a = int(input())

team=list(map(int,input().split()))

team.sort()
team.reverse()
idx=0
cnt=0
for i in range(len(team)):

    max = team[i]
    i+=max
    idx += max
    if (idx > len(team)):
        print(cnt)
        break
    cnt+=1
