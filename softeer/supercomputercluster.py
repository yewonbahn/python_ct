import sys

a, b = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

array2=set(array)
c = min(array2)
array2.remove(c)
d=min(array2)
print(c,d)
check2=False
while True:
    if check2==True:
        break
    if b<=0:
        print(min(array))
        break

    for i in range(len(array)):
        if b <= 0:
            print(min(array)-1)
            check2=True
            break
        print("i",i,"c",c,array[i])
        if c>=array[i]:
            print(c,"보다",i,"번쨰",array[i],"가 더")
            money=0
            check=array[i]
            for j in range(c+1,d+1):
                money=(j-array[i])*(j-array[i])
                if money>=b:
                    break
                check = j
            print("mo",money)
            b-=money
            print("b",b)
            print("check,",check)
            array[i]=check
            print(array)
    array2 = set(array)
    c = min(array2)
    array2.remove(c)
    print()
    d = min(array2)
    print(c,d)




