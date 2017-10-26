import random
import sys

# Complete task with random's shuffle function
word_list = sys.argv[1:]

random.shuffle(word_list)

print(" ".join(word_list))

'''
'''

# Complete task with custom shuffle function
words = raw_input().split()


def shuffle(words):
    # Generate empty array to hold shuffled words
    shuffledWords_arr = []

    # Condition to ensure loop will run as long as new array is not at capacity
    # Each time word is added, word is popped from words. So we are done when
    # words is empty
    while len(words) > 0:
        # Randomly choose index from 0 to length of sentence, pop the word at
        # that index from words,
        # and append it to new shuffled array
        shuffledWords_arr.append(words.pop(random.randrange(0, len(words))))
    # Return the shuffled array
    return shuffledWords_arr


# Function output formatting - add a space behind each word
test = " ".join(shuffle(words))

print(test)
