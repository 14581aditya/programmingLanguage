#Aditya Mishra
#1001663720
#04/26/2022
#MACOS
import os.path

#importing os.path to check is the file exists
fileInside = 'input_EC.txt'

#Assigning file name
ifFileInside = os.path.exists(fileInside) 

#checking the file
eachline = None

#assigning none value or null value
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

for x, l in enumerate(eachline):
    xyz = 0
    for x in range(len(l)):

        #checking for '//' and if then break
        if x + 1 < len(l) and l[x:x + 2] == '//':
            break
        
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
        
        #checking for '{' if yes then add in number and use nextline
        if l[x] == '{':
            
            if len(l[xyz:x].strip()) != 0:
                new.append((number * 4 * ' ') + l[xyz:x].strip())
            new.append((number * 4 * ' ') + '{')
            xyz = x + 1
            number += 1
            stk.append('{')

        #checking for '/*' if yes then subtract from number
        if l[x] == '}':
            
            if not stk or stk[-1] != '{':
                raise Exception('found "}" that does not correspond to any "{" on l ' + str(x + 1))
            
            if len(l[xyz:x].strip()) != 0:
                new.append((number * 4 * ' ') + l[xyz:x].strip())
            number -= 1
            new.append(' ' * 4 * number + '}')
            xyz = x + 1
            stk.pop()
    if len(l[xyz:].strip()) != 0:
        new.append(' ' * 4 * number + l[xyz:].strip())

#Using if to raise exception
if stk:
    raise Exception('expected ‘}’ but found EOF')

#printing the java code 
print('\n'.join(new))
