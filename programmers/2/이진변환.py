def solution(s):
    cnt=0
    cnt2=0
    while s!="1":
        cnt2+=1
        news = ''
        for i in range(len(s)):
            if s[i]=='0':
                cnt+=1
                continue
            news+=s[i]
        s=str(bin(len(news)))[2:]
    answer=[cnt2,cnt]
    return answer
print(solution("110010101001"))