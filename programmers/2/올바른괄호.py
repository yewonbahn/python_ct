def solution(s):
    stack=[]
    cnt=0
    for i in s:
        if len(stack)!=0:
            if stack[-1]=="(" and i==")":
                cnt+=1
                stack.pop()
                continue
        stack.append(i)
    if len(stack)==0:
        return True
    else:
        return False
solution("()()")