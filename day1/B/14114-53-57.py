def np(p):
    no = p.replace('1', '')

    pos = p.index(no)

    p = list(p)

    if no == '2':
        p[pos] = '3'
    elif no == '3':
        p[pos] = '5'
    elif no == '5':
        p[pos] = '7'
    else:
        if pos == 0:
            return '1' * len(p) + '2'
        else:
            p[pos] = '1'
            p[pos - 1] = '2'

    return ''.join(p)

lst = list()
i = '2'
while len(i) <= 101:
    lst.append(int(i))
    i = np(i)

l, r = input(), input()
if len(r) <= 101:
    res = 0
    for i in lst:
        if int(l) <= i <= int(r):
            res += 1
    print(res)
else:
    print(2 * len(r) * (len(r) - 1))
