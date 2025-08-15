import random

def main():
    level = get_level()
    score = 0
    problems ={}
    num = 1
    while num <= 10:
        x = generate_integer(level)
        y = generate_integer(level)
        problems[f"problem{num}"] = f"{x} + {y}"
        question = problems[f"problem{num}"]

        attempt = 1
        while attempt <=3:
            answer = input(f"{question} = ")
            if answer == str(x + y):
                score += 1
                break
            else:
                print("EEE")
                attempt+=1
        
        if attempt == 4:
            print(f"{question} = {x+y}")

        num+=1
    print(f"{score}/10")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                pass

def generate_integer(level):
    if level == 1:
        return random.randint(1,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)

if __name__ == "__main__":   
    main()