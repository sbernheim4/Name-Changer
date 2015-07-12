# This program renames files based on a desired output and information in the current name that you want to keep
# preserved

# CHECK THE THIRD TO LAST COMMENT BEFORE RUNNING

__author__ = 'samuelbernheim'

from os import listdir, rename, system, path
import sys

# checks to see if there is a folder on the desktop named FilesToRename
if path.isdir("/Users/samuelbernheim/Desktop/FilesToRename/"):
    print "folder exists"
else:
    print "No such folder found"
    print "Making folder"
    system("cd /Users/samuelbernheim/Desktop/; mkdir FilesToRename")
    print "Folder was created."
    print "Please transfer the files whose names you wish to change into /Users/samuelbernheim/Desktop/FilesToRename/" \
          " and then rerun this script."
    sys.exit(1)


# path of the directory which houses the files whose names will be changed
sourcePath = "/Users/samuelbernheim/Desktop/FilesToRename/"

# path of this project folder where files will be copied to for the name change
projPath = "/Users/samuelbernheim/Python/NameChanger/"

sourceDir = listdir(sourcePath)  # directory of the files' current location
projDir = listdir(projPath)  # directory of this project


# copies all the files from the source directory into the project directory for later manipulation [
system("cp /Users/samuelbernheim/Desktop/FilesToRename/* /Users/samuelbernheim/Python/NameChanger/")

fileNumber = 1

# renames the files
for theFile in sourceDir:

    # Enter here the new name of the files you wish. Use of the variable fileNumber can be used or a current part of the
    # files' names
    newName = "Batman - A Death in the Family (" + str(fileNumber) + ").jpg"
    print "New Name: " + newName

    rename(theFile, newName)

    fileNumber += 1

# removes the files with the old names from the source folder
system("rm /Users/samuelbernheim/Desktop/FilesToRename/*")

# MATCH THE END OF THE FIRST PATH OF THE NEXT SYSTEM CALL AND THE SECOND SYSTEM CALL.
# copies all the files which begin with "Image" in the project folder, into the source folder with the right name
system("cp /Users/samuelbernheim/Python/NameChanger/Batman* /Users/samuelbernheim/Desktop/FilesToRename/")

# removes the files from the project folder
system("rm Batman*")
