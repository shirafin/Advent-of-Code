with open("AoC puz 3 input.txt", "r") as f:
    TSet = [line.strip() for line in f]
THit = 0 #trees hit
TIndex = 0 #index of toboggan
LineLen = len(TSet[0])

for treeline in TSet:
    if TIndex<LineLen:
        if treeline[TIndex] == "#":
            THit += 1
    else:
        TIndex -= LineLen
        if treeline[TIndex] == "#":
            THit += 1
    TIndex += 3

Slope31 = THit
print (Slope31)
THit = 0
TIndex = 0

for treeline in TSet:
    if TIndex<LineLen:
        if treeline[TIndex] == "#":
            THit += 1
    else:
        TIndex -= LineLen
        if treeline[TIndex] == "#":
            THit += 1
    TIndex += 1

Slope11 = THit
print(Slope11)
THit = 0
TIndex = 0

for treeline in TSet:
    if TIndex<LineLen:
        if treeline[TIndex] == "#":
            THit += 1
    else:
        TIndex -= LineLen
        if treeline[TIndex] == "#":
            THit += 1
    TIndex += 5

Slope51 = THit
print (Slope51)
THit = 0
TIndex = 0

for treeline in TSet:
    if TIndex<LineLen:
        if treeline[TIndex] == "#":
            THit += 1
    else:
        TIndex -= LineLen
        if treeline[TIndex] == "#":
            THit += 1
    TIndex += 7

Slope71 = THit
print (Slope71)
THit = 0
TIndex = 0

for i in range(0, len(TSet), 2):
        if TIndex<LineLen:
            if TSet[i][TIndex] == "#":
                THit += 1
        else:
            TIndex -= LineLen
            if TSet[i][TIndex] == "#":
                THit += 1
        TIndex += 1

Slope12 = THit
print (Slope12)

print (Slope31*Slope11*Slope51*Slope71*Slope12)
