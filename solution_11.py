# =============== day and input ===============
day = "11"

import sys
if len(sys.argv) > 1:
    ex = "." + sys.argv[1]
else:
    ex = "." + "in"

filename = "data_" + day + ex


# =============== imports ===============
import numpy as np
import itertools as it
import collections as col


# =============== preparation ===============
with open(filename) as f:
  data = f.read().splitlines()

data = [list(e) for e in data]
np_data = np.array(data).astype(int)

# print(np_data)


# =============== part 1 ===============

def neighbours(i,j):
    return set([(i+x, j+y) for x,y in it.product([-1,0,1], [-1, 0, 1]) if 0 <= i+x < np_data.shape[0] and 0 <= j+y < np_data.shape[1]]) - {(i,j)}


res1 = 0
res2 = 0

synchron = False
hundred = False
counter = 0
while not synchron or not hundred:
    counter += 1
    flashed = set()
    np_data += 1
    q = col.deque(zip(*np.where(np_data > 9)))
    while len(q) > 0:
        e = q.popleft()
        flashed.add(e)
        for n in neighbours(*e):
            np_data[n] += 1
            if n not in flashed and n not in q and np_data[n] > 9:
                q.append(n)

    for e in flashed:
        np_data[e] = 0

    if not hundred:
        res1 += len(flashed)
    if counter == 100:
        hundred = True

    if len(flashed) == len(np_data.ravel()):
        synchron = True#
        res2 = counter

print(res1)
print(res2)

# =============== part 2 ===============
