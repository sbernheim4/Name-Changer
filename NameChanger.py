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

# goes through the name and replaces all "_" with " "
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

def showExample(name):
    # the spacing allows for only 56 characters in a sample name to fit naturally on the terminal screen
    # when it is at full size. Otherwise make the screen bigger.
    i = 0
    for letter in name:
        if i < 10:
            # using sys.stdout.write to control the exact spacing and to have everything print on one line
            sys.stdout.write(letter + " ")
        else:
            # print one extra space after letter since num will now take up two spaces instead of just one
            sys.stdout.write(letter + "  ")
        i = i+1
    print
    for num in range(56):
            sys.stdout.write(str(num) + " ")

    print

# Use this function if the current names of your files contain specific attributes like individual names
# Test this before hand in a separate python file to make sure the output is correct
def getTheFullTitle(rawNameOfEpisode, nameOfShow, episodeInfoIndexOne, episodeInfoIndexTwo, usableNameIndex):

    nameSize = len(rawNameOfEpisode)

    # THIS SECTION IS FOR GETTING THE EPISODE INFO LIKE S02E05
    episodeInfo = rawNameOfEpisode[episodeInfoIndexOne:episodeInfoIndexTwo]
    print "Episode Info: " + episodeInfo


    # THIS SECTION GETS THE EPISODE TITLE FROM, THIS USUALLY COMES AFTER THE EPISODE INFO
    # TODO: This line must be modified for every new set that will use this function
    usableName = rawNameOfEpisode[usableNameIndex:nameSize]
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
    fullName = nameOfShow + " - " + episodeInfo + " - " + titleOfEpisode +  ".mkv"

    return fullName

sourcePath = "/Users/samuelbernheim/Desktop/FilesToRename" # path of the directory which houses the files whose names will be changed
projPath = "/Users/samuelbernheim/Github-Projects/Name-Changer" # path of this project folder where files will be copied to for the name change

sourceDir = listdir(sourcePath)  # directory of the files' current location
projDir = listdir(projPath)  # directory of this project

# copies all the files from the source directory into the project directory for later manipulation
system("cp /Users/samuelbernheim/Desktop/FilesToRename/* /Users/samuelbernheim/Github-Projects/Name-Changer/")

# Established outside the below for loop so they act more as constants that cannot be reset
# inside the loop
fileNumber = 1
nameOfShow = raw_input("Enter the name of the show\n")
episodeInfoIndexOne = 0
episodeInfoIndexTwo = 0
usableNameIndex = 0
firstFile = True

# renames the files
for eachFile in sourceDir:

    # if the file name does not contain any information you wish to preserve use the following if block. Otherwise use
    # the getTheFullTitle function. Just be sure to run that using an example name before running this program on your
    # batch of files. Do not use both the if block and the getTheFullTitle function.
    if eachFile != ".DS_Store":
        # # if using fileNumber, use this if statement to have the same number of digits ex: going from 09 to 10
        # if fileNumber < 10:
        #     newName = "Attack on Titan - S01E0" + str(fileNumber) + ".mp4"
        # else:
        #     newName = "Attack on Titan - S01E" + str(fileNumber) + ".mp4"
        #
        # print "New Name: " + newName

        if firstFile:
            showExample(eachFile)
            episodeInfoIndexOne = int(raw_input("Enter the index of where the episode info begins\n"))
            episodeInfoIndexTwo = int(raw_input("Enter the index of where the episode info ends\n"))
            usableNameIndex = int(raw_input("Enter the index where the title begins\n"))
            firstFile = False



        newName = getTheFullTitle(eachFile, nameOfShow, episodeInfoIndexOne, episodeInfoIndexTwo, usableNameIndex)

        print newName
        print

        # comment this line out before running to see if the names are correct.
        rename(eachFile, newName)

        # fileNumber is used in the if statement above.
        fileNumber += 1

system("rm /Users/samuelbernheim/Desktop/FilesToRename/*") # removes the files with the old names from the source folder

# TODO: MATCH THE END OF THE FIRST PATH OF THE NEXT SYSTEM CALL AND THE SECOND SYSTEM CALL TO THE FIRST WORD OF FIRST
# TODO: FEW LETTERS OF WHAT EVERY FILE WILL BEGIN WITH.

# copies all the files which begin with "Cow" in the project folder, into the source folder with the right name
system("cp /Users/samuelbernheim/Github-Projects//Name-Changer/Game* /Users/samuelbernheim/Desktop/FilesToRename/")

# removes the files from the project folder
system("rm Game*")
# TODO: Experiment with using the %s placeholder so this does not have to be changed in the .py file
# print "My name is %s and weight is %d kg!" % ('Zara', 21)

print "Program completed"
