def solution(arr):
    a=max(arr)
    cnt=0
    v=1
    value=a
    while True:
        if cnt==len(arr)-1:
            break
        for i in range(len(arr)):
            if value%arr[i]==0:
                cnt+=1
                continue
        if cnt==len(arr):
            break
        v+=1
        value=a*v
        cnt=0
    return value