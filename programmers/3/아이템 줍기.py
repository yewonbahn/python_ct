from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    q = deque()
    q.append((characterX, characterY,0))
    visited=[[0]*50 for i in range(50)]
    arr=[]

    while q:
        x, y, z= q.popleft()
        if [x,y]==[itemX,itemY]:
            arr.append(z)
        visited[x][y]=1

        for i in range(len(rectangle)):
            # 1 1 7 4
            rx = rectangle[i][0]
            ry = rectangle[i][1]
            rx2 = rectangle[i][2]
            ry2 = rectangle[i][3]
            if (x == rx and y == ry):
                if not visited[rx][ry2]:
                    q.append((rx, ry2,z+ry2))
                if not visited[rx2][ry]:
                    q.append((rx2, ry,z+rx2))
            if (x == rx2 and y == ry2):
                if not visited[rx][ry2]:
                    q.append((rx, ry2,z+rx2))
                if not visited[rx2][ry]:
                    q.append((rx2, ry,z+ry2))
            if (x == rx and y == ry2):
                if not visited[rx][ry]:
                    q.append((rx, ry,z+ry2))
                if not visited[rx][ry2]:
                    q.append((rx, ry2,z+rx2))
            if (x == rx2 and y == ry):
                if not visited[rx][ry]:
                    q.append((rx, ry,z+rx2))
                if not visited[rx][ry2]:
                    q.append((rx, ry2,z+ry2))
            if (y != ry or y != ry2):
                if not visited[x][ry]:
                    q.append((x, ry,z+abs(ry-y)))
                if not visited[x][ry2]:
                    q.append((x, ry2,z+abs(ry2-y)))
            if (x != rx or x != rx2):

                if not visited[rx][y]:
                    q.append((rx, y,z+abs(rx-x)))
                if not visited[rx2][y]:
                    q.append((rx2, y,z+abs(rx2-x)))
        print(q)

    answer = 0
    print(arr)
    return answer

solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8)