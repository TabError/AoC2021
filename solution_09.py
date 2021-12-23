# =============== day and input ===============
day = "09"

import sys
if len(sys.argv) > 1:
    ex = "." + sys.argv[1]
else:
    ex = "." + "in"

filename = "data_" + day + ex


# =============== preparation ===============
import numpy as np

with open(filename) as f:
  data = f.read().splitlines()

data = [list(e) for e in data]

np_data = np.array(data).astype(int)
# print(np_data)

# =============== part 1 ===============

# print(np_data.shape)
def neighbours(i,j):
    return [(np_data[i+x,j+y], i+x, j+y) for x,y in [(0, 1), (0, -1), (1, 0), (-1, 0)] if 0 <= i+x < np_data.shape[0] and 0 <= j+y < np_data.shape[1]]

l = [(np_data[i,j], i, j) for i in range(np_data.shape[0]) for j in range(np_data.shape[1]) if np_data[i,j] < min(neighbours(i,j), key = (lambda k: k[0]))[0] ]

res = sum([e[0] + 1 for e in l])

print(res)

# =============== part 2 ===============

from collections import deque

basins = []
for lowpoint in l:
    q = deque([lowpoint])
    basin = set()
    while len(q) > 0:
        e = q.popleft()
        if e[0] < 9:
            q.extend(set(neighbours(e[1], e[2])) - basin )
            basin.add(e)
    basins.append(basin)

res = sorted([len(b) for b in basins], reverse = True)[0:3]
print(res[0] * res[1] * res[2])
