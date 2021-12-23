# =============== day and input ===============
day = "17"

import sys
if len(sys.argv) > 1:
    ex = "." + sys.argv[1]
else:
    ex = "." + "in"

filename = "data_" + day + ex


# =============== preparation ===============
with open(filename) as f:
  data = f.read()

import re

d = re.match(r"^target area: x=(-?\d*)\.\.(-?\d*), y=(-?\d*)\.\.(-?\d*)$", data)
minX = int(d.group(1))
maxX = int(d.group(2))
minY = int(d.group(3))
maxY = int(d.group(4))


# =============== part 1 ===============
print(abs(minY) * (abs(minY) - 1) / 2)


# =============== part 2 ===============
import itertools as it

res = 0
for velX, velY in it.product(range(min(minX, 0) , max(0, maxX + 1)), range(-abs(minY) , abs(minY) + 1)):
        # calc steps
        x = y = 0
        reached = False
        while not reached:
            x += velX
            y += velY
            if y < minY:
                reached = True
            if minX <= x <= maxX and minY <= y <= maxY:
                res += 1
                reached = True
            velX += -1 if velX > 0 else 1 if velX < 0 else 0
            velY -= 1

print(res)
