# =============== day and input ===============
day = "16"

import sys
if len(sys.argv) > 1:
    ex = "." + sys.argv[1]
else:
    ex = "." + "in"

filename = "data_" + day + ex

# =============== preparation ===============
with open(filename) as f:
  data = f.read().splitlines()

hexdata = data[0]
bindata = ""
for c in hexdata:
    bindata += f"{int(c, 16):04b}"

# print(hexdata, bindata)

# =============== part 1 and 2 ===============

LiteralID = 4

DATA = {}
versionSUM = 0

def parsePacket(s: str, data: dict):
    index = 0
    data["version"] = int(s[index: index + 3], 2); index += 3
    global versionSUM
    versionSUM += data["version"]
    data["id"] = int(s[index: index + 3], 2); index += 3
    if data["id"] == LiteralID:
        last = False
        data["rawBinaries"] = ""
        while(not last):
            last = s[index: index + 1] == "0" ; index += 1
            data["rawBinaries"] += s[index: index + 4]; index += 4
        data["value"] = int(data["rawBinaries"], 2)

    else:
        data["values"] = []
        data["lengthType"] = int(s[index: index + 1], 2); index += 1
        if data["lengthType"] == 0:
            data["totalLength"] = int(s[index: index + 15], 2); index += 15
            parseuntil = index + data["totalLength"]
            i = 0
            while(index < parseuntil):
                data[i] = dict()
                index += parsePacket(s[index:], data[i])
                data["values"].append(data[i]["value"])
                i += 1
            # print(f"totalLength reached: {parseuntil=}, {index=}, {data['totalLength']=}")
        else:
            data["numSubpackets"] = int(s[index: index + 11], 2); index += 11
            for i in range(data["numSubpackets"]):
                data[i] = dict()
                index += parsePacket(s[index:], data[i])
                data["values"].append(data[i]["value"])

        if data["id"] == 0:
            data["value"] = sum(data["values"])
        elif data["id"] == 1:
            from functools import reduce
            data["value"] = reduce(lambda x,y: x*y, data["values"])
        elif data["id"] == 2:
            data["value"] = min(data["values"])
        elif data["id"] == 3:
            data["value"] = max(data["values"])
        elif data["id"] == 5:
            data["value"] = 1 if data["values"][0] > data["values"][1] else 0
        elif data["id"] == 6:
            data["value"] = 1 if data["values"][0] < data["values"][1] else 0
        elif data["id"] == 7:
            data["value"] = 1 if data["values"][0] == data["values"][1] else 0
        else:
            print("ERROR")

    return index


parsePacket(bindata, DATA)
# print(f"{DATA=}")
print(f"{versionSUM=}")
print(f"{DATA['value']=}")

# =============== part 2 ===============
