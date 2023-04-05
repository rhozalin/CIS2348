# Name-Rhozalin Nath
# PS ID: 2050395

class ItemToPurchase:

    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print(
            f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(self.item_price * self.item_quantity)}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:

    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_name, new_quantity):
        for item in self.cart_items:
            if item.item_name == item_name:
                item.item_quantity = new_quantity
                return
        print("Item not found in cart. Nothing modified.\n")

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost

    def print_total(self):
        total_cost = self.get_cost_of_cart()
        print("OUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        if total_cost == 0:
            print("SHOPPING CART IS EMPTY\n")
            print("Total: $0\n")
            return
        for item in self.cart_items:
            item.print_item_cost()
        print(f"\nTotal: ${int(total_cost)}\n")

    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit\n")


def execute_menu(option, shoppingcart):
    if option == "a":
        print("\nADD ITEM TO CART")
        item_name = input("Enter the item name:\n")
        item_description = input("Enter the item description:\n")
        item_price = float(input("Enter the item price:\n"))
        item_quantity = int(input("Enter the item quantity:\n"))
        print()
        item_to_purchase = ItemToPurchase(item_name, item_price, item_quantity, item_description)
        shoppingcart.add_item(item_to_purchase)

    elif option == "r":
        print("\nREMOVE ITEM FROM CART")
        item_name = input("Enter name of item to remove:\n")
        shoppingcart.remove_item(item_name)
        print()

    elif option == "c":
        print("\nCHANGE ITEM QUANTITY")
        item_name = input("Enter the item name:\n")
        item_quantity = int(input("Enter the new quantity:\n"))
        item = ItemToPurchase(item_name, item_quantity=item_quantity)
        shoppingcart.modify_item(item_name, item_quantity)

    elif option == "i":
        print("OUTPUT ITEMS' DESCRIPTIONS")
        shoppingcart.print_descriptions()
        print()

    elif option == "o":
        shoppingcart.print_total()

    else:
        return


def main():
    customer_name = input("Enter customer's name:\n")
    customer_date = input("Enter today's date:\n")
    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {customer_date}\n")
    shoppingcart = ShoppingCart(customer_name, customer_date)

    print_menu()

    while True:
        option = input("Choose an option:\n")
        if option in "arcio":
            execute_menu(option, shoppingcart)
            print_menu()
        elif option not in "arcioq":
            option = input("Choose an option:\n")
        elif option == "q":
            break


if __name__ == '__main__':
    main()