# =============== day and input ===============
day = "10"

import sys
if len(sys.argv) > 1:
    ex = "." + sys.argv[1]
else:
    ex = "." + "in"

filename = "data_" + day + ex


# =============== preparation ===============
with open(filename) as f:
  data = f.read().splitlines()

# print(data)

# =============== part 1 ===============

corr = {'(':')', '[':']', '{':'}', '<':'>'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
completionValues = {'(':1, '[':2, '{':3, '<':4}

res1 = 0
res2l = []

for l in data:
    s = []
    for c in l:
        if c in "([{<":
            s.append(c)
        else:
            expec = corr[s.pop()]
            if(c != expec):
                res1 += points[c]
                break
    else:
        r = 0
        for c in reversed(s):
            r *= 5
            r += completionValues[c]
        res2l.append(r)


print(res1)
print(sorted(res2l)[len(res2l)//2])

# =============== part 2 ===============
