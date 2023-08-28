import customer

# Create customer object
cust = customer.Customer('Manny', 'Lee') # enter names as parameters to the constructor
# instance variables stored in customer object
# Need to prevent changing of instance variables using encapsulation
# cust._lastName = "Alexis"
# call print function on customer object

# Decorator effect is calling setter function (encapsulation)
cust.first_name = "Bruce"
cust.print()

