def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif s[0:2].isalpha() == False:
        return False
    elif s.isalnum()== False:
        return False
    else:
        numbers_started = False
        for character in s:
            if character.isdigit() and numbers_started == False:
                if character == "0":
                    return False
                else: numbers_started = True
            elif character.isalpha() and numbers_started == True:
                return False
        else:
            return True
    
        

    



main()