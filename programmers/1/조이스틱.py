def solution(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)
    print("중간", answer)

    move = n - 1

    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)
        print("d", distance)
        print("m", move)

    answer += move
    return answer
#예를 들어 "BBBAAAB" 를 생각해보면 idx가 2일때 next_idx는 6이고
# distance는 idx에 0까지 거리인 2 와 0부터 next_idx까지 거리인 1중 1이 됩니다.
# 이때 A가 아닌 모든 알파벳을 방문하는데 필요한 총 움직임은 2까지 오른쪽으로 idx 만큼
# 0에서 왼쪽으로 n - next_idx만큼 , 왼쪽 오른쪽 중 가장 짧은 distance만큼 한번) 입니다.