def main():
    prompt = input("what time is it? ")
    converted_time = convert(prompt)

    if converted_time >= 7.00 and converted_time <= 8.00:
        print("Breakfast time")
    elif converted_time >= 12.00 and converted_time <= 13.00:
        print ("Lunch time")
    elif converted_time >= 18.00 and converted_time <= 19.00:
        print("Dinner time")
    else:
        pass
    
def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    converted_minutes = float(minutes) / 60
    return hours + converted_minutes


if __name__ == "__main__":
    main()