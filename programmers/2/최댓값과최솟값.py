def solution(s):
    answer =list(map(int,s.split()))
    str2=str(min(answer))+" "+str(max(answer))
    return str2