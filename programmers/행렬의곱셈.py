def solution(arr1, arr2):
    answer = []
    print(arr2)
    for i in range(len(arr1)):
        lst=[]
        for j in range(len(arr2[0])):
            sum=0
            for k in range(len(arr2)):
                sum=sum+arr1[i][k]*arr2[k][j]
            lst.append(sum)
        answer.append(lst)
    return answer
solution([[1, 2, 3], [4, 5, 6]],[[1, 2], [3, 4], [5, 6]])