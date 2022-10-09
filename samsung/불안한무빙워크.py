from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * n)
res = 0
print(belt)
print(robot)
while 1:

    belt.rotate(1)
    robot.rotate(1)
    print("belt",belt)
    print("robot",robot)
    robot[-1] = 0  # 로봇이 내려가는 부분이니 0
    if sum(robot):  # 로봇이 존재하면
        print("1번째 조건문, 벨트위 로봇이 있다면")

        for i in range(n - 2, -1, -1):  # 로봇 내려가는 부분 인덱스 i-1 이므로 그 전인 i-2부터
            print("[",i,"인덱스의 벨트 계산]")
            if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] >= 1:
                print(i,"번째 벨트 부분에 로봇이 있고, 그 다음 번째 벨트에 로봇이 없고 그 담 벨트 내구성이 1이상임")
                print("다음 인덱스의 로봇 리스트 1로 설정하고 현재 인덱스는 0 그리고 내구성 -1 ")
                robot[i + 1] = 1
                robot[i] = 0
                belt[i + 1] -= 1
        robot[-1] = 0  # 이 부분도 로봇 out -> 0임
    if robot[0] == 0 and belt[0] >= 1:
        print("2번째 조건문. 벨트 1번째값이 1이상이고 로봇리스트의 첫값이 0임")
        print("벨트 1번째 값에서 -1 하고, 로봇리스트 첫값 1로 설정")
        robot[0] = 1
        belt[0] -= 1
    res += 1
    print("회전완료 현재:",res)
    if belt.count(0) >= k:
        break

print(res)

