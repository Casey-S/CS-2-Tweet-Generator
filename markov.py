import sys
import random
import word_frequency_analysis


# sample string: "One fish two fish red fish blue fish"
def markov(corpus_string):
    word_array = word_frequency_analysis.simplified_text_array(corpus_string)
    markov_obj = {{}}
    for index in len(word_array) - 1:
        word = word_array[index]
        if word in markov_obj.keys():
            word_hist = markov_obj[word]
            next_word = word_array[i+1]
            if next_word in word_hist.keys():
