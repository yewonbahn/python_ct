n,m = map(int,input().split())

input_lst=list(set(list(map(int,input().split()))))
input_lst.sort()
s=[]

def dfs(start):
    if(len(s)==m):
        print(' '.join(map(str,s)))
        return
    for i in range(len(input_lst)):
        s.append(input_lst[i])
        dfs(start+1)
        s.pop()
dfs(0)