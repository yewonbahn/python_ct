n = input()
cnt=0

for i in range(int(n)+1):
    for j in range(60):
        for k in range(60):
            if(n in str(k) or n in str(j) or n in str(i) ):
                cnt+=1
print(cnt)