__author__ = 'Areo'


import re
import operator

book_path = 'files/napisy_11.txt'

file = open(book_path, encoding="utf-8").read()

splitted_words = file.split()

give_word_regex = re.compile('[a-zA-Z]+')

counts = {}
for word in splitted_words:

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
    print('%s %s' % (word, count))
    # print('%s' % (word))
