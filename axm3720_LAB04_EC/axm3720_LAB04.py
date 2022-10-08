#Aditya Mishra
#1001663720
#04/26/2022
#MACOS

#importing os.path to check is the file exists
import os.path

#Assigning file name
fileInside = 'input.txt'

#checking the file
ifFileInside = os.path.exists(fileInside) 

#assigning none value or null value
eachline = None

if(ifFileInside):
    #opening file
    insideFile = open(fileInside, "r")
    #reading between lines
    eachline = insideFile.readlines()
    #closing the file 
    insideFile.close()

stk = [] #varray variable
number = 1 # variable to count the brackets
new = [] #array variable
a = 1 #variable
#using for loop to read between the lines
for l in eachline:
    for x in range(len(l)):
        #number=0
        #checking for '//' and if then break

        if x + 1 < len(l) and l[x:x + 2] == '//':
            #number=number-1
            break
        #new.append(str(number-1) + ' ' * (3 - len(str(number))) + l)
        #checking for '"' if yes then contine

        if stk and stk[-1] == '"':
            if l[x] == '"' and (x == 0 or l[x - 1] != '\\'):
                stk.pop()
            continue

        #checking for '"' if yes then contine
        if l[x] == '"':
            stk.append('"')
            continue

        #checking for '/*' if yes then contine
        if stk and stk[-1] == '/*':
            if x + 1 < len(l) and l[x:x + 2] == '*/':
                stk.pop()
                x += 1
            continue

        #checking for '/*' if yes then contine
        if x + 1 < len(l) and l[x:x + 2] == '/*':
            stk.append('/*')
            x += 1
            continue

        #checking for '{' if yes then add in number
        if l[x] == '{':
            number += 1
            stk.append('{')

        #checking for '}' if yes then subtract in number


        if l[x] == '}':
            number = number+a
            if l[x] == '}':
                if not stk or stk[-1] != '{':
                   raise Exception('something went wrong')
                number = number - 1
                a = 0
                stk.pop()
    #appending into new
    new.append(str(number-1) + ' ' * (3 - len(str(number))) + l)
        

    
    

    
#Using if to raisw exception
if stk:
    raise Exception('expected ‘}’ but found EOF')
#printing the java code 
print(''.join(new))
