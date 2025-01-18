def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    p = 1
    for i in list(map(int, list(str(n)))):
        p *= i
    return is_prime(p)

l, r = input(), input()

if len(r) < 7:
    l = int(l)
    r = int(r)
    res = 0
    for i in range(l, r + 1):
        if (check(i)):
            res += 1
    print(res)

else:
    s = len(r) - 1
    e = (s * (s + 1)) // 2
    print(4 * e)
