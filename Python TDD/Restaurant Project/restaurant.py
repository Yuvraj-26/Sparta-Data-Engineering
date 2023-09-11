import math

""""
restaurant.py
This python file defines the Table class which represents tables at a restaurant
The class has several methods for the required functionality
"""


class Table:
    # constructor method initialises a table object
    def __init__(self, number_of_diners):
        self.number_of_diners = number_of_diners
        # initialise empty bill list
        self.bill = []

    # order method
    def order(self, item, price, quantity=1):
        # iterate through existing orders
        for order in self.bill:
            # check if existing order matches the item and price
            if order['item'] == item and order['price'] == price:
                order['quantity'] += quantity
                return

        # append menu item in dict format
        self.bill.append({'item': item, 'price': price, 'quantity': quantity})

    # remove method
    def remove(self, item, price, quantity):
        # initialise empty list updated bill
        updated_bill = []
        # boolean to indicate whether an item is removed
        order_item_removed = False

        # iterated through order
        for order in self.bill:
            # check if existing order matches the item and price
            if order['item'] == item and order['price'] == price:
                # calculate the min of current order and the quantity to remove
                # which ensures we only remove an existing quantity
                quantity_removed = min(order['quantity'], quantity)
                # reduce the quantity
                order['quantity'] -= quantity_removed
                # check if quantity is greater than 0
                if order['quantity'] > 0:
                    # append as quantity is positive
                    updated_bill.append(order)
                # update boolean, if item is removed then return true
                order_item_removed = order_item_removed or (quantity_removed > 0)
            else:
                updated_bill.append(order)

        # update current bill to updated bill
        self.bill = updated_bill
        return order_item_removed

    # get_subtotal method
    def get_subtotal(self):
        # generator expression to calculate the subtotal
        subtotal = sum(order['price'] * order['quantity'] for order in self.bill)
        return round(subtotal, 2)

    # get_total method
    def get_total(self, service_charge_percentage=0.10):
        subtotal = self.get_subtotal()
        # calculate total including service charge (10% is default)
        service_charge = subtotal * service_charge_percentage
        total = subtotal + service_charge

        # return a dictionary in correct currency format
        return {
            'Sub Total': f'£{subtotal:.2f}',
            'Service Charge': f'£{service_charge:.2f}',
            'Total': f'£{total:.2f}'
        }

    # split_bill method
    def split_bill(self):
        subtotal = self.get_subtotal()
        # calculate individual cost to be paid by each diner and round up
        individual_share = math.ceil(subtotal / self.number_of_diners * 100) / 100
        return individual_share
