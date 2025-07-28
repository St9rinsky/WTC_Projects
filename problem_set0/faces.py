def convert(word):
    converted = word.replace(":)","🙂").replace(":(","🙁")
    return converted

def main ():
    speak = input("talk")
    print(convert(speak))

main()
