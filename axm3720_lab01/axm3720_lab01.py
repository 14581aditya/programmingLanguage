# Aditya Mishra 
# 1001663720
# python3
# MACOS
import os #fetching the content of this directory.

def currentDirectorySize(totalFile): #creating a function to calculate the size of ghe directory
    totalSize = os.path.getsize(totalFile)
    for whole in os.listdir(totalFile): # using for loop in directory to find the total number of files
        altogether = os.path.join(totalFile, whole)
        if os.path.isdir(altogether): # using recursive function to check if it is directory
            totalSize += directorySize(altogether) # adding the directory size
        elif os.path.isfile(altogether): #using recursive function to check if it is file
            totalSize += os.path.getsize(altogether) # adding the file size
    return totalSize #will return the total size of the directory

print ("\n" + "Total size of the directory:"+ " " + str(currentDirectorySize("."))+ " " + "bytes"+"\n") # displaying the size of whole directory
