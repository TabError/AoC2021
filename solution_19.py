# =============== day and input ===============
day = "19"

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
  data = f.read().split("\n\n")


class Scanner:
    def __init__(self, ls):
        self.id = re.match("--- scanner (\d+) ---", ls[0]).group(1)
        self.bs = []
        for b in ls[1:]:
            m = re.match("(-?\d+),(-?\d+),(-?\d+)", b)
            self.bs.append((int(m.group(1)), int(m.group(2)), int(m.group(3))))

    def __str__(self):
        return f"Scanner No. {self.id} with length: {len(self.bs)}"

    def scannerIntersect(self, other):
        pass

data = [Scanner(sc.splitlines()) for sc in data]

print(data)
print(data[0])



# =============== part 1 ===============



# =============== part 2 ===============
