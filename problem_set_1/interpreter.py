def main():
    # ask user for prompt
    prompt = input("Expression: ")
    #separate each variable
    x,y,z = prompt.split(" ")

    # convert strings to numbers
    str_to_num_x = float(x)
    str_to_num_z = float(z)

    # a case for each operator
    match y:
        case "+":
            print(str_to_num_x + str_to_num_z)

        case "-":
            print(str_to_num_x - str_to_num_z)

        case "*":
            print(str_to_num_x * str_to_num_z)

        case "/":
            print(str_to_num_x / str_to_num_z)

main()