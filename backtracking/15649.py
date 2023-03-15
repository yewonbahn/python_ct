from itertools import permutations

n,m=map(int,input().split())
lst=[]
for i in range(n):
    lst.append(i+1)
for i in permutations(lst,m):
    print(" ".join(map(str,list(i))))