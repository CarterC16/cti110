# Write a program that asks the user to enter the amount that he or she has bugeted
# for a month. A loop should then prompt the user to enter each of his or her expenses
# for the month and keep a running total. When the loop finishes, the program should
# display the amount that the user is over or under budget.
# 10/28/2018
# CTI-110 P4HW1-Budget Analysis
# Christian Carter


# the amount of the budget
budget = float(input("Please input the amount of budget for a month: "))
newexpenses = 1.
expenses = 0
print("")
print("It will ask for an expense and keep a tally, to end it just enter 0.")
print("")

# putting in the expense
while newexpenses > 0:
  newexpenses = float(input("Please put in the new expense: "))
  expenses += newexpenses

# calculate for each of them
loss = expenses - budget
profit = budget - expenses

if expenses > budget:
  print("You are over budget by", format(loss, '.2f'))
elif expenses < budget:
  print("You are under budget by", format(profit, '.2f'))
elif expenses == budget:
  print("You have met your budget exactly.")
