def main():
    total_counter = []
    unique_items = []
    items = get_items()

    # the aim is to create a new list with unique items only
    # and create another list that counts occurances of the unique item in the old list
    # to prevent re counting items we pass wenever we find an occurance of a non unique item
    for item in items:
        if item in unique_items:
            pass
        else:
            total_counter.append(items.count(item))
            unique_items.append(item)

    for item in unique_items:
        print(f"{total_counter[unique_items.index(item)]} {item}")

def get_items():
    items = []
    while True:
        try:
            item = input("item: ").upper()
        except EOFError:
            items.sort()
            return items
        else: items.append(item)
    
main()