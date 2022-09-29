#1이 될때까지

n,k = map(int,input().split())
ori=k

while True:
    if(n<=k):
        print(n)
        break
    n=n/k
    print(n)