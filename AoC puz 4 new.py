with open("AoC puz 4 input.txt", "r") as f:
    #PPData = f.read().replace(' ', '\n') separates each field into a new line
    PPData = [line.strip() for line in f]
\
def FindCID(string):
    if string.find('cid') == -1:
        return 'No'
    else:
        return 'Yes'

ValidPPs = 0
CIDPresent = None
NumOfFields = 0
for PPfield in PPData:
    if PPfield != '':
        NumOfFields += PPfield.count(":")
        if FindCID(PPfield) == 'Yes':
            CIDPresent = True
    else:
        if NumOfFields == 7 and CIDPresent != True  or NumOfFields == 8:
            ValidPPs += 1
        CIDPresent = None
        NumOfFields = 0 
if NumOfFields == 8 or NumOfFields == 7 and not CIDPresent == True:
    ValidPPs += 1

print (ValidPPs)

        
        
    
