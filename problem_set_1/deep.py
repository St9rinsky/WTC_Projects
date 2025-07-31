#ask user question
Answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

if Answer == "42":
    print ("Yes")

elif Answer.lower().strip() == "forty-two":
    print("Yes")

elif Answer.lower().strip() == "forty two":
    print ("Yes")

else:
    print ("No")