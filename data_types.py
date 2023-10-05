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

# String #
# We create string variables by enclosing characters
# in quotes
# Python uses single quotes '' double quotes ""
# and triple quotes """""" to denote literal strings
# Only the triple quotes will automatically continue
# across the en dof the line statement

firstName = 'john'
lastName = "doe"
message = """This is a string that will span across multiple lines.
 using newline characters and no spaces for the next lines. The end of
 lines within this string also count as a newLine when printed"""

# String can be accessed as a whole string, or a substring of the complete varaible
# using brackets []

var1 = 'hello World!'
var2 = "Python"

print var1[0] ##Prints first character in string
print var2[1:5] #Prints the substring 'Pytho'

# Python can format multiple strings and numbers using a special syntax
#

print ("The item {} is repeated {} times".format(element, count))

#The {} are placeholders that are substitued with the variables
# element and count in the final string.
# There is an older version of this not much used#

print "The item %i is repeated %i times"% (element, count)


#Lists #
# A list can contain a series of values.
# List variables are declared using brackets [] following
# the variable name.#

A = [] #blank list of vars
B = [1l 23, 45, 67] #Creates initial list of 4 nums
C = [2, 3, 'john'] #lists can contain different variable types

# All lists are zero based indexed
# When referencing a member or the length
# of a list the number of list elements is always the number showne
# plus one# 

mylist = ['Rhino', 'Bear','Lion','Tiger','Cheetah']
B = len(mylist) #This will return the length of the list which is 3
print mylist[1] #Returns calue at index 1
print mylist[0:2] #Returns the first 3 elements

# Assign data to a specific element in the list using indexes
mylist = [0, 1, 2, 3]
mylist[0] = 'cat'


# Lists can be multi-dimensional

MyTable = [[[][]],[[][]]]

#In two-dimensional arrays, the first number is always the numbe of rows
# The second number is the number of columns

# Tuples #
# Tuples are a group of values like a list but they're fixed in size#

myGroup ('Rhino', 'Grasshopper', 'Flamingo', 'Bongo')



# Dictionary #
# Dictionaries are lists of Key;Value pairs
# Holds related information that can be associated through
# keys.
# The main operation of a dictionary is to extract a value based on
# the key name
# Indexes aren't used so dictionaries extract value based on the key
# Dictionaries are also used to sort, iterate, and compare data #

room_num = {'john':425, 'tom':212}
room_num['john'] = 645 #set the value associated with the 'john' key to 645
print (room_num['tom']) #print the value of the 'tom' key
room_num['isaac'] = 345
print (room_num.keys()) #print out a list of keys in the dictionary
print ('isaac' in room_num) #test to see if 'isaac' is in the dictionary. returns true


# More on dictionaries: https://developer.rhino3d.com/guides/rhinopython/python-dictionaries/ 













