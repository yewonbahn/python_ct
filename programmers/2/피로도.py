answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer

#두번째 방법

from itertools import permutations


def length_check(lst, length, k, dungeons):
    lst2 = list(permutations(lst, length))
    for i in range(len(lst2)):
        cur = k
        check = False
        for j in lst2[i]:
            if cur >= dungeons[j][0]:
                cur -= dungeons[j][1]
            else:
                check = True
                break

        if check == False:
            return True

    return False


def solution(k, dungeons):
    lst = [i for i in range(len(dungeons))]
    answer = 0
    for i in range(len(dungeons), 0, -1):
        if length_check(lst, i, k, dungeons) == True:
            answer = i
            break

    return answer

