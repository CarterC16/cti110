# CTI-110
# P3HW1-Roman Numerals
# Christian Carter
# 10/3/2018

# Write a program that prompts the user to enter a number within the range of 1 throught 10.
# The program should display the Roman numeral verison of that number. If the number is outside
# the range of 1 through 10, the program should display an error message. The following table
# shows the Roman Numerals for the numbers 1 through 10.
# Number      Roman Numeral
#    1           I
#    2           II
#    3           III
#    4           IV
#    5           V
#    6           VI
#    7           VII
#    8           VIII
#    9           IX
#    10          X

# Code that reads the number
number = int(input("Enter a number from 1-10: "))
 
# Code that prints Roman Numeral
if number == 1:
    print ("The Roman Numeral is I")
elif number == 2:
    print ("The Roman Numeral is II")
elif number == 3:
    print ("The Roman Numeral is III")
elif number == 4:
    print ("The Roman Numeral is IV")
elif number == 5:
    print ("The Roman Numeral is V")
elif number == 6:
    print ("The Roman Numeral is VI")
elif number == 7:
    print ("The Roman Numeral is VII")
elif number == 8:
    print ("The Roman Numeral is VIII")
elif number == 9:
    print ("The Roman Numeral is IX")
elif number == 10:
    print ("The Roman Numeral is X")
else:
    print ("Error: Invalid Number. Please put numbers between 1 through 10.")
