def solution(brown, yellow):
    cnt=1
    ori=yellow
    answer=[0,0]
    while True:
        if yellow*2+cnt*2+4==brown:
            answer=[yellow+2,cnt+2]
            break
        while True:
            if ori%(cnt+1)==0:
                cnt+=1
                break
            cnt+=1
        yellow=ori//cnt
    return answer

# 테스트 반례 코드
# _list  = []
# for i in range(1,1000):
#     for j in range(1,1000):
#         brown = (i+2)*2 + (j*2)
#         yellow = i*j
#         _min = min(i+2,j+2)
#         _max = max(i+2,j+2)
#         _list.append([brown,yellow,_max,_min])
#
# for i in _list:
#     print(i)
#     res = solution(i[0],i[1])
#     print("myanser",res)
#     if i[2] != res[0] or i[3] != res[1]:
#         print("{},{},[{},{}]".format(i[0],i[1],i[2],i[3]))
#         break
#
#     print("pass")