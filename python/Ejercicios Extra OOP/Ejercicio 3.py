class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def add_item(self, inventory):
        inventory.items.append(self)

    def __repr__(self):
        return f"Name: {self.name}\nPrice: {self.price}\nAmount: {self.amount}\n"


class Inventory:
    def __init__(self):
        self.items = []

    def show_items(self):
        print(self.items)

    def get_inventory_value(self):
        total_sum = 0
        for item in self.items:
            total_sum += item.price * item.amount
        return print(f"TOTAL INVENTORY VALUE: {total_sum}")


inventory1 = Inventory()

product1 = Product("Laptop", 500, 1)
product2 = Product("Monitor", 1000, 2)

product1.add_item(inventory1)
product2.add_item(inventory1)

inventory1.show_items()

inventory1.get_inventory_value()
