from collections import deque
def solution(priorities, location):
    answer=0
    q=deque()
    for i in range(len(priorities)):
        q.append((priorities[i],i))
    print(q)
    a=priorities[0]
    while q:
        answer2 = False
        check=False
        answer+=1
        print(answer)
        for i in q:
            if a<i[0]:
                a,b=q.popleft()
                print(q)
                q.remove((i[0],i[1]))
                print(q)
                if i[1]==location:
                    answer2=True
                    break
                q.append((a,b))
                print(q)
                check=True
                break
        if answer2==True:
            break
        if check == True:
            continue
        c,d=q.popleft()
        print(q)
        if d==location:
            answer-=1
            break
    return answer

solution([2, 1, 3, 2],2)