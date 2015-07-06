# Name-Changer

This program makes it easy to batch rename files based on a desired pattern which already exists within the names of files. For example if you have 3 files named 

    badNameFile (01) createdby userTest.jpg
    badNameFile (02) createdby userTest.jpg
    badNameFile (03) createdby userTest.jpg

and you wanted to rename them such as 
    
    Image (01).jpg
    Image (02).jpg
    Image (03).jpg
    
this script allows you to isolate only certain parts of the current name and add in your own name and conventions to the file names. This can also be modified to be used with counter variables if the current file names do not contain anything worth preserving. Some modification to the script is needed as some of the paths are hardcoded.  

THE ORIGINAL FILES ARE OVERWRITTEN WITH THE NEW FILES. 

How to Use this program
THIS PROGRAM ONLY WORKS FOR MAC OR *nix BASED COMPUTERS 

1. Using your terminal or powershell, navigate to the folder where you have the files whose name you wish to change.
2. If you are using a mac, remove the .DS_Store file
3. Modify the paths in this program to suit your specific file paths