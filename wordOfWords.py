#Python script to make a phrase out of the letters of a word.
import re
import random

wordList = ['apple', 'amla', 'banana', 'csv', 'dt', 'exodia', 'fear', 'game', 'hotel', 'incredible', 'i', 'joker', 'key', 'low', 'my', 'no', 'oxigen', 'pill', 'quora', 'race', 'speed', 'table', 'uptown', 'viagra', 'why', 'xorg', 'yes', 'zen']
def splitSearch(word):
    testList = []
    outputList = []
    #first letter of each words joins in a string
    #if resulting string matches, prints the word
    #TODO dictionary.sort()
    for i in range(len(word)):
        firstLetter = word[i]
        indexes = findIndexes(firstLetter)
        
        feedback = False
        while feedback == False:
            testList = outputList.copy()
            wordToTry = chooseBetween(indexes)
            testList.append(wordToTry)
            feedback = checkValidity(testList)

        outputList = testList.copy()

    return " ".join(outputList)


#makes a list of all words that start with a letter
#then it takes the first and last elements indexes
def findIndexes(letter):
    listParsed = [idx for idx in wordList if idx.lower().startswith(letter)] 
    startIndex = wordList.index(listParsed[0])
    #? find index of the next letter and subtract 1 to get last word of the letter before
    endIndex = wordList.index(listParsed[len(listParsed)-1])
    indexes = [startIndex, endIndex]
    #print(startIndex, endIndex) #debug print
    return indexes

#pick a random word in the dictionary (csv) between previously set indexes
def chooseBetween(indexes):
    wordIndex = random.randint(indexes[0], indexes[1])
    trial = wordList[wordIndex] #TODO pick the word at wordIndex in csv file - csvFile[wordIndex]
    return trial

def checkValidity(query):
    #search on Google and the other stuff, for now it's always ok
    bul = random.random()
    if bul < 0.5:
        return True
    else:
        return False

theWord = 'michiamogianni' #input("Insert a word to see the magic: ")
theWord = theWord.lower()
thePhrase = splitSearch(theWord)
print(thePhrase)