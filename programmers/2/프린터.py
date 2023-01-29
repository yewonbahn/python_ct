def solution(priorities, location):
    lst = []
    for i in range(len(priorities)):
        lst.append([i, priorities[i]])
    cnt=1
    while True:
        a, b = lst.pop(0)
        max_v=b
        for i in range(len(lst)):
            if max_v < lst[i][1]:
                max_idx,max_v=i,lst[i][1]
        if b<max_v:
            if lst[max_idx][0] == location:
                break
            del lst[max_idx]
            lst.append([a, b])
            for j in range(max_idx):
                c,d=lst.pop(0)
                lst.append([c,d])
        else:
            if a==location:
                break
        cnt+=1
    return cnt

solution([1, 1, 9, 1, 1, 1], 0)