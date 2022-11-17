def solution(s):
    answer = ''
    check = 0
    for i in range(len(s)):
        if s[i] == " ":
            check = i+1
            answer += " "
            continue
        if i == check and not s[i].isdigit():
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    print(answer)
    return answer
solution("3people unFollowed me")