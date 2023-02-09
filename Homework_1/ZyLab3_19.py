from math import ceil                # needed in Step #3
wall_height=int(input("Enter wall height (feet):\n"))
wall_width=int(input("Enter wall width (feet):\n"))
wall_area=wall_height*wall_width
print(f"Wall area: {wall_area} square feet")
paint_needed= wall_area/350
print(f"Paint needed: {paint_needed:.2f} gallons")
print(f"Cans needed: {ceil(paint_needed)} can(s)")
print()
costs={"red":35,"blue":75,"green":23}
color=input("Choose a color to paint the wall:\n")
print(f"Cost of purchasing {color} paint: ${costs[color]}")
