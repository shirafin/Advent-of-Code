with open("AoC puz 4 input.txt", "r") as f:
    PPRawData = f.read().replace(' ', '\n')
PPData = PPRawData.split('\n')

def FindField(string, field):
    if string.find(field) == -1:
        return 'No'
    else:
        return 'Yes'


ValidPPs = 0
CIDPresent = None
NumOfValidFields = 0
for PPfield in PPData:
    if PPfield != '':
        ColonIndex = PPfield.find(':')
        if FindField(PPfield, 'cid') == 'Yes':
            CIDPresent = True
            NumOfValidFields +=1
        elif FindField(PPfield, 'byr') == 'Yes':
            BYR = int(PPfield[ColonIndex+1:])
            if 1920 <= BYR <= 2002:
                NumOfValidFields +=1
        elif FindField(PPfield, 'iyr') == 'Yes':
            IYR = int(PPfield[ColonIndex+1:])
            if 2010 <= IYR <= 2020:
                NumOfValidFields +=1
        elif FindField(PPfield, 'eyr') == 'Yes':
            EYR = int(PPfield[ColonIndex+1:])
            if 2020 <= EYR <= 2030:
                NumOfValidFields +=1
        elif FindField(PPfield, 'hcl') == 'Yes':
            HCL = PPfield[ColonIndex+1:]
            if len(HCL) == 7 and HCL[0] == '#' and HCL[1:].isalnum() == True:
                NumOfValidFields +=1
        elif FindField(PPfield, 'ecl') == 'Yes':
            ECL = PPfield[ColonIndex+1:]
            if ECL == 'amb' or ECL == 'blu' or ECL == 'brn' or ECL == 'gry' or ECL == 'grn' or ECL == 'hzl' or ECL == 'oth':
                NumOfValidFields +=1
        elif FindField(PPfield, 'pid') == 'Yes':
            PID = PPfield[ColonIndex+1:]
            if len(PID) == 9:
                NumOfValidFields +=1
        elif FindField(PPfield, 'hgt') == 'Yes':
            if PPfield.find('in') == -1:
                HGT = int(PPfield[ColonIndex+1:PPfield.find('cm')])
                if 150 <= HGT <= 193:
                    NumOfValidFields +=1
            else:
                HGT = int(PPfield[ColonIndex+1:PPfield.find('in')])
                if 59 <= HGT <= 76:
                    NumOfValidFields +=1
    else:
        if NumOfValidFields == 7 and CIDPresent != True  or NumOfValidFields == 8:
            ValidPPs += 1
        CIDPresent = None
        NumOfValidFields = 0 
if NumOfValidFields == 8 or NumOfValidFields == 7 and not CIDPresent == True:
    ValidPPs += 1

print (ValidPPs)

"""
def field_map(field):
    NumOfValidFields = 0
    switcher = {
        byr: def BYR():
        int(PPfield[ColonIndex+1:])
            if 1920 <= BYR <= 2002:
                NumOfValidFields +=1
        eyr: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    switcher.get(field)
"""     
    
