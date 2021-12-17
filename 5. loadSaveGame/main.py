from time import sleep
from os import close
import csv


def getChoiceGame():
    validate = False
    allowed = [1,2,3]
    while (validate == False):
        # print name of game and choices
        print(f'****** Text Adventure Game v1.0 ******')
        print(f'*                                    *')
        print(f'*           1 - New Game             *')
        print(f'*           2 - Load Game            *')
        print(f'*           3 - Quit                 *')
        print(f'*                                    *')
        print(f'**************************************')
        userInput = input("> ")
        print("")

        # Error check for input value
        if (userInput.isdigit() == False):
            print("*** Invalid Input : Please enter integer number ...")
        elif int(userInput) not in allowed:
            print("*** Invalid Input : Must be in range from 1 to 3...")
        else:
            validate = True
            return userInput

def loadGame(loadNumber,savedLineNumber):

    # get story data list
    storyData = getStoryData()

    while storyData[savedLineNumber][1] != "":
        validate = False
        allowed = [1,2,3]
        while (validate == False):

            if loadNumber == 1:
                # load saved.txt file
                infile = open("saved.txt","r")
                # # construct a CSV Reader object
                # csvReader = csv.reader(infile)

                # savedData = []

                # for row in csvReader:
                #     savedData.append(row)
                savedLineNumber = int(infile.readline())                
                infile.close()

                # # print decision point and choices
                # makeStoryLine(0, savedData)

                # print decision point and choices
                makeStoryLine(savedLineNumber, storyData)
                
                loadNumber += 1
            else:
                # print decision point and choices
                makeStoryLine(savedLineNumber, storyData)                

            # get user input
            userInput = input("> ")
            print("")

            # Error check for input value
            if (userInput.isdigit() == False):
                print("*** Invalid Input : Please enter integer number ...")
            elif int(userInput) not in allowed:
                print("*** Invalid Input : Must be in range from 1 to 3...")
            else:
                validate = True

        # save game
        if int(userInput) == 3:
            loadNumber += 1
            saveGame(savedLineNumber)
            print(">>> Game Saved")
            print("")

        else:
            savedLineNumber = int(storyData[savedLineNumber][int(userInput)+2])-1
        

    print(storyData[savedLineNumber][0])
    print("")

def saveGame(savedLineNumber):
    # write out lines to saved.txt
    outfile = open("saved.txt","w")
    # for i in range(0,len(storyData[savedLineNumber])):
    #     outfile.write(storyData[savedLineNumber][i]+",")
    outfile.write(str(savedLineNumber))
    outfile.close()

def getStoryData():
    # open the story.csv file for reading
    infile = open("story.csv","r")

    # construct a CSV Reader object
    csvReader = csv.reader(infile)
    
    storyData = []

    for row in csvReader:
        storyData.append(row)

    infile.close()
    return storyData

def makeStoryLine(lineNumber, storyData):
    print(storyData[lineNumber][0])
    print("What do you want to do?")
    print(f'1 - {storyData[lineNumber][1]}')
    print(f'2 - {storyData[lineNumber][2]}')
    print(f'3 - Save Game')

def getUserDecision(loadNumber):

    # get story data list
    storyData = getStoryData()

    lineNumber = 0
    savedLineNumber = 0
    while storyData[lineNumber][1] != "":
        validate = False
        allowed = [1,2,3]
        while (validate == False):
            # print decision point and choices
            makeStoryLine(lineNumber, storyData)

            # get user input
            userInput = input("> ")
            print("")

            # Error check for input value
            if (userInput.isdigit() == False):
                print("*** Invalid Input : Please enter integer number ...")
            elif int(userInput) not in allowed:
                print("*** Invalid Input : Must be in range from 1 to 3...")
            else:
                validate = True

        # save game
        if int(userInput) == 3:
            # make variable for save line number
            savedLineNumber = lineNumber
            saveGame(savedLineNumber)
            loadNumber += 1
            print(">>> Game Saved")
            print("")

        else:
            lineNumber = int(storyData[lineNumber][int(userInput)+2])-1

    print(storyData[lineNumber][0])
    print("")

    return savedLineNumber,loadNumber

def main():
    # load game number initiate
    loadNumber = 0

    while True:
        # get user input
        choiceGame = getChoiceGame()

        # execute game choice
        if int(choiceGame) == 3:
            return
        elif int(choiceGame) == 2:

            # check there is saved.txt
            if loadNumber == 0:
                print("*** Error : There is no game to load ...")
            else:
                loadGame(loadNumber,savedLineNumber)
                sleep(2)

        else:
            savedLineNumber,loadNumber = getUserDecision(loadNumber)
            sleep(2)

main()