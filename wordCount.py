import re
import string
import functools
import operator

frequency = {}
document_text = open('declaration.txt', 'r')
text_string = document_text.read()
match_pattern = re.findall(r'\b[a-zA-Z]{0,15}\b', text_string)

for word in match_pattern:
    if word == '':
        continue
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

f = open("myOutput.txt", "w+")
for words in frequency_list:
    toPrint = words, frequency[words]
    print(toPrint)
