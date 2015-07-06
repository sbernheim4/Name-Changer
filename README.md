# Name-Changer

This program makes it easy to batch rename files based on a desired pattern which already exists within the names of files. For example if you have 3 files named 

    badNameFile (01) createdby userTest.jpg
    badNameFile (02) createdby userTest.jpg
    badNameFile (03) createdby userTest.jpg

    and you wanted to rename them such as 
    
    Image (01).jpg
    Image (02).jpg
    Image (03.jpg)
    
    this script allows you to isolate only certain parts of the current name and add in your own name and conventions to the file names. This can also be modified to be used with counter variables if the current name of the files does not contain anything worth preserving. Some modification to the script is needed as some of the paths are hardcoded.  