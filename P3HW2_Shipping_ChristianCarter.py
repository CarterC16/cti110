# CTI-110
# P3HW2-Shipping Charges
# Christian Carter
# 10/3/2018

# The Fast Freight Shipping Company charges the following rates:

# Weight of Package                         || Rate per Pound
# 2 pounds or less                          || $1.50
# Over 2 pounds but not more than 6 pounds  || $3.00
# Over 6 pounds but not more than 10 pounds || $4.00
# Over 10 Pounds                            || $4.75

# Write a program that asks the user to enter the weight of a package and then 
# displays the shipping charges.

# Variables to represent the weight
A_weight = 10
B_weight = 6
C_weight = 2

# code that ask user to enter the weight
weight = int(input("Enter the weight of the package: "))

# code that prints the rate per pound
if weight >= A_weight:
    print("Your Rate is $4.75.")
else:
    if weight >= B_weight:
        print("Your Rate is $4.00")
    else:
        if weight >= C_weight:
            print("Your Rate ia $3.00")
        else:
            if weight <= C_weight:
                print("Your Rate is $1.50")
