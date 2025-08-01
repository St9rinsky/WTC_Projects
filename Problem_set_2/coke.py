amount_due = 50
print(f"amount due: {amount_due}")

while amount_due >= 1:
    inserted_coin = int(input("insert coin: "))

    if inserted_coin == 25:
        amount_due -= 25

        if amount_due > 0:
            print(f"amount due: {amount_due}")
        else:
            change = amount_due * -1
            print(f"change owed: {change}")

    elif inserted_coin == 10:
        amount_due -= 10
        if amount_due > 0:
            print(f"amount due: {amount_due}")
        else:
            change = amount_due * -1
            print(f"change owed: {change}")

    elif inserted_coin == 5:
        amount_due -= 5
        if amount_due > 0:
            print(f"amount due: {amount_due}")
        else:
            change = amount_due * -1
            print(f"change owed: {change}")
    else:
        print(f"amount due: {amount_due}")

    
    


