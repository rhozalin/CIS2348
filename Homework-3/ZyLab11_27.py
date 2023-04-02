# Name-Rhozalin Nath
# PS ID: 2050395
d = {}
for i in range(5):
    jersey = int(input(f"Enter player {i + 1}'s jersey number:"))
    print()
    rating = int(input(f"Enter player {i + 1}'s rating:"))
    print()
    print()
    d[jersey] = rating
dict1 = dict(sorted(d.items()))
print("ROSTER")
for i in dict1.keys():
    print(f"Jersey number: {i}, Rating: {dict1[i]}")

while True:
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    option = input("\nChoose an option:")
    print()

    if option == "o":
        print("ROSTER")
        for i in dict1.keys():
            print(f"Jersey number: {i}, Rating: {dict1[i]}")

    elif option == "a":
        new_player = int(input("Enter a new player's jersey number:"))
        print()
        rating = int(input("Enter the player's rating:"))
        print()
        d[new_player] = rating
        dict1 = dict(sorted(d.items()))
    elif option == "d":
        player = int(input("Enter a jersey number:"))
        del d[player]
        dict1 = dict(sorted(d.items()))
    elif option == "u":
        jersey = int(input("Enter a jersey number:"))
        updated_rating = int(input("Enter a new rating for player:"))
        dict1[jersey] = updated_rating

    elif option == "r":
        above_rating = int(input("Enter a rating:"))
        print(f"\nABOVE {above_rating}")
        for i in dict1.keys():
            if dict1[i] > above_rating:
                print(f"Jersey number: {i}, Rating: {dict1[i]}")
    elif option == "q":
        break






