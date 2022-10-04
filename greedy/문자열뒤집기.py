data = input()
s=data[0]
cnt=0

store=[]
for i in data:
    if(s!=i):
        if (len(store)==0):
            store.append(i)
            s = i
            continue
        if(store[-1]!=i):
            s = i
            continue
        s=i
        store.append(i)

print(len(store))