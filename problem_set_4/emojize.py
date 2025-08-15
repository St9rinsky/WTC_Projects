import emoji

User_input = input("input: ")
edit = emoji.emojize(User_input, language="alias")
print(edit)