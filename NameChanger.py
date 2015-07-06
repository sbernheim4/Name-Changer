__author__ = 'samuelbernheim'

from os import listdir, rename, system

# path of the directory which houses the files whose names will be changed
sourcePath = "/Users/samuelbernheim/Desktop/FilesToRename/"
projPath = "/Users/samuelbernheim/Python/NameChanger/"

sourceDir = listdir(sourcePath)
projDir = listdir(projPath)

# copies the files from the source directory into the project directory
for theFile in sourceDir:
    system("cp /Users/samuelbernheim/Desktop/FilesToRename/* /Users/samuelbernheim/Python/NameChanger/")

# renames the files
for theFile in sourceDir:

    newName = "Image " + theFile[25:28] + ".jpg"
    print newName
    rename(theFile, newName)

# removes the files with the old names from the source folder
system("cd /Users/samuelbernheim/Desktop/FilesToRename/; rm *")

# copies all the files which begin with "Image" in the project folder, back to the source folder with the right name
system("cp /Users/samuelbernheim/Python/NameChanger/Image* /Users/samuelbernheim/Desktop/FilesToRename/")

