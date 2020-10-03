#Python script to make a phrase out of the letters of a word.
import random

wordList = ['apple', 'amla', 'banana', 'csv', 'dt', 'exodia', 'fear', 'game', 'hotel', 'incredible', 'i', 'joker', 'key', 'low', 'my', 'no', 'oxigen', 'pill', 'quora', 'race', 'speed', 'table', 'uptown', 'viagra', 'why', 'xorg', 'yes', 'zen']
def splitSearch(word):
    testList = []
    outputList = []
    #search current letter as the first letter of an entry in the wordlist
    #if the word is valid, it's appended in the output list, otherwise it's deleted from the testlist
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
    
    return indexes

#pick a random word in the dictionary (csv) between previously set indexes
def chooseBetween(indexes):
    wordIndex = random.randint(indexes[0], indexes[1])
    trial = wordList[wordIndex] #TODO pick the word at wordIndex in csv file - csvFile[wordIndex]
    return trial

#searches on Google and the other stuff, for now it's 50% times ok
def checkValidity(query): #TODO make it actually search on google
    bul = random.random()
    if bul < 0.5:
        return True
    else:
        return False

theWord = 'michiamogianni' #input("Insert a word to see the magic: ")
theWord = theWord.lower()
thePhrase = splitSearch(theWord)
print(thePhrase)