word = input("camelCase: ")
#initialise empty list to store all words
word_list = []


start = 0
for character in word:
    if character.isupper():
        #when we find an uppercase character
        #append every character before the position of the last uppper character(excl.) to list
        index_of_upper_character = word.index(character)
        word_list.append(word[start:index_of_upper_character]) 

        #change start to continue from the last unrecorded character 
        start = word.index(character)       
    else: pass

#for the last word after the last case upper case that was not recorded
word_list.append(word[start:])

#join up the list using _ to create snake case
snake_case = "_".join(word_list)

print(f"snake case :{snake_case}")