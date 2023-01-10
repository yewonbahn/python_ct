def is_prime_number(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    rb = rev_base[::-1]

    print(rb)
    lst = str(rb).split('0')
    print(lst)
    for i in lst:
        if i == "" or i == '1' or '0' in i:
            continue
        print(type(i))
        v = is_prime_number(int(i))
        if v == True:
            answer += 1

    return answer