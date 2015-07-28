# Name-Changer

This program makes it easy to batch rename files based on a desired pattern which already exists within the names of 
files or based on a simple numbering scheme. For example if you have 3 files named 

    badFileName (01) createdby obnoxiousTextThatPeoplePut.jpg
    badFileName (02) createdby obnoxiousTextThatPeoplePut.jpg
    badFileName (03) createdby obnoxiousTextThatPeoplePut.jpg

and you wanted to rename them to something like
    
    Image 01.jpg
    Image 02.jpg
    Image 03.jpg
    
this script allows you to isolate only certain parts of the current name and add it in your own name in addition to any 
conventions you would like to follow. This can also be modified to be used with counter variables if the current file 
names do not contain anything worth preserving. Some modification to the script may be needed as some of the paths are 
hardcoded.  

THE ORIGINAL FILES ARE OVERWRITTEN WITH THE NEW FILES. 

How to Use this program
THIS PROGRAM ONLY WORKS FOR MAC OR *nix BASED COMPUTERS 

1. Open this in PyCharm 
2. If you are using a mac, remove the .DS_Store file
3. Modify the paths in this program to suit your specific file paths
4. Type your desired name in the python file in the newName variable
5. Make sure all the path names are correct 
6. Read the third to last comment before running 

Limitations 

1. The new file name cannot include the / character
