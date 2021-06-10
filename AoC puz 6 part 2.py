with open("AoC puz 6 input.txt", "r") as f:
    answers = [line.strip() for line in f]

Total = 0
Lines = 0
Instances = {}
for answer in answers:
    if answer != '':
        for char in answer:
            if char in Instances:
                Instances[char] += 1
            else:
                Instances[char] = 1
        Lines += 1
    else:
        for value in Instances.values():
            if value == Lines:
                Total += 1
        Instances.clear()
        Lines = 0

for value in Instances.values():
            if value == Lines:
                Total += 1
print (Total)            
