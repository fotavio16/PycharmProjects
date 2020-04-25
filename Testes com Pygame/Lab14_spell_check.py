'''
Programa de busca sequencial e binária
'''

import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

# Leitura do arquivo 'dictionary.txt' num array
dictionary_list = []
file = open("dictionary.txt")

for line in file:
    line = line.strip()
    dictionary_list.append(line)

file.close()

'''
print('--- Linear Search ---')

file = open("AliceInWonderLand200.txt")
line_number = 0
for line in file:
    line_number += 1
    line = line.strip()
    words = split_line(line)
    for word in words:
        i = 0
        while i < len(dictionary_list) and dictionary_list[i] != word.upper():
            i += 1

        if i >= len(dictionary_list):
            print(f'{word} na linha nº: {line_number}')

file.close()
'''

print('--- Binary Search ---')
file = open("AliceInWonderLand200.txt")
line_number = 0
for line in file:
    line_number += 1
    line = line.strip()
    words = split_line(line)
    for word in words:
        lower_b = 0
        upper_b = len(dictionary_list) - 1
        achei = False
        while lower_b <= upper_b and not achei:
            middle_pos = (lower_b + upper_b) // 2

            if dictionary_list[middle_pos] < word.upper():
                lower_b = middle_pos + 1
            elif dictionary_list[middle_pos] > word.upper():
                upper_b = middle_pos - 1
            else:
                achei = True

        if not achei:
            print(f'{word} na linha nº: {line_number}')

file.close()
