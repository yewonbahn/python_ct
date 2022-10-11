from collections import deque
n=int(input())
lst=[]
for i in range(n):
    lst.append(list(map(int,input().split())))

def bfs():
    dist=[[-1]*n for i in range(n)]
    q=deque([()])
now_size=2

while True:
    bfs()


print(lst)