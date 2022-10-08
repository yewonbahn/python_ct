a=int(input())
lst=[]
for i in range(a):
    lst.append(int(input()))
lst.sort()
lst.reverse()
print(" ".join(map(str,lst)))