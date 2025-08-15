import random

def main():
    level = get_number("Level: ")
    generate_num = random.randint(1,level)
    guess = get_number("Guess: ")
    while True:
        if generate_num > guess:
            print("Too Small!")
            guess = get_number("Guess: ")
        elif generate_num < guess:
            print("Too Large!")
            guess = get_number("Guess: ")
        else:
            print("just right!")
            break

def get_number(prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            pass
        else:
            if number <= 0:
                pass
            else:
                return number

            
main()
        