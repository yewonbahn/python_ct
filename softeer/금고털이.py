import sys

lst = []
answer = 0
w, n = map(int, input().split())
for i in range(n):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x: x[1], reverse=True)

for a, b in lst:
    if w < 0:
        break
    if a >= w:
        answer += w * b
        break
    else:
        answer += a * b
        w -= a

print(answer)