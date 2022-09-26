# 큰수의 법칙

n,m,k = map(int,input().split())
lst = list(map(int, input().split()))

lst.sort()
lst.reverse()
cnt=0
answer=0

for i in range(m):
    if(k==cnt):
        answer += lst[1]
        cnt=0
    else:
        answer+=lst[0]
        cnt+=1;


print(answer)