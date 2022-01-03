# =============== day and input ===============
day = "25"

import sys
if len(sys.argv) > 1:
    ex = "." + sys.argv[1]
else:
    ex = "." + "in"

filename = "data_" + day + ex


# =============== imports ===============
import re, copy
import numpy as np
import itertools as it
import functools as ft
import collections as col


# =============== preparation ===============
with open(filename) as f:
  data = f.read().splitlines()

l1 = len(data)
l2 = len(data[0])

P = 0; # incrP = (0,0)
E = 1; incrE = (0,1)
S = 2; incrS = (1,0)

data = [[ P if c == '.' else E if c == '>' else S for c in l ] for l in data]
np_data = np.array(data)

print(np_data)

# =============== part 1 ===============
el = set()
sl = set()

def init():
    for i,j in it.product(range(l1), range(l2)):
        if np_data[i,j] == E:
            el.add((i,j))
        if np_data[i,j] == S:
            sl.add((i,j))

def add(s, o):
    return ((s[0] + o[0]) % l1, (s[1] + o[1]) % l2)

def step():
    def forwardHerde(x):
        cur, ls, incr = (E, el, incrE) if x == 0 else (S, sl, incrS)

        forw = set()
        for e in ls:
            i,j = add(e, incr)
            if np_data[i,j] == P:
                forw.add(e)

        for e in forw:
            ls.remove(e)
            np_data[e[0], e[1]] = P
            new = add(e, incr)
            ls.add(new)
            np_data[new[0], new[1]] = cur
        return len(forw)

    return forwardHerde(0) + forwardHerde(1)

init()

c = 0
while step() != 0:
    c += 1

print(c + 1)



# =============== part 2 ===============

pass
