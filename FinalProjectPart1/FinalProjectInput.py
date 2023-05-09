# Name-Rhozalin Nath
# PS ID: 2050395

import csv  # Importing csv module to read and write csv files
from datetime import datetime  # Importing datetime module to handle dates


# Defining the classes
class Item:
    def __init__(self, item_id, manufacturer, item_type, damaged):
        self.item_id = item_id
        self.manufacturer = manufacturer
        self.item_type = item_type
        self.damaged = damaged
        self.price = None
        self.service_date = None

    # Specifying how the code should be presented as a string
    def __repr__(self):
        return f'{self.item_id},{self.manufacturer},{self.item_type},{self.price},{self.service_date},{self.damaged}'


class Price:
    def __init__(self, item_id, price):
        self.item_id = item_id
        self.price = price


class ServiceDate:
    def __init__(self, item_id, service_date):
        self.item_id = item_id
        self.service_date = service_date


# Adding functions to sort information easily
def get_manufacturer(item):
    return (item.manufacturer)


if __name__ == '__main__':
    # Reading in the input files
    items = []
    with open('ManufacturerList.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            item_id = row[0]
            manufacturer = row[1]
            item_type = row[2]
            damaged = row[3] if len(row) == 4 else ''
            items.append(Item(item_id, manufacturer, item_type, damaged))
    prices = {}
    with open('PriceList.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            item_id = row[0]
            price = row[1]
            prices[item_id] = Price(item_id, price)
    service_dates = {}
    with open('ServiceDatesList.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            item_id = row[0]
            service_date = row[1]
            service_dates[item_id] = ServiceDate(item_id, service_date)

    # Combining the data by matching the item ID in each file and adding the price and service date to the item object
    for item in items:
        item_id = item.item_id
        if item_id in prices:
            item.price = prices[item_id].price
        if item_id in service_dates:
            item.service_date = service_dates[item_id].service_date

    # sorting the items list by manufacturer
    items.sort(key=get_manufacturer)

    while True:
        query = input("Please input manufacturer and item type: ").lower().split()
        if query[0] == "q":  # The query breaks when the user enters "q"
            break
        # Creates a list of all the manufacturers from items dictionary
        manufacturer_list = [item.manufacturer.strip().lower() for item in items]
        # Creates a list of all the item types from items dictionary
        item_type_list = [item.item_type.strip().lower() for item in items]

        manufacturer_assigned = None
        item_type_assigned = None

        for word in query:
            if word in manufacturer_list:  # checks if the word is in the manufacturer list
                if manufacturer_assigned is not None and manufacturer_assigned != word:
                    print("No such item in inventory")
                    break
                else:
                    manufacturer_assigned = word  # assigns the word as the manufacturer

            if word in item_type_list:  # checks if the word is in the item type list
                if item_type_assigned is not None and item_type_assigned != word:
                    print("No such item in inventory")
                    break
                else:
                    item_type_assigned = word  # assigns the word as the item type
        else:
            found = []  # creates an empty dictionary that will store items if found
            for item in items:
                # checks if the item meets the required criteria
                if item.manufacturer.strip().lower() == manufacturer_assigned and item.item_type.strip().lower() == item_type_assigned and not item.damaged and datetime.strptime(
                        item.service_date, '%m/%d/%Y').date() >= datetime.now().date():
                    found.append(item)

            if len(found) == 0:
                print("No such item in inventory")  # prints if there's no such item found
            elif len(found) > 1:
                # assigns max_price and max_item that meets the criteria
                max_price = 0
                max_item = None
                for item in found:
                    if float(item.price) > float(max_price) and datetime.strptime(item.service_date,
                                                                                  '%m/%d/%Y').date() >= datetime.now().date() and not item.damaged:
                        max_price = item.price
                        max_item = item
                if max_item is None:
                    print("No such item in inventory")  # prints if there's no such item found
                else:  # prints if it meets the search criteria
                    print(
                        f"Your item is: {max_item.item_id}, {max_item.manufacturer.strip()}, {max_item.item_type}, {max_item.price}")
                closestprice_diff = float("inf")  # assigns the closest price difference to positive infinity
                closestprice_item = None  # initializes the closest price item to None
                for item in items:
                    if item.manufacturer.strip().lower() != manufacturer_assigned and item.item_type.strip().lower() == item_type_assigned and not item.damaged and datetime.strptime(
                            item.service_date, '%m/%d/%Y').date() >= datetime.now().date():
                        # assinges price diff to find the closest match
                        price_diff = abs(float(item.price) - float(max_item.price))
                        if price_diff < closestprice_diff:
                            closestprice_diff = price_diff
                            closestprice_item = item
                if closestprice_item is not None:
                    # prints the information is the criteria is matched
                    print(
                        f"You may also consider: {closestprice_item.item_id}, {closestprice_item.manufacturer.strip()}, {closestprice_item.item_type}, {closestprice_item.price}")

            elif len(found) == 1:
                # prints information that is found
                for item in found:
                    print(f"Your item is: {item.item_id}, {item.manufacturer.strip()}, {item.item_type}, {item.price}")
                    itemprice = item.price  # assings item price to the item in found list
                    closestprice_diff = float("inf")  # initializes the closest price difference to positive infinity
                    closestprice_item = None  # initializes the closest price item to None
                    for item in items:
                        if item.manufacturer.strip().lower() != manufacturer_assigned and item.item_type.strip().lower() == item_type_assigned and not item.damaged and datetime.strptime(
                                item.service_date, '%m/%d/%Y').date() >= datetime.now().date():
                            price_diff = abs(float(item.price) - float(itemprice))
                            if price_diff < closestprice_diff:
                                closestprice_diff = price_diff
                                closestprice_item = item
                    if closestprice_item is not None:
                        # prints if closestprice_item is not empty
                        print(
                            f"You may also consider: {closestprice_item.item_id}, {closestprice_item.manufacturer.strip()}, {closestprice_item.item_type}, {closestprice_item.price}")
