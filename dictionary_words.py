import sys
from random import randrange

#Get sentence length from command line
sentenceLength = int(sys.argv[-1])

#Open file and read lines into array called words
file = open("dictionary")
words = [line.rstrip("\n") for line in file.readlines()]

#Initialize array to hold random words
sentenceArray = []

#Iterate through length of desired sentence
for i in xrange(sentenceLength):
    #Append a randomly indexed word from words to the array
    sentenceArray.append(words[randrange(0, len(words))])

#Print out each word in array without a new line
for word in sentenceArray:
    print word

#Close the file
file.close()
