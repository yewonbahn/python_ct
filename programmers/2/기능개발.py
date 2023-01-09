def solution(progresses, speeds):
    answer = []
    answer2=[]
    num=1
    for i in range(len(progresses)):
        a = (100-(progresses[i]))//(speeds[i])
        if (100-(progresses[i]))%(speeds[i])!=0:
            a+=1
        if i==0:
            answer.append(a)
            continue
        if(answer[-1]>=a):
            num+=1
            if i==len(progresses)-1:
                answer2.append(num)

        else:
            answer2.append(num)
            num=1
            answer.append(a)
            if i==len(progresses)-1:
                answer2.append(num)

    return answer2