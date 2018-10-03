# Turtorial - P3T1 - Areas of Rectangles
# 10/3/2018
# CTI-110 P3T1 - Areas of Rectangles
# Christian Carter

# Get the dimesions of rectangle 1.
lenght1 = int(input('Enter the lenght of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))

# Get the dimesions of rectangle 2.
lenght2 = int(input('Enter the lenght of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

# Calculate the area of rectangles.
area1 = lenght1 * width1
area2 = lenght2 * width2

# Determine which has the greater area.
if area1 > area2:
    print("Rectangle 1 has the greatest area.")
elif area2 > area1:
    print("Rectangle 2 has the greatest area.")
else:
    print("Both have the same area")
