n, m, k = map(int, input().split())
n -= 1
m -= 1
res = min(m, n) // k + (1 if min(n, m) % k != 0 else 0)
o = max(m, n) - min(n, m)
if o == 0:
    print(res)
    exit()
res += o // k + (1 if o % k != 0 else 0)
print(res)
