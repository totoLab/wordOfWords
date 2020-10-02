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
        
        while feedback == False:
            testList = outputList
            wordToTry = chooseBetween(indexes)
            testList.append(wordToTry)
            feedback = checkValidity(testList)

        outputList = testList

    return outputList.join()


#find the first appearance of the letter, as capital, in the list
#set the search's start at that and end at the next letter index
#! not sure if these are the commands to get the indexes. TODO
def findIndexes(letter):
    startIndex = wordList.find(letter)
    #? find index of the next letter and subtract 1 to get last word of the letter before
    endIndex = wordList.find(letter+1) - 1 
    indexes = [startIndex, endIndex]

    return indexes

#pick a random word in the dictionary (csv) between previously set indexes
def chooseBetween(indexes):
    wordIndex = random.randrange(indexes[0], indexes[1])
    trial = 0 #pick the word at wordIndex in csv file
    return trial

def checkValidity(query):
    #search on Google and the other stuff, for now it's always ok
    return True

theWord = 'iammabell' #input("Insert a word to see the magic: ")
theWord = theWord.lower()
thePhrase = splitSearch(theWord)
