# At one college, the tuition for a full-time student is $8,000 per semester. It
# has been announced that the tuition will increase by 3 Percent each year for
# the next 5 years. Write a program with a loop that displays the projected
# semester tuition amount for the next 5 years.
# 10/28/2018
# CTI-110 P4HW3-Tuition Increase
# Christian Carter

# 8000 per semester. Two Semester each year.

tuition = 16000

for x in range(5):
  percent = tuition * .03
  tuition += percent
  print("The tuition this year is $", format(tuition, '.2f'))


#test
#currentTuition = 8000
#
#print("Year\tTuition\n-----\t-----")
#for currentYear in range( 1, 6):
#    currentTuition += (0.03) * currentTuition
#    print(currentYear, "\t$", format(currentTuition, ".2f" ), sep = "")
