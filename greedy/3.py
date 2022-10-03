#숫자 카드 게임
#여러개의 숫자카드 중에서 가장 높은 숫자가 쓰인 카드 한장을 뽑는 게임

a,b=map(int,input().split())
lst=[]
num = 0

for i in range(a):
    lst.append(list(map(int,input().split())))
    lst[i].sort()
    if (num < lst[i][0]):
        num = lst[i][0]
print(num)
