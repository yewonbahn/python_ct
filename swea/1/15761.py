a=int(input())
data=[]

for i in range(a):
    data.append(list(map(int,input().split())))
for i in range(len(data)):
    small=''
    big=''
    big=big+'1'*data[i][0]
    small+='1'
    big+='0'*data[i][1]
    small+='0'*data[i][1]
    small+='1'*(data[i][0]-1)
    total=str(bin(int(big,2)*int(small,2)))
    print("#"+str(i+1),total.count('1'))


