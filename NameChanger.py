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


def getTheFullTitle(rawNameOfEpisode):

    series = "The Flash"
    episodeInfo = rawNameOfEpisode[15:21]

    print series
    print episodeInfo

    nameSize = len(rawNameOfEpisode)

    # TODO: this line must be modified for every new set that will use this function
    # gets the part of the title from after the episode info (S01E01) to the end of the name
    usableName = rawNameOfEpisode[22:nameSize]

    # prints the usable name
    print "Usable Name: " + usableName

    # counter variable
    currentPosition = 0

    # parses through the usableName to find the first occurance of 1 which would be in 1080p and gets that position
    for letter in usableName:
        currentPosition = currentPosition + 1
        if letter == "1":
            break


    # variable for the title of the episode
    titleOfEpisode = usableName[0:currentPosition-2]
    print "Episode Title: " + titleOfEpisode

    # because strings are immutable a second variable must be used to get the final correct name
    duplicate = ""

    currentPosition = 0

    # goes through the name and replaces all "." with " "
    for letter in titleOfEpisode:
        currentPosition = currentPosition + 1
        if letter == ".":
            duplicate = duplicate + " "
        else:
            duplicate = duplicate + letter

    # this way either variable can be used and the same result will be output
    titleOfEpisode = duplicate
    print "Episode Title Formatted: " + titleOfEpisode

    fullName = series + " - " + episodeInfo + " - " + titleOfEpisode + ".mkv"
    return fullName





# path of the directory which houses the files whose names will be changed
sourcePath = "/Users/samuelbernheim/Desktop/FilesToRename/"

# path of this project folder where files will be copied to for the name change
projPath = "/Users/samuelbernheim/Python/Name-Changer/"

sourceDir = listdir(sourcePath)  # directory of the files' current location
projDir = listdir(projPath)  # directory of this project

# copies all the files from the source directory into the project directory for later manipulation [
system("cp /Users/samuelbernheim/Desktop/FilesToRename/* /Users/samuelbernheim/Python/Name-Changer/")

fileNumber = 1

# renames the files
for eachFile in sourceDir:

    if eachFile != ".DS_Store":


        # if using fileNumber, use this if statement to have the same number of digits ex: going from 09 to 10
        # if fileNumber < 10:
        #     newName = "Attack on Titan - S01E0" + str(fileNumber) + ".mp4"
        # else:
        #     newName = "Attack on Titan - S01E" + str(fileNumber) + ".mp4"
        #
        # print "New Name: " + newName

        newName = getTheFullTitle(eachFile)

        # comment this line out before running to see if the names are correct.
        rename(eachFile, newName)

        fileNumber += 1


# removes the files with the old names from the source folder
system("rm /Users/samuelbernheim/Desktop/FilesToRename/*")

# MATCH THE END OF THE FIRST PATH OF THE NEXT SYSTEM CALL AND THE SECOND SYSTEM CALL.
# copies all the files which begin with "Image" in the project folder, into the source folder with the right name
system("cp /Users/samuelbernheim/Python/Name-Changer/The* /Users/samuelbernheim/Desktop/FilesToRename/")

# removes the files from the project folder
system("rm The*")
