l, r = input(), input()

if r[1] == '0':
    r = '1' * len(r)

ll = len(l)
lr = len(r)

sigma = lambda a: (a * (a + 1)) * 2

res = (sigma(lr) - sigma(ll))

# print(res)

unl = 0
lop = 0

um = 4
for i in l:
    if i in ['1', '2']:
        if 4 <= um:
            unl += 4
            um = 4
    elif i in ['3']:
        if 3 <= um:
            unl += 3
            um = 3
    elif i in ['4', '5']:
        if 2 <= um:
            unl += 2
            um = 2
    elif i in ['6', '7']:
        if 1 <= um:
            unl += 1
            um = 1
    else:
        break

lm = 4
for i in r:
    if i in ['1']:
        if 4 <= lm:
            lop += 4
            lm = 4
    elif i in ['2']:
        if 3 <= lm:
            lop += 3
            lm = 3
    elif i in ['3', '4']:
        if 2 <= lm:
            lop += 2
            lm = 2
    elif i in ['5', '6']:
        if 1 <= lm:
            lop += 1
            lm = 1
    else:
        break

res += unl

# print(res)

res -= lop

print(res)
