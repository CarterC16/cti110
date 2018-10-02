# create a code that asks the what number of males and the number of females registered in class and the code should display the percentage of males and females in the class.
# 9/19/2018
# CTI-110 P2HW2-Male Female Percentage
# Christian Carter

males=int(input("Enter number of males:"))
females=int(input("Enter number of females:"))

total= males+females

percentmale= males/total
percentfemale= females/total

print("Percent males:", end=" ")
print(format(percentmale,'.0%'))
print("Percent females:", end=" ")
print(format(percentfemale,'.0%'))

