vowels = ["a","e","i","o","u"]
word = input( "Input: ")
final_word =""

for character in word:
    if character.lower() in vowels:
        continue
    else:
        final_word += character
print(f"Output: {final_word}")