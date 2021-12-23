# =============== day and input ===============
day = "07"

import sys
if len(sys.argv) > 1:
    ex = "." + sys.argv[1]
else:
    ex = "." + "in"

filename = "data_" + day + ex


# =============== preparation ===============

with open(filename) as f:
  data = f.read().splitlines()

data = data[0].split(',')
data = [int(i) for i in data]

# print(data)
# print(len(data))

# =============== part 1 ===============
res = []
for x in range(100, 777):
    d = []
    for e in data:
        d.append(abs(e-x))
    res.append(sum(d))

print(min(res))


# =============== part 2 ===============
res = []
for x in range(100, 777):
    d = []
    for e in data:
        n = abs(e-x)
        d.append(n*(n+1)/2)
    res.append(sum(d))

print(min(res))
