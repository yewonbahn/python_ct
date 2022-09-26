# 큰수의 법칙
#가장 큰수 K번 더하고 두번째로 큰수 한번 더하는 연산
n,m,k = map(int,input().split())
lst = list(map(int, input().split()))

lst.sort()
lst.reverse()
answer=0
#
# for i in range(m):
#     if(k==cnt):
#         answer += lst[1]
#         cnt=0
#     else:
#         answer+=lst[0]
#         cnt+=1;

# M의 크기가 100억 이상이라면?
cnt=m/(k+1)*k+m%(k+1)
answer+=cnt*lst[0]
answer+=(m-cnt)*lst[1]


print(int(answer))