#Aditya Mishra
#1001663720
#April 07 2022
#MAC OS
#Python 3.9.7
#Extra Credit

#importing os
import os.path

#assigning file name
fileInside = "input_RPN_EC.txt"

#function to calcualte the mathenatical expression
def calculatorPython(mathematical):
    mathematical = mathematical.replace('\n', '')
    mathematical = mathematical.replace('\r', '')
    mathematical = mathematical.replace(' ', '')

    mathematicalOperators = {
        '+': lambda x, y: x + y,#addition
        '-': lambda x, y: x - y,#substration
        '*': lambda x, y: x * y,#multiplication
        '/': lambda x, y: x // y, # assumes integer division
        '%': lambda x, y: x % y, # extraCredit, modulo operation
        '^': lambda x, y: x * y # extraCredit, power operaion
    }    

    num = []
    for char in mathematical:
        if char.isdigit():
            num.append(int(char))
        else:
            if len(num) < 2:
                raise ValueError(f'Invalid RPN  "{mathematical}".')
            last = num.pop()
            if char not in mathematicalOperators:
                raise ValueError(f'Unsupported operation "{char}" in RPN  "{mathematical}".')
            num[-1] = mathematicalOperators[char](num[-1], last)

    if len(num) > 1:
        raise ValueError(f'Invalid RPN  "{mathematical}".')
    return num[0]

#functiin to convert to run
def convertToRpn(mathematical):
    mathematical = mathematical.replace('\n', '')
    mathematical = mathematical.replace('\r', '')
    mathematical = mathematical.replace(' ', '')

    token_priority = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3, 
        '%': 4,

    }

    mathematicalOperators = []
    answerList = []

    for token in mathematical:
        if token.isdigit():
            answerList.append(token)
        elif token == '(':
            mathematicalOperators.append(token)
        elif token == ')':
            cur_op = mathematicalOperators.pop()
            while cur_op != '(':
                answerList.append(cur_op)
                cur_op = mathematicalOperators.pop()
        else:
            while mathematicalOperators and mathematicalOperators[-1] != '(' and token_priority[token] <= token_priority[mathematicalOperators[-1]]:
                  answerList.append(mathematicalOperators.pop())
            mathematicalOperators.append(token)

    answerList += mathematicalOperators[::-1]
    return ' '.join(answerList)

#checks if file is inside
ifFileInside = os.path.exists(fileInside)

if(ifFileInside):
    #opening the file  
    insideFile = open(fileInside, "r")
    #reading between lines
    readLine = insideFile.readlines() 
    #closing the file
    insideFile.close()

    for line in readLine:
        #remove spaces and strip the line.
        line = line.strip()
        #using our calcultorPython function to calculate the output
        rpn = convertToRpn(line)
        
        
        #print the answer.
        print(rpn)

        solved = calculatorPython(rpn)
        print(line + " = " + str(solved)+"\n")
else:
    #if the file doesnt exist, write an error message
    print("The input file doesn't exist")

