# =============== day and input ===============
day = "18"

import sys
if len(sys.argv) > 1:
    ex = "." + sys.argv[1]
else:
    ex = "." + "in"

filename = "data_" + day + ex

print("HALLO")

# =============== imports ===============
import re, copy
import numpy as np
import itertools as it
import functools as ft
import collections as col

# =============== preparation ===============
with open(filename) as f:
  data = f.read().splitlines()

def parse(s: str):
    c = 0
    if len(s) == 1:
        return int(s)
    s = s[1:-1]
    for i in range(len(s)):
        if s[i] == '[':
            c += 1
        elif s[i] == ']':
            c -= 1
        else:
            pass
        if c == 0:
            l = parse(s[:i+1])
            r = parse(s[i+2:])
            break
    return (l,r)

data = [parse(d) for d in data]


# =============== part 1 ===============

class sfn:
    def __init__(self, arg, depth: int = 0, parent = None):
        self.depth = depth
        self.parent = parent

        def kid(e):
            if isinstance(e, int):
                r = e
            elif isinstance(e, sfn):
                r = e
                r.parent = self
            else:
                r = sfn(e, self.depth + 1, self)
            return r

        self.left = kid(arg[0])
        self.right = kid(arg[1])


    def incrDepth(self):
        self.depth += 1
        if isinstance(self.left, sfn):  self.left.incrDepth()
        if isinstance(self.left, sfn)  and self.left.depth >= 4:    self.left.explode()

        if isinstance(self.right, sfn):  self.right.incrDepth()
        if isinstance(self.right, sfn) and self.right.depth >= 4:   self.right.explode()

    def explode(self):
        self.addToLeftNeighbor(self.left)
        self.addToRightNeighbor(self.right)
        self = 0


    def addToLeftNeighbor(self, value: int):
        if self.parent == None:
            return
        if self.parent.left is self:
            self.parent.addToLeftNeighbor(value)
        elif isinstance(self.parent.left, int):
            self.parent.addToLeftestKid(value)
            # self.parent.left += value
            # if self.left > 9:
            #     self.left = sfn((self.left // 2, (self.left + 1) // 2), self.depth + 1, self)
            #     if self.left.depth >= 4:
            #         self.left.explode()
        else:
            self.parent.left.addToRightestKid(value)

    def addToRightNeighbor(self, value: int):
        if self.parent == None:
            return
        if self.parent.right is self:
            self.parent.addToRightNeighbor(value)
        elif isinstance(self.parent.right, int):
            self.parent.addToRightestKid(value)
            # self.parent.left += value
            # if self.left > 9:
            #     self.left = sfn((self.left // 2, (self.left + 1) // 2), self.depth + 1, self)
            #     if self.left.depth >= 4:
            #         self.left.explode()
        else:
            self.parent.right.addToLeftestKid(value)


    def addToRightestKid(self, value: int):
        if isinstance(self.right, int):
            self.right += value
            if self.right > 9:
                self.right = sfn((self.right // 2, (self.right + 1) // 2), self.depth + 1, self)
                if self.right.depth >= 4:
                    self.right.explode()
        else:
            self.right.addToRightestKid(value)

    def addToLeftestKid(self, value: int):
        if isinstance(self.left, int):
            self.left += value
            if self.left > 9:
                self.left = sfn((self.left // 2, (self.left + 1) // 2), self.depth + 1, self)
                if self.left.depth >= 4:
                    self.left.explode()
        else:
            self.left.addToLeftestKid(value)

    def __str__(self):
        return f"SFN: {{ {self.left} | {self.right} }}"

    def __add__(self, other):
        r = sfn((copy.deepcopy(self), copy.deepcopy(other)), -1)
        r.incrDepth()
        return r

def addSFNs(a, b):
    print(f"{a} + {b}")
    return a + b

data = [sfn(d) for d in data]

d = data[0]
e = data[1]
for i in [d, e, d+e]:
    print(i.depth, i)

res = ft.reduce(addSFNs, data)

# =============== part 2 ===============
