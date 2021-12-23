# =============== day and input ===============
day = "15"

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

# =============== part 1 ===============

pathRisk = np.ones(np_data.shape) * (-1)
pathRisk[0,0] = 0

pathStack = [(0,0,np_data[0,0])]
risk = np_data

while len(pathStack) > 0:
    cur = cur_i, cur_j, cur_risk = min(pathStack, key = lambda k: k[2])
    for i,j in [ (cur_i + 1, cur_j), (cur_i - 1, cur_j), (cur_i, cur_j + 1), (cur_i, cur_j - 1) ]:
        if i in range(pathRisk.shape[0]) and j in range(pathRisk.shape[1]) and pathRisk[i,j] == -1:
            pathRisk[i,j] = pathRisk[cur_i,cur_j] + risk[i,j]
            pathStack.append((i,j,pathRisk[i,j]))
    pathStack.remove(cur)

print(pathRisk)


# =============== part 2 ===============

newdata = np_data

newdata = newdata - 1
newdata = np.hstack((newdata, (newdata + 1) % 9, (newdata + 2) % 9, (newdata + 3) % 9, (newdata + 4) % 9))
newdata = np.vstack((newdata, (newdata + 1) % 9, (newdata + 2) % 9, (newdata + 3) % 9, (newdata + 4) % 9))
newdata = newdata + 1

# print(newdata)


# pathRisk is where the results will be saved
pathRisk = np.ones(newdata.shape) * (-1)
pathRisk[0,0] = 0

# here are the fields saved which have to be processed
pathStack = [(0,0,np_data[0,0])]
risk = newdata

while len(pathStack) > 0:
    cur = cur_i, cur_j, cur_risk = min(pathStack, key = lambda k: k[2])
    for i,j in [ (cur_i + 1, cur_j), (cur_i - 1, cur_j), (cur_i, cur_j + 1), (cur_i, cur_j - 1) ]:
        if i in range(pathRisk.shape[0]) and j in range(pathRisk.shape[1]) and pathRisk[i,j] == -1:
            pathRisk[i,j] = pathRisk[cur_i,cur_j] + risk[i,j]
            pathStack.append((i,j,pathRisk[i,j]))
    pathStack.remove(cur)

print(pathRisk)
