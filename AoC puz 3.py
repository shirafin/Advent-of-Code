with open("AoC puz 3 input.txt", "r") as f:
    TSet = [line.strip() for line in f]
THit = 0 #trees hit
TIndex = 0 #index of tree
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
print (THit)
