def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        check=False
        for k in range(len(number)):
            if discount[i:i+10].count(want[k])<number[k]:
                check=True
                break
        if check==False:
            answer+=1
    return answer