word = input("Enter word: ")
#1
word_list = list(word.lower())
word_list_without_spaces = []
for i in word_list:
    if i != ' ':
        word_list_without_spaces.append(i)
reversed_list_without_spaces = word_list_without_spaces[::-1]

print(word_list_without_spaces == reversed_list_without_spaces)

#2
word_list = list(word.lower().replace(' ', ''))
reversed_list = word_list[::1]
print(word_list == reversed_list)







