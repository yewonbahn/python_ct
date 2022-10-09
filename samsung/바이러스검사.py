n=int(input())
cus=list(map(int,input().split()))
teamb,teamt=map(int,input().split())
answer=0

for i in cus:
    remain= i-teamb
    if(remain<=0):
        continue
    if(remain==teamt):
        answer+=1
        continue
    if(remain%teamt == 0):
        requirenum=remain/teamt

    else:
        requirenum= remain//teamt+1

    answer+=requirenum
print(int(answer+n))
