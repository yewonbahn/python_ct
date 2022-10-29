def solution(ingredient):
    stack=[]
    cnt=0
    i=0
    while True:
        lent=len(stack)
        if len(stack)>=4:
            if(stack[lent-1]==1 and stack[lent-2]==3 and stack[lent-3]==2 and stack[lent-4]==1):
                cnt+=1
                for j in range(4):
                    stack.pop()
                continue
        if(i==len(ingredient)):
            break
        stack.append(ingredient[i])

        i+=1

    return cnt
