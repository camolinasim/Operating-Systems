import re
import string
import operator

frequency = {}
document_text = open('speech.txt', 'r')
text_string = document_text.read()
match_pattern = re.findall(r'\b[a-zA-Z]{1,30}\b', text_string)
print(len(match_pattern))
match_pattern = [x.lower() for x in match_pattern]
# populating dictionary
for word in match_pattern:
    if word == '':
        continue
    count = frequency.get(word, 0)
    frequency[word] = count + 1

# sorting the dictionary
sorted_frequency = sorted(frequency.items())
# print(sorted_frequency)


frequency_list = frequency.keys()
# print(frequency_list)

# print(range(len(sorted_frequency)))

f = open("myOutput.txt", "w+")
for i in range(len(sorted_frequency)):
    index = i

    tuple = sorted_frequency[i]
    #print("first: " + str(tuple[0]))
    #print("second: " + str(tuple[1]))

    print(str(str(tuple[0])) + " " + str(tuple[1]))
    f.write(str(str(tuple[0])) + " " + str(tuple[1]) + "\n")
