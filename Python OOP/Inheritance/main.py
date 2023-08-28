import customer
import employee

# Create customer object
cust = customer.Customer('Manny', 'Lee', 'London')  # enter names as parameters to the constructor
# features of the subclass has been inherited by the superclass
cust.first_name = "Bruce"
cust.print()

# create an employee object
emp = employee.Employee('Kendall', 'Joshua', 'Finance')
emp.print()

# Call the cust.print to get customer version of print function in customer class
# call the emp.print function to get the employee version of print function in employee class
