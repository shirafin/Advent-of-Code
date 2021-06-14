with open("AoC puz 1 input.txt", "r") as f:
    expenses = [int(line.strip()) for line in f] #create list with all numbers

iExpense = 0
for expense in expenses:
    for i in range (iExpense, len(expenses)):
        if expense + expenses[i] == 2020:
                print (expense * expenses[i])
                break
    iExpense+=1
