with open("AoC puz 6 input.txt", "r") as f:
    answers = [line.strip() for line in f]

instances = set() #set of all answers that appear
Total = 0
for answer in answers:
    if answer != '':
        for char in answer:
            instances.add(char)
    else: #empty line means end of a set of answers
        Total += len(instances)
        instances.clear() #reset the count

Total += len(instances) #adding the last set of answers to the total
print (Total)
            
