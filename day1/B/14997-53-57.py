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
while len(i) <= 19:
    lst.append(int(i))
    i = np(i)

l, r = input(), input()
if len(r) <= 19:
    res = 0
    for i in lst:
        if int(l) <= i <= int(r):
            res += 1
    print(res)
elif r == ('1' + ('0' * (len(r) - 1))):
    print(2 * len(r) * (len(r) - 1))
else:
    ll = len(l) - 1
    rl = len(r)

    ul = lambda a: 2 * a * (a - 1)
    res = ul(rl - 1) - ul(ll)

    fpl = '1' * ll + '2'
    while int(fpl) < int(l):
        res -= 1
        fpl = np(fpl)

    fpr = '1' * (rl - 1) + '2'
    while int(fpr) < int(r):
        res += 1
        fpr = np(fpr)

    print(res)
