def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #remove dollar sign
    D_removed = d.strip("$")

    return float(D_removed)


def percent_to_float(p):
    #remove percentage sign
    sign_removed = p.rstrip("%")

    #covert to decimal
    converted_number = float(sign_removed) / 100

    return converted_number


main()
