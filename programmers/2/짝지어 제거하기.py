def solution(s):
    answer = -1
    st = []

    for i in s:
        if not st:
            st.append(i)
        elif i == st[-1]:
            st.pop()
        else:
            st.append(i)
    if len(st) > 0:
        return 0
    else:
        return 1

solution("baabaa")