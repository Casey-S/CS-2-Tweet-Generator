import sys
from random import randrange
from time import time

# Get sentence length from command line
sentenceLength = int(sys.argv[-1])

# Take a sample of epoch time
time_before = time()

# Open file and read lines into array called words,
# Stripping \n character in every line read
file = open("words.txt")
words = [line.rstrip("\n") for line in file.readlines()]

# Initialize array to hold random words
sentenceArray = []

# Iterate through length of desired sentence
# Append a randomly indexed word from words to the array
for i in xrange(sentenceLength):
    sentenceArray.append(words[randrange(0, len(words))])

# Print out each word in array without a new line
for word in sentenceArray:
    print word
# Take a sample of epoch time after printing the result
time_after = time()

# Print the runtime by subtracting time_before from time_after
print(time_after - time_before)

# Close the file
file.close()
