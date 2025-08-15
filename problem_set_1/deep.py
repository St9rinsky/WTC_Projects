#ask user question
Answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
Answer = Answer.lower().strip()

if Answer == "42":
    print ("Yes")

elif Answer == "forty-two":
    print("Yes")

elif Answer == "forty two":
    print ("Yes")

else:
    print ("No")