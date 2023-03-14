a=int(input())
b=input().split()
captin, member=map(int,input().split())
lst=[]
total=0

for i in range(a):
    lst.append(int(b[i]))

for i in range(a):
    if lst[i]-captin<=0:
        total+=1
        continue
    if (lst[i]-captin)%member==0:
        total+=(lst[i]-captin)//member+1
        continue
    total+=(lst[i]-captin)//member+2
print(total)