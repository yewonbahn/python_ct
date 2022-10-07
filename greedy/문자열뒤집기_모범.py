#그리디 방식
# 전부 0 으로 바꾸는 경우와 전부 1로 바꾸는 경우중에 더 적은 횟수 가지는 경우 계산

data=input()
cnt0 =0
cnt1 =1

if data[0] == '1':
    cnt0 +=1
else:
    cnt1 +=1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            cnt0 +=1
        else:
            cnt1+=1

print(min(cnt0,cnt1))
