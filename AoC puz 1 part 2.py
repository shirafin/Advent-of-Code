a_file = open("AoC puz 1 numbers.txt", "r")
expenses = []
for line in a_file:
    stripped_line = int(line.strip())
    expenses.append(stripped_line)

iExpense = 0
for expense in expenses:
    for i in range (iExpense, len(expenses)):
        for j in range (iExpense+1, len(expenses)):
            if expense + expenses[i] + expenses[j] == 2020:
                print (expense * expenses[i] * expenses[j])
                break
    iExpense+=1
