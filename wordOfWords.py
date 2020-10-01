#Python script to make a phrase out of the letters of a word.
import re
import random

feedback = False
testList = []
outputList = []

def splitSearch(word):
    #first letter of each words joins in a string
    #if resulting string matches, prints the word
    for i in range(len(word)):
        firstLetter = word[i]
        indexes = findIndexes(firstLetter)
        
        testList = outputList
        while feedback == False:
            wordToTry = chooseBetween(indexes)
            testList.append(wordToTry)
            feedback = checkValidity(testList)

        outputList = testList

    return outputList.join()


#find the first appearance of the letter, as capital, in the list
#set the search's start at that and end at the next letter index
def findIndexes(letter):
    startIndex = wordList.find(letter)
    endIndex = wordList.find(letter+1) - 1
    indexes = [startIndex, endIndex]

    return indexes

#pick a random word in the dictionary (csv) between previously set indexes
def chooseBetween(indexes):
    wordIndex = random(indexes[0], indexes[1])
    trial = 0 #pick the word at wordIndex in csv file
    return trial

def checkValidity():
    #search on Google and the other stuff, for now it's always ok
    return True

theWord = 'iammabell' #input("Insert a word to see the magic: ")
#word = lowerCase(word)
thePhrase = splitSearch(theWord)
