#Computing with Operators #
# #

a = 3
b = 1
c = a+b

print (c)

print (a + b)

#Practice
Operators

#Arthmetic Operators

     # Addition
    print("10 + 3 = " + str(10 + 3))

    # Subtraction
    print("10 - 3 = " + str(10 - 3))

    # Multiplication
    print("10 * 3 = " + str(10 * 3))

    # Division
    print("10 / 3 = " + str(10 / 3))

    # Division with integer
    print("10 //3 = " + str(10 // 3))

    # Modulus 
    print("10 % 3 = " + str(10 % 3))

    # Exponent
    print("10 ** 3 = " + str(10 ** 3))

    # Augmented operators
    x = 10
    x += 3
    print(x)

    #Operator Precedence
    x = 10 + 3 * 2
    print (x)

#Comparison Operators
# They return boolean (True/False) solutions

    # Greater than
    print("10 > 3: " + str(10 > 3))
    # Greater than or equal to
    print("3 >= 3: " + str(10 >= 3))
    # Less than
    print("10 < 3: " + str(10 < 3))
    # Less than or equal to
    print("10 <= 3: " + str(10 <= 3))
    # Equal
    print("10 == 3: " + str(10 == 3))
    # Not equal
    print("10 != 3: " + str(10 != 3))

#Logical Operators
# Used for building complex rules and conditions

    # Using "and" check that a price is between two values
    price = 25
    print("Price between 10 and 30: " + str(price > 10 and price < 30))

    # Using "or" check that a price is either of two values
    price = 25
    print("Price is either 10 or 30: " + str(price == 10 or price == 30))

    # Using "not" check that a price is less than a value
    price = 25
    print("Price is less than 30: " + str(not price > 30))
