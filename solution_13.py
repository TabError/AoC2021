# =============== day and input ===============
day = "13"

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
  data, inst = f.read().split("\n\n")

data = [tuple(l.split(',')) for l in data.splitlines()]
data = [(int(x), int(y)) for x, y in data]
# print(data)

folds = []
for i in inst.splitlines():
    m = re.match("fold along (x|y)=(\d+)", i)
    folds.append((m.group(1), int(m.group(2))))
# print(folds)

# =============== part 1 ===============
dots = set(data)

for i, f in enumerate(folds):
    ffunc = lambda x : x[0 if f[0] == 'x' else 1] < f[1]
    ndots = set(filter(ffunc, dots))
    dots -= ndots
    mfunc = lambda x: (2*f[1] - x[0], x[1]) if f[0] == 'x' else (x[0], 2*f[1] - x[1])
    ndots |= set(map(mfunc, dots))
    dots = ndots
    if i == 0:
        print(len(dots))


# =============== part 2 ===============

# print(dots)

xhi = max([x for x,y in dots])
yhi = max([y for x,y in dots])

for j in range(yhi + 1):
    r = ""
    for i in range(xhi + 1):
        r += '#' if (i,j) in dots else ' '
    print(r)
