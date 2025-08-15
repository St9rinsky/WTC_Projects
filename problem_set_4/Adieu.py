
import inflect
p = inflect.engine()

def main():
    names = get_names()
    preset = "Adieu, adieu, to "
    greet = p.join(names)
    print(f"{preset}{greet}")


def get_names():
    input_names =[]
    while True:
        try:
            name = input("name: ")
        except EOFError:
            return input_names
        else:
            input_names.append(name)

main()