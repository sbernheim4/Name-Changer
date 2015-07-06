__author__ = 'samuelbernheim'

from os import listdir, rename, system

# path of the directory which houses the files whose names will be changed
sourcePath = "/Users/samuelbernheim/Desktop/FilesToRename/"
projPath = "/Users/samuelbernheim/Python/NameChanger/"

sourceDir = listdir(sourcePath)
projDir = listdir(projPath)

# copies all the files from the source directory into the project
system("cp /Users/samuelbernheim/Desktop/FilesToRename/* /Users/samuelbernheim/Python/NameChanger/")

# renames the files
for theFile in sourceDir:

    newName = "Image " + theFile[21:24] + ".jpg"
    print "New Name: " + newName

    rename(theFile, newName)

# removes the files with the old names from the source folder
system("cd /Users/samuelbernheim/Desktop/FilesToRename/; rm *")

# copies all the files which begin with "Image" in the project folder, into the source folder with the right name
system("cp /Users/samuelbernheim/Python/NameChanger/Image* /Users/samuelbernheim/Desktop/FilesToRename/")

# removes the files from the project folder
system("rm Image*")

