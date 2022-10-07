def solution(n, lost, reserve):
    cnt = 0
    num = n - len(lost)
    lost.sort()
    reserve.sort()
    intersection = set(lost) & set(reserve)
    for i in list(intersection):
        reserve.remove(i)
        lost.remove(i)

    for i in lost:
        for j in reserve:
            if i == j or i - 1 == j or i + 1 == j:
                print(i)
                reserve.remove(j)
                print(reserve)
                cnt += 1
                break

    answer = num + cnt + len(list(intersection))
    return answer