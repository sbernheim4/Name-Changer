__author__ = 'samuelbernheim'

from os import listdir, rename

path = "/Users/samuelbernheim/Desktop/FilesToRename/"
sourceDir = listdir(path)

for theFile in sourceDir:

    newName = "Image " + theFile[25:28] + ".jpg"
    print newName
    rename(theFile, newName)
