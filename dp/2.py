a=int(input())

d=[0]*30001

for i in range(2,a+1):
    print(i,"일떄")
    d[i]=d[i-1]+1
    if i%2==0:
        print("1")
        d[i]=min(d[i],d[i//2]+1)
    if i%3==0:
        print("2")
        d[i]=min(d[i],d[i//3]+1)
    if i%5==0:
        print("3")
        d[i]=min(d[i],d[i//5]+1)
print(d)
print(d[a])

