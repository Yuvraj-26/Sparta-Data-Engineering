<a id="top"></a>
# Restaurant Unit Test Project in Python

## Project Overview

This project is centred around the utilisation of the Kanban framework to efficiently manage the development process. Kanban is employed to streamline the creation of user stories, which in turn will guide the Python implementation of a class designed for managing restaurant bills. Additionally, a suite of unit tests will be established to validate the class and its methods, ensuring they meet the specified requirements and perform as expected.

## Kanban: User Stories 

User stories play a pivotal role in our project, and they are created and managed within Trello, the chosen platform for agile project management and collaboration.

[Link to the Trello Project Board](https://trello.com/invite/b/5dcjGLdw/ATTI374fe2501ca03bb3179c5c0d4029944711043A01/kanban-restaurant-user-stories)


## Files

`main.py`

This script serves as a practical example of using the `Table` class defined in `restaurant.py`. It showcases various operations, such as ordering items, removing items, computing subtotals, calculating totals with a service charge, and splitting the bill. Additionally, it automatically runs the unit tests.

`restaurant.py`

Contained within this file is the implementation of the `Table` class, which models restaurant tables. The class includes methods for handling bills and computing costs.

`test_module.py`

This file houses the unit tests for the `Table` class, utilising Python's `unittest` framework. These tests verify the correctness of the `Table` class methods, ensuring they adhere to the specified behavior.

<div align="right">
    <a href="#top">Back to Top</a>
</div>

## Running the Project

To run the project on your local machine, follow these steps:

1. Ensure you have Python 3 installed.

2. Clone the repository to your local system:

   ```shell
   git clone https://github.com/your-username/Restaurant_unit_test_project.git

## Project Specifications

This aim of the project is to implement a class that represents tables at a restaurant.

- The `Table` class in `restaurant.py`instantiates objects to represent tables of diners at a restaurant.  When objects are created they are passed in the number of people dining at that table.  The class has an instance variable called `bill` that is a list.  

The class has several methods for the required functionality.

- An `order` method that accepts an item and a price.  It optionally accept a quantity, which should default to 1 if none is provided.  The method appends a menu item to the bill in the form of `{"item": item, "price": price, "quantity": quantity}`.  If the bill already contains an item with the same item name and price, then it updates the quantity by adding on the new quantity to the existing quantity.
- A `remove` method, that removes an item from the bill or decreases the quantity from the item in the bill with the matching item and price.  If this reduces the quantity to zero, the item is removed from the bill entirely.  The method returns `True` unless there is not an item with the corresponding item name and price (or the corresponding item has a quantity less than the quantity desired for removal), in which case it returns `False` and makes no changes to the bill.
- A `get_subtotal` method that computes and returns the total cost for the table based on the prices and quantities in the bill.
- A `get_total` method that accepts a service charge percentage in the form of a decimal. It calculates the total bill, inclusive of a service charge (defaulting to 10% i.e. `0.10`).  This method returns a dictionary with the following keys: `Sub Total`, `Service Charge`, `Total`.  The values are each string representations of the corresponding prices in British pounds and pence.  e.g. `{"Sub Total": "£120.00", "Service Charge": "£12.00", "Total": "£132.00"}`
- A `split_bill` method, which computes and returns the the subtotal cost of the bill divided by the number of diners as a float rounded up to the nearest penny.

## Contact

Yuvraj M - [yuvrajmahida](https://www.linkedin.com/in/yuvrajmahida/) - 2604yuvraj@gmail.com

<div align="right">
    <a href="#top">Back to Top</a>
</div>


