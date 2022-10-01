#완전 탐색: 모든 경우의 수를 주저없이 다 계산하는 해결방법
#시뮬레이션 : 문제에서 제시한 알고리즘을 한단계씩 차례대로 직접수행


n=input()
x=n[0]
y=int(n[1])

lst={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
x=lst[x]

steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result=0
for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if(nx >=1 and ny<=8 and ny >=1 and ny<=8):
        result+=1


print(result)