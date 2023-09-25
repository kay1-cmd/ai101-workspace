# There are two different types of data: categorial and numerical
# CATEGORICAL data stores data in categories 
# or groups by using labels assigned to them
# NUMERICAL is expressed in numbers

# There are 5 data types:
# - Numbers
# - String
# - List
# - Tuple
# - DIctionary

# Python sets the variable type based on the variable assigned to it.
# It will also change the variable type 
# if the variable value is set to a different type.

var = 123 # number int
var = 'Nia' # var is now holding a string type

# NUMBERS #
# If a specific number is needed, the format can be forced using syntax:
# Type      Format         Description
# int       a = 10         Signed integer
# long      a = 345L       (L) long integers, can also be represented in octal or hexa
# float     a = 45.67      (.) Floating point real values
# complex   a = 3.14J      (J) Contains integer in the range 0 to 255

# Can also force variable conversion manually via functions
# int(), long(), float(), complex()
# The type function returns data about how the data is stored withina var.

message = 'Good morning'
num = 19
pi = 3.14159

print(type(message))
print(type(num))
print(type(pi))




