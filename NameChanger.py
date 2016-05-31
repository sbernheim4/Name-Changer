# This program renames files based on a desired output and information in the current name that you want to keep
# preserved

# CHECK THE THIRD TO LAST COMMENT BEFORE RUNNING

__author__ = 'samuelbernheim'

from os import listdir, rename, system, path
import sys

# checks to see if there is a folder on the desktop named FilesToRename
if path.isdir("/Users/samuelbernheim/Desktop/FilesToRename"):
    print "Source folder exists"
else:
    print "Source folder does not exist"
    print "Making folder"
    system("cd /Users/samuelbernheim/Desktop/; mkdir FilesToRename;")
    print "Folder was created."
    print "Please transfer the files whose names you wish to change into /Users/samuelbernheim/Desktop/FilesToRename/" \
          " and then rerun this script."
    sys.exit(1)


# goes through the name and replaces all "." with " "
def removePeriodsFromName(name):
    currentPosition = 0
    duplicate = ""
    for letter in name:
        currentPosition = currentPosition + 1
        if letter == ".":
            duplicate = duplicate + " "
        else:
            duplicate = duplicate + letter
    return duplicate


def removeUnderscoresFromName(name):
    currentPosition = 0
    duplicate = ""
    for letter in name:
        currentPosition = currentPosition + 1
        if letter == "_":
            duplicate = duplicate + " "
        else:
            duplicate = duplicate + letter
    return duplicate

# Use this function if the current names of your files contain specific attributes like individual names
# Test this before hand in a separate python file to make sure the output is correct
def getTheFullTitle(rawNameOfEpisode, nameOfShow):

    # THIS SECTION IS FOR GETTING THE EPISODE INFO LIKE S02E05
    # TODO: Modify this variable to make sure the numbers are correct for your specific batch of files.
    episodeInfo = rawNameOfEpisode[16:22]
    # episodeInfoLength = len(episodeInfo)
    # episodeInfo = "S01E" + episodeInfo[0:episodeInfoLength]


    # THIS SECTION GETS THE PART OF THE TITLE FROM AFTER THE EPISODE INFO (S01E01) TO THE END OF THE NAME
    # TODO: This line must be modified for every new set that will use this function
    nameSize = len(rawNameOfEpisode)
    usableName = rawNameOfEpisode[16:nameSize]
    print "Usable Name: " + usableName


    # THIS SECTION GETS THE INDEX OF WHERE THE TITLE OF THE EPISODE ENDS
    # counter variable
    currentPosition = 0
    # TODO: Modify this code for every new batch run.
    # parses through the usableName to find the first toccurence of 1 which would be in 1080p and gets that position
    for letter in usableName:
        currentPosition = currentPosition + 1
        if letter == "1":
            break

    # variable for the title of the episode
    titleOfEpisode = usableName[0:currentPosition-2]
    titleOfEpisode = removeUnderscoresFromName(titleOfEpisode)
    titleOfEpisode = removePeriodsFromName(titleOfEpisode)
    print "Episode Title: " + titleOfEpisode

    # this way either variable can be used and the same result will be output
    fullName = nameOfShow + " - " + episodeInfo + " - " + titleOfEpisode + ".mkv"

    return fullName


# path of the directory which houses the files whose names will be changed
sourcePath = "/Users/samuelbernheim/Desktop/FilesToRename/"

# path of this project folder where files will be copied to for the name change
projPath = "/Users/samuelbernheim/ Projects/Name-Changer"

sourceDir = listdir(sourcePath)  # directory of the files' current location
projDir = listdir(projPath)  # directory of this project

# copies all the files from the source directory into the project directory for later manipulation [
system("cp /Users/samuelbernheim/Desktop/FilesToRename/* /Users/samuelbernheim/Github\ Projects//Desktop/Name-Changer/")

fileNumber = 1

nameOfShow = raw_input("Enter the name of the show\n")


# renames the files
for eachFile in sourceDir:

    # if the file name does not contain any information you wish to preserve use the following if block. Otherwise use
    # the getTheFullTitle function. Just be sure to run that using an example name before running this program on your
    # batch of files.

    if eachFile != ".DS_Store":
        # # if using fileNumber, use this if statement to have the same number of digits ex: going from 09 to 10
        # if fileNumber < 10:
        #     newName = "Attack on Titan - S01E0" + str(fileNumber) + ".mp4"
        # else:
        #     newName = "Attack on Titan - S01E" + str(fileNumber) + ".mp4"
        #
        # print "New Name: " + newName

        newName = getTheFullTitle(eachFile, nameOfShow)

        print newName
        print
        print

        # comment this line out before running to see if the names are correct.
        rename(eachFile, newName)

        fileNumber += 1

# removes the files with the old names from the source folder
system("rm /Users/samuelbernheim/Desktop/FilesToRename/*")

# TODO: MATCH THE END OF THE FIRST PATH OF THE NEXT SYSTEM CALL AND THE SECOND SYSTEM CALL TO THE FIRST WORD OF FIRST
# TODO: FEW LETTERS OF WHAT EVERY FILE WILL BEGIN WITH.

# copies all the files which begin with "Cow" in the project folder, into the source folder with the right name
system("cp /Users/samuelbernheim/Github\ Projects//Name-Changer/Game* /Users/samuelbernheim/Desktop/FilesToRename/")

# removes the files from the project folder
system("rm Game*")

print "Program completed"
