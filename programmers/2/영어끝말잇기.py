def solution(n, words):
    wordslst = []
    answer=[]
    for i in range(len(words)):
        print(i % n + 1, i // n + 1)
        if i>=1 and words[i-1][-1]!=words[i][0]:
            answer=[i % n + 1, i // n + 1]
            break
        if words[i] in wordslst:
            answer=[i % n + 1, i // n + 1]
            break
        wordslst.append(words[i])
    if len(answer)==0:
        answer=[0,0]
    return answer
solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])