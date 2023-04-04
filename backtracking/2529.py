from itertools import permutations
n=int(input())
lst=list(input().split())
numbers=[0,1,2,3,4,5,6,7,8,9]
per_lst=list(permutations(numbers,n+1))
answer=["",""]

for i in range(len(per_lst)):
    flag=False
    for j in range(n):
        if lst[j]=="<":
            if per_lst[i][j] > per_lst[i][j+1]:
                flag=True
                break
        else:
            if per_lst[i][j] < per_lst[i][j+1]:
                flag=True
                break
    if flag==False:
        answer[1]=" ".join(map(str,per_lst[i]))
        break

per_lst.sort(reverse=True)
for i in range(len(per_lst)):
    flag=False
    for j in range(n):
        if lst[j]=="<":
            if per_lst[i][j] > per_lst[i][j+1]:
                flag=True
                break
        else:
            if per_lst[i][j] < per_lst[i][j+1]:
                flag=True
                break
    if flag==False:
        answer[0] = "".join(map(str,per_lst[i]))
        break

for i in range(2):
    print(answer[i])
