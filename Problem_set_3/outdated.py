def main():
    std_year,std_month,std_day = get_date()
    print(f"{std_year}-{std_month:02}-{std_day:02}")

def get_date():
    while True:
        input_date = input("date: ")
        if "/" in input_date:
            month,day,year = input_date.split("/")
            numerical_date = edit_numerical_date(month,day,year)
            return numerical_date
        
        elif "," in input_date:
            month,day,year = input_date.split(" ")
            day = day.strip(",")
            month = convert_month(month)
            numerical_date = edit_numerical_date(month,day,year)
            return numerical_date
        
        else:
            continue

def edit_numerical_date(month,day,year):
    try:
        month,day,year = int(month),int(day),int(year)
    except ValueError:
        get_date()
    else:
        if month <= 0 or month >12:
            get_date()
        elif day <=0 or day > 31:
            get_date()
        elif year <=0 or year > 9999:
            get_date()
        else:
            return year,month,day

def convert_month(month):
    month = month.capitalize()
    months= [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"]

    if month in months:
        return months.index(month) + 1
    else:
        get_date()

main()