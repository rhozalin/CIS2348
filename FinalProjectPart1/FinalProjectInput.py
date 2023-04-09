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


def get_item_id(item):
    return (item.item_id)


def get_item_price(item):
    return item.price


def get_item_service_date(item):
    return item.service_date


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

    # Writing out the FullInventory.csv file
    with open('FullInventory.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for item in items:
            writer.writerow([item.item_id, item.manufacturer.strip(), item.item_type, item.price, item.service_date,
                             item.damaged.strip() if item.damaged else ''])

    # Creating item_types list to get unique item types from items
    item_types = []
    for item in items:
        if item.item_type not in item_types:
            item_types.append(item.item_type)

    #  Write out inventory files of all types
    for item_type in item_types:
        with open(f'{item_type.capitalize()}Inventory.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            items_of_type = []
            for item in items:
                if item.item_type == item_type:
                    items_of_type.append(item)
            items_of_type.sort(key=get_item_id)
            for item in items_of_type:
                writer.writerow([item.item_id, item.manufacturer, item.price, item.service_date,
                                 item.damaged.strip() if item.damaged else ''])

    # Writing out the PastServiceDateInventory.csv file
    with open('PastServiceDateInventory.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for item in items:
            if datetime.strptime(item.service_date, '%m/%d/%Y') < datetime.today():
                writer.writerow(
                    [item.item_id, item.manufacturer, item.item_type, item.price, item.service_date, item.damaged])

    # Creating a damanged_items list to get all items that are damaged from the items list
    damaged_items = []
    for item in items:
        if item.damaged == 'damaged':
            damaged_items.append(item)

    # Sorting damaged_item list by item price
    damaged_items.sort(key=get_item_price, reverse=True)

    # Writing out the DamagedInventory.csv file
    with open('DamagedInventory.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for item in damaged_items:
            writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date])
