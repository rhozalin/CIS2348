print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print()
services={"Oil change":35,"Tire rotation": 19,"Car wash":7,"Car wax":12}
first_service=input("Select first service:\n")
second_service=input("Select second service:\n")
print()
print("Davy's auto shop invoice\n")
total=0
if first_service=="-":
    print("Service 1: No service")
    print(f"Service 2: {second_service}, ${services[second_service]}")
    total=services[second_service]
elif second_service=="-":
    print(f"Service 1: {first_service}, ${services[first_service]}")
    print("Service 2: No service")
    total=services[first_service]
else:
    print(f"Service 1: {first_service}, ${services[first_service]}")
    print(f"Service 2: {second_service}, ${services[second_service]}")
    total=services[first_service]+services[second_service]
print()
print(f"Total: ${total}")
