# =============== day and input ===============
day = "02"

import sys
if len(sys.argv) > 1:
    ex = "." + sys.argv[1]
else:
    ex = "." + "in"

filename = "data_" + day + ex

# =============== preparation ===============
with open(filename) as f:
  data = f.read().splitlines()

data = [(e[0], int(e[1])) for e in [i.split() for i in data]]

# print(data)


# =============== part 1 ===============
x = y = 0

for d, a in data:
    if d == "forward":
        x += a
    else:
        y += a if d == "down" else -a

print(x,y,x*y)


# =============== part 2 ===============

aim = depth = pos = 0

for d, a in data:
    if d == "forward":
        pos += a
        depth += a * aim
    else:
        aim += a if d == "down" else -a

print(depth * pos)
