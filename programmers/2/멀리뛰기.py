import math


def solution(n):
    answer = 0
    dp = [0] * 2000
    dp[1] = 1  # 1
    dp[2] = 2  # 1 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n] % 1234567