def solution(n,a,b):
    answer = 0
    while(a!=b):
        answer+=1
        if(a%2==0):
            a=a/2
        else:
            a=(a+1)/2

        if(b%2==0):
            b=b/2
        else:
            b=(b+1)/2
        print(a,b)
    return answer