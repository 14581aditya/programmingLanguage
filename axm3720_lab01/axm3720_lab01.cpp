//Aditya Mishra
//1001663720
//MacOS

#include<dirent.h>
#include<string.h>
#include<stdio.h>

#include<sys/stat.h>
#include <unistd.h>
#include<iostream>

using namespace std;

float CurrentdirectorySize(char altogether[]) // creating a function to calculate the size of the directory.
{
    char whole[250];
    float totalSize=0;
    struct dirent *dt_p;
    struct stat totalFile;
   
  
    DIR *directory = opendir(altogether);
    if(directory == NULL)
    {
        printf("Not a directory"); // Display "Cannot open Directory" if this is not a directory
        return 0;
    }
    while ((dt_p=readdir(directory))!=NULL) // take data until the directory is empty
    {
        if(strcmp(dt_p->d_name,".")==0 || strcmp(dt_p->d_name,"..")==0)
            continue;

            strcpy(whole,altogether);
            strcat(whole,"/");
            strcat(whole,dt_p->d_name);
            stat(whole,&totalFile);
            if(S_ISREG(totalFile.st_mode)) //checks if it is a file by using recursive
            {
                
                totalSize+=totalFile.st_size; // adds the total size of the file
            }
            else //other than file i.e a directory
            {
                totalSize+=CurrentdirectorySize(whole); // adds the total size of the file
            }
    }
    return totalSize; // Returns the total value size of this directory
}
int main()
{
    float size = CurrentdirectorySize((char *)".");
    printf("\nTotal size of the directory: %0.0f bytes \n",size); //displays the size of the whole directory
}
