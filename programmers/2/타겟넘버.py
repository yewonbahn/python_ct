# def solution(numbers, target):
#     n = len(numbers)
#     answer = 0
#
#     def dfs(idx, result):
#         if (idx == n):
#             if (result == target):
#                 nonlocal answer
#                 answer += 1
#             return
#         else:
#             dfs(idx + 1, result + numbers[idx])
#             dfs(idx + 1, result - numbers[idx])
#
#     dfs(0, 0)
#     return answer
from collections import deque

def solution(numbers, target):
    answer=0

    q=deque()
    q.append([numbers[0],0])
    q.append([-numbers[0],0])

    while q:
        a,b=q.popleft()
        b+=1
        if b < len(numbers):
            q.append([a+numbers[b],b])
            q.append([a-numbers[b],b])
        else:
            if target==a:
                answer+=1
    return answer
solution([1, 1, 1, 1, 1],3)