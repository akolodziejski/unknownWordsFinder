__author__ = 'Areo'

import re
import os
import operator


def getSplittedWords(input_file_name):
    file = open(input_file_name, encoding="utf-8").read()
    return file.split()


def getKnownWords(folder_path):

    files = os.listdir(folder_path)

    uniqueWords = []

    for file_name in files:

        _splitted_words = getSplittedWords(folder_path + '/' + file_name)

        for word in _splitted_words:
            if word not in uniqueWords:
                uniqueWords.append(word.lower())

    return uniqueWords

def isKnownWord(word, knownWordsList):
    if word in knownWordsList:
        return True

    #check pass time ( simple -ed -d postfix)
    wordInSimplePass = word + 'd'

    if wordInSimplePass in knownWordsList:
        return True

    #check single 3 form ( added -s)
    wordIn3FormOrPlural = word + 's'

    if wordIn3FormOrPlural in knownWordsList:
        return True

    # cut of the last s
    if word.endswith('s'):
        singularWord = word[:-1]
        if singularWord in knownWordsList:
            return True
    return False


give_word_regex = re.compile('[a-zA-Z]+')

counts = {}

splitted_words = getSplittedWords('files/Freeman/s01e02.txt')
knownWords = getKnownWords('knownWords')

for word in splitted_words:

    groups = give_word_regex.search(word)

    if groups:
        word = groups.group(0).lower()
    else:
        continue

    #known word and input word are lower case
    if isKnownWord(word, knownWords):
        continue

    if not word in counts:
        counts[word] = 0
    current_count = counts[word]
    counts[word] = current_count + 1

# just sort
sorted = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)

for word, count in sorted:
    # print('%s %s' % (word, count))
    print('%s' % (word))
