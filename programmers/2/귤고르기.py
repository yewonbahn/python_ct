def solution(k, tangerine):
    counter = {}
    for i in tangerine:
        counter.setdefault(i, 0)
        counter[i] += 1
    value = len(tangerine) - k
    cnt=0
    counter = sorted(counter.items(),key=lambda x: x[1])
    for k,v in counter:
        if value>=v:
            value -= v
            cnt+=1
        else:
            break

    return len(counter)-cnt