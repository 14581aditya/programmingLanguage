#Aditya Mishra
#1001663720
#April 07 2022
#MAC OS
#Python 3.9.7

#importing os
import os.path

#assigning file name
fileInside = "input_RPN.txt"

#function to calcualte the mathenatical expression
def calculatorPython(mathematical):
    mathematical = mathematical.replace('\n', '')
    mathematical = mathematical.replace('\r', '')
    mathematical = mathematical.replace(' ', '')

    mathematicalOperators = {
        '+': lambda x, y: x + y,#addition
        '-': lambda x, y: x - y,#substration
        '*': lambda x, y: x * y,#multiplecation
        '/': lambda x, y: x // y,# integer division
        #for extra credit see another file named axm3720_EC.py
        #'%': lambda x, y: x % y, # extra, modulo operation
        #'^': lambda x, y: x * y # extra, power operaion
    }    

    num = []
    for char in mathematical:
        if char.isdigit():
            num.append(int(char))
        else:
            if len(num) < 2:
                raise ValueError(f'Invalid RPN "{mathematical}".')
            last = num.pop()
            if char not in mathematicalOperators:
                raise ValueError(f'Unsupported operation "{char}" in RPN "{mathematical}".')
            num[-1] = mathematicalOperators[char](num[-1], last)

    if len(num) > 1:
        raise ValueError(f'Invalid RPN "{mathematical}".')
    return num[0]

#checks if file is inside
ifFileInside = os.path.exists(fileInside) 

if(ifFileInside):
    #opening file
    insideFile = open(fileInside, "r")
    #reading between lines
    readLine = insideFile.readlines()
    #closing the file 
    insideFile.close()

    for line in readLine:
        # remove spaces and strip the line.
        line = line.strip()
        #using our calcultorPython function to calculate the output
        solved = calculatorPython(line)
        
        #print the answer.
        print(line + " = " + str(solved))
else:
    #if the file name is diff or not in the directory print
    print("The input file doesn't exist")


