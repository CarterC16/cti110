# Write a program that keeps a running total of the number of bugs collected during the seven days.
# The loop should ask for the number of bugs collected for each day, and when the loop is finished, the program should display the total number of bugs collected.
# 10/28/2018
# CTI-110 P4T2-Bug Collector
# Christian Carter

# initialize the accumulator.
total = 0

# get the bugs collected for each day.
for day in range(1, 6):
    print('Enter the bugs collected on day', day)
    bugs = int(input())
    total += bugs

# display the total bugs.
print('You collected a total of', total, 'bugs.')
