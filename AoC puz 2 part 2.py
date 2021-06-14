with open("AoC puz 2 input.txt", "r") as f:
    passwords = [line.strip() for line in f]

"""
#need to get key letter at beginning of line (character before colon?)
#need to turn numbers at beginning and end of range into variables a and b
#need to ensure each key letter and range numbers stay tied to each password.
    #make into dictionary with key and values?
    #make number pairs into list with corresponding index to key/value pairs?
    #make 3 lists - number range, key letter, and passwords?
    #make number range a dictionary?
"""

#find key letter in string
def findKeyLetter(string):
    colonIndex = string.find(":")
    KeyLetIndex = colonIndex-1
    return KeyLetIndex

"""
#find dash in string
dashIndex = string.find("-")

#lower number in range
def findNumRange(string):
    LowNum = int(string[:dashIndex])
    HighNum = int(string[dashIndex+1:keyLetterIndex-1])
"""

correctPasswords = 0
for password in passwords:
    KeyLetterIndex = findKeyLetter(password)
    KeyLetter = password[KeyLetterIndex]
    dashIndex = password.find("-")
    LowNum = int(password[:dashIndex]) #first number in range
    HighNum = int(password[dashIndex+1:KeyLetterIndex-1]) #second number in range
    passletters = password[KeyLetterIndex+3:]
    if passletters[LowNum-1] == KeyLetter and passletters[HighNum-1] == KeyLetter:
        pass
    elif passletters[LowNum-1] == KeyLetter or passletters[HighNum-1] == KeyLetter:
        correctPasswords +=1
    else:
        pass
print (correctPasswords)

        
