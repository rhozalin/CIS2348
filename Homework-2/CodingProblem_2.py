# Name-Rhozalin Nath
# PS ID: 2050395
#Code at stage A.

import datetime

current_date = datetime.datetime.today()

while True:
    input_date = input()
    if input_date == '-1':
        break

    m = input_date.find(' ')
    d = input_date.find(',')
    y = d + 1
    month = input_date[:m]
    day =input_date[m + 1:d]
    year =input_date[y:]

    try:
        date = datetime.datetime.strptime(month + ' ' + day + ' ' + year, '%B %d %Y')

    except ValueError:
        continue

    if date > current_date:
        continue
    output_date = date.strftime("%-m/%-d/%Y")
    print(output_date)
