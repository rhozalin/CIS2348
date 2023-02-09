lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups=float(input("Enter amount of water (in cups):\n"))
agave_nectar_cups=float(input("Enter amount of agave nectar (in cups):\n"))
servings=int(input("How many servings does this make?\n"))
print()
print(f"Lemonade ingredients - yields {servings:.2f} servings")
print(f"{lemon_juice_cups:.2f} cup(s) lemon juice")
print(f"{water_cups:.2f} cup(s) water")
print(f"{agave_nectar_cups:.2f} cup(s) agave nectar")
print()


desired_servings=int(input("How many servings would you like to make?\n"))
print()
print(f"Lemonade ingredients - yields {desired_servings:.2f} servings")
print(f"{(lemon_juice_cups/servings*desired_servings):.2f} cup(s) lemon juice")
print(f"{(water_cups/servings*desired_servings):.2f} cup(s) water")
print(f"{(agave_nectar_cups/servings*desired_servings):.2f} cup(s) agave nectar")
print()

print(f"Lemonade ingredients - yields {desired_servings:.2f} servings")
print(f"{(lemon_juice_cups/servings*desired_servings/16):.2f} gallon(s) lemon juice")
print(f"{(water_cups/servings*desired_servings/16):.2f} gallon(s) water")
print(f"{(agave_nectar_cups/servings*desired_servings/16):.2f} gallon(s) agave nectar")


