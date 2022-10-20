# def fibo(x):
#     if x==1 or x==2:
#         return 1
#     return fibo(x-1)+fibo(x-2)
#
# print(fibo(4))

# N이 커지면, 시간복잡도가 너무 커짐
# 1. 큰문제를 작은 문제로 나눌 수 있다.
# 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰문제에서도 동일하다
d= [0]*100
def fibo(x):
    if x==1 or x==2:
        return 1
    if d[x]!=0:
        return d[x]
    d[x]= fibo(x-1)+fibo(x-2)
    return d[x]
print(fibo(99))

#다이나믹 프로그래밍? 큰문제를 작게 나누고, 같은 문제라면 한번씩만 풀어 문제를 효율적으로 해결하는 알고리즘 기법
#큰 문제를 해결하기 위해 작은 문제를 호출 -> 탑다운 방식