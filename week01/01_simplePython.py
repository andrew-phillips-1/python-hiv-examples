# Example for running simple Python

# Variables can be of different types
# Numbers
x = 0.5
y = 1.0

# Strings
name = "Python"

# Logical values ("boolean")
is_valid = True
should_stop = False

# Variables can be updated
x = 0.6

# And we can do arithmetic...
z = 2*x + y
x_squared = x**2
x_over_y = x/y

# ...and comparisons
x_greater_y = x > y  # similarly <, >=, <=
x_equal_y = x == y
x_different_y = x != y

# We can get the minimum or maximum of a pair of values
w = min(x, 1.0)
v = max(y, 3.2)

# Some functionality requires external modules e.g. math
import math
exponential = math.exp(x)
square_root = math.sqrt(x - 0.1)

# We can display information using print()
print("Value of z = ", z)
print("Value of z cubed = ", z**3)
print("Is x different to y? ", x != y)
