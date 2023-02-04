import math
def solution(str1, str2):
    new_s = []
    new_s2 = []
    answer = 0
    cnt=0
    v=0
    for i in range(0,len(str1)):
        if i==len(str1)-1:
            break
        if str1[i:i + 2].isalpha() :
            new_s.append(str1[i:i + 2].lower())
    for i in range(0,len(str2)):
        if i==len(str2)-1:
            break
        if str2[i:i + 2].isalpha():
            new_s2.append(str2[i:i + 2].lower())
    new_s.sort()
    new_s2.sort()

    if len(new_s)<=len(new_s2):
        min_s=new_s
        max_s=new_s2
    else:
        min_s=new_s2
        max_s=new_s
    for i in range(len(min_s)):
        for j in range(v, len(max_s)):
            if v==len(max_s):
                break
            if min_s[i] == max_s[j]:
                cnt += 1
                v=j
                v+=1
                break
    sum=len(max_s)+len(min_s)-cnt
    if sum==0 :
        answer=1*65536
    else:
        answer=(cnt/sum)*65536
    return math.floor(answer)