def main():
    cost = get_cost()
    total_cost = 0
    for price in cost:
        total_cost = total_cost + price
    
    print(f"total:${total_cost:.2f} ")

def get_cost():
    cost = []
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
    while True:
        try:
            Item = input("item:").title()
            if Item in menu:
                cost.append(menu.get(Item))
        except EOFError:
            return cost
        else:
            pass

main()



