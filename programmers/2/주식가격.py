def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt=0
        for j in range(i,len(prices)):
            cnt+=1
            if prices[i]>prices[j]:
                break
        answer.append(cnt-1)
    return answer