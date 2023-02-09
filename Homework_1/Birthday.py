print("Birthday Calculator")
print("Current day")
current_month=int(input("Month:"))
current_day=int(input("Day:"))
current_year=int(input("Year:"))
print("Birthday")
birth_month=int(input("Month:"))
birth_day=int(input("Day:"))
birth_year=int(input("Year:"))
year=current_year-birth_year
if current_month<birth_month:
    year-=1
elif current_month==birth_month:
    if current_day<birth_day:
        year-=1
if current_month==birth_month and current_day==birth_day:
    print("Happy Birthday")
print(f"You are {year} years old")

