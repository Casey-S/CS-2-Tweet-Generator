import sys
import string

words_input = sys.argv[1]

def histogram(source_text):
    words = open("%s" % source_text)
    words_string = words.read()
    # words = [line.rstrip("\n") for line in file.readlines()]
    words_clean = words_string.translate(string.maketrans("", ""), string.punctuation)
    return words_clean
print(histogram(words_input))
