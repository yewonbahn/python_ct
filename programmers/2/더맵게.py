import heapq


def solution(scoville, K):
    answer = 0
    q = []
    cnt = len(scoville)
    for i in scoville:
        heapq.heappush(q, i)
    while len(q) >= 2:

        minsco = heapq.heappop(q)
        minsco2 = heapq.heappop(q)
        if minsco >= K and minsco2 >= K:
            break
        answer += 1
        heapq.heappush(q, minsco + minsco2 * 2)
        if answer >= cnt - 2:
            if minsco + minsco2 * 2 < K:
                return -1

    return answer