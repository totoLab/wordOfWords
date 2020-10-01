#Python script to make a phrase out of the letters of a word.
import re
word = 'iammabell'

#integrations with web crawling and regexes; future feature
test1 = 'io amo mangiare male a burgerking e le lotterie'
test2 = 'bambi ancora non amo nemmeno ariel'
tests = [test1, test2]
regex = '\b[a-zA-Z]'

#first letter of each words joins in a string
#if resulting string matches, prints the word
for i in range(len(word)):
    firstLetter = word[i]
    if re.match(regex, word) is not None:
        print(word[i])



print()