# =============== day and input ===============
day = "08"

import sys
if len(sys.argv) > 1:
    ex = "." + sys.argv[1]
else:
    ex = "." + "in"

filename = "data_" + day + ex


# =============== preparation ===============
with open(filename) as f:
  data = f.read().splitlines()

data = [e.split(" | ") for e in data]
data = [ (tuple(e[0].split()), tuple(e[1].split())) for e in data]


# =============== part 1 ===============
res = 0

dataA = [a for e in data for a in e[1]]
res = sum([1 if len(a) in [2,3,4,7] else 0 for a in dataA])
print(res)


# =============== part 2 ===============

def solveWiring(t, f):
    pents = []
    hexas = []
    for e in t:
        if len(e) == 2:
            one = frozenset(e)
        elif len(e) == 3:
            seven = frozenset(e)
        elif len(e) == 4:
            four = frozenset(e)
        elif len(e) == 7:
            eight = frozenset(e)
        elif len(e) == 5:
            # 5 letters -> two, three, five
            pents.append(frozenset(e))
        elif len(e) == 6:
            # 6 letters -> six, nine, zero
            hexas.append(frozenset(e))
        else:
            print("Error")
    for h in hexas:
        if len(h - four) == 2:
            nine = h
        elif len(h - one) == 5:
            six = h
        else:
            zero = h
    for p in pents:
        if len(p - one) == 3:
            three = p
        elif len(p - six) == 0:
            five = p
        else:
            two = p
    number = []

    mapy = {one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9, zero: 0}
    for e in f:
        number.append(mapy[frozenset(e)])

    return 1000 * number[0] + 100 * number[1] + 10 * number[2] + 1 * number[3]

res = sum([solveWiring(*e) for e in data])
print(res)
