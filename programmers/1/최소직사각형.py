def solution(sizes):
    answer = 0
    sizes[0].sort()
    a = sizes[0][0]
    b = sizes[0][1]

    for i in range(1, len(sizes)):
        sizes[i].sort()
        if sizes[i][0] > a:
            a = sizes[i][0]
        if sizes[i][1] > b:
            b = sizes[i][1]
    print(a, b)
    return a * b