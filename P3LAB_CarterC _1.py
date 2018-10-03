# For these Lab fix and add code to make it work properly. Also use correct indentation
# P3LAB-Debugging
# Christian Carter
# 10/3/2018

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80    ## added the other grades
    C_score = 70
    D_score = 60
    

    score = int(input("Enter your grade: ")) ## added int and brackets 
                                             
    if score >= A_score:                    ## added the other verison on the if and else code
        print("Your grade is A.")           ## the ones i added is C and D and used indentation
    else:
        if score >= B_score:
            print("Your grade is B.")
        else:
            if score >= C_score:
                print("Your grade is C.")
            else:
                if score >= D_score:
                    print("Your grade is D.")
                else:
                    print("Your grade is F.")   


# program start
main()
