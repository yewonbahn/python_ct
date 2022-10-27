from collections import deque


def solution(n, computers):
    visited = [False] * (n + 1)
    q = deque()
    lst2 = []
    answer_lst = []
    for i in range(n):
        lst2.append(i)
    print(lst2)
    lst = []
    for j in range(n):
        cnt = 0
        print(j, ":")
        q.append(j)
        while q:
            x = q.popleft()
            lst.append(x)

            for i in range(n):
                if computers[i][x] == 1 and not visited[i]:
                    q.append(i)
                    visited[i] = True
            print(q)
            if len(q) == 0:
                if cnt != 0:
                    answer_lst.append(cnt)

            cnt += 1
    new_lst = list(set(lst))
    if len(new_lst) == n:
        answer = 1
    else:
        answer = n - len(new_lst) + 1

    answer = (len(answer_lst))
    return answer