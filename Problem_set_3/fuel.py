#need to be 100% sure we are getting a proper fraction per our rules

def main():
    proper_fraction = get_fraction()
    percentage = round(proper_fraction * 100)
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


def get_fraction():
    while True:
        fraction = input("Fraction: ")
        try:
            x,y = fraction.split("/")
            x,y = int(x),int(y)
            if x <= y:
                return x/y
            else:
                1/0
        except (ValueError, ZeroDivisionError,):
            pass
        else:
            break

main()
