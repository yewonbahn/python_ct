def solution(s):
    strtolst = []
    lst2 = []
    lst3 = []
    temp = ''
    for i in s:
        if i == ',':
            strtolst.append(temp)
            temp = ''
            continue
        if i == "}":
            strtolst.append(temp)
            temp = ''
            continue
        if i == "{":
            continue
        if i.isdigit():
            temp += i

    for i in strtolst:
        if i.isdigit():
            lst2.append(int(i))
        else:
            lst3.append(lst2)
            lst2 = []
    answer = []
    lst3.sort(key=lambda x: len(x))
    for i in lst3:
        for j in i:
            if j not in answer:
                answer.append(j)

    return answer