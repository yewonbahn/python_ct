import math


def solution(fees, records):
    dic = {}
    answer = []
    for rec in records:
        time, num, his = rec.split()
        if int(num) not in dic:
            dic[int(num)] = [[time, num, his]]
        else:
            dic[int(num)].append([time, num, his])
    dic = sorted(dic.items())
    for i in dic:
        car_lst = i[1]
        total_min = 0
        for j in range(0, len(car_lst)):
            if j % 2 != 0:
                cur_h, cur_m = map(int, car_lst[j][0].split(":"))
                l_h, l_m = map(int, car_lst[j - 1][0].split(":"))
                dif_h = cur_h - l_h
                dif_m = cur_m - l_m
                if dif_m < 0:
                    dif_m += 60
                    dif_h -= 1
                total_min += dif_h * 60 + dif_m

            if j == len(car_lst) - 1 and car_lst[j][2] == "IN":
                l_h, l_m = map(int, car_lst[j][0].split(":"))
                dif_h = 23 - l_h
                dif_m = 59 - l_m
                if dif_m < 0:
                    dif_m += 60
                    dif_h -= 1
                print(dif_h * 60 + dif_m)
                total_min += dif_h * 60 + dif_m
        if fees[0] >= total_min:
            value = fees[1]
        else:
            value = fees[1] + math.ceil((total_min - fees[0]) / fees[2]) * fees[3]
        answer.append(value)
    return answer