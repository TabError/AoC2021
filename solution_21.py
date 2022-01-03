# =============== day and input ===============
day = "21"

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

p1 = re.match("^Player 1 starting position: (\d+)$", data[0]).group(1)
p2 = re.match("^Player 2 starting position: (\d+)$", data[1]).group(1)

p1, p2 = int(p1), int(p2)
# print(p1, p2)

# =============== part 1 ===============

s1, s2 = 0, 0
die = 0
while True:
    p1 = ((p1 + 3 * die + 6) - 1) % 10 + 1
    s1 += p1 + 1
    die += 3
    if s1 >= 1000:
        res = s2 * die
        # print(s2, die)
        break

    p2 = ((p2 + 3 * die + 6) - 1) % 10 + 1
    s2 += p2 + 1
    die += 3
    if s2 >= 1000:
        res = s1 * die
        # print(s1, die)
        break

print(res)

# =============== part 2 ===============

def valuesOf(ls):
    return map(lambda x: x[2], ls)

def fill1(table):
    i = 0
    while sum( valuesOf(table[i]) ) > 0:
        i += 1
        table.append([])
        for pos, val, amount in table[i-1]:
            if val >= 21:
                continue
            for posIncr, amountMulti in [(3,1), (4,3), (5,6), (6,7), (7,6), (8,3), (9,1)]:
                newPos = ((pos + posIncr) - 1) % 10 + 1
                newPoints = val + newPos
                table[i].append((newPos, newPoints, amount * amountMulti))

def fill2(table):
    pos = []
    neg = []
    for i in range(len(table)):
        pos.append( sum( map( lambda x: x[2], filter(lambda x: x[1] >= 21, table[i]) ) ) )
        neg.append( sum( map( lambda x: x[2], filter(lambda x: x[1] < 21,  table[i]) ) ) )
    return pos, neg



p1 = [[(7,0,1)]]
p2 = [[(3,0,1)]]

fill1(p1)
fill1(p2)

pos1, neg1 = fill2(p1)
pos2, neg2 = fill2(p2)

# print(pos1, pos2)
# print(neg1, neg2)

win1 = win2 = 0

for i in range(1, len(pos1)):
    win1 += pos1[i] * neg2[i-1]
    win2 += pos2[i] * neg1[i]

print(max(win1, win2))
