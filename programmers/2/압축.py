from string import ascii_lowercase

alphabet_dict = {}

for i in range(len(ascii_lowercase)):
    alphabet_dict[ascii_lowercase[i].upper()] = i + 1


def solution(msg):
    answer = []
    word = ''
    cnt = 0
    check = False
    while True:
        cnt2 = 0
        for i in range(cnt, len(msg)):
            before = word
            word += msg[i]
            cnt2 += 1
            if i == len(msg) - 1 and word in alphabet_dict:
                answer.append(alphabet_dict[word])
                check = True
                break
            if word not in alphabet_dict and len(word) >= 2:
                alphabet_dict[word] = len(alphabet_dict) + 1
                answer.append(alphabet_dict[before])
                break
        if check == True:
            break
        val = cnt + len(word)
        if len(word) <= 1:
            cnt += 1
        else:
            cnt += len(word) - 1
        if val > len(msg):
            break
        word = ''

    return answer