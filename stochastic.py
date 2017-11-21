import sys
import random
import word_frequency_analysis


def randomWordSelector(histogram):
    words = histogram.keys()
    randIndex = random.randrange(0, len(words)-1)
    return words[randIndex]


# TO-DO: Fix prob. calculation
def probabilityHistogram(histogram):
    weightedHistogram = {}
    for word, count in histogram.items():
        weightedHistogram[word] = float(count)/len(histogram)
    return weightedHistogram


def weightedWordListGenerator(histogram):
    wordList = [[key] * count for key, count in histogram.items()]
    # wordList = sum(wordList, [])
    newWordList = []
    for words in wordList:
        newWordList.extend(words)
    return newWordList


def weightedRandomWordSelector(weightedWordList):
    randomWord = weightedWordList[random.randrange(0, len(weightedWordList)-1)]
    return randomWord


def randomSentenceGenerator(sentenceLength, histogram):
    sentenceWords = []
    randomWordList = weightedWordListGenerator(histogram)
    for i in range(sentenceLength):
        sentenceWords.append(weightedRandomWordSelector(randomWordList))
    return (" ").join(sentenceWords)


if __name__ == "__main__":
    file = open(sys.argv[1], "r")
    sentenceLength = int(sys.argv[2])
    fileString = file.read()
    fileString = word_frequency_analysis.simplified_text_array(fileString)
    hist = word_frequency_analysis.histogram(fileString)
    randSentence = randomSentenceGenerator(sentenceLength, hist)
    print(randSentence)
