def solution(n):
    answer = 0
    ori = n
    while True:
        n += 1
        if bin(ori).count("1") == bin(n).count("1"):
            answer = n
            break

    return answer