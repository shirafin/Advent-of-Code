a_file = open("AoC puz 1 input.txt", "r")
#create list with all numbers
expenses = []
for line in a_file:
    stripped_line = int(line.strip()) #strip formatting
    expenses.append(stripped_line)

iExpense = 0
for expense in expenses:
    for i in range (iExpense, len(expenses)):
        if expense + expenses[i] == 2020:
                print (expense * expenses[i])
                break
    iExpense+=1
