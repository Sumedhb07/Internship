def is_leap(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
start_year = int(input("Enter the start Year:- "))
end_year = int(input("Enter the end year:- "))
leap_years = []
print(f"Laep year from {start_year} to {end_year} are: ")
for year in range(start_year , end_year + 1):
    if is_leap(year):
        print(year)
       