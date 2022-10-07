data = input()
s=data[0] #for문 돌릴라고 첫번째값 저장

store=[]
for i in data:
    if(s!=i): # 현재값이 저장된s랑 다르다면
        if (len(store)==0): # 임의 list안에 값 비어있으면 - 첫번째 반복돌때
            store.append(i)
            s = i
            continue
        if(store[-1]!=i): # 현재값이 store 저장값과 다르다면?
            s = i #s값 일단 변경
            continue
        s=i
        store.append(i)

print(len(store))