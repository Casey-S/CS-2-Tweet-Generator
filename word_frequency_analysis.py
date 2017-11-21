import sys
import string


def simplified_text_array(raw_file_string):
    # # Removes 's and then any punctuation from the string
    # simplified_text = file_string.replace("'s", "").translate(None, string.punctuation).lower()
    # # Returns simplified text as an array of words
    # return simplified_text.split()
    words_clean = raw_file_string.translate(string.maketrans("", ""), string.punctuation)
    words_clean = words_clean.replace('\n', '')
    words_clean = words_clean.replace('\r', '')
    words_clean = words_clean.split(" ")
    return words_clean


# Takes a string of file text and generates a histogram of word counts
def histogram(file_string):
    # Initializes dictionary for histogram
    word_count_dict = {}
    # Loops through array of words and adds each to the dictionary if not there
    # Or increments the count in the dictionary by 1 if it is already there
    for word in file_string:
        if word in word_count_dict.keys():
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    # Return the final dictionary for histogram
    return word_count_dict


# Function to return number of unique words given a histogram of word counts
def unique_words(histogram):
    # Returns the length of the histogram's keys array
    unique_word_count = len(histogram.keys())
    return unique_word_count


# Return the frequency of a given word in a histogram of word counts
def frequency(word):
    frequency_list = histogram(word)
    # Tries to lookup the key word in the histogram dictionary
    try:
        # Returns the value associated with given key if it finds it
        return frequency_list[word]
    except:
        # Return failure message if the try fails - word is not in histogram
        return "Entry not found"


if __name__ == "__main__":
    words = open(sys.argv[1])
    # word_specific = sys.argv[2]
    words_string = words.read()
    words_string = simplified_text_array(words_string)

    print(histogram(words_string))
