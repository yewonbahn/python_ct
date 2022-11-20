from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    q = deque()
    q.append((characterX, characterY, 0))
    distance=[[0]*100 for i in range(100)]
    recheck=[0]*len(rectangle)

    while q:
        x, y, z = q.popleft()
        for i in range(len(rectangle)):
            # 1 1 7 4
            print(recheck)
            print(recheck[i]==0 and rectangle[i][0]<=x<=rectangle[i][2] or rectangle[i][1] <= y <= rectangle[i][3])
            if recheck[i]==0 and (rectangle[i][0]<=x<=rectangle[i][2] or rectangle[i][1] <= y <= rectangle[i][3]):
                print(i)
                lst = [[rectangle[i][0], rectangle[i][1]], [rectangle[i][0], rectangle[i][3]],
                       [rectangle[i][2], rectangle[i][1]], [rectangle[i][2], rectangle[i][3]]]
                for j in lst:
                    if distance[j[0]][j[1]]==0:
                        check = 0
                        for k in range(len(rectangle)):
                            if rectangle[k][0] < j[0] < rectangle[k][2] and rectangle[k][1] < j[1] < rectangle[k][3]:
                                print(k)
                                check = 1
                                break;
                        if check == 1:
                            print("못가")
                            continue

                        q.append((j[0], j[1], z + abs(x - j[0]) + abs(y - j[1])))
                        distance[j[0]][j[1]]=1
                        recheck[i] = 1
                break
        print(q)

    answer = 0
    return answer

solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8)