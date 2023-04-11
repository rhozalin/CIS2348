# Name-Rhozalin Nath
# PS ID: 2050395

def get_age():
    age = int(input())
    # TODO: Raise exception for invalid ages
    if (age >= 18 and age <= 75):
        return age
    else:
        raise ValueError("Invalid age.")


# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * 0.70

    return heart_rate


if __name__ == "__main__":

    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    try:
        age = get_age()
        print(f"Fat burning heart rate for a {age} year-old: {fat_burning_heart_rate(age)} bpm")
    except ValueError as excpt:
        print(excpt.args[0])
        print("Could not calculate heart rate info.\n")

