# Name-Rhozalin Nath
# PS ID: 2050395

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    # FIXME: The following line will throw ValueError exception.
    #        Insert try/except blocks to catch the exception.
    try:
        age = int(parts[1]) + 1
        print(f'{name} {age}')

    except Exception as ex:
        age = 0
        print('{} {}'.format(name, age))
        # Get next line
    parts = input().split()
    name = parts[0]






