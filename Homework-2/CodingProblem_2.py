# Name-Rhozalin Nath
# PS ID: 2050395
#Code at stage C.
import datetime

current_date = datetime.datetime.today()
input_file = open("inputDates.txt", "r")
output_file = open("parsedDates.txt", "w")

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
    output_file.write(output_date + "\n")