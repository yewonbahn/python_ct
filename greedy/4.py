#1이 될때까지

n,k = map(int,input().split())
ori=n
cnt=0
while True:
    if (n==1):
        print(cnt)
        break
    if(n%k==0):
        n = n / k
        cnt+=1
    else:
        n=n-1
        cnt+=1
