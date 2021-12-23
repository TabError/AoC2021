# =============== day and input ===============
day = "22"

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

# print(data)

def parseRange(s):
    m = re.match(r"(-?\d+)\.\.(-?\d+)?", s)
    return int(m.group(1)), int(m.group(2))

newdata = []
for l in data:
    m = re.match(r"(on|off) x=(.*),y=(.*),z=(.*)", l)
    t = (m.group(1), parseRange(m.group(2)), parseRange(m.group(3)), parseRange(m.group(4)))
    newdata.append(t)


# =============== part 1 ===============

r = radius = 50
one = np.zeros((2*r + 1, 2*r + 1, 2*r + 1)).astype('bool')


for pow, x, y, z in newdata:
    one[x[0]+r:x[1]+r+1 , y[0]+r:y[1]+r+1 , z[0]+r:z[1]+r+1] = True if pow == "on" else False

# print(one)
print(one.sum())


# =============== part 2 ===============

def emulateSurvivor(cuboid: tuple, it: int, until: int):
    if it >= until:
        return countCuboid(cuboid)
    splits = splitCuboid(cuboid, newdata[it][1:])
    return sum([emulateSurvivor(c, it+1, until = until) for c in splits])


def splitCuboid(cuboid: tuple, splitter: tuple):
    # if no intersection: return cuboid
    if  (splitter[2][0] > cuboid[2][1] or splitter[2][1] < cuboid[2][0]) \
     or (splitter[1][0] > cuboid[1][1] or splitter[1][1] < cuboid[1][0]) \
     or (splitter[0][0] > cuboid[0][1] or splitter[0][1] < cuboid[0][0]):       # if splitter outside of cuboid in x-, y- or z-dimension
        div = [cuboid]

    # else cut into pieces
    else:
        below = (cuboid[0], cuboid[1], (cuboid[2][0], splitter[2][0] - 1))
        above = (cuboid[0], cuboid[1], (splitter[2][1] + 1, cuboid[2][1]))

        left  = (cuboid[0], (cuboid[1][0], splitter[1][0] - 1), (max(splitter[2][0], cuboid[2][0]), min(splitter[2][1], cuboid[2][1])) )
        right = (cuboid[0], (splitter[1][1] + 1, cuboid[1][1]), (max(splitter[2][0], cuboid[2][0]), min(splitter[2][1], cuboid[2][1])) )

        front = ((cuboid[0][0], splitter[0][0] - 1), (max(splitter[1][0], cuboid[1][0]), min(splitter[1][1], cuboid[1][1])), (max(splitter[2][0], cuboid[2][0]), min(splitter[2][1], cuboid[2][1])) )
        back  = ((splitter[0][1] + 1, cuboid[0][1]), (max(splitter[1][0], cuboid[1][0]), min(splitter[1][1], cuboid[1][1])), (max(splitter[2][0], cuboid[2][0]), min(splitter[2][1], cuboid[2][1])) )

        div = [c for c in [below, above, left, right, front, back] if checkCuboid(c)]

    # print(f"cuboid: {str(cuboid):35}, splitter: {str(splitter):35}, split: {div}")
    return div

def checkCuboid(cuboid: tuple):
    return cuboid[0][0] <= cuboid[0][1] and cuboid[1][0] <= cuboid[1][1] and cuboid[2][0] <= cuboid[2][1]

def countCuboid(cuboid: tuple):
    return (cuboid[0][1] - cuboid[0][0] + 1) * (cuboid[1][1] - cuboid[1][0] + 1) * (cuboid[2][1] - cuboid[2][0] + 1)


until = 20; counter = 0
for i in reversed(range(until)):
    # print("iteration:", i)
    if newdata[i][0] == 'on':
        counter += emulateSurvivor(newdata[i][1:], i+1, until)
print(counter)

until = len(newdata); counter = 0
for i in reversed(range(until)):
    # print("iteration:", i)
    if newdata[i][0] == 'on':
        counter += emulateSurvivor(newdata[i][1:], i+1, until = until)
print(counter)
