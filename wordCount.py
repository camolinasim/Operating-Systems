import re
import string
import operator

frequency = {}
document_text = open('declaration.txt', 'r')
text_string = document_text.read()
match_pattern = re.findall(r'\b[a-zA-Z]{0,15}\b', text_string)

# populating dictionary
for word in match_pattern:
    if word == '':
        continue
    count = frequency.get(word, 0)
    frequency[word] = count + 1

# sorting the dictionary
sorted_frequency = sorted(
    frequency.items(), key=operator.itemgetter(1), reverse=True)
# print(sorted_frequency)


frequency_list = frequency.keys()
# print(frequency_list)

print(range(len(sorted_frequency)))

f = open("myOutput.txt", "w+")
for i in range(len(sorted_frequency)):
    index = i
    print("word: " + str(i))
    tuple = sorted_frequency[i]
    print("first: " + str(tuple[0]))
    print("second: " + str(tuple[1]))

    #print(str(index) + " " + str(tuple))
    f.write(str(str(tuple[0])) + " " + str(tuple[1]) + "\n")
