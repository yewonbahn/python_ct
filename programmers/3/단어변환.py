from collections import deque


def solution(begin, target, words):
    q = deque()
    answer = 0
    lst = []
    q.append((begin, 0))
    check = False
    while q:
        if check == True:
            break
        qword, y = q.popleft()
        for word in range(len(words)):
            print(words[word])
            cnt = 0
            for i in range(len(qword)):
                if words[word][i] == qword[i]:
                    cnt += 1
            print(cnt)
            if cnt == len(qword) - 1 and words[word] not in lst:
                if words[word] == target:
                    check = True
                    answer = y + 1
                    break
                q.append((words[word], y + 1))
                lst.append(words[word])
        print(q)

    return answer