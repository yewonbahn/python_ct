s = input()
lst = list(s)
for i in range(len(lst)) :
    lst[i]=int(lst[i])

for i in range(len(lst)):
    if(i==len(lst)-1):
        break
    lst[i+1]=max(lst[i]+lst[i+1],lst[i]*lst[i+1])

print(lst[-1])