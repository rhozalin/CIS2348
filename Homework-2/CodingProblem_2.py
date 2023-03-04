# Name-Rhozalin Nath
# PS ID: 2050395
#Code at stage B.
import datetime

current_date = datetime.datetime.today()
input_file = open("inputDates.txt", "r")

for line in input_file:
    if line == -1:
         break
    string = line.strip()

    try:
        date = datetime.datetime.strptime(string, '%B %d, %Y')
    except ValueError:
        continue

    if date > current_date:
        continue
    output_date =date.strftime("%-m/%-d/%Y")
    print(output_date)
