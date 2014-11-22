__author__ = 'Areo'


from basic.countWordsOnly import splitted_words

__author__ = 'Areo'


import re
import operator



def getSplittedWords(input_file_name):
    file = open(input_file, encoding="utf-8").read()
    return file.split()

def getKnownWords(file_path):

    uniqueWords = []
    splitted_words = getSplittedWords(file_path)

    for word in splitted_words:
        if word not in uniqueWords:
            uniqueWords.append(word)

    return uniqueWords


give_word_regex = re.compile('[a-zA-Z]+')

counts = {}

input_file = 'files/napisy_11.txt'
known_words_file = 'knownWords/knownWords'

splitted_words = getSplittedWords(input_file)
knownWords = getKnownWords(known_words_file)


for word in splitted_words:

    #if you know - ommit
    if word in knownWords:
        continue

    groups = give_word_regex.search(word)

    if groups:
       word = groups.group(0).lower()
    else:
        continue
    if not word in counts:
       counts[word] = 0
    current_count = counts[word]
    counts[word] = current_count + 1

# just sort
sorted = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)

for word, count in sorted:
  #  print('%s %s' % (word, count))
    print('%s' % (word))

