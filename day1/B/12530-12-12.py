l, r = input(), input()

for i in range(len(l)):
    if l[i] == '0':
        l = l[:i] + ('1' * (len(l) - i))
        break

for i in range(len(r)):
    if r[i] == '0':
        r = r[:i] + ('1' * (len(r) - i))
        break

# print(l, r)

ll = len(l)
lr = len(r)

sigma = lambda a: (a * (a + 1)) * 2

res = (sigma(lr) - sigma(ll))

unl = 0
lop = 0

um = 4
for ii in range(len(l)):
    i = l[ii]
    if i in '1':
        if 4 <= um:
            unl += 4
            um = 4
    elif i in '2':
        if 3 <= um:
            unl += 3
            um = 3
    elif i in '34':
        if 2 <= um:
            unl += 2
            um = 2
    elif i in '56':
        if 1 <= um:
            unl += 1
            um = 1
    else:
        break

    if i in '2357':
        if l[ii+1:].count('1') == (len(l) - ii):
            unl += 1

lm = 4
for ii in range(len(r)):
    i = r[ii]
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

    if i in '2357':
        if r[ii+1:].count('1') == (len(r) - ii - 1):
            lop += 1

res += unl

# print(unl, lop)

res -= lop

print(res)
