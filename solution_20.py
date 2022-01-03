# =============== day and input ===============
day = "20"

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

algo = data[0]
data = data[2:]
data = [[0 if e == '.' else 1 for e in l] for l in data]
im = np_data = np.array(data).astype('int8')

# print(algo)
# print(len(algo))

# print(data)
# print(np_data)


# =============== part 1 ===============

def show(im):
    for r in im:
        s = ""
        for c in r:
            s += '#' if c == 1 else '.'
        print(s)

def enhancePi(im, x, y, surroundedByZeros):
    s = 0
    p = 1
    for i,j in it.product([1, 0, -1], repeat = 2):
        if x+i not in range(im.shape[0]) or y+j not in range(im.shape[1]):
            s += (0 if surroundedByZeros else 1) * p
        else:
            s += im[x+i, y+j] * p
        p *= 2
    return 1 if algo[s] == '#' else 0

def enhanceIm(im, surroundedByZeros):
    def extendImage(o, surroundedByZeros):
        fill = np.zeros if surroundedByZeros else np.ones
        x = np.hstack([fill(o.shape[0]).reshape((-1,1)), o, fill(o.shape[0]).reshape((-1,1))])
        y = np.vstack([fill(x.shape[1]).reshape((1,-1)), x, fill(x.shape[1]).reshape((1,-1))]).astype('int8')
        return y

    im = extendImage(im, surroundedByZeros)

    newIm = np.zeros(im.shape, dtype='int8')
    l1, l2 = newIm.shape

    for i,j in it.product( range(l1), range(l2) ):
        newIm[i,j] = enhancePi(im, i, j, surroundedByZeros)
    # print(newIm)
    return newIm


im = enhanceIm(im, True)
im = enhanceIm(im, False)
print(im.sum())


# =============== part 2 ===============

for i in range(24):
    im = enhanceIm(im, True)
    im = enhanceIm(im, False)
print(im.sum())
