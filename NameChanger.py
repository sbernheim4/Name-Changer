__author__ = 'samuelbernheim'

from os import listdir, rename, system

# path of the directory which houses the files whose names will be changed
sourcePath = "/Users/samuelbernheim/Desktop/FilesToRename/"
sourceDir = listdir(sourcePath)

# copies the files from the source directory into the project directory
for theFile in sourceDir:
    system("cp /Users/samuelbernheim/Desktop/FilesToRename/* /Users/samuelbernheim/Python/NameChanger/")

# renames the files 
for theFile in sourceDir:

    newName = "Image " + theFile[25:28] + ".jpg"
    print newName
    rename(theFile, newName)