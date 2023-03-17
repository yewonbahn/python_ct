n = int(input())
x, y = 0, 0
global answer
answer=0
check_col=[0]*15
check_l=[0]*30
check_r=[0]*30

def backtracking(cnt):
    global answer
    if cnt==n: #탈출 조건
        answer+=1
        return;

    for i in range(n):

        if not check_col[i] and not check_l[cnt+i] and not check_r[cnt-i+n]:
            check_col[i]=1
            check_l[cnt+i]=1
            check_r[cnt-i+n]=1
            backtracking(cnt+1)

            check_col[i]=0
            check_l[cnt+i]=0
            check_r[cnt-i+n]=0

backtracking(0)
print(answer)