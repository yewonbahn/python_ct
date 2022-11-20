def solution(n):
    val = 1
    k=1
    while k<n//2+1:
        cnt = 0
        for i in range(k,n):
            cnt += i
            if cnt >= n:
                if cnt==n:
                    val+=1
                break

        k+=1

    answer = val
    return answer
print(solution(15))